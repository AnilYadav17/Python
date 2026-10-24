"""
Automated Unit Tests for Advanced Language Features, Typing & Runtime (Modules 14-23)
"""

from contextlib import contextmanager
import sqlite3
from typing import Protocol, runtime_checkable
import unittest


@runtime_checkable
class Greeter(Protocol):
    def greet(self) -> str:
        ...


class FriendlyBot:
    def greet(self) -> str:
        return "Hello!"


class TestAdvancedLanguageFeatures(unittest.TestCase):
    def test_walrus_operator(self):
        """Verify walrus operator assignment expression within conditional."""
        items = [1, 2, 3, 4, 5]
        filtered = [sq for x in items if (sq := x * x) > 10]
        self.assertEqual(filtered, [16, 25])

    def test_extended_sequence_unpacking(self):
        """Verify extended sequence unpacking captures middle elements."""
        head, *body, tail = (1, 2, 3, 4, 5)
        self.assertEqual(head, 1)
        self.assertEqual(body, [2, 3, 4])
        self.assertEqual(tail, 5)

    def test_runtime_checkable_protocol(self):
        """Verify runtime Protocol verification via isinstance()."""
        bot = FriendlyBot()
        self.assertTrue(isinstance(bot, Greeter))

    def test_contextmanager_exception_safety(self):
        """Verify custom contextmanager executes finally block on exception."""
        cleaned_up = False

        @contextmanager
        def managed_resource():
            nonlocal cleaned_up
            try:
                yield "resource"
            finally:
                cleaned_up = True

        with self.assertRaises(ZeroDivisionError):
            with managed_resource():
                _ = 1 / 0

        self.assertTrue(cleaned_up)

    def test_sqlite_transaction_rollback_guarantee(self):
        """Verify SQLite transaction context manager rolls back on exception."""
        conn = sqlite3.connect(":memory:")
        with conn:
            conn.execute("CREATE TABLE counter (val INT)")
            conn.execute("INSERT INTO counter VALUES (10)")

        with self.assertRaises(ValueError):
            with conn:
                conn.execute("UPDATE counter SET val = 20")
                raise ValueError("Simulated transaction error")

        cursor = conn.execute("SELECT val FROM counter")
        val = cursor.fetchone()[0]
        self.assertEqual(val, 10)  # Value remains 10 due to rollback
        conn.close()


if __name__ == "__main__":
    unittest.main()
