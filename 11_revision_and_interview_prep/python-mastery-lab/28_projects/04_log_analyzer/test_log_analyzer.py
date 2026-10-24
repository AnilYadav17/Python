"""
Automated Unit & Integration Tests for Streaming Log Analyzer (Project 04)
"""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from log_analyzer import LogAnalyzer, LogRecord


SAMPLE_LOG_LINES = """192.168.1.10 - - [24/Oct/2026:12:00:01 +0000] "GET /index.html HTTP/1.1" 200 4520
192.168.1.11 - - [24/Oct/2026:12:00:02 +0000] "POST /api/login HTTP/1.1" 200 512
192.168.1.10 - - [24/Oct/2026:12:00:03 +0000] "GET /api/user/profile HTTP/1.1" 200 1280
10.0.0.5 - - [24/Oct/2026:12:00:04 +0000] "GET /admin HTTP/1.1" 403 240
10.0.0.8 - - [24/Oct/2026:12:00:05 +0000] "GET /missing HTTP/1.1" 404 180
192.168.1.12 - - [24/Oct/2026:12:00:06 +0000] "GET /index.html HTTP/1.1" 200 4520
MALFORMED JUNK LINE THAT SHOULD BE SKIPPED SAFELY
192.168.1.10 - - [24/Oct/2026:12:00:07 +0000] "POST /api/checkout HTTP/1.1" 500 0
"""


class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        self.sample_log_path = self.test_dir / "access.log"
        self.sample_log_path.write_text(SAMPLE_LOG_LINES, encoding="utf-8")
        self.analyzer = LogAnalyzer(self.sample_log_path)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_parse_valid_line(self):
        line = '127.0.0.1 - - [24/Oct/2026:10:00:00 +0000] "GET /health HTTP/1.1" 200 50'
        record = self.analyzer.parse_line(line)
        self.assertIsNotNone(record)
        self.assertEqual(record.ip, "127.0.0.1")
        self.assertEqual(record.method, "GET")
        self.assertEqual(record.endpoint, "/health")
        self.assertEqual(record.status_code, 200)
        self.assertEqual(record.response_bytes, 50)

    def test_parse_malformed_line_returns_none(self):
        record = self.analyzer.parse_line("corrupt line without apache format")
        self.assertIsNone(record)

    def test_streaming_metrics_aggregation(self):
        metrics = self.analyzer.analyze(top_n=3)

        # 7 valid lines (1 malformed skipped)
        self.assertEqual(metrics.total_requests, 7)
        # Unique IPs: 192.168.1.10, 192.168.1.11, 10.0.0.5, 10.0.0.8, 192.168.1.12 => 5 IPs
        self.assertEqual(metrics.unique_ips, 5)

        # Status distribution: 4 200s, 1 403, 1 404, 1 500
        self.assertEqual(metrics.status_distribution[200], 4)
        self.assertEqual(metrics.status_distribution[403], 1)
        self.assertEqual(metrics.status_distribution[404], 1)
        self.assertEqual(metrics.status_distribution[500], 1)

        # Error count: 3 errors (403, 404, 500) out of 7 requests = 3/7 * 100 = ~42.86%
        self.assertAlmostEqual(metrics.error_rate_percent, 42.86, places=1)

        # Top endpoint: /index.html has 2 hits
        top_endpoint, top_count = metrics.top_endpoints[0]
        self.assertEqual(top_endpoint, "/index.html")
        self.assertEqual(top_count, 2)


if __name__ == "__main__":
    unittest.main()
