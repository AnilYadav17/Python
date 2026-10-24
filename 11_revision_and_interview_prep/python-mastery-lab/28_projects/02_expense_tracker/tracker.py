"""
Project 2: Expense Tracker (Modular JSON Accounting Engine)
===========================================================
Demonstrates dataclasses, JSON serialization, pathlib, safe file I/O,
and domain-driven separation of concerns.
"""

from dataclasses import asdict, dataclass, field
from datetime import datetime
import json
from pathlib import Path
from typing import Any


@dataclass
class Expense:
    id: int
    title: str
    amount: float
    category: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Expense":
        return cls(
            id=int(data["id"]),
            title=str(data["title"]),
            amount=float(data["amount"]),
            category=str(data["category"]),
            timestamp=str(data.get("timestamp", datetime.now().isoformat())),
        )


class ExpenseTracker:
    def __init__(self, storage_path: Path | str = "expenses.json") -> None:
        self.storage_path = Path(storage_path)
        self.expenses: list[Expense] = []
        self._load()

    def add_expense(self, title: str, amount: float, category: str) -> Expense:
        if amount <= 0:
            raise ValueError("Expense amount must be strictly greater than zero.")
        clean_title = title.strip()
        if not clean_title:
            raise ValueError("Expense title cannot be empty.")

        next_id = max((e.id for e in self.expenses), default=0) + 1
        new_expense = Expense(
            id=next_id,
            title=clean_title,
            amount=amount,
            category=category.strip().title(),
        )
        self.expenses.append(new_expense)
        self._save()
        return new_expense

    def total_spending(self) -> float:
        return sum(e.amount for e in self.expenses)

    def spending_by_category(self) -> dict[str, float]:
        category_totals: dict[str, float] = {}
        for e in self.expenses:
            category_totals[e.category] = category_totals.get(e.category, 0.0) + e.amount
        return category_totals

    def filter_by_category(self, category: str) -> list[Expense]:
        target = category.strip().lower()
        return [e for e in self.expenses if e.category.lower() == target]

    def _save(self) -> None:
        raw_list = [e.to_dict() for e in self.expenses]
        self.storage_path.write_text(json.dumps(raw_list, indent=2), encoding="utf-8")

    def _load(self) -> None:
        if not self.storage_path.exists():
            self.expenses = []
            return

        try:
            raw_text = self.storage_path.read_text(encoding="utf-8").strip()
            if not raw_text:
                self.expenses = []
                return
            raw_list = json.loads(raw_text)
            self.expenses = [Expense.from_dict(item) for item in raw_list]
        except (json.JSONDecodeError, KeyError, ValueError) as err:
            # Corrupted storage fallback
            self.expenses = []
