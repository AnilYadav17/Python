"""
Production Tested CLI Application (Project 07)

Demonstrates:
- Clean modular CLI with argparse
- Dependency Injection architecture for 100% testability
- Strict exit code contracts (0: OK, 1: WARNING, 2: CRITICAL)
- Formatted human output and JSON serialization
"""

import argparse
import json
import logging
import os
import shutil
import sys
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional, Protocol


@dataclass
class HealthMetric:
    name: str
    status: str  # OK, WARNING, CRITICAL
    value: float
    unit: str
    message: str


@dataclass
class HealthReport:
    overall_status: str
    metrics: List[HealthMetric]
    timestamp: str


class MetricsCollector(Protocol):
    """Protocol for dependency injection of system metrics."""
    def get_memory_usage_percent(self) -> float: ...
    def get_disk_usage_percent(self) -> float: ...


class SystemMetricsCollector:
    """Production implementation using OS inspection."""
    def get_memory_usage_percent(self) -> float:
        # Approximate using /proc/meminfo on Linux or fallback to safe constant
        try:
            with open("/proc/meminfo", "r") as f:
                lines = f.readlines()
                total = int([l for l in lines if "MemTotal" in l][0].split()[1])
                available = int([l for l in lines if "MemAvailable" in l][0].split()[1])
                return round(((total - available) / total) * 100, 2)
        except Exception:
            return 35.0

    def get_disk_usage_percent(self) -> float:
        try:
            usage = shutil.disk_usage("/")
            return round((usage.used / usage.total) * 100, 2)
        except Exception:
            return 50.0


class CliApplication:
    """Core CLI application with decoupled dependencies."""

    def __init__(self, collector: MetricsCollector, logger: Optional[logging.Logger] = None):
        self.collector = collector
        self.logger = logger or logging.getLogger("syspulse")

    def evaluate_health(self) -> HealthReport:
        import datetime

        mem = self.collector.get_memory_usage_percent()
        disk = self.collector.get_disk_usage_percent()

        metrics: List[HealthMetric] = []
        overall = "OK"

        # Memory evaluation
        if mem > 90.0:
            mem_status = "CRITICAL"
            overall = "CRITICAL"
        elif mem > 75.0:
            mem_status = "WARNING"
            if overall != "CRITICAL":
                overall = "WARNING"
        else:
            mem_status = "OK"

        metrics.append(HealthMetric("Memory", mem_status, mem, "%", f"RAM used: {mem}%"))

        # Disk evaluation
        if disk > 90.0:
            disk_status = "CRITICAL"
            overall = "CRITICAL"
        elif disk > 80.0:
            disk_status = "WARNING"
            if overall != "CRITICAL":
                overall = "WARNING"
        else:
            disk_status = "OK"

        metrics.append(HealthMetric("Disk", disk_status, disk, "%", f"Root disk used: {disk}%"))

        return HealthReport(
            overall_status=overall,
            metrics=metrics,
            timestamp=datetime.datetime.now().isoformat()
        )

    def run(self, argv: List[str]) -> int:
        parser = argparse.ArgumentParser(prog="syspulse", description="System Health & Diagnostic CLI")
        subparsers = parser.add_subparsers(dest="command", required=True)

        # Health command
        health_cmd = subparsers.add_parser("health", help="Check system health thresholds")
        health_cmd.add_argument("--json", action="store_true", help="Output machine-readable JSON")

        args = parser.parse_args(argv)

        if args.command == "health":
            report = self.evaluate_health()
            if args.json:
                print(json.dumps(asdict(report), indent=2))
            else:
                print(f"Overall Status: [{report.overall_status}]")
                for m in report.metrics:
                    print(f"  - {m.name:10}: [{m.status:8}] {m.value}{m.unit} ({m.message})")

            # Exit code mapping
            if report.overall_status == "OK":
                return 0
            elif report.overall_status == "WARNING":
                return 1
            else:
                return 2

        return 0


def main():
    app = CliApplication(collector=SystemMetricsCollector())
    sys.exit(app.run(sys.argv[1:]))


if __name__ == "__main__":
    main()
