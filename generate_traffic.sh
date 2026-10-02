#!/usr/bin/env bash
# ==============================================================================
# NGINX Plus Traffic Generator for HTTP, HTTPS, and Stream (TCP/UDP)
# ==============================================================================
# Generates realistic traffic patterns to populate all Grafana dashboard panels:
#  - Steady HTTP 200 OK & Bandwidth throughput
#  - Status code distribution (2xx, 3xx, 4xx, 5xx)
#  - Latency spikes (P50, P90, P99) and TTFB metrics
#  - Rate limiting & connection bursts (Slab allocation)
#  - SSL/TLS handshakes and session resumption
#  - Layer 4 Stream TCP/UDP DNS queries and session durations
# ==============================================================================

set -u

# --- Configuration (Override via environment variables or CLI flags) ---
TARGET_HOST="${1:-${NGINX_HOST:-"127.0.0.1"}}"
HTTP_PORT="${2:-${NGINX_HTTP_PORT:-80}}"
HTTPS_PORT="${3:-${NGINX_HTTPS_PORT:-8443}}"
STREAM_PORT="${4:-${NGINX_STREAM_PORT:-20053}}"
CONCURRENCY="${5:-${CONCURRENCY:-4}}"

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

echo -e "${CYAN}================================================================${NC}"
echo -e "${CYAN}   NGINX Plus Multi-Protocol Telemetry Traffic Generator       ${NC}"
echo -e "${CYAN}================================================================${NC}"
echo -e " Target Host:   ${YELLOW}${TARGET_HOST}${NC}"
echo -e " HTTP Port:     ${YELLOW}${HTTP_PORT}${NC}  (http://${TARGET_HOST}:${HTTP_PORT}/)"
echo -e " HTTPS Port:    ${YELLOW}${HTTPS_PORT}${NC} (https://${TARGET_HOST}:${HTTPS_PORT}/)"
echo -e " Stream Port:   ${YELLOW}${STREAM_PORT}${NC} (TCP/UDP DNS proxy)"
echo -e " Concurrency:   ${YELLOW}${CONCURRENCY} workers per stream${NC}"
echo -e "${CYAN}----------------------------------------------------------------${NC}"
echo -e " Press ${RED}[Ctrl+C]${NC} to stop traffic generation at any time."
echo -e "${CYAN}----------------------------------------------------------------${NC}"

# Detect installed tools
HAS_DIG=false
if command -v dig &>/dev/null; then
    HAS_DIG=true
fi

HAS_NC=false
if command -v nc &>/dev/null; then
    HAS_NC=true
fi

# Cleanup child processes on exit
cleanup() {
    echo -e "\n${YELLOW}[!] Terminating background traffic workers...${NC}"
    kill $(jobs -p) 2>/dev/null || true
    wait 2>/dev/null || true
    echo -e "${GREEN}[✔] All workers stopped cleanly. Dashboard telemetry intact.${NC}"
    exit 0
}
trap cleanup SIGINT SIGTERM EXIT

# ------------------------------------------------------------------------------
# Worker 1: Steady HTTP Traffic & Bandwidth (2xx Success)
# ------------------------------------------------------------------------------
worker_http_steady() {
    local id=$1
    local endpoints=("/" "/api/v1/" "/status/200" "/status/201")
    while true; do
        for ep in "${endpoints[@]}"; do
            curl -s -o /dev/null -w "%{http_code}" "http://${TARGET_HOST}:${HTTP_PORT}${ep}" >/dev/null 2>&1 || true
            sleep 0.1
        done
    done
}

# ------------------------------------------------------------------------------
# Worker 2: Status Code Distribution (3xx, 4xx, 5xx Errors)
# ------------------------------------------------------------------------------
worker_http_status_codes() {
    local error_endpoints=(
        "/status/301"
        "/status/302"
        "/status/400"
        "/status/401"
        "/status/403"
        "/status/404"
        "/status/429"
        "/status/500"
        "/status/502"
        "/status/503"
        "/status/504"
        "/nonexistent-page-$(date +%s)"
    )
    while true; do
        for ep in "${error_endpoints[@]}"; do
            curl -s -o /dev/null "http://${TARGET_HOST}:${HTTP_PORT}${ep}" >/dev/null 2>&1 || true
            sleep 0.3
        done
    done
}

# ------------------------------------------------------------------------------
# Worker 3: Latency & TTFB Simulation (Httpbin Delay)
# ------------------------------------------------------------------------------
worker_http_latency() {
    while true; do
        # Call /delay endpoint which waits ~1s before returning
        curl -s -o /dev/null "http://${TARGET_HOST}:${HTTP_PORT}/delay" >/dev/null 2>&1 || true
        sleep 1
    done
}

