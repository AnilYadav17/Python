"""
Unit Tests for Project 2: Expense Tracker
=========================================
Tests adding expenses, input validation, category summaries,
and JSON file persistence.
"""

from pathlib import Path
import unittest
from tracker import ExpenseTracker


class TestExpenseTracker(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file = Path("test_expenses.json")
        if self.test_file.exists():
            self.test_file.unlink()
        self.tracker = ExpenseTracker(storage_path=self.test_file)

    def tearDown(self) -> None:
        if self.test_file.exists():
            self.test_file.unlink()

    def test_add_and_total(self) -> None:
        """Verify adding expenses and calculating aggregate totals."""
        e1 = self.tracker.add_expense("Coffee", 4.50, "Food")
        e2 = self.tracker.add_expense("Notebook", 15.00, "Supplies")

        self.assertEqual(e1.id, 1)
        self.assertEqual(e2.id, 2)
        self.assertEqual(self.tracker.total_spending(), 19.50)

    def test_category_breakdown(self) -> None:
        """Verify spending aggregation by category."""
        self.tracker.add_expense("Coffee", 4.50, "Food")
        self.tracker.add_expense("Lunch", 12.00, "Food")
        self.tracker.add_expense("Subway Pass", 30.00, "Transport")

        breakdown = self.tracker.spending_by_category()
        self.assertEqual(breakdown["Food"], 16.50)
        self.assertEqual(breakdown["Transport"], 30.00)

    def test_persistence_reload(self) -> None:
        """Verify expenses persist to disk and reload accurately."""
        self.tracker.add_expense("Hosting", 25.00, "Cloud")

        # Load fresh instance pointing to same file
        reloaded = ExpenseTracker(storage_path=self.test_file)
        self.assertEqual(len(reloaded.expenses), 1)
        self.assertEqual(reloaded.expenses[0].title, "Hosting")
        self.assertEqual(reloaded.expenses[0].amount, 25.00)

    def test_validation_errors(self) -> None:
        """Verify negative amounts and empty titles raise ValueError."""
        with self.assertRaises(ValueError):
            self.tracker.add_expense("", 10.0, "Misc")

        with self.assertRaises(ValueError):
            self.tracker.add_expense("Gift", -5.0, "Misc")


if __name__ == "__main__":
    unittest.main()
