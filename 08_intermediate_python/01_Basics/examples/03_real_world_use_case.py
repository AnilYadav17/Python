"""
03_real_world_use_case.py
Real-world scenario: Processing raw server access logs.
Demonstrates:
- String manipulation and parsing (.split, .strip, f-strings)
- Data type conversion and validation
- Dictionaries for frequency aggregation
- Sets for unique IP / user tracking
- List and Dict comprehensions for analytics reporting
"""

# Simulated raw server log entries: "TIMESTAMP | IP | STATUS_CODE | RESPONSE_TIME_MS | PATH"
RAW_LOGS = [
    "2026-09-05T08:00:01 | 192.168.1.10 | 200 | 45.2 | /api/v1/users",
    "2026-09-05T08:00:02 | 192.168.1.11 | 404 | 12.0 | /unknown",
    "2026-09-05T08:00:03 | 192.168.1.10 | 200 | 110.5 | /api/v1/products",
    "2026-09-05T08:00:04 | 192.168.1.12 | 500 | 320.1 | /api/v1/checkout",
    "2026-09-05T08:00:05 | 192.168.1.10 | 200 | 50.8 | /api/v1/users",
    "2026-09-05T08:00:06 | 192.168.1.13 | 200 | 25.0 | /health",
    "2026-09-05T08:00:07 | 192.168.1.12 | 200 | 95.4 | /api/v1/cart",
]

def parse_and_analyze_logs(raw_data):
    parsed_records = []
    unique_ips = set()
    status_distribution = {}
    path_latencies = {}

    for line in raw_data:
        # Split line by delimiter and strip surrounding whitespace from each token
        parts = [part.strip() for part in line.split("|")]
        if len(parts) != 5:
            continue  # Malformed line guard

        timestamp, ip, status_str, latency_str, path = parts

        # Type conversion with safe parsing
        status_code = int(status_str)
        latency_ms = float(latency_str)

        # Track unique client IP addresses
        unique_ips.add(ip)

        # Count status code frequencies using dict.get() default fallback
        status_distribution[status_code] = status_distribution.get(status_code, 0) + 1

        # Collect response times per endpoint path
        path_latencies.setdefault(path, []).append(latency_ms)

        parsed_records.append({
            "timestamp": timestamp,
            "ip": ip,
            "status": status_code,
            "latency": latency_ms,
            "path": path
        })

    # Dict comprehension: Compute average latency per path
    average_latencies = {
        path: round(sum(latencies) / len(latencies), 2)
        for path, latencies in path_latencies.items()
    }

    # List comprehension: Filter slow requests (> 100ms)
    slow_requests = [
        rec for rec in parsed_records
        if rec["latency"] > 100.0
    ]

    return {
        "total_requests": len(parsed_records),
        "unique_clients": len(unique_ips),
        "status_distribution": status_distribution,
        "average_latencies": average_latencies,
        "slow_requests": slow_requests
    }

def main():
    print("Processing access logs...")
    analytics = parse_and_analyze_logs(RAW_LOGS)

    print(f"Total Requests: {analytics['total_requests']}")
    print(f"Unique Client IPs: {analytics['unique_clients']}")
    print("HTTP Status Breakdown:")
    for status, count in sorted(analytics["status_distribution"].items()):
        print(f"  [{status}]: {count} occurrences")

    print("\nAverage Latency Per Endpoint:")
    for path, avg_time in analytics["average_latencies"].items():
        print(f"  {path:<20} -> {avg_time:>6.2f} ms")

    print(f"\nSlow Requests (>100ms): {len(analytics['slow_requests'])}")
    for sr in analytics["slow_requests"]:
        print(f"  [{sr['timestamp']}] {sr['ip']} -> {sr['path']} ({sr['latency']} ms)")

if __name__ == "__main__":
    main()
