# Project 2: Expense Tracker (JSON Accounting Engine)

## 1. Problem Statement
Managing personal or departmental expenses requires persistent data storage, categorized aggregation, input validation, and transactional integrity. 

This project implements an idiomatic, lightweight expense tracking engine in Python using `@dataclass`, standard `json` persistence, and `pathlib.Path`.

---

## 2. Architecture & Design
- **Domain Entity**: `Expense` dataclass modeling identity, title, amount, category, and timestamp.
- **Service Layer**: `ExpenseTracker` repository encapsulating collection state, filtering, totals, and atomic JSON file synchronization.
- **Safety**: Rejects negative amounts, validates title strings, and handles missing or corrupted storage files gracefully.

---

## 3. Running & Testing

```bash
# Run unit tests:
python3 -m unittest 28_projects/02_expense_tracker/test_tracker.py
```
