"""
Automated Integration Tests for Lab Projects (P01 - P09)
=========================================================
Ensures all 9 projects integrate cleanly with the central test harness.
"""

import asyncio
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest

# Add all project paths to sys.path
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir / "28_projects" / "01_cli_calculator"))
sys.path.insert(0, str(root_dir / "28_projects" / "02_expense_tracker"))
sys.path.insert(0, str(root_dir / "28_projects" / "03_file_organizer"))
sys.path.insert(0, str(root_dir / "28_projects" / "04_log_analyzer"))
sys.path.insert(0, str(root_dir / "28_projects" / "05_package_development" / "src"))
sys.path.insert(0, str(root_dir / "28_projects" / "06_async_api_client"))
sys.path.insert(0, str(root_dir / "28_projects" / "07_tested_cli_application"))
sys.path.insert(0, str(root_dir / "28_projects" / "08_database_application"))
sys.path.insert(0, str(root_dir / "28_projects" / "09_production_style_python_service"))

import calculator  # type: ignore
from tracker import ExpenseTracker  # type: ignore
from organizer import FileOrganizer  # type: ignore
from log_analyzer import LogAnalyzer  # type: ignore
import pypulse  # type: ignore
from client import AsyncApiClient  # type: ignore
from cli import CliApplication  # type: ignore
from db import MigrationManager, Product, ProductRepository, UnitOfWork  # type: ignore
from service import EnterpriseService, ServiceConfig  # type: ignore


class TestProjectIntegration(unittest.TestCase):
    def test_project1_calculator_integration(self) -> None:
        """Verify Project 1 calculator evaluates complex expressions accurately."""
        expr = "(100 - 20) / (2 ** 3) + 15 % 4"
        result = calculator.evaluate(expr)
        self.assertEqual(result, 13.0)

    def test_project2_tracker_integration(self) -> None:
        """Verify Project 2 expense tracker adds items and calculates totals."""
        test_file = Path("integration_test_expenses.json")
        if test_file.exists():
            test_file.unlink()

        try:
            tracker = ExpenseTracker(storage_path=test_file)
            tracker.add_expense("Server VPS", 10.0, "Infrastructure")
            tracker.add_expense("Domain Name", 12.0, "Infrastructure")

            self.assertEqual(tracker.total_spending(), 22.0)
            self.assertEqual(tracker.spending_by_category()["Infrastructure"], 22.0)
        finally:
            if test_file.exists():
                test_file.unlink()

    def test_project3_file_organizer_integration(self) -> None:
        """Verify Project 3 file organizer categorizes files correctly."""
        temp_dir = Path(tempfile.mkdtemp())
        try:
            (temp_dir / "invoice.pdf").write_text("dummy", encoding="utf-8")
            (temp_dir / "photo.jpg").write_text("dummy", encoding="utf-8")
            (temp_dir / "script.py").write_text("dummy", encoding="utf-8")

            organizer = FileOrganizer(temp_dir, dry_run=False)
            actions = organizer.organize()

            self.assertEqual(len(actions), 3)
            self.assertTrue((temp_dir / "Documents" / "invoice.pdf").exists())
            self.assertTrue((temp_dir / "Images" / "photo.jpg").exists())
            self.assertTrue((temp_dir / "Code" / "script.py").exists())
            self.assertTrue((temp_dir / "organize_audit.json").exists())
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_project4_log_analyzer_integration(self) -> None:
        """Verify Project 4 streaming log analyzer computes correct metrics."""
        temp_dir = Path(tempfile.mkdtemp())
        log_file = temp_dir / "server.log"
        log_file.write_text(
            '192.168.1.1 - - [24/Oct/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 1500\n'
            '192.168.1.2 - - [24/Oct/2026:10:00:01 +0000] "POST /api/data HTTP/1.1" 500 200\n',
            encoding="utf-8"
        )
        try:
            analyzer = LogAnalyzer(log_file)
            metrics = analyzer.analyze(top_n=2)
            self.assertEqual(metrics.total_requests, 2)
            self.assertEqual(metrics.unique_ips, 2)
            self.assertEqual(metrics.status_distribution[200], 1)
            self.assertEqual(metrics.status_distribution[500], 1)
            self.assertEqual(metrics.error_rate_percent, 50.0)
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_project5_package_development_integration(self) -> None:
        """Verify Project 5 pypulse package validates emails and transforms slugs."""
        self.assertTrue(pypulse.is_valid_email("dev@python.org"))
        self.assertFalse(pypulse.is_valid_email("invalid-email"))
        self.assertEqual(pypulse.slugify("Python Mastery Lab 2026!"), "python-mastery-lab-2026")
        self.assertEqual(pypulse.camel_to_snake("UserProfileController"), "user_profile_controller")

    def test_project6_async_api_client_integration(self) -> None:
        """Verify Project 6 AsyncApiClient executes async calls."""
        async def run_async():
            async with AsyncApiClient() as client:
                res = await client.get("/test_endpoint")
                return res

        response = asyncio.run(run_async())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.attempt_count, 1)

    def test_project7_tested_cli_integration(self) -> None:
        """Verify Project 7 CLI application produces health report."""
        class TestCollector:
            def get_memory_usage_percent(self) -> float: return 45.0
            def get_disk_usage_percent(self) -> float: return 60.0

        app = CliApplication(collector=TestCollector())
        report = app.evaluate_health()
        self.assertEqual(report.overall_status, "OK")
        self.assertEqual(len(report.metrics), 2)

    def test_project8_database_app_integration(self) -> None:
        """Verify Project 8 Database Application creates products and enforces constraints."""
        conn = sqlite3.connect(":memory:")
        MigrationManager.apply_migrations(conn)
        repo = ProductRepository(conn)
        prod = repo.create(Product(id=None, sku="SKU-TEST", name="Test Item", price=19.99, stock_quantity=10))

        self.assertIsNotNone(prod.id)
        found = repo.find_by_sku("SKU-TEST")
        self.assertEqual(found.name, "Test Item")

        # Atomic stock deduction
        repo.update_stock(prod.id, -4)
        self.assertEqual(repo.find_by_sku("SKU-TEST").stock_quantity, 6)
        conn.close()

    def test_project9_production_service_integration(self) -> None:
        """Verify Project 9 Enterprise Service health and request dispatch."""
        svc = EnterpriseService(ServiceConfig(service_name="integration-svc"))
        health = svc.health_check()
        self.assertEqual(health["status"], "UP")

        res = svc.dispatch_request("/api/ping", lambda: {"status": "pong"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.body["status"], "pong")
        self.assertIn("X-Request-ID", res.headers)


if __name__ == "__main__":
    unittest.main()
