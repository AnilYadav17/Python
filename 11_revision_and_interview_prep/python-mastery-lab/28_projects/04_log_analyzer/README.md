# Project 04: High-Performance Streaming Log Analyzer

A production-style log analysis engine capable of processing gigabyte-scale web server access logs with constant $O(1)$ memory consumption using Python generator pipelines.

---

## Key Features
- **Streaming Generator Pipeline**: Uses `yield` to process log lines one by one without buffering files in RAM.
- **Regex Extraction**: Fast pattern parsing of Common and Combined Log Format (Apache, Nginx, Traefik).
- **Aggregated Analytics**: Total hits, unique visitors, status code distribution (2xx, 4xx, 5xx), error rate %, and top endpoints.
- **Dual Output**: Formatted console summary and machine-readable JSON output.

---

## Usage

### 1. Terminal Report
```bash
python log_analyzer.py /var/log/nginx/access.log --top 10
```

### 2. JSON Output
```bash
python log_analyzer.py access.log --json > metrics.json
```

---

## Testing
Run automated unit tests:
```bash
python -m unittest test_log_analyzer.py
```
