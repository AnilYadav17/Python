"""
Automated Unit Tests for Tested CLI Application (Project 07)
"""

from pathlib import Path
import sys
import unittest
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cli import CliApplication, MetricsCollector


class MockMetricsCollector:
    """Mock collector for testing specific threshold branches."""
    def __init__(self, memory: float = 30.0, disk: float = 40.0):
        self.memory = memory
        self.disk = disk

    def get_memory_usage_percent(self) -> float:
        return self.memory

    def get_disk_usage_percent(self) -> float:
        return self.disk


class TestCliApplication(unittest.TestCase):
    def test_healthy_status_returns_code_0(self):
        collector = MockMetricsCollector(memory=40.0, disk=50.0)
        app = CliApplication(collector=collector)
        exit_code = app.run(["health"])
        self.assertEqual(exit_code, 0)

        report = app.evaluate_health()
        self.assertEqual(report.overall_status, "OK")

    def test_warning_status_returns_code_1(self):
        collector = MockMetricsCollector(memory=78.0, disk=50.0)
        app = CliApplication(collector=collector)
        exit_code = app.run(["health"])
        self.assertEqual(exit_code, 1)

        report = app.evaluate_health()
        self.assertEqual(report.overall_status, "WARNING")

    def test_critical_status_returns_code_2(self):
        collector = MockMetricsCollector(memory=95.0, disk=92.0)
        app = CliApplication(collector=collector)
        exit_code = app.run(["health"])
        self.assertEqual(exit_code, 2)

        report = app.evaluate_health()
        self.assertEqual(report.overall_status, "CRITICAL")

    def test_json_flag_structure(self):
        collector = MockMetricsCollector(memory=50.0, disk=60.0)
        app = CliApplication(collector=collector)
        report = app.evaluate_health()
        self.assertEqual(len(report.metrics), 2)
        self.assertEqual(report.metrics[0].name, "Memory")
        self.assertEqual(report.metrics[1].name, "Disk")


if __name__ == "__main__":
    unittest.main()
