# Python Mastery Lab

> **A Systematic, Internals-Driven, Production-Grade Python Engineering Workspace.**

Welcome to the **Python Mastery Lab**. This repository is not a casual tutorial or a collection of superficial syntax cheat sheets. It is an end-to-end, multi-file engineering workspace designed to rebuild your Python knowledge from absolute first principles to expert-level runtime mechanics, architecture, and production readiness.

---

## 1. Core Principles

1. **Start from Zero**: No hand-waving or skipping foundations. We dissect what programming is, why Python was created, how the CPython virtual machine works, and how code moves from text to execution.
2. **Precision Over Metaphor**: Variables are not "boxes"; they are named pointers in namespaces referencing heap-allocated `PyObject` structs. We distinguish language specifications from CPython implementation choices.
3. **Internal Mechanics**: Learn not just *how* Python works, but *why* it works that way under the hood—memory layout, evaluation frames, AST compilation, bytecode, adaptive specialization, and reference counting.
4. **Active Experimentation**: Every theoretical concept is coupled with executable Python experiments in `26_experiments/`, verification tests in `tests/`, and progressive exercises in `27_exercises/`.
5. **No Placeholders**: Every file created contains rich, verifiable, production-grade material.

---

## 2. Workspace Navigation

```
python-mastery-lab/
│
├── README.md                 # Workspace guide and overview (you are here)
├── ROADMAP.md                # 5-level curriculum, module dependencies & milestones
├── PROGRESS.md               # Active mastery checklist, diagnostic logs & project status
├── GLOSSARY.md               # Rigorous technical definitions (LEGB, PyObject, GIL, AST)
├── PYTHON_VERSION.md         # Active environment specs, version milestones, language vs CPython
├── LEARNING_METHOD.md        # The 24-point standard lesson framework & learning tracks
├── pyproject.toml            # Project configuration (pytest, ruff, mypy)
├── .gitignore                # Production Python git exclusions
│
├── 00_orientation/           # Module 00: Architecture, computing model, compilation pipeline
├── 01_language_fundamentals/ # Module 01: Lexing, indentation, tokens, expressions & statements
├── 02_names_objects_memory/  # Module 02: Pointers, bindings, mutability, aliasing, GC
├── 03_data_types/            # Module 03: All 16 primitive and collection types & hashability
├── 04_operators/             # Module 04: Precedence, short-circuiting, dunder protocols
├── 05_control_flow/          # Module 05: Branching, pattern matching, loop mechanics
├── 06_functions/             # Module 06: Parameters, closures, scope, decorators, frames
├── 07_iterators_generators/  # Module 07: Iteration protocol, generators, lazy evaluation
├── 08_data_structures_algo/  # Module 08: Algorithmic complexity, sequences, hash tables
├── 09_oop/                   # Module 09: Class construction, MRO, descriptors, metaclasses
├── 10_exceptions/            # Module 10: Exception hierarchies, chaining, context managers
├── 11_modules_imports/       # Module 11: sys.modules, import hooks, circular imports
├── 12_files_data_formats/    # Module 12: Encodings, pathlib, JSON, CSV, binary streams
├── 13_standard_library/      # Module 13: itertools, functools, subprocess, re, logging, etc.
├── 14_advanced_features/     # Module 14: Structural typing, assignment expressions, edge cases
├── 15_typing/                # Module 15: Static analysis, generics, protocols, TypeVar
├── 16_testing_quality/       # Module 16: Pytest, fixtures, mocks, property testing, coverage
├── 17_debugging/             # Module 17: Breakpoints, tracebacks, logging, reproducing bugs
├── 18_runtime_internals/     # Module 18: CPython VM, bytecode, code objects, vectorcall
├── 19_concurrency/           # Module 19: Threads, multiprocessing, GIL, AsyncIO
├── 20_performance/           # Module 20: cProfile, tracemalloc, timeit, optimization
├── 21_security/              # Module 21: Injection, deserialization, path traversal, secrets
├── 22_networking_apis/       # Module 22: Sockets, HTTP, connection pools, async clients
├── 23_database_programming/  # Module 23: DB-API, transactions, ACID, repository patterns
├── 24_professional_eng/      # Module 24: Architecture, 12-factor apps, packaging, CI/CD
├── 25_c_extensions/          # Module 25: C API, ctypes, PyO3/Rust, runtime tradeoffs
│
├── 26_experiments/           # Executable test-bench scripts to inspect runtime behavior
├── 27_exercises/             # Beginner, intermediate, advanced, output prediction & bugs
├── 28_projects/              # 9 progressively harder end-to-end software projects
├── 29_reference/             # Quick references, traps, complexity tables, interview prep
└── tests/                    # Automated test suites validating concepts and projects
```

---

## 3. Quickstart & Environment Setup

Run Python from within this repository using Linux terminal:

```bash
# 1. Navigate to the workspace
cd /home/anil/Desktop/Revise/python-mastery-lab

# 2. Verify active Python interpreter (targets 3.12+; current: 3.14.4)
python3 --version

# 3. Create a dedicated virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 4. Run tests
python3 -m unittest discover tests/
```

---

## 4. How We Study Together

Each lesson follows an interactive pair-programming dynamic:
1. **Lesson Presentation**: We cover the concept thoroughly using the 24-point structure (theory, motivation, syntax, execution trace, CPython internals, edge cases).
2. **Interactive Probe**: I will pause with targeted questions, output-prediction drills, or debugging challenges.
3. **Hands-On Verification**: You run the accompanying `.py` experiments in `26_experiments/` and observe what the interpreter outputs.
4. **Demonstration & Update**: Only when you articulate the mechanics correctly and solve the exercise will we mark the topic as `MASTERED` in [PROGRESS.md](file:///home/anil/Desktop/Revise/python-mastery-lab/PROGRESS.md) and move to the next concept.