# ------------------------------------------------------------------------------
# Worker 4: Burst Traffic (Rate Limiting & Slab Allocations)
# ------------------------------------------------------------------------------
worker_http_bursts() {
    while true; do
        # Rapid burst of 40 requests to hit limit_req and limit_conn
        for i in {1..40}; do
            curl -s -o /dev/null "http://${TARGET_HOST}:${HTTP_PORT}/status/200" >/dev/null 2>&1 &
        done
        wait 2>/dev/null || true
        sleep 2
    done
}

# ------------------------------------------------------------------------------
# Worker 5: SSL / TLS Handshakes & Session Reuses
# ------------------------------------------------------------------------------
worker_ssl_traffic() {
    local cookie_file=$(mktemp)
    while true; do
        # Initial handshake
        curl -k -s -o /dev/null --sessionid "https://${TARGET_HOST}:${HTTPS_PORT}/status/200" >/dev/null 2>&1 || true
        # Session reuse
        curl -k -s -o /dev/null --sessionid "https://${TARGET_HOST}:${HTTPS_PORT}/" >/dev/null 2>&1 || true
        sleep 0.2
    done
    rm -f "$cookie_file" 2>/dev/null || true
}

# ------------------------------------------------------------------------------
# Worker 6: Stream Layer 4 TCP Traffic (DNS over TCP / Port 20053)
# ------------------------------------------------------------------------------
worker_stream_tcp() {
    local domains=("example.com" "google.com" "cloudflare.com" "wikipedia.org" "github.com")
    while true; do
        for domain in "${domains[@]}"; do
            if [ "$HAS_DIG" = true ]; then
                dig +tcp +short +time=2 +tries=1 "@${TARGET_HOST}" -p "${STREAM_PORT}" "${domain}" >/dev/null 2>&1 || true
            elif [ "$HAS_NC" = true ]; then
                echo -e "HEAD / HTTP/1.0\r\n\r\n" | nc -w 2 "${TARGET_HOST}" "${STREAM_PORT}" >/dev/null 2>&1 || true
            else
                # Pure bash TCP socket probe
                (exec 3<>/dev/tcp/${TARGET_HOST}/${STREAM_PORT} && echo "ping" >&3 && cat <&3 >/dev/null 2>&1 && exec 3>&-) 2>/dev/null || true
            fi
            sleep 0.2
        done
    done
}

# ------------------------------------------------------------------------------
# Worker 7: Stream Layer 4 UDP Traffic (DNS over UDP / Port 20053)
# ------------------------------------------------------------------------------
worker_stream_udp() {
    local domains=("nginx.com" "f5.com" "kernel.org" "gnu.org" "debian.org")
    while true; do
        for domain in "${domains[@]}"; do
            if [ "$HAS_DIG" = true ]; then
                dig +notcp +short +time=2 +tries=1 "@${TARGET_HOST}" -p "${STREAM_PORT}" "${domain}" >/dev/null 2>&1 || true
            elif [ "$HAS_NC" = true ]; then
                echo -n "test-packet" | nc -u -w 1 "${TARGET_HOST}" "${STREAM_PORT}" >/dev/null 2>&1 || true
            fi
            sleep 0.2
        done
    done
}

# --- Launch Background Worker Pools ---
echo -e "${BLUE}[*] Starting HTTP steady traffic pool (${CONCURRENCY} workers)...${NC}"
for ((i=1; i<=CONCURRENCY; i++)); do
    worker_http_steady "$i" &
done

echo -e "${YELLOW}[*] Starting HTTP error & status code generator...${NC}"
worker_http_status_codes &

echo -e "${MAGENTA}[*] Starting Latency & TTFB injector (/delay endpoint)...${NC}"
worker_http_latency &

echo -e "${RED}[*] Starting Rate-limit & Slab allocation burst generator...${NC}"
worker_http_bursts &

echo -e "${GREEN}[*] Starting SSL/TLS handshake & session resumption worker...${NC}"
worker_ssl_traffic &

echo -e "${CYAN}[*] Starting Stream TCP proxy traffic worker (Port ${STREAM_PORT})...${NC}"
worker_stream_tcp &

echo -e "${CYAN}[*] Starting Stream UDP proxy traffic worker (Port ${STREAM_PORT} UDP)...${NC}"
worker_stream_udp &

echo -e "${GREEN}[✔] All traffic generation engines are running!${NC}"
echo -e "${CYAN}----------------------------------------------------------------${NC}"

# Active terminal heartbeat display
start_time=$(date +%s)
while true; do
    elapsed=$(( $(date +%s) - start_time ))
    echo -ne "\r${GREEN}[ACTIVE]${NC} Generating HTTP + Stream traffic... Runtime: ${YELLOW}${elapsed}s${NC} | Check Grafana dashboard for real-time updates."
    sleep 2
done
