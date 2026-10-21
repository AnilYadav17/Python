"""
03_real_world_use_case.py
Real-world scenario: Processing massive server access logs using a streaming pipeline.
Demonstrates:
- Multi-stage generator pipeline
- Constant O(1) memory usage regardless of file/data size
- Decoupled pipeline stages: generate -> parse -> filter -> aggregate
"""

# Simulated raw log stream (could be gigabytes of lines streamed from disk/network)
RAW_STREAM = [
    "2026-09-05 10:00:01 | GET /api/users | 200 | 45ms",
    "2026-09-05 10:00:02 | POST /api/login | 500 | 250ms",
    "2026-09-05 10:00:03 | GET /api/products | 200 | 30ms",
    "2026-09-05 10:00:04 | GET /api/users | 500 | 310ms",
    "2026-09-05 10:00:05 | PUT /api/orders | 200 | 120ms",
    "2026-09-05 10:00:06 | GET /api/orders | 500 | 190ms"
]

# Stage 1: Line generator (source stream)
def generate_lines(source_data):
    for line in source_data:
        yield line

# Stage 2: Parser generator (transforms string to structured dict)
def parse_log_entries(lines):
    for line in lines:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) == 4:
            ts, method_path, status, latency = parts
            yield {
                "timestamp": ts,
                "endpoint": method_path,
                "status": int(status),
                "latency_ms": float(latency.replace("ms", ""))
            }

# Stage 3: Filter generator (filters errors only)
def filter_server_errors(entries):
    for entry in entries:
        if entry["status"] >= 500:
            yield entry

# Stage 4: Consumer (aggregates metrics)
def compute_error_metrics(error_entries):
    count = 0
    total_latency = 0.0
    for err in error_entries:
        count += 1
        total_latency += err["latency_ms"]
        print(f"  [Error Alert] {err['timestamp']} -> {err['endpoint']} ({err['latency_ms']}ms)")

    avg_latency = total_latency / count if count else 0.0
    return count, avg_latency


def main():
    print("--- Multi-Stage Lazy Streaming Pipeline ---")
    # Build generator pipeline (Nothing executes yet - lazy composition!)
    lines = generate_lines(RAW_STREAM)
    parsed = parse_log_entries(lines)
    errors_only = filter_server_errors(parsed)

    # Execution starts only when consumer iterates
    print("Consuming pipeline stream:")
    err_count, avg_err_time = compute_error_metrics(errors_only)

    print(f"\nPipeline Summary:")
    print(f"Total Server 500 Errors: {err_count}")
    print(f"Average Error Latency: {avg_err_time:.2f} ms")

if __name__ == "__main__":
    main()
