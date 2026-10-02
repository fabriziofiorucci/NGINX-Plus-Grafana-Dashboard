"""
Enterprise Grafana Dashboard Generator for NGINX Plus Prometheus Exporter
Generates nginx-plus-overview.json with 52 panels across 10 functional rows.
Fully supports both new exporter format (worker singular metrics, limit_req, limit_conn,
numeric state codes 1-6, Go/process telemetry) and legacy format.
"""

import json
import os

def create_dashboard():
    dashboard = {
        "__inputs": [
            {
                "name": "DS_PROMETHEUS",
                "label": "Prometheus",
                "description": "Select Prometheus datasource scraping NGINX Plus exporter",
                "type": "datasource",
                "pluginId": "prometheus",
                "pluginName": "Prometheus"
            }
        ],
        "__elements": {},
        "__requires": [
            {"type": "grafana", "id": "grafana", "name": "Grafana", "version": "9.0.0"},
            {"type": "datasource", "id": "prometheus", "name": "Prometheus", "version": "1.0.0"},
            {"type": "panel", "id": "timeseries", "name": "Time series", "version": ""},
            {"type": "panel", "id": "stat", "name": "Stat", "version": ""},
            {"type": "panel", "id": "table", "name": "Table", "version": ""},
            {"type": "panel", "id": "bargauge", "name": "Bar gauge", "version": ""}
        ],
        "annotations": {
            "list": [
                {
                    "builtIn": 1,
                    "datasource": {"type": "grafana", "uid": "-- Grafana --"},
                    "enable": True,
                    "hide": True,
                    "name": "Annotations & Alerts",
                    "type": "dashboard"
                }
            ]
        },
        "description": "Enterprise-grade Grafana dashboard for NGINX Plus Prometheus Exporter monitoring HTTP traffic, Stream (TCP/UDP), SSL/TLS, Rate Limiting, Connection Limiting, Slab Memory, Worker processes, and Go runtime telemetry.",
        "editable": True,
        "fiscalYearStartMonth": 0,
        "graphTooltip": 1,
        "id": None,
        "links": [
            {
                "asDropdown": False,
                "icon": "external link",
                "includeVars": True,
                "keepTime": True,
                "tags": [],
                "targetBlank": True,
                "title": "NGINX Plus API Reference",
                "tooltip": "Open official NGINX Plus API Docs",
                "url": "https://docs.nginx.com/nginx/admin-guide/monitoring/nginx-plus-api-reference/"
            }
        ],
        "liveNow": False,
        "panels": [],
        "refresh": "10s",
        "schemaVersion": 38,
        "tags": ["nginx", "nginx-plus", "stream", "tcp", "udp", "rate-limiting", "load-balancer", "prometheus", "proxy", "observability"],
        "templating": {
            "list": [
                {
                    "current": {"selected": True, "text": "default", "value": "default"},
                    "hide": 0,
                    "includeAll": False,
                    "label": "Data Source",
                    "multi": False,
                    "name": "DS_PROMETHEUS",
                    "options": [],
                    "query": "prometheus",
                    "refresh": 1,
                    "regex": "",
                    "type": "datasource"
                },
                {
                    "allValue": ".*",
                    "current": {"selected": True, "text": "All", "value": "$__all"},
                    "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                    "definition": "label_values({__name__=~\"nginxplus_.*|nginx_.*\"}, instance)",
                    "hide": 0,
                    "includeAll": True,
                    "label": "Instance",
                    "multi": True,
                    "name": "instance",
                    "options": [],
                    "query": {
                        "query": "label_values({__name__=~\"nginxplus_.*|nginx_.*\"}, instance)",
                        "refId": "StandardVariableQuery"
                    },
                    "refresh": 1,
                    "regex": "",
                    "sort": 1,
                    "type": "query"
                },
                {
                    "allValue": ".*",
                    "current": {"selected": True, "text": "All", "value": "$__all"},
                    "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                    "definition": "label_values({__name__=~\"nginxplus_server_zone_.*\", instance=~\"$instance\"}, server_zone)",
                    "hide": 0,
                    "includeAll": True,
                    "label": "HTTP Server Zone",
                    "multi": True,
                    "name": "server_zone",
                    "options": [],
                    "query": {
                        "query": "label_values({__name__=~\"nginxplus_server_zone_.*\", instance=~\"$instance\"}, server_zone)",
                        "refId": "StandardVariableQuery"
                    },
                    "refresh": 2,
                    "regex": "",
                    "sort": 1,
                    "type": "query"
                },
                {
                    "allValue": ".*",
                    "current": {"selected": True, "text": "All", "value": "$__all"},
                    "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                    "definition": "label_values({__name__=~\"nginxplus_upstream_server_.*\", instance=~\"$instance\"}, upstream)",
                    "hide": 0,
                    "includeAll": True,
                    "label": "HTTP Upstream",
                    "multi": True,
                    "name": "upstream",
                    "options": [],
                    "query": {
                        "query": "label_values({__name__=~\"nginxplus_upstream_server_.*\", instance=~\"$instance\"}, upstream)",
                        "refId": "StandardVariableQuery"
                    },
                    "refresh": 2,
                    "regex": "",
                    "sort": 1,
                    "type": "query"
                },
                {
                    "allValue": ".*",
                    "current": {"selected": True, "text": "All", "value": "$__all"},
                    "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                    "definition": "label_values({__name__=~\"nginxplus_upstream_server_.*\", instance=~\"$instance\", upstream=~\"$upstream\"}, server)",
                    "hide": 0,
                    "includeAll": True,
                    "label": "HTTP Backend Server",
                    "multi": True,
                    "name": "server",
                    "options": [],
                    "query": {
                        "query": "label_values({__name__=~\"nginxplus_upstream_server_.*\", instance=~\"$instance\", upstream=~\"$upstream\"}, server)",
                        "refId": "StandardVariableQuery"
                    },
                    "refresh": 2,
                    "regex": "",
                    "sort": 1,
                    "type": "query"
                },
                {
                    "allValue": ".*",
                    "current": {"selected": True, "text": "All", "value": "$__all"},
                    "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                    "definition": "label_values({__name__=~\"nginxplus_stream_server_zone_.*\", instance=~\"$instance\"}, server_zone)",
                    "hide": 0,
                    "includeAll": True,
                    "label": "Stream Zone (TCP/UDP)",
                    "multi": True,
                    "name": "stream_server_zone",
                    "options": [],
                    "query": {
                        "query": "label_values({__name__=~\"nginxplus_stream_server_zone_.*\", instance=~\"$instance\"}, server_zone)",
                        "refId": "StandardVariableQuery"
                    },
                    "refresh": 2,
                    "regex": "",
                    "sort": 1,
                    "type": "query"
                },
                {
                    "allValue": ".*",
                    "current": {"selected": True, "text": "All", "value": "$__all"},
                    "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                    "definition": "label_values({__name__=~\"nginxplus_stream_upstream_server_.*\", instance=~\"$instance\"}, upstream)",
                    "hide": 0,
                    "includeAll": True,
                    "label": "Stream Upstream",
                    "multi": True,
                    "name": "stream_upstream",
                    "options": [],
                    "query": {
                        "query": "label_values({__name__=~\"nginxplus_stream_upstream_server_.*\", instance=~\"$instance\"}, upstream)",
                        "refId": "StandardVariableQuery"
                    },
                    "refresh": 2,
                    "regex": "",
                    "sort": 1,
                    "type": "query"
                },
                {
                    "allValue": ".*",
                    "current": {"selected": True, "text": "All", "value": "$__all"},
                    "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                    "definition": "label_values({__name__=~\"nginxplus_stream_upstream_server_.*\", instance=~\"$instance\", upstream=~\"$stream_upstream\"}, server)",
                    "hide": 0,
                    "includeAll": True,
                    "label": "Stream Backend Server",
                    "multi": True,
                    "name": "stream_server",
                    "options": [],
                    "query": {
                        "query": "label_values({__name__=~\"nginxplus_stream_upstream_server_.*\", instance=~\"$instance\", upstream=~\"$stream_upstream\"}, server)",
                        "refId": "StandardVariableQuery"
                    },
                    "refresh": 2,
                    "regex": "",
                    "sort": 1,
                    "type": "query"
                },
                {
                    "allValue": ".*",
                    "current": {"selected": True, "text": "All", "value": "$__all"},
                    "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                    "definition": "label_values({__name__=~\"nginxplus_limit_.*|nginxplus_slab_.*\", instance=~\"$instance\"}, zone)",
                    "hide": 0,
                    "includeAll": True,
                    "label": "Limit & Memory Zone",
                    "multi": True,
                    "name": "zone",
                    "options": [],
                    "query": {
                        "query": "label_values({__name__=~\"nginxplus_limit_.*|nginxplus_slab_.*\", instance=~\"$instance\"}, zone)",
                        "refId": "StandardVariableQuery"
                    },
                    "refresh": 2,
                    "regex": "",
                    "sort": 1,
                    "type": "query"
                }
            ]
        },
        "time": {"from": "now-6h", "to": "now"},
        "timepicker": {
            "refresh_intervals": ["5s", "10s", "30s", "1m", "5m", "15m", "30m", "1h"]
        },
        "timezone": "browser",
        "title": "NGINX Plus - Observability & Traffic Overview",
        "uid": "nginxplus-traffic-overview",
        "version": 3
    }

    panel_id = 1
    panels = []

    def make_row(title, y, collapsed=False):
        nonlocal panel_id
        r = {
            "collapsed": collapsed,
            "gridPos": {"h": 1, "w": 24, "x": 0, "y": y},
            "id": panel_id,
            "panels": [],
            "title": title,
            "type": "row"
        }
        panel_id += 1
        return r

    # State mapping for upstream servers across HTTP & Stream
    upstream_state_mapping = [
        {
            "options": {
                "0": {"color": "#F2495C", "index": 0, "text": "DOWN"},
                "1": {"color": "#73BF69", "index": 1, "text": "UP"},
                "2": {"color": "#E5A00D", "index": 2, "text": "DRAINING"},
                "3": {"color": "#F2495C", "index": 3, "text": "DOWN"},
                "4": {"color": "#F2495C", "index": 4, "text": "UNAVAIL"},
                "5": {"color": "#5794F2", "index": 5, "text": "CHECKING"},
                "6": {"color": "#E02F44", "index": 6, "text": "UNHEALTHY"}
            },
            "type": "value"
        }
    ]

    upstream_state_thresholds = {
        "mode": "absolute",
        "steps": [
            {"color": "#F2495C", "value": None},
            {"color": "#73BF69", "value": 1},
            {"color": "#E5A00D", "value": 2},
            {"color": "#F2495C", "value": 3},
            {"color": "#F2495C", "value": 4},
            {"color": "#5794F2", "value": 5},
            {"color": "#E02F44", "value": 6}
        ]
    }

    # =========================================================================
    # ROW 1: System Status & Core KPIs
    # =========================================================================
    panels.append(make_row("System Status & Core KPIs", 0))

    # Stat 1: Config Generation & Version / Exporter UP
    panels.append({
        "id": panel_id,
        "title": "Config Generation & Version",
        "type": "stat",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Total NGINX configuration reloads, build version info, or exporter active state.",
        "gridPos": {"h": 4, "w": 3, "x": 0, "y": 1},
        "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "thresholds": {"mode": "absolute", "steps": [{"color": "#5794F2", "value": None}]},
                "unit": "none"
            },
            "overrides": []
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "nginxplus_nginx_config_generation{instance=~\"$instance\"} or (nginxplus_up{instance=~\"$instance\"})",
                "instant": True,
                "legendFormat": "Gen {{value}} ({{build}})",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Stat 3: Total HTTP Request Rate
    panels.append({
        "id": panel_id,
        "title": "Total HTTP Request Rate",
        "type": "stat",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Global client HTTP request throughput handled by NGINX Plus.",
        "gridPos": {"h": 4, "w": 4, "x": 3, "y": 1},
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "thresholds": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}]},
                "unit": "reqps"
            },
            "overrides": []
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_http_requests_total{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "HTTP req/s",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Stat 4: Total Stream Connection Rate
    panels.append({
        "id": panel_id,
        "title": "Total Stream Connection Rate",
        "type": "stat",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Global L4 TCP/UDP connection throughput across all stream server zones.",
        "gridPos": {"h": 4, "w": 4, "x": 7, "y": 1},
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "thresholds": {"mode": "absolute", "steps": [{"color": "#5794F2", "value": None}]},
                "unit": "cps"
            },
            "overrides": []
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_stream_server_zone_connections{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Stream conn/s",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Stat 5: Active Client Connections
    panels.append({
        "id": panel_id,
        "title": "Active Client Connections",
        "type": "stat",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Total number of active client connections currently established.",
        "gridPos": {"h": 4, "w": 3, "x": 11, "y": 1},
        "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "thresholds": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}]},
                "unit": "none"
            },
            "overrides": []
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(nginxplus_connections_active{instance=~\"$instance\"}) or sum(nginxplus_worker_connection_active{instance=~\"$instance\"})",
                "legendFormat": "Active Connections",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Stat 6: In-Flight Processing (HTTP & Stream)
    panels.append({
        "id": panel_id,
        "title": "In-Flight Processing (HTTP & Stream)",
        "type": "stat",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Concurrent HTTP requests and Stream sessions actively being processed.",
        "gridPos": {"h": 4, "w": 3, "x": 14, "y": 1},
        "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "thresholds": {"mode": "absolute", "steps": [{"color": "#B877D9", "value": None}]},
                "unit": "none"
            },
            "overrides": []
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(nginxplus_http_requests_current{instance=~\"$instance\"}) or sum(nginxplus_worker_http_requests_current{instance=~\"$instance\"})",
                "legendFormat": "HTTP In-Flight",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(nginxplus_stream_server_zone_processing{instance=~\"$instance\"})",
                "legendFormat": "Stream In-Flight",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Stat 7: License Expiration Countdown
    panels.append({
        "id": panel_id,
        "title": "License Expiration",
        "type": "stat",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Time remaining until NGINX Plus subscription license expires.",
        "gridPos": {"h": 4, "w": 3, "x": 17, "y": 1},
        "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "#F2495C", "value": None},
                        {"color": "#F2495C", "value": 0},
                        {"color": "#EAB839", "value": 604800},
                        {"color": "#73BF69", "value": 2592000}
                    ]
                },
                "unit": "dtdurations"
            },
            "overrides": []
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "nginxplus_license_expiration_timestamp_seconds{instance=~\"$instance\"} - time()",
                "instant": True,
                "legendFormat": "License Remaining",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Stat 8: Worker Crashes & License Reporting Status
    panels.append({
        "id": panel_id,
        "title": "Worker Crashes & License Reporting",
        "type": "stat",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Abnormally terminated & respawned workers (crashes), and license reporting health state.",
        "gridPos": {"h": 4, "w": 4, "x": 20, "y": 1},
        "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "#73BF69", "value": None},
                        {"color": "#F2495C", "value": 1}
                    ]
                },
                "unit": "none"
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "Respawned Workers"},
                    "properties": [
                        {
                            "id": "mappings",
                            "value": [
                                {
                                    "options": {
                                        "0": {"color": "#73BF69", "index": 0, "text": "0 (Healthy)"}
                                    },
                                    "type": "value"
                                }
                            ]
                        },
                        {
                            "id": "thresholds",
                            "value": {
                                "mode": "absolute",
                                "steps": [
                                    {"color": "#73BF69", "value": None},
                                    {"color": "#F2495C", "value": 1}
                                ]
                            }
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Reporting Status"},
                    "properties": [
                        {
                            "id": "mappings",
                            "value": [
                                {
                                    "options": {
                                        "0": {"color": "#F2495C", "index": 0, "text": "Unhealthy"},
                                        "1": {"color": "#73BF69", "index": 1, "text": "Healthy"}
                                    },
                                    "type": "value"
                                }
                            ]
                        },
                        {
                            "id": "thresholds",
                            "value": {
                                "mode": "absolute",
                                "steps": [
                                    {"color": "#F2495C", "value": None},
                                    {"color": "#73BF69", "value": 1}
                                ]
                            }
                        }
                    ]
                }
            ]
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(nginxplus_processes_respawned{instance=~\"$instance\"}) or vector(0)",
                "instant": True,
                "legendFormat": "Respawned Workers",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "min(nginxplus_license_reporting_healthy{instance=~\"$instance\"}) or min(nginxplus_up{instance=~\"$instance\"})",
                "instant": True,
                "legendFormat": "Reporting Status",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # =========================================================================
    # ROW 2: Traffic & Connection Dynamics
    # =========================================================================
    panels.append(make_row("Traffic & Connection Dynamics", 5))

    # Panel 9: Global HTTP Request Rate
    panels.append({
        "id": panel_id,
        "title": "Global HTTP Request Rate",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Total client HTTP requests per second partitioned by instance.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 6},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "gradientMode": "opacity",
                    "showPoints": "never",
                    "spanNulls": False
                },
                "unit": "reqps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (instance) (rate(nginxplus_http_requests_total{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "{{instance}}",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Panel 10: Client Connections Breakdown
    panels.append({
        "id": panel_id,
        "title": "Client Connections Breakdown (Accepted, Active, Idle, Dropped)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Rate of accepted and dropped client connections alongside current active and idle connections.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 6},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "linear",
                    "lineWidth": 2,
                    "fillOpacity": 10,
                    "showPoints": "never"
                },
                "unit": "none",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "Accepted / sec"},
                    "properties": [
                        {"id": "unit", "value": "cps"},
                        {"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Active"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byName", "options": "Idle"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#B7DBAB", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byName", "options": "Dropped / sec"},
                    "properties": [
                        {"id": "unit", "value": "cps"},
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_connections_accepted{instance=~\"$instance\"}[$__rate_interval])) or sum(rate(nginxplus_worker_connection_accepted{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Accepted / sec",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(nginxplus_connections_active{instance=~\"$instance\"}) or sum(nginxplus_worker_connection_active{instance=~\"$instance\"})",
                "legendFormat": "Active",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(nginxplus_connections_idle{instance=~\"$instance\"}) or sum(nginxplus_worker_connection_idle{instance=~\"$instance\"})",
                "legendFormat": "Idle",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_connections_dropped{instance=~\"$instance\"}[$__rate_interval])) or sum(rate(nginxplus_worker_connection_dropped{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Dropped / sec",
                "refId": "D"
            }
        ]
    })
    panel_id += 1

    # Panel 11: Worker Process Request Distribution
    panels.append({
        "id": panel_id,
        "title": "Worker Process Request Distribution",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Verifies that incoming traffic is evenly balanced across NGINX worker processes (PID & ID).",
        "gridPos": {"h": 8, "w": 8, "x": 0, "y": 14},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 12,
                    "showPoints": "never",
                    "stacking": {"group": "A", "mode": "normal"}
                },
                "unit": "reqps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (id, pid) (rate(nginxplus_worker_http_requests_total{instance=~\"$instance\"}[$__rate_interval])) or sum by (id) (rate(nginxplus_workers_http_requests{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Worker #{{id}} (PID {{pid}})",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Panel 12: Worker Concurrency & Connections Breakdown
    panels.append({
        "id": panel_id,
        "title": "Worker Concurrency & Connection States",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Per-worker breakdown of active, idle, and accepted connections.",
        "gridPos": {"h": 8, "w": 8, "x": 8, "y": 14},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 10,
                    "showPoints": "never"
                },
                "unit": "none",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": "Active.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": "Idle.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (id) (nginxplus_worker_connection_active{instance=~\"$instance\"}) or sum by (id) (nginxplus_workers_connections{instance=~\"$instance\", connections=\"active\"})",
                "legendFormat": "Active - Worker #{{id}}",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (id) (nginxplus_worker_connection_idle{instance=~\"$instance\"}) or sum by (id) (nginxplus_workers_connections{instance=~\"$instance\", connections=\"idle\"})",
                "legendFormat": "Idle - Worker #{{id}}",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (id) (rate(nginxplus_worker_connection_accepted{instance=~\"$instance\"}[$__rate_interval])) or sum by (id) (rate(nginxplus_workers_connections{instance=~\"$instance\", connections=\"accepted\"}[$__rate_interval]))",
                "legendFormat": "Accepted/s - Worker #{{id}}",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # Panel 13: Process & Worker Memory Footprint
    panels.append({
        "id": panel_id,
        "title": "Worker & Process Memory Footprint",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Physical resident memory (RSS), virtual/private memory, and Go runtime allocations.",
        "gridPos": {"h": 8, "w": 8, "x": 16, "y": 14},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "bytes",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "Resident Memory (RSS)"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byName", "options": "Virtual / Private Memory"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#B877D9", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byName", "options": "Go Heap In-Use"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(nginxplus_workers_mem_rss{instance=~\"$instance\"}) or sum(process_resident_memory_bytes{instance=~\"$instance\"})",
                "legendFormat": "Resident Memory (RSS)",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(nginxplus_workers_mem_private{instance=~\"$instance\"}) or sum(process_virtual_memory_bytes{instance=~\"$instance\"})",
                "legendFormat": "Virtual / Private Memory",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(go_memstats_heap_inuse_bytes{instance=~\"$instance\"})",
                "legendFormat": "Go Heap In-Use",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # =========================================================================
    # ROW 3: HTTP Server Zones
    # =========================================================================
    panels.append(make_row("HTTP Server Zones (Frontend Endpoints & Virtual Hosts)", 22))

    # Panel 14: Request Rate by Server Zone
    panels.append({
        "id": panel_id,
        "title": "Request Rate by Server Zone",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Incoming HTTP requests per second partitioned by HTTP server zone / virtual host.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 23},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "gradientMode": "opacity",
                    "showPoints": "never"
                },
                "unit": "reqps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_server_zone_requests{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{server_zone}}",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Panel 15: HTTP Status Code Classes
    panels.append({
        "id": panel_id,
        "title": "HTTP Status Code Classes by Server Zone",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "HTTP response codes categorized into classes (1xx, 2xx, 3xx, 4xx, 5xx) across server zones.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 23},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 20,
                    "showPoints": "never",
                    "stacking": {"group": "A", "mode": "normal"}
                },
                "unit": "reqps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*2xx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*3xx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*4xx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#FF9900", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*5xx.*"},
                    "properties": [
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (code) (rate(nginxplus_server_zone_responses{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{code}}",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Panel 16: HTTP Bandwidth Throughput
    panels.append({
        "id": panel_id,
        "title": "HTTP Network Bandwidth (Received vs Sent)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Network traffic volume received from clients vs transmitted back per server zone.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 31},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "Bps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Rx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Tx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_server_zone_received{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{server_zone}} (Rx Ingress)",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_server_zone_sent{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{server_zone}} (Tx Egress)",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Panel 17: HTTP Error Codes Spikes
    panels.append({
        "id": panel_id,
        "title": "HTTP Error Codes (4xx & 5xx Spikes)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Specific client error and server error codes (e.g. 400, 403, 404, 500, 502, 503, 504).",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 31},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "bars",
                    "lineWidth": 1,
                    "fillOpacity": 80,
                    "showPoints": "never",
                    "stacking": {"group": "A", "mode": "normal"}
                },
                "unit": "reqps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone, code) (rate(nginxplus_server_zone_responses_codes{instance=~\"$instance\", server_zone=~\"$server_zone\", code=~\"4..|5..\"}[$__rate_interval])) > 0",
                "legendFormat": "{{server_zone}} HTTP {{code}}",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Panel 18: HTTP Server Zones Performance Matrix Table
    panels.append({
        "id": panel_id,
        "title": "HTTP Server Zones Performance Matrix",
        "type": "table",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Detailed operational summary matrix across all active HTTP server zones.",
        "gridPos": {"h": 7, "w": 24, "x": 0, "y": 39},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "custom": {"align": "auto", "cellOptions": {"type": "auto"}, "inspect": True},
                "thresholds": {"mode": "absolute", "steps": [{"color": "green", "value": None}]}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "Requests / sec"},
                    "properties": [{"id": "unit", "value": "reqps"}]
                },
                {
                    "matcher": {"id": "byName", "options": "Discarded / sec"},
                    "properties": [
                        {"id": "unit", "value": "reqps"},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#F2495C", "value": 0.001}]}
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Bandwidth In"},
                    "properties": [{"id": "unit", "value": "Bps"}]
                },
                {
                    "matcher": {"id": "byName", "options": "Bandwidth Out"},
                    "properties": [{"id": "unit", "value": "Bps"}]
                }
            ]
        },
        "options": {
            "cellHeight": "sm",
            "footer": {"countRows": False, "fields": "", "reducer": ["sum"], "show": False},
            "sortBy": [{"desc": True, "displayName": "Requests / sec"}]
        },
        "transformations": [
            {
                "id": "joinByField",
                "options": {"byField": "server_zone", "mode": "outer"}
            },
            {
                "id": "organize",
                "options": {
                    "excludeByName": {
                        "Time": True, "Time 1": True, "Time 2": True, "Time 3": True, "Time 4": True,
                        "__name__": True, "__name__ 1": True, "__name__ 2": True, "__name__ 3": True, "__name__ 4": True,
                        "instance": True, "instance 1": True, "instance 2": True, "instance 3": True, "instance 4": True
                    },
                    "renameByName": {
                        "server_zone": "Server Zone",
                        "Value #A": "Requests / sec",
                        "Value": "Requests / sec",
                        "Value #B": "In-Flight Processing",
                        "Value #C": "Discarded / sec",
                        "Value #D": "Bandwidth In",
                        "Value #E": "Bandwidth Out"
                    }
                }
            }
        ],
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_server_zone_requests{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval]))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (nginxplus_server_zone_processing{instance=~\"$instance\", server_zone=~\"$server_zone\"}) or (0 * sum by (server_zone) (nginxplus_server_zone_requests{instance=~\"$instance\", server_zone=~\"$server_zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_server_zone_discarded{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval])) or (0 * sum by (server_zone) (nginxplus_server_zone_requests{instance=~\"$instance\", server_zone=~\"$server_zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_server_zone_received{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval])) or (0 * sum by (server_zone) (nginxplus_server_zone_requests{instance=~\"$instance\", server_zone=~\"$server_zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "D"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_server_zone_sent{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval])) or (0 * sum by (server_zone) (nginxplus_server_zone_requests{instance=~\"$instance\", server_zone=~\"$server_zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "E"
            }
        ]
    })
    panel_id += 1

    # =========================================================================
    # ROW 4: HTTP Upstreams & Backend Health
    # =========================================================================
    panels.append(make_row("HTTP Upstreams & Backend Servers", 46))

    # Panel 19: HTTP Backend Servers Status Table (Full 1-6 Enum Support!)
    panels.append({
        "id": panel_id,
        "title": "HTTP Backend Server Status & Health Check State",
        "type": "table",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Live health status, active connections, and fail counts for all HTTP upstream servers (supports UP, DRAINING, DOWN, UNAVAIL, CHECKING, UNHEALTHY).",
        "gridPos": {"h": 7, "w": 24, "x": 0, "y": 47},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "custom": {"align": "auto", "cellOptions": {"type": "auto"}, "inspect": True},
                "thresholds": {"mode": "absolute", "steps": [{"color": "green", "value": None}]}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "State"},
                    "properties": [
                        {"id": "mappings", "value": upstream_state_mapping},
                        {"id": "custom.cellOptions", "value": {"type": "color-background"}},
                        {"id": "thresholds", "value": upstream_state_thresholds}
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Active Connections"},
                    "properties": [{"id": "unit", "value": "none"}]
                },
                {
                    "matcher": {"id": "byName", "options": "Requests / sec"},
                    "properties": [{"id": "unit", "value": "reqps"}]
                },
                {
                    "matcher": {"id": "byName", "options": "Comm Failures / sec"},
                    "properties": [
                        {"id": "unit", "value": "ops"},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#F2495C", "value": 0.001}]}
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "HC Fails / sec"},
                    "properties": [
                        {"id": "unit", "value": "ops"},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#F2495C", "value": 0.001}]}
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Unavail Events (1h)"},
                    "properties": [
                        {"id": "unit", "value": "none"},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#F2495C", "value": 1}]}
                        }
                    ]
                }
            ]
        },
        "options": {
            "cellHeight": "sm",
            "footer": {"countRows": False, "fields": "", "reducer": ["sum"], "show": False},
            "sortBy": [{"desc": False, "displayName": "State"}]
        },
        "transformations": [
            {
                "id": "joinByField",
                "options": {"byField": "server", "mode": "outer"}
            },
            {
                "id": "organize",
                "options": {
                    "excludeByName": {
                        "Time": True, "Time 1": True, "Time 2": True, "Time 3": True, "Time 4": True, "Time 5": True,
                        "__name__": True, "__name__ 1": True, "__name__ 2": True, "__name__ 3": True, "__name__ 4": True, "__name__ 5": True, "__name__ 6": True,
                        "instance": True, "instance 1": True, "instance 2": True, "instance 3": True, "instance 4": True, "instance 5": True,
                        "job": True, "job 1": True, "job 2": True, "job 3": True, "job 4": True, "job 5": True,
                        "upstream 1": True, "upstream 2": True, "upstream 3": True, "upstream 4": True, "upstream 5": True
                    },
                    "indexByName": {
                        "upstream": 0,
                        "server": 1,
                        "Value #A": 2,
                        "Value": 2,
                        "Value #B": 3,
                        "Value #C": 4,
                        "Value #D": 5,
                        "Value #E": 6,
                        "Value #F": 7
                    },
                    "renameByName": {
                        "upstream": "Upstream",
                        "server": "Server",
                        "Value #A": "State",
                        "Value": "State",
                        "Value #B": "Active Connections",
                        "Value #C": "Requests / sec",
                        "Value #D": "Comm Failures / sec",
                        "Value #E": "HC Fails / sec",
                        "Value #F": "Unavail Events (1h)"
                    }
                }
            }
        ],
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "nginxplus_upstream_server_state{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "nginxplus_upstream_server_active{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"} or (0 * nginxplus_upstream_server_state{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "rate(nginxplus_upstream_server_requests{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]) or (0 * nginxplus_upstream_server_state{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "rate(nginxplus_upstream_server_fails{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]) or (0 * nginxplus_upstream_server_state{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "D"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "rate(nginxplus_upstream_server_health_checks_fails{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]) or (0 * nginxplus_upstream_server_state{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "E"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "increase(nginxplus_upstream_server_unavail{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[1h]) or (0 * nginxplus_upstream_server_state{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "F"
            }
        ]
    })
    panel_id += 1

    # Panel 20: HTTP Backend Request Rate by Server
    panels.append({
        "id": panel_id,
        "title": "HTTP Backend Request Rate by Server",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Load distribution across individual upstream backend servers.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 54},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never",
                    "stacking": {"group": "A", "mode": "normal"}
                },
                "unit": "reqps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_upstream_server_requests{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]))",
                "legendFormat": "{{upstream}} -> {{server}}",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Panel 21: HTTP Latency Percentiles (P50, P90, P99)
    panels.append({
        "id": panel_id,
        "title": "HTTP Upstream Latency Percentiles (P50, P90, P99)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Upstream response latency percentiles (P50, P90, P99) if histogram buckets are exposed, with automatic fallback to Max, Avg, Min response times and Header TTFB from nginx-prometheus-exporter.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 54},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 10,
                    "showPoints": "never"
                },
                "unit": "ms",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*P99.*|.*Max.*"},
                    "properties": [
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*P90.*|.*Avg.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#FF9900", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*P50.*|.*TTFB.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Min.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "(histogram_quantile(0.99, sum by (le, upstream) (rate(nginxplus_upstream_server_response_time_hist_bucket{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]))) * 1000) or max by (upstream) (nginxplus_upstream_server_response_time{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "legendFormat": "{{upstream}} P99 / Max Latency",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "(histogram_quantile(0.90, sum by (le, upstream) (rate(nginxplus_upstream_server_response_time_hist_bucket{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]))) * 1000) or avg by (upstream) (nginxplus_upstream_server_response_time{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "legendFormat": "{{upstream}} P90 / Avg Latency",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "(histogram_quantile(0.50, sum by (le, upstream) (rate(nginxplus_upstream_server_response_time_hist_bucket{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]))) * 1000) or avg by (upstream) (nginxplus_upstream_server_header_time{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "legendFormat": "{{upstream}} P50 / Header TTFB",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "min by (upstream) (nginxplus_upstream_server_response_time{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "legendFormat": "{{upstream}} Min Latency",
                "refId": "D"
            }
        ]
    })
    panel_id += 1

    # Panel 22: HTTP Response Time vs Header TTFB Time
    panels.append({
        "id": panel_id,
        "title": "HTTP Response Time vs Header TTFB Time",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Average time to receive first response header (TTFB) vs total upstream response completion time.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 62},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 10,
                    "showPoints": "never"
                },
                "unit": "ms",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "avg by (upstream, server) (nginxplus_upstream_server_header_time{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "legendFormat": "{{upstream}} [{{server}}] - Header TTFB",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "avg by (upstream, server) (nginxplus_upstream_server_response_time{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"})",
                "legendFormat": "{{upstream}} [{{server}}] - Total Response",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Panel 23: HTTP Health Check Probes & Failures
    panels.append({
        "id": panel_id,
        "title": "HTTP Health Check Probes & Failures",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Active synthetic health checks executed and failures detected per backend server.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 62},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "linear",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "ops",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Fails.*"},
                    "properties": [
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Unhealthy.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#FF9900", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Checks.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_upstream_server_health_checks_checks{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} Checks / sec",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_upstream_server_health_checks_fails{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} HC Fails / sec",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_upstream_server_health_checks_unhealthy{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} Transitions to Unhealthy",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # Panel 24: HTTP Upstream Bandwidth Throughput
    panels.append({
        "id": panel_id,
        "title": "HTTP Upstream Bandwidth Throughput",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Data sent to and received from upstream backend servers.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 70},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "Bps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_upstream_server_received{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} (Rx from Backend)",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_upstream_server_sent{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} (Tx to Backend)",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Panel 25: HTTP Upstream Keepalive Pools & Zombie Backends
    panels.append({
        "id": panel_id,
        "title": "HTTP Upstream Keepalive Pools & Zombie Backends",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Idle keepalive connections maintained with backends, and zombie servers being drained after reload.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 70},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "none",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Keepalive.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Zombie.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#FF9900", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream) (nginxplus_upstream_keepalive{instance=~\"$instance\", upstream=~\"$upstream\"})",
                "legendFormat": "{{upstream}} Keepalive Idle",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream) (nginxplus_upstream_zombies{instance=~\"$instance\", upstream=~\"$upstream\"})",
                "legendFormat": "{{upstream}} Zombie Servers",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Panel 26: HTTP Upstream Response Codes
    panels.append({
        "id": panel_id,
        "title": "HTTP Upstream Response Codes (2xx, 3xx, 4xx, 5xx)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Status codes returned directly by upstream backend servers.",
        "gridPos": {"h": 7, "w": 24, "x": 0, "y": 78},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 20,
                    "showPoints": "never",
                    "stacking": {"group": "A", "mode": "normal"}
                },
                "unit": "reqps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*2xx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*3xx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*4xx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#FF9900", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*5xx.*"},
                    "properties": [
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (code) (rate(nginxplus_upstream_server_responses{instance=~\"$instance\", upstream=~\"$upstream\", server=~\"$server\"}[$__rate_interval]))",
                "legendFormat": "HTTP {{code}}",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # =========================================================================
    # ROW 5: Stream Server Zones
    # =========================================================================
    panels.append(make_row("Stream Server Zones (L4 TCP/UDP Frontend Proxies)", 85))

    # Panel 27: Stream Connections Rate by Zone
    panels.append({
        "id": panel_id,
        "title": "Stream Connections Rate by Zone",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Incoming TCP/UDP connections per second across stream server zones.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 86},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "gradientMode": "opacity",
                    "showPoints": "never"
                },
                "unit": "cps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_stream_server_zone_connections{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{server_zone}}",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Panel 28: Stream Sessions Completed by Status Code
    panels.append({
        "id": panel_id,
        "title": "Stream Sessions Completed by Status Code",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Completed L4 TCP/UDP sessions categorized by status code classes (2xx success, 4xx client errors, 5xx backend errors).",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 86},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 20,
                    "showPoints": "never",
                    "stacking": {"group": "A", "mode": "normal"}
                },
                "unit": "ops",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*2xx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*4xx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#FF9900", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*5xx.*"},
                    "properties": [
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (code) (rate(nginxplus_stream_server_zone_sessions{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{code}}",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Panel 29: Stream Bandwidth Throughput
    panels.append({
        "id": panel_id,
        "title": "Stream Bandwidth Throughput (Received vs Sent)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Network traffic volume received from stream clients vs transmitted back per stream server zone.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 94},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "Bps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Rx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Tx.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_stream_server_zone_received{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{server_zone}} (Rx Ingress)",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_stream_server_zone_sent{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{server_zone}} (Tx Egress)",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Panel 30: Stream Active Processing & Discarded Connections
    panels.append({
        "id": panel_id,
        "title": "Stream Active Processing & Discarded Connections",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Active in-flight stream connections alongside discarded connections per zone.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 94},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "linear",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "none",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Processing.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Discarded.*"},
                    "properties": [
                        {"id": "unit", "value": "cps"},
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (nginxplus_stream_server_zone_processing{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"})",
                "legendFormat": "{{server_zone}} In-Flight Processing",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_stream_server_zone_discarded{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{server_zone}} Discarded / sec",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Panel 31: Stream Server Zones Performance Matrix
    panels.append({
        "id": panel_id,
        "title": "Stream Server Zones Performance Matrix",
        "type": "table",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Comprehensive summary table for L4 TCP/UDP stream server zones.",
        "gridPos": {"h": 7, "w": 24, "x": 0, "y": 102},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "custom": {"align": "auto", "cellOptions": {"type": "auto"}, "inspect": True},
                "thresholds": {"mode": "absolute", "steps": [{"color": "green", "value": None}]}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "Connections / sec"},
                    "properties": [{"id": "unit", "value": "cps"}]
                },
                {
                    "matcher": {"id": "byName", "options": "Discarded / sec"},
                    "properties": [
                        {"id": "unit", "value": "cps"},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#F2495C", "value": 0.001}]}
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Bandwidth In"},
                    "properties": [{"id": "unit", "value": "Bps"}]
                },
                {
                    "matcher": {"id": "byName", "options": "Bandwidth Out"},
                    "properties": [{"id": "unit", "value": "Bps"}]
                }
            ]
        },
        "options": {
            "cellHeight": "sm",
            "footer": {"countRows": False, "fields": "", "reducer": ["sum"], "show": False},
            "sortBy": [{"desc": True, "displayName": "Connections / sec"}]
        },
        "transformations": [
            {
                "id": "joinByField",
                "options": {"byField": "server_zone", "mode": "outer"}
            },
            {
                "id": "organize",
                "options": {
                    "excludeByName": {
                        "Time": True, "Time 1": True, "Time 2": True, "Time 3": True, "Time 4": True,
                        "__name__": True, "__name__ 1": True, "__name__ 2": True, "__name__ 3": True, "__name__ 4": True,
                        "instance": True, "instance 1": True, "instance 2": True, "instance 3": True, "instance 4": True
                    },
                    "renameByName": {
                        "server_zone": "Stream Zone",
                        "Value #A": "Connections / sec",
                        "Value": "Connections / sec",
                        "Value #B": "Active Processing",
                        "Value #C": "Discarded / sec",
                        "Value #D": "Bandwidth In",
                        "Value #E": "Bandwidth Out"
                    }
                }
            }
        ],
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_stream_server_zone_connections{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval]))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (nginxplus_stream_server_zone_processing{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}) or (0 * sum by (server_zone) (nginxplus_stream_server_zone_connections{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_stream_server_zone_discarded{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval])) or (0 * sum by (server_zone) (nginxplus_stream_server_zone_connections{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_stream_server_zone_received{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval])) or (0 * sum by (server_zone) (nginxplus_stream_server_zone_connections{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "D"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_stream_server_zone_sent{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval])) or (0 * sum by (server_zone) (nginxplus_stream_server_zone_connections{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "E"
            }
        ]
    })
    panel_id += 1

    # =========================================================================
    # ROW 6: Stream Upstreams & TCP/UDP Backends
    # =========================================================================
    panels.append(make_row("Stream Upstreams & TCP/UDP Backend Servers", 109))

    # Panel 32: Stream Backend Server Status Table (Full 1-6 Enum Support!)
    panels.append({
        "id": panel_id,
        "title": "Stream Backend Server Status & Availability Matrix",
        "type": "table",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Live health status, active connections, and fail counts for all Stream upstream backend targets (supports UP, DRAINING, DOWN, UNAVAIL, CHECKING, UNHEALTHY).",
        "gridPos": {"h": 7, "w": 24, "x": 0, "y": 110},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "custom": {"align": "auto", "cellOptions": {"type": "auto"}, "inspect": True},
                "thresholds": {"mode": "absolute", "steps": [{"color": "green", "value": None}]}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "State"},
                    "properties": [
                        {"id": "mappings", "value": upstream_state_mapping},
                        {"id": "custom.cellOptions", "value": {"type": "color-background"}},
                        {"id": "thresholds", "value": upstream_state_thresholds}
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Active Connections"},
                    "properties": [{"id": "unit", "value": "none"}]
                },
                {
                    "matcher": {"id": "byName", "options": "Forwarded Conns / sec"},
                    "properties": [{"id": "unit", "value": "cps"}]
                },
                {
                    "matcher": {"id": "byName", "options": "Comm Failures / sec"},
                    "properties": [
                        {"id": "unit", "value": "ops"},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#F2495C", "value": 0.001}]}
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "HC Fails / sec"},
                    "properties": [
                        {"id": "unit", "value": "ops"},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#F2495C", "value": 0.001}]}
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Unavail Events (1h)"},
                    "properties": [
                        {"id": "unit", "value": "none"},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#F2495C", "value": 1}]}
                        }
                    ]
                }
            ]
        },
        "options": {
            "cellHeight": "sm",
            "footer": {"countRows": False, "fields": "", "reducer": ["sum"], "show": False},
            "sortBy": [{"desc": False, "displayName": "State"}]
        },
        "transformations": [
            {
                "id": "joinByField",
                "options": {"byField": "server", "mode": "outer"}
            },
            {
                "id": "organize",
                "options": {
                    "excludeByName": {
                        "Time": True, "Time 1": True, "Time 2": True, "Time 3": True, "Time 4": True, "Time 5": True,
                        "__name__": True, "__name__ 1": True, "__name__ 2": True, "__name__ 3": True, "__name__ 4": True, "__name__ 5": True, "__name__ 6": True,
                        "instance": True, "instance 1": True, "instance 2": True, "instance 3": True, "instance 4": True, "instance 5": True,
                        "job": True, "job 1": True, "job 2": True, "job 3": True, "job 4": True, "job 5": True,
                        "upstream 1": True, "upstream 2": True, "upstream 3": True, "upstream 4": True, "upstream 5": True
                    },
                    "indexByName": {
                        "upstream": 0,
                        "server": 1,
                        "Value #A": 2,
                        "Value": 2,
                        "Value #B": 3,
                        "Value #C": 4,
                        "Value #D": 5,
                        "Value #E": 6,
                        "Value #F": 7
                    },
                    "renameByName": {
                        "upstream": "Upstream",
                        "server": "Server",
                        "Value #A": "State",
                        "Value": "State",
                        "Value #B": "Active Connections",
                        "Value #C": "Forwarded Conns / sec",
                        "Value #D": "Comm Failures / sec",
                        "Value #E": "HC Fails / sec",
                        "Value #F": "Unavail Events (1h)"
                    }
                }
            }
        ],
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "nginxplus_stream_upstream_server_state{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "nginxplus_stream_upstream_server_active{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"} or (0 * nginxplus_stream_upstream_server_state{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"})",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "rate(nginxplus_stream_upstream_server_connections{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[$__rate_interval]) or (0 * nginxplus_stream_upstream_server_state{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"})",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "rate(nginxplus_stream_upstream_server_fails{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[$__rate_interval]) or (0 * nginxplus_stream_upstream_server_state{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"})",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "D"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "rate(nginxplus_stream_upstream_server_health_checks_fails{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[$__rate_interval]) or (0 * nginxplus_stream_upstream_server_state{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"})",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "E"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "increase(nginxplus_stream_upstream_server_unavail{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[1h]) or (0 * nginxplus_stream_upstream_server_state{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"})",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "F"
            }
        ]
    })
    panel_id += 1

    # Panel 33: Stream Forwarded Connections Rate by Server
    panels.append({
        "id": panel_id,
        "title": "Stream Forwarded Connections Rate by Server",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "L4 connections forwarded per second to each stream backend target.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 117},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never",
                    "stacking": {"group": "A", "mode": "normal"}
                },
                "unit": "cps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_stream_upstream_server_connections{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[$__rate_interval]))",
                "legendFormat": "{{upstream}} -> {{server}}",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Panel 34: Stream Latency (Connect Time, First Byte, Response Time)
    panels.append({
        "id": panel_id,
        "title": "Stream Latency: Connect Time, First Byte, Response Time",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "TCP connection establishment time, first byte received, and full session response time in milliseconds.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 117},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 10,
                    "showPoints": "never"
                },
                "unit": "ms",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Connect.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*First Byte.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#FF9900", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Response.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "avg by (upstream, server) (nginxplus_stream_upstream_server_connect_time{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"})",
                "legendFormat": "{{server}} Connect Time",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "avg by (upstream, server) (nginxplus_stream_upstream_server_first_byte_time{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"})",
                "legendFormat": "{{server}} First Byte Time",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "avg by (upstream, server) (nginxplus_stream_upstream_server_response_time{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"})",
                "legendFormat": "{{server}} Response Time",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # Panel 35: Stream Upstream Bandwidth Throughput
    panels.append({
        "id": panel_id,
        "title": "Stream Upstream Bandwidth Throughput",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Data sent to and received from stream backend targets per second.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 125},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "Bps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_stream_upstream_server_received{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} (Rx from Backend)",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_stream_upstream_server_sent{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} (Tx to Backend)",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Panel 36: Stream Health Check Probes & Failures
    panels.append({
        "id": panel_id,
        "title": "Stream Health Check Probes & Failures",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Active synthetic TCP/UDP health checks executed and failures detected per stream backend.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 125},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "linear",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "ops",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Fails.*"},
                    "properties": [
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Unhealthy.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#FF9900", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Checks.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_stream_upstream_server_health_checks_checks{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} Checks / sec",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_stream_upstream_server_health_checks_fails{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} HC Fails / sec",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_stream_upstream_server_health_checks_unhealthy{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} Transitions to Unhealthy",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # Panel 37: Stream Active Connections, Zombies & Unavailability
    panels.append({
        "id": panel_id,
        "title": "Stream Active Connections, Zombies & Unavailability",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Active in-flight TCP/UDP connections per server, zombie servers being drained, and unavailability events.",
        "gridPos": {"h": 7, "w": 24, "x": 0, "y": 133},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 10,
                    "showPoints": "never"
                },
                "unit": "none",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Active.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Zombie.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#FF9900", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Unavail.*"},
                    "properties": [
                        {"id": "unit", "value": "ops"},
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (nginxplus_stream_upstream_server_active{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"})",
                "legendFormat": "{{server}} Active Conns",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream) (nginxplus_stream_upstream_zombies{instance=~\"$instance\", upstream=~\"$stream_upstream\"})",
                "legendFormat": "{{upstream}} Zombie Backends",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (upstream, server) (rate(nginxplus_stream_upstream_server_unavail{instance=~\"$instance\", upstream=~\"$stream_upstream\", server=~\"$stream_server\"}[$__rate_interval]))",
                "legendFormat": "{{server}} Unavail Events / sec",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # =========================================================================
    # ROW 7: SSL / TLS Handshakes & Security
    # =========================================================================
    panels.append(make_row("SSL / TLS Handshakes & Certificate Security", 140))

    # Panel 38: SSL Handshakes vs Reuses (Global)
    panels.append({
        "id": panel_id,
        "title": "SSL/TLS Handshake Rate & Session Reuses (Global)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Total SSL handshakes completed and session resumption rate (caching/tickets).",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 141},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "ops",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "Handshakes / sec"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byName", "options": "Session Reuses / sec"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_handshakes{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Handshakes / sec",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_session_reuses{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Session Reuses / sec",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Panel 39: SSL Handshakes & Failures by Server Zone
    panels.append({
        "id": panel_id,
        "title": "SSL Handshakes & Reuses by Server Zone (HTTP & Stream)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "SSL negotiation activity broken down per frontend virtual host and Stream TCP/UDP proxy.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 141},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "ops",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Failed.*"},
                    "properties": [
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_server_zone_ssl_handshakes{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval])) or sum by (server_zone) (rate(nginxplus_stream_server_zone_ssl_handshakes{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{server_zone}} Handshakes",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_server_zone_ssl_session_reuses{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval])) or sum by (server_zone) (rate(nginxplus_stream_server_zone_ssl_session_reuses{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{server_zone}} Session Reuses",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (server_zone) (rate(nginxplus_server_zone_ssl_handshakes_failed{instance=~\"$instance\", server_zone=~\"$server_zone\"}[$__rate_interval])) or sum by (server_zone) (rate(nginxplus_stream_server_zone_ssl_handshakes_failed{instance=~\"$instance\", server_zone=~\"$stream_server_zone\"}[$__rate_interval]))",
                "legendFormat": "{{server_zone}} Failed Handshakes",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # Panel 40: SSL Handshake Failure Causes
    panels.append({
        "id": panel_id,
        "title": "SSL Handshake Failure Root Causes",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "SSL negotiation errors categorized by protocol mismatch, cipher incompatibility, timeout, or peer rejection.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 149},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "linear",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "ops",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_handshakes_failed{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Total Handshakes Failed",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_no_common_protocol{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "No Common Protocol",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_no_common_cipher{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "No Common Cipher",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_handshake_timeout{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Handshake Timeout",
                "refId": "D"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_peer_rejected_cert{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Peer Rejected Cert",
                "refId": "E"
            }
        ]
    })
    panel_id += 1

    # Panel 41: Client Certificate Verification Failures
    panels.append({
        "id": panel_id,
        "title": "Client Certificate Verification Failures (mTLS / Client Auth)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Mutual TLS (mTLS) client certificate verification failures categorized by error type.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 149},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "bars",
                    "lineWidth": 1,
                    "fillOpacity": 80,
                    "showPoints": "never",
                    "stacking": {"group": "A", "mode": "normal"}
                },
                "unit": "ops",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_verify_failures_expired_cert{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Expired Certificate",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_verify_failures_revoked_cert{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Revoked Certificate",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_verify_failures_no_cert{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "No Certificate Provided",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_verify_failures_hostname_mismatch{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Hostname Mismatch",
                "refId": "D"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(nginxplus_ssl_verify_failures_other{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Other Validation Errors",
                "refId": "E"
            }
        ]
    })
    panel_id += 1

    # =========================================================================
    # ROW 8: Traffic Rate Limiting & Connection Limiting (NEW!)
    # =========================================================================
    panels.append(make_row("Traffic Rate Limiting & Connection Limiting (limit_req & limit_conn)", 157))

    # Panel 42: HTTP Rate Limiting Dynamics (limit_req)
    panels.append({
        "id": panel_id,
        "title": "HTTP Rate Limiting Dynamics (limit_req)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Traffic rate limiting dynamics showing passed, delayed (burst queue), and rejected (burst exceeded) requests per limit zone.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 158},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "reqps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Passed.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Delayed.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#EAB839", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Rejected.*"},
                    "properties": [
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Dry-Run.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_request_passed{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Passed - {{zone}}",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_request_delayed{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Delayed (Burst) - {{zone}}",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_request_rejected{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Rejected - {{zone}}",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_request_delayed_dry_run{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Delayed (Dry-Run) - {{zone}}",
                "refId": "D"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_request_rejected_dry_run{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Rejected (Dry-Run) - {{zone}}",
                "refId": "E"
            }
        ]
    })
    panel_id += 1

    # Panel 43: Connection Limiting Dynamics (limit_conn)
    panels.append({
        "id": panel_id,
        "title": "Connection Limiting Dynamics (limit_conn)",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Concurrent client connection limiting dynamics showing passed and rejected connections per limit_conn zone.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 158},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "cps",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*Passed.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Rejected.*"},
                    "properties": [
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Dry-Run.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#B877D9", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_connection_passed{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Conn Passed - {{zone}}",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_connection_rejected{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Conn Rejected - {{zone}}",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_connection_rejected_dry_run{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Conn Rejected (Dry-Run) - {{zone}}",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # Panel 44: Rate & Connection Limiting Performance Matrix (Table)
    panels.append({
        "id": panel_id,
        "title": "Rate & Connection Limiting Operational Matrix",
        "type": "table",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Per-zone audit table for traffic shaping, rate limits, and concurrency limiting enforcement.",
        "gridPos": {"h": 7, "w": 24, "x": 0, "y": 166},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "custom": {"align": "auto", "cellOptions": {"type": "auto"}, "inspect": True},
                "thresholds": {"mode": "absolute", "steps": [{"color": "green", "value": None}]}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "Req Passed / sec"},
                    "properties": [{"id": "unit", "value": "reqps"}]
                },
                {
                    "matcher": {"id": "byName", "options": "Req Delayed / sec"},
                    "properties": [
                        {"id": "unit", "value": "reqps"},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#EAB839", "value": 0.001}]}
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Req Rejected / sec"},
                    "properties": [
                        {"id": "unit", "value": "reqps"},
                        {"id": "custom.cellOptions", "value": {"type": "color-background"}},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#F2495C", "value": 0.001}]}
                        }
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Conn Passed / sec"},
                    "properties": [{"id": "unit", "value": "cps"}]
                },
                {
                    "matcher": {"id": "byName", "options": "Conn Rejected / sec"},
                    "properties": [
                        {"id": "unit", "value": "cps"},
                        {"id": "custom.cellOptions", "value": {"type": "color-background"}},
                        {
                            "id": "thresholds",
                            "value": {"mode": "absolute", "steps": [{"color": "#73BF69", "value": None}, {"color": "#F2495C", "value": 0.001}]}
                        }
                    ]
                }
            ]
        },
        "options": {
            "cellHeight": "sm",
            "footer": {"countRows": False, "fields": "", "reducer": ["sum"], "show": False},
            "sortBy": [{"desc": True, "displayName": "Req Passed / sec"}]
        },
        "transformations": [
            {
                "id": "joinByField",
                "options": {"byField": "zone", "mode": "outer"}
            },
            {
                "id": "organize",
                "options": {
                    "excludeByName": {
                        "Time": True, "Time 1": True, "Time 2": True, "Time 3": True, "Time 4": True,
                        "__name__": True, "__name__ 1": True, "__name__ 2": True, "__name__ 3": True, "__name__ 4": True,
                        "instance": True, "instance 1": True, "instance 2": True, "instance 3": True, "instance 4": True
                    },
                    "renameByName": {
                        "zone": "Limit Zone",
                        "Value #A": "Req Passed / sec",
                        "Value": "Req Passed / sec",
                        "Value #B": "Req Delayed / sec",
                        "Value #C": "Req Rejected / sec",
                        "Value #D": "Conn Passed / sec",
                        "Value #E": "Conn Rejected / sec"
                    }
                }
            }
        ],
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_request_passed{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_request_delayed{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval])) or (0 * sum by (zone) (nginxplus_limit_request_passed{instance=~\"$instance\", zone=~\"$zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_request_rejected{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval])) or (0 * sum by (zone) (nginxplus_limit_request_passed{instance=~\"$instance\", zone=~\"$zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_connection_passed{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "D"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_connection_rejected{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval])) or (0 * sum by (zone) (nginxplus_limit_connection_passed{instance=~\"$instance\", zone=~\"$zone\"}))",
                "format": "table",
                "instant": True,
                "legendFormat": "",
                "refId": "E"
            }
        ]
    })
    panel_id += 1

    # =========================================================================
    # ROW 9: Shared Memory Zones (Slab Allocator)
    # =========================================================================
    panels.append(make_row("Shared Memory Zones & Process Memory (Slab Allocator)", 173))

    # Panel 45: Slab Page Memory Usage (%) per Zone & Process Memory
    panels.append({
        "id": panel_id,
        "title": "Shared Memory Zone Slab Page Usage (%) & Process Memory",
        "type": "bargauge",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Percentage of allocated memory pages currently used in each shared memory zone (via NJS/API) or NGINX Process RSS vs Virtual Memory footprint (via nginx-prometheus-exporter).",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 174},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [],
                "max": 100,
                "min": 0,
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "#73BF69", "value": None},
                        {"color": "#EAB839", "value": 70},
                        {"color": "#F2495C", "value": 85}
                    ]
                },
                "unit": "percent"
            },
            "overrides": []
        },
        "options": {
            "displayMode": "gradient",
            "orientation": "horizontal",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "showUnfilled": True
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "((nginxplus_slab_pages_used{instance=~\"$instance\", zone=~\"$zone\"} / (nginxplus_slab_pages_used{instance=~\"$instance\", zone=~\"$zone\"} + nginxplus_slab_pages_free{instance=~\"$instance\", zone=~\"$zone\"})) * 100) or ((process_resident_memory_bytes{instance=~\"$instance\"} / process_virtual_memory_bytes{instance=~\"$instance\"}) * 100)",
                "legendFormat": "{{zone}}{{instance}} Memory Usage (%)",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "((go_memstats_heap_inuse_bytes{instance=~\"$instance\"} / go_memstats_sys_bytes{instance=~\"$instance\"}) * 100)",
                "legendFormat": "{{instance}} Exporter Heap Utilization (%)",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Panel 46: Slab Allocation Failures & Saturation Alerts
    panels.append({
        "id": panel_id,
        "title": "Slab Allocation Failures & Saturation Alerts",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Failed memory allocation attempts inside shared memory zones (indicates zone size needs to be increased). Defaults to 0 baseline when scraped via nginx-prometheus-exporter.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 174},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "linear",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "auto"
                },
                "unit": "ops",
                "color": {"mode": "thresholds"},
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "#73BF69", "value": None},
                        {"color": "#F2495C", "value": 0.001}
                    ]
                }
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone, slot) (rate(nginxplus_slab_fails{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval])) or (0 * sum by (instance) (process_resident_memory_bytes{instance=~\"$instance\"}))",
                "legendFormat": "{{zone}} Allocation Failures / sec",
                "refId": "A"
            }
        ]
    })
    panel_id += 1

    # Panel 47: Shared Memory Zone Operations & Slab Request Rate
    panels.append({
        "id": panel_id,
        "title": "Shared Memory Zone Operations & Slab Request Rate",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Shared memory zone request rate and slot allocation attempts (8B to 2048B) or limit zone operational rates from nginx-prometheus-exporter.",
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 182},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 10,
                    "showPoints": "never",
                    "stacking": {"group": "A", "mode": "normal"}
                },
                "unit": "ops",
                "color": {"mode": "palette-classic"}
            },
            "overrides": []
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (slot) (rate(nginxplus_slab_reqs{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Slot {{slot}}B Req/s",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_request_passed{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Zone {{zone}} Request Rate",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (zone) (rate(nginxplus_limit_connection_passed{instance=~\"$instance\", zone=~\"$zone\"}[$__rate_interval]))",
                "legendFormat": "Zone {{zone}} Connection Rate",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # Panel 48: Process Memory Footprint & Slab Slot Usage
    panels.append({
        "id": panel_id,
        "title": "Process Memory Footprint & Slab Slot Allocation",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Process Resident Set Size (RSS) physical memory and virtual memory from nginx-prometheus-exporter, alongside slab slot counts when available.",
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 182},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 10,
                    "showPoints": "never"
                },
                "unit": "bytes",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byRegexp", "options": ".*RSS.*|.*Used.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byRegexp", "options": ".*Virtual.*|.*Free.*"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "process_resident_memory_bytes{instance=~\"$instance\"} or sum(nginxplus_workers_mem_rss{instance=~\"$instance\"})",
                "legendFormat": "{{instance}} Process RSS Memory",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "process_virtual_memory_bytes{instance=~\"$instance\"}",
                "legendFormat": "{{instance}} Process Virtual Memory",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (slot) (nginxplus_slab_used{instance=~\"$instance\", zone=~\"$zone\"})",
                "legendFormat": "Slot {{slot}}B (Used)",
                "refId": "C"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum by (slot) (nginxplus_slab_free{instance=~\"$instance\", zone=~\"$zone\"})",
                "legendFormat": "Slot {{slot}}B (Free)",
                "refId": "D"
            }
        ]
    })
    panel_id += 1

    # =========================================================================
    # ROW 10: Prometheus Exporter & Go Runtime Observability (NEW!)
    # =========================================================================
    panels.append(make_row("Prometheus Exporter & Go Runtime Observability", 190))

    # Panel 49: Exporter Health & Scrape KPIs (Stat)
    panels.append({
        "id": panel_id,
        "title": "Exporter Scrape Status & Health",
        "type": "stat",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "NGINX Plus Prometheus exporter scrape target health, scrape request rate, and build info.",
        "gridPos": {"h": 8, "w": 6, "x": 0, "y": 191},
        "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": "auto"
        },
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [
                    {
                        "options": {
                            "0": {"color": "#F2495C", "index": 0, "text": "DOWN"},
                            "1": {"color": "#73BF69", "index": 1, "text": "HEALTHY (UP)"}
                        },
                        "type": "value"
                    }
                ],
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "#F2495C", "value": None},
                        {"color": "#73BF69", "value": 1}
                    ]
                },
                "unit": "none"
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "Scrapes / sec"},
                    "properties": [{"id": "unit", "value": "reqps"}]
                }
            ]
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "nginxplus_up{instance=~\"$instance\"}",
                "instant": True,
                "legendFormat": "Exporter Target Status",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(promhttp_metric_handler_requests_total{instance=~\"$instance\"}[$__rate_interval]))",
                "instant": True,
                "legendFormat": "Scrapes / sec",
                "refId": "B"
            }
        ]
    })
    panel_id += 1

    # Panel 50: Exporter Process CPU & System Resources
    panels.append({
        "id": panel_id,
        "title": "Exporter Process CPU & System Resources",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "CPU core utilization and resident/virtual memory footprint of the exporter process.",
        "gridPos": {"h": 8, "w": 6, "x": 6, "y": 191},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 15,
                    "showPoints": "never"
                },
                "unit": "bytes",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "CPU Core Usage"},
                    "properties": [
                        {"id": "unit", "value": "percentunit"},
                        {"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "Process RSS Memory"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byName", "options": "Process Virtual Memory"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#B877D9", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(process_cpu_seconds_total{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "CPU Core Usage",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(process_resident_memory_bytes{instance=~\"$instance\"})",
                "legendFormat": "Process RSS Memory",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(process_virtual_memory_bytes{instance=~\"$instance\"})",
                "legendFormat": "Process Virtual Memory",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # Panel 51: Go Goroutines, Threads & File Descriptors
    panels.append({
        "id": panel_id,
        "title": "Go Goroutines, Threads & Open File Descriptors",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Active Go runtime goroutines, operating system threads, and open file descriptors.",
        "gridPos": {"h": 8, "w": 6, "x": 12, "y": 191},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 10,
                    "showPoints": "never"
                },
                "unit": "none",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "Goroutines"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byName", "options": "OS Threads"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byName", "options": "Open File Descriptors"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#FF9900", "mode": "fixed"}}]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(go_goroutines{instance=~\"$instance\"})",
                "legendFormat": "Goroutines",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(go_threads{instance=~\"$instance\"})",
                "legendFormat": "OS Threads",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(process_open_fds{instance=~\"$instance\"})",
                "legendFormat": "Open File Descriptors",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    # Panel 52: Go GC Latency & Memory Allocations
    panels.append({
        "id": panel_id,
        "title": "Go GC Pause Latency & Allocations Rate",
        "type": "timeseries",
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Garbage collection stop-the-world pause quantiles (P50, Max) and heap allocation rate.",
        "gridPos": {"h": 8, "w": 6, "x": 18, "y": 191},
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "drawStyle": "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": 10,
                    "showPoints": "never"
                },
                "unit": "s",
                "color": {"mode": "palette-classic"}
            },
            "overrides": [
                {
                    "matcher": {"id": "byName", "options": "GC Pause (Max)"},
                    "properties": [
                        {"id": "color", "value": {"fixedColor": "#F2495C", "mode": "fixed"}},
                        {"id": "custom.lineWidth", "value": 3}
                    ]
                },
                {
                    "matcher": {"id": "byName", "options": "GC Pause (P50)"},
                    "properties": [{"id": "color", "value": {"fixedColor": "#73BF69", "mode": "fixed"}}]
                },
                {
                    "matcher": {"id": "byName", "options": "Heap Alloc Rate"},
                    "properties": [
                        {"id": "unit", "value": "Bps"},
                        {"id": "color", "value": {"fixedColor": "#5794F2", "mode": "fixed"}}
                    ]
                }
            ]
        },
        "options": {
            "tooltip": {"mode": "multi", "sort": "desc"},
            "legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "lastNotNull", "max"]}
        },
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "max(go_gc_duration_seconds{quantile=\"1\", instance=~\"$instance\"})",
                "legendFormat": "GC Pause (Max)",
                "refId": "A"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "avg(go_gc_duration_seconds{quantile=\"0.5\", instance=~\"$instance\"})",
                "legendFormat": "GC Pause (P50)",
                "refId": "B"
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "sum(rate(go_memstats_alloc_bytes_total{instance=~\"$instance\"}[$__rate_interval]))",
                "legendFormat": "Heap Alloc Rate",
                "refId": "C"
            }
        ]
    })
    panel_id += 1

    dashboard["panels"] = panels
    return dashboard

if __name__ == "__main__":
    dash = create_dashboard()
    output_path = "nginx-plus-overview.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dash, f, indent=2)
    print(f"Generated enterprise dashboard '{output_path}' successfully with {len(dash['panels'])} panels across 10 functional rows.")
