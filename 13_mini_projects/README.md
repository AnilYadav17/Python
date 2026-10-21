# 🛠️ 13_Mini_Projects: Real-World Applications

## Overview
Moving from isolated syntax exercises to building complete software requires integrating multiple Python concepts into cohesive applications. This directory showcases **three practical, runnable multi-file mini-projects**, each demonstrating a specific software engineering discipline:

1. **Modular Architecture & Packages:** Decoupling business domains across distinct Python packages.
2. **File Processing & Error Logging:** Parsing raw data records, applying business rules, and directing valid/invalid outputs to distinct file streams.
3. **Enterprise Layered Architecture:** Building a production-style application using Models, Data Access Objects (DAO), Service layers, and SQLite database persistence.

---

## 🚀 The Projects

```text
13_mini_projects/
├── 📁 01_hospital_management_system/      # Modular Package Architecture
├── 📁 02_student_result_processor/        # File Stream Processing & Error Logging
└── 📁 03_bank_account_management/         # Layered Enterprise Architecture (DAO + SQLite)
```

---

### Project 1: Hospital Management System (`01_hospital_management_system/`)

* **Architecture:** Multi-package Python modular design.
* **Domains:**
  * `patient/` — Patient registration, search, and medical record display.
  * `doctor/` — Doctor registry and availability tracking.
  * `appointment/` — Scheduling appointments between doctors and patients.
  * `billing/` — Calculating fees, consultation charges, and generating bills.
* **Concepts:** Package `__init__.py` namespaces, cross-module imports, menu-driven CLI.
* **How to Run:**
  ```bash
  cd 13_mini_projects/01_hospital_management_system
  python3 main.py
  ```

---

### Project 2: Student Result Processing Engine (`02_student_result_processor/`)

* **Architecture:** File-driven batch processor.
* **Workflow:**
  1. Reads raw comma-separated records from `students.txt` (`id, name, subject, marks`).
  2. Validates records: verifies field counts, ensures numeric marks, checks range ($0 \le \text{marks} \le 100$).
  3. Writes malformed or invalid records with diagnostic error messages to `error_log.txt`.
  4. Classifies passing students (`Excellent`, `Very Good`, `Good`, `Pass`, `Fail`) and outputs to `result.txt`.
* **Concepts:** Stream reading, string parsing, conditional classification, defensive file writes.
* **How to Run:**
  ```bash
  cd 13_mini_projects/02_student_result_processor
  python3 student_result.py
  ```

---

### Project 3: Bank Account Management System (`03_bank_account_management/`)

* **Architecture:** Full 4-Tier Layered Architecture with SQLite DB-API.
* **Layers:**
  * **Model Layer (`model/account.py`):** `Account` data class encapsulating account number, holder name, balance, and account type.
  * **Database Layer (`database/connection.py`, `schema.sql`):** SQLite connection factory and relational schema definition.
  * **Data Access Layer (`dao/account_dao.py`):** Encapsulates raw SQL queries (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) with parameterized queries preventing SQL injection.
  * **Service Layer (`service/account_service.py`):** Business logic and transaction rules.
  * **Presentation Layer (`main.py`):** Interactive menu-driven console interface with `match-case` routing.
* **Features:** Create account, update holder name/balance, delete account, search account, and display all accounts.
* **How to Run:**
  ```bash
  cd 13_mini_projects/03_bank_account_management
  python3 main.py
  ```

---

## Next Step

👉 Explore academic unit tests and exam assessments in **[14_tests_and_assessments](../14_tests_and_assessments/)**!
