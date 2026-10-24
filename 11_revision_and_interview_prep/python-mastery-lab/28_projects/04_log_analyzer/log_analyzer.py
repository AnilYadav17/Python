"""
High-Performance Streaming Log Analyzer (Project 04)

Processes gigabyte-scale web server logs (Common / Combined Log Format)
using streaming generator pipelines with O(1) constant memory.
"""

import argparse
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Generator, Iterator, List, Optional

# Standard Combined Log Format Regex:
# e.g.: 192.168.1.1 - - [24/Oct/2026:13:30:00 +0000] "GET /api/v1/users HTTP/1.1" 200 1234
LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<method>[A-Z]+)\s+(?P<endpoint>\S+)[^"]*"\s+(?P<status>\d{3})\s+(?P<bytes>\S+)'
)


@dataclass
class LogRecord:
    ip: str
    timestamp: str
    method: str
    endpoint: str
    status_code: int
    response_bytes: int


@dataclass
class LogMetrics:
    total_requests: int
    unique_ips: int
    status_distribution: Dict[int, int]
    top_endpoints: List[tuple]
    error_rate_percent: float
    total_bytes_transferred: int


class LogAnalyzer:
    """Streams and analyzes log files line-by-line without loading entire file to RAM."""

    def __init__(self, log_path: Path):
        self.log_path = Path(log_path)
        if not self.log_path.exists():
            raise FileNotFoundError(f"Log file not found: {self.log_path}")

    def parse_line(self, line: str) -> Optional[LogRecord]:
        """Parse single raw log line into typed LogRecord, returns None if malformed."""
        match = LOG_PATTERN.match(line.strip())
        if not match:
            return None

        data = match.groupdict()
        try:
            status = int(data["status"])
            size = int(data["bytes"]) if data["bytes"] != "-" else 0
        except ValueError:
            return None

        return LogRecord(
            ip=data["ip"],
            timestamp=data["timestamp"],
            method=data["method"],
            endpoint=data["endpoint"],
            status_code=status,
            response_bytes=size
        )

    def stream_records(self) -> Generator[LogRecord, None, None]:
        """Lazy generator: streams LogRecord objects one-by-one."""
        with open(self.log_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                record = self.parse_line(line)
                if record:
                    yield record

    def analyze(self, top_n: int = 5) -> LogMetrics:
        """Single-pass streaming metrics aggregation."""
        total_requests = 0
        unique_ips = set()
        status_counts = Counter()
        endpoint_counts = Counter()
        total_bytes = 0
        error_count = 0

        for rec in self.stream_records():
            total_requests += 1
            unique_ips.add(rec.ip)
            status_counts[rec.status_code] += 1
            endpoint_counts[rec.endpoint] += 1
            total_bytes += rec.response_bytes

            if rec.status_code >= 400:
                error_count += 1

        error_rate = (error_count / total_requests * 100) if total_requests > 0 else 0.0

        return LogMetrics(
            total_requests=total_requests,
            unique_ips=len(unique_ips),
            status_distribution=dict(status_counts),
            top_endpoints=endpoint_counts.most_common(top_n),
            error_rate_percent=round(error_rate, 2),
            total_bytes_transferred=total_bytes
        )


def main():
    parser = argparse.ArgumentParser(description="Streaming High-Performance Log Analyzer.")
    parser.add_argument("logfile", help="Path to log file")
    parser.add_argument("--top", type=int, default=5, help="Number of top endpoints (default 5)")
    parser.add_argument("--json", action="store_true", help="Output metrics in JSON format")
    args = parser.parse_args()

    analyzer = LogAnalyzer(Path(args.logfile))
    metrics = analyzer.analyze(top_n=args.top)

    if args.json:
        print(json.dumps(asdict(metrics), indent=2))
    else:
        print("\n" + "=" * 50)
        print("          LOG ANALYSIS REPORT")
        print("=" * 50)
        print(f"Total Requests:       {metrics.total_requests:,}")
        print(f"Unique Visitors (IP): {metrics.unique_ips:,}")
        print(f"Total Bytes Sent:     {metrics.total_bytes_transferred:,} bytes")
        print(f"Error Rate (4xx/5xx): {metrics.error_rate_percent}%")
        print("\nStatus Code Breakdown:")
        for status, count in sorted(metrics.status_distribution.items()):
            print(f"  {status}: {count:,}")
        print(f"\nTop {args.top} Endpoints:")
        for endpoint, count in metrics.top_endpoints:
            print(f"  {endpoint} ({count:,} hits)")
        print("=" * 50)


if __name__ == "__main__":
    main()
