"""
Automated Unit Tests for Enterprise Service (Project 09)
"""

import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from service import EnterpriseService, JsonLogFormatter, ServiceConfig


class TestEnterpriseService(unittest.TestCase):
    def test_config_from_defaults(self):
        config = ServiceConfig()
        self.assertEqual(config.app_env, "development")
        self.assertEqual(config.port, 8080)
        self.assertEqual(config.log_level, "INFO")

    def test_health_and_readiness_checks(self):
        svc = EnterpriseService(ServiceConfig(service_name="test-svc"))
        health = svc.health_check()
        self.assertEqual(health["status"], "UP")
        self.assertEqual(health["service"], "test-svc")

        readiness = svc.readiness_check()
        self.assertTrue(readiness["ready"])

    def test_request_dispatch_success_with_headers(self):
        svc = EnterpriseService()
        response = svc.dispatch_request("/api/test", lambda: {"message": "hello"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.body["message"], "hello")
        self.assertIn("X-Request-ID", response.headers)
        self.assertIn("X-Response-Time-Ms", response.headers)

    def test_request_dispatch_handles_exceptions_gracefully(self):
        svc = EnterpriseService()

        # ValueError should convert to 400
        def bad_client():
            raise ValueError("Invalid query parameter")

        res_400 = svc.dispatch_request("/api/bad", bad_client)
        self.assertEqual(res_400.status_code, 400)
        self.assertEqual(res_400.body["error"], "Bad Request")

        # Generic Exception should convert to 500 without leaking stack traces
        def server_crash():
            raise RuntimeError("Database pool connection dropped")

        res_500 = svc.dispatch_request("/api/crash", server_crash)
        self.assertEqual(res_500.status_code, 500)
        self.assertEqual(res_500.body["error"], "Internal Server Error")

    def test_shutdown_lifecycle(self):
        svc = EnterpriseService()
        svc.shutdown()

        self.assertFalse(svc.is_ready)
        response = svc.dispatch_request("/api/test", lambda: {"ok": True})
        self.assertEqual(response.status_code, 503)


if __name__ == "__main__":
    unittest.main()
