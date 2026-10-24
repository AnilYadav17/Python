"""
Automated Unit & Integration Tests for Database Application (Project 08)
"""

from pathlib import Path
import sqlite3
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db import MigrationManager, Product, ProductRepository, UnitOfWork


class TestDatabaseApplication(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        # Enable foreign keys and foreign key constraints
        self.conn.execute("PRAGMA foreign_keys = ON;")
        MigrationManager.apply_migrations(self.conn)
        self.repo = ProductRepository(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_migrations_are_idempotent(self):
        # Applying migrations again should apply 0 additional migrations
        count = MigrationManager.apply_migrations(self.conn)
        self.assertEqual(count, 0)

    def test_product_crud_lifecycle(self):
        prod = Product(id=None, sku="TECH-001", name="Mechanical Keyboard", price=89.99, stock_quantity=15)
        created = self.repo.create(prod)
        self.assertIsNotNone(created.id)

        # Retrieve
        retrieved = self.repo.find_by_sku("TECH-001")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.name, "Mechanical Keyboard")
        self.assertEqual(retrieved.stock_quantity, 15)

    def test_stock_update_atomic_bounds(self):
        prod = self.repo.create(Product(id=None, sku="TECH-002", name="Mouse", price=29.99, stock_quantity=5))

        # Successfully deduct 3
        success = self.repo.update_stock(prod.id, -3)
        self.assertTrue(success)
        self.assertEqual(self.repo.find_by_sku("TECH-002").stock_quantity, 2)

        # Attempt to deduct 5 when only 2 remain (should fail due to CHECK constraint / rowcount guard)
        fail = self.repo.update_stock(prod.id, -5)
        self.assertFalse(fail)
        # Quantity must remain 2
        self.assertEqual(self.repo.find_by_sku("TECH-002").stock_quantity, 2)

    def test_unit_of_work_transaction_rollback(self):
        prod = self.repo.create(Product(id=None, sku="TECH-003", name="Monitor", price=299.99, stock_quantity=10))

        # Perform transaction that raises an unhandled error midway
        try:
            with UnitOfWork(self.conn) as uow:
                uow.products.update_stock(prod.id, -2)
                # Intentionally crash before completion:
                raise RuntimeError("Payment gateway network failure")
        except RuntimeError:
            pass

        # Verify stock was rolled back to initial 10!
        refreshed = self.repo.find_by_sku("TECH-003")
        self.assertEqual(refreshed.stock_quantity, 10)


if __name__ == "__main__":
    unittest.main()
