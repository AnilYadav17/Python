# 🚀 Python Learning Hub

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](./LICENSE)
[![Code Style: PEP 8](https://img.shields.io/badge/Code%20Style-PEP%208-informational?style=for-the-badge)](https://peps.python.org/pep-0008/)
[![Repository Status](https://img.shields.io/badge/Status-Maintained%20%26%20Curated-success?style=for-the-badge)](#-repository-status--authenticity)

<h3>A Structured, Beginner-Friendly & Production-Minded Python Resource</h3>
<p>From absolute zero to object-oriented design, standard packages, algorithmic problem solving, and real-world projects.</p>

</div>

---

## 📖 Overview

**Python Learning Hub** is a structured collection of Python tutorials, hands-on examples, programming exercises, and revision resources designed to help learners progress from fundamentals to more advanced concepts.

Born out of an authentic, disciplined daily programming journey, this repository brings together **over 1,200 executable Python programs**, **75+ in-depth Markdown guides**, **640+ solved homework assignments**, **30 days of structured daily revision notes**, and **runnable multi-file mini-projects**.

Every folder is intentionally named, sequentially numbered, and accompanied by a dedicated `README.md` explaining the concepts, practical code examples, common pitfalls, and next steps.

---

## 🎯 Who Is This For?

* 🐣 **Absolute Beginners:** Start at `01_getting_started` without prior coding experience. Follow the step-by-step installation guides and learn the fundamentals cleanly.
* 🎓 **College & University Students:** Access 640+ topic-wise assignment solutions, lab exercises, and scenario-based unit test problems.
* 💼 **Interview Candidates:** Revise Python internals (CPython memory management, LEGB scope, MRO, GIL, generators) and practice LeetCode array and string patterns.
* 🛠️ **Self-Taught Developers:** Reference production design patterns, package construction, custom exceptions, and layered SQLite database architecture.

---

## 🗺️ Learning Roadmap

Follow this sequential progression to navigate the curriculum from zero to advanced:

```text
[ 01_getting_started ] ──> Install Python, REPL, VS Code setup, first script
          │
          ▼
[ 02_python_fundamentals ] ─> Variables, Data Types, Operators, Conditionals, Loops
          │
          ▼
[ 03_python_collections ] ──> Lists, Matrices, Dictionaries (Hash Maps), Sets, Tuples
          │
          ▼
[ 04_functions ] ───────────> Parameters, Scopes (LEGB), Lambdas, Recursion, Decorators
          │
          ▼
[ 05_object_oriented_prog ] ─> Classes, Objects, 5 Types of Inheritance, MRO, Abstraction
          │
          ▼
[ 06_modules_and_packages ] ─> sys.path, __init__.py, Custom Packages, Standard Libraries
          │
          ▼
[ 07_error_and_file_handling ] ─> try-except-else-finally, Custom Errors, Stream I/O, Context Managers
          │
          ▼
[ 08_intermediate_python ] ─> 18 Mastery Modules: Concurrency, Memory, Big-O, TDD, Regex
          │
          ├────────────────────────────────┬───────────────────────────────┐
          ▼                                ▼                               ▼
[ 09_practice_assignments ]    [ 10_coding_challenges ]          [ 13_mini_projects ]
  640+ Solved Homework Tasks     LeetCode Arrays & Strings         Hospital, Banking & Results
          │                                │                               │
          └────────────────────────────────┴───────────────────────────────┘
                                           │
                                           ▼
                       [ 11_revision_and_interview_prep ]
                         30-Day Daily Sprint & Mock Tests
```

---

## 🗂️ Clickable Table of Contents

| Directory | Core Topics & Focus | Key Highlight |
|:---|:---|:---|
| 📁 **[01_getting_started](./01_getting_started/)** | Installation (Linux, Mac, Windows), REPL, Running Scripts | Beginner onboarding & setup |
| 📁 **[02_python_fundamentals](./02_python_fundamentals/)** | Types, Memory (`id`, `sizeof`), Operators, Conditions, Loops, Math | 120+ classroom scripts & exam guide |
| 📁 **[03_python_collections](./03_python_collections/)** | 2D Matrices, Matrix Math ($O(N^3)$), Hash Maps, Frequency Sets | Pair sums & matrix addition |
| 📁 **[04_functions](./04_functions/)** | Scopes (LEGB), `*args`/`**kwargs`, Lambdas, Map/Filter, Recursion | Functional programming & decorators |
| 📁 **[05_object_oriented_programming](./05_object_oriented_programming/)** | 5 Inheritance Types, MRO, `super()`, ABC Abstraction, Closures | Domain modeling & OOP pillars |
| 📁 **[06_python_modules_and_packages](./06_python_modules_and_packages/)** | Package design, `__init__.py`, `sys.path`, `os`, `time`, `calendar` | Multi-directory architecture |
| 📁 **[07_error_and_file_handling](./07_error_and_file_handling/)** | `try`/`except`/`finally`, Custom Exceptions, File Modes (`r`, `w`, `a`, `r+`, `w+`, `x`) | Defensive I/O & context managers |
| 📁 **[08_intermediate_python](./08_intermediate_python/)** | 18 Architecture Modules: Concurrency, Memory, Big-O, TDD, Regex | 90 runnable advanced demos |
| 📁 **[09_practice_and_assignments](./09_practice_and_assignments/)** | 640+ Solved Assignment Problems organized by subtopic | Question sheets + verified solutions |
| 📁 **[10_coding_challenges](./10_coding_challenges/)** | LeetCode solutions (Arrays, Two Pointers, Strings, Sliding Window) | Algorithmic problem solving |
| 📁 **[11_revision_and_interview_prep](./11_revision_and_interview_prep/)** | 30-Day Markdown Revision Challenge + Interview Cheatsheets | Daily structured revision sprint |
| 📁 **[12_learning_resources](./12_learning_resources/)** | Master Reference PDFs, WeasyPrint generator, 16 MCQ sheets | High-yield offline revision books |
| 📁 **[13_mini_projects](./13_mini_projects/)** | Hospital System, Student Result Engine, 4-Tier Banking App | Multi-file runnable applications |
| 📁 **[14_tests_and_assessments](./14_tests_and_assessments/)** | Academic unit tests across learning timeline (April – September) | Scenario-based exam problems |
| 📁 **[15_archive](./15_archive/)** | Raw trial scratchpads, digit prototypes, and sandbox experiments | Preserved learning history |

---

## ⚡ Quickstart: Running Your First Script

### 1. Clone the Repository
```bash
git clone https://github.com/AnilYadav17/Python.git
cd Python
```

### 2. Verify Your Environment
No external third-party dependencies are required for the tutorials or assignments! All examples run out of the box on Python 3.10+ using only the **Python Standard Library**.

```bash
python3 --version
```

### 3. Run an Example
```bash
# Beginner first program:
python3 01_getting_started/first_program.py

# Armstrong number validator:
python3 02_python_fundamentals/Class_Work/Day10/loops/armstrong.py

# Custom banking exceptions:
python3 07_error_and_file_handling/exception_handling/custom_exception_bank_account.py

# Interactive Bank Account Management application:
python3 13_mini_projects/03_bank_account_management/main.py
```

*(Optional development tools like `pytest` and `weasyprint` can be installed via `pip install -r requirements.txt`).*

---

## 🚀 Featured Mini-Projects

Looking to explore complete applications? Head over to **[13_mini_projects](./13_mini_projects/)**:

1. **🏥 [Hospital Management System](./13_mini_projects/01_hospital_management_system/):**
   * Multi-package architecture (`patient`, `doctor`, `appointment`, `billing`).
   * Demonstrates package boundary isolation, clean imports, and modular records.
2. **📊 [Student Result Processing Engine](./13_mini_projects/02_student_result_processor/):**
   * Batch file stream processing with automated CSV parsing.
   * Input validation, marks categorization, result generation, and defensive error logging to `error_log.txt`.
3. **🏦 [Bank Account Management System](./13_mini_projects/03_bank_account_management/):**
   * Full 4-Tier layered architecture: Model (`Account`), Database (`SQLite`), Data Access Object (`DAO`), Service Layer, and CLI Presentation.
   * Implements secure parameterized SQL statements and full CRUD capabilities.

---

## 🔍 Repository Status & Authenticity

* **Authentic Learning Record:** This repository documents real coursework, coding bootcamps, and disciplined daily practice.
* **100% Syntax Validated:** All **1,209 Python files** have been compiled and verified with Python 3's `py_compile` compiler with **0 syntax errors**.
* **Zero Artificial Inflation:** We do not claim this repository is an all-inclusive computer science degree. Gaps, unfinished trials, and scratchpad experiments are honestly designated in **[15_archive](./15_archive/)**.
* **Non-Destructive Curation:** Original code logic, beginner implementations, and question prompts have been preserved intact without overwriting the original learning journey.

---

## 🔭 Future Learning Goals & Roadmap

The following topics represent planned additions currently under active development:

- [ ] **Advanced Backend Web Development:** Production REST APIs using FastAPI and Flask.
- [ ] **Automated CI/CD Testing:** GitHub Actions test runners executing automated test suites via `pytest`.
- [ ] **Graph Algorithms & Dynamic Programming:** Expanding `10_coding_challenges` with intermediate/hard graph traversals (BFS/DFS, Dijkstra) and DP state machines.
- [ ] **Dockerization:** Containerizing the mini-projects with reproducible Docker environments.

---

## 🤝 Contributing

Contributions, typo fixes, improved docstrings, alternative algorithmic solutions, and additional test cases are always welcome! Please check our **[CONTRIBUTING.md](./CONTRIBUTING.md)** for our pull request workflow and coding standards.

---

## 📜 License

This repository is distributed under the **[MIT License](./LICENSE)**. You are free to use, study, fork, and share this code for educational and personal projects.

---

## 👤 Author

**Anil Yadav**  
*Computer Science & Engineering Student*  
*Passionate Software Developer & Open Source Contributor*  
* **GitHub:** [@AnilYadav17](https://github.com/AnilYadav17)

---

<div align="center">

> *"Consistency beats intensity. Small daily improvements over time lead to stunning results."*  
> Crafted with ❤️ and dedication. If this repository helps your Python journey, give it a ⭐ on GitHub!

</div>
