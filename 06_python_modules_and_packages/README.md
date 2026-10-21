# 📦 06_Python_Modules_and_Packages: Architecture & Modularity

## Overview
As Python projects grow beyond single-file scripts, structuring code into **Modules** (individual `.py` files) and **Packages** (directories containing an `__init__.py` file) becomes essential.

A well-structured modular architecture prevents namespace collisions, enables clean code separation, speeds up collaborative development, and makes code distributable via package managers.

This directory teaches you how Python searches for code (`sys.path`), how to import specific functions or entire modules, how to construct custom multi-tiered packages, and how standard library modules like `os`, `time`, and `calendar` work.

---

## Learning Objectives
By studying this module, you will understand:
1. The difference between a **module** (a single `.py` file) and a **package** (a directory with `__init__.py`).
2. Import mechanics: `import module`, `from module import function`, `import module as alias`, and `from module import *`.
3. The role of `__init__.py` in package initialization and controlling exported symbols via `__all__`.
4. Working with Python's standard library utilities (`time`, `calendar`, `os`).
5. How Python locates imports using `sys.path` and the `PYTHONPATH` environment variable.
6. Execution context differences: Running a package script from the same directory vs. running from an arbitrary path.

---

## Prerequisites
* **[04_functions](../04_functions/)** (Function definitions and modular code organization).

---

## Learning Path

```text
1. Standard Library Modules (Modules/)
   └── Built-in modules: os, time, calendar, custom helper modules
       ▼
2. Custom Module Creation & Import Styles (Modules/)
   └── module1.py, module2.py, importing functions across files
       ▼
3. Package Architecture & __init__.py (Packages/)
   └── Subpackages, namespace boundaries, package initialization
       ▼
4. Execution Paths & sys.path (Packages/03 & 04)
   └── Same-directory execution vs. Root-level imports
```

---

## Repository Contents & Examples

| Folder / File | Description |
|:---|:---|
| 📁 **`Class_Work/Modules`** | `module1.py`, `module2.py`, `module3.py`, `calen.py`, `time_.py`, `os_module_demo.py` (filesystem operations) |
| 📁 **`Class_Work/Packages/02`** | Basic package initialization demo with `mypackages/` |
| 📁 **`Class_Work/Packages/03_Main_Same_Folder`** | Package structure where `main.py` runs alongside the package directory |
| 📁 **`Class_Work/Packages/04_Main_Anywhere`** | Advanced package import setup decoupling execution location from the package path |
| 📄 **`Python_Modules_and_Packages_Master_Guide.pdf`** | Comprehensive illustrated reference guide on Python module architecture |

---

## How to Run Examples

```bash
# Run the calendar standard library demo:
python3 06_python_modules_and_packages/Class_Work/Modules/calen.py

# Run a custom package execution:
cd 06_python_modules_and_packages/Class_Work/Packages/03_Main_Same_Folder
python3 main.py
```

---

## Practice & Assignments

Solve the modular architecture assignments in **`09_practice_and_assignments/03_Modules_and_Packages/`**:
* **[02_Package_Design_Homework](../09_practice_and_assignments/03_Modules_and_Packages/02_Package_Design_Homework/)** — 4 distinct multi-module package designs:
  * `01/` — Employee analytics package
  * `02/` — Student grading package
  * `03/` — Number theory package
  * `04/` — Billing and invoice processing package

---

## Common Beginner Mistakes

1. **Naming Your File the Same as a Standard Library Module:**
   * Naming a file `math.py`, `random.py`, or `os.py` shadows the standard library! When you later write `import math`, Python imports your local file instead of the built-in module, resulting in confusing `AttributeError` exceptions.
2. **Circular Imports:**
   * If `module_a` imports `module_b` and `module_b` imports `module_a` at the top level, Python fails to initialize one of them. Resolve this by refactoring shared code into a third module or importing inside functions.
3. **Using Wildcard Imports (`from module import *`):**
   * Wildcard imports pollute the namespace, make it impossible for linters to trace symbol definitions, and risk silent name collisions. Always import explicit symbols: `from math import sqrt, pi`.
4. **`ModuleNotFoundError: No module named '...'`:**
   * Happens when the directory containing the package is not in Python's search path (`sys.path`). Run your script from the project root using `python3 -m package_name.main`.

---

## Next Step

👉 Advance to **[07_error_and_file_handling](../07_error_and_file_handling/)** to master Exception Handling, Custom Exceptions, File Streams, and Context Managers!
