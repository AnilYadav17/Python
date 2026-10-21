# 🧠 08_Intermediate_Python: The Definitive Reference & Knowledge Base

Welcome to **08_Intermediate_Python**, the definitive, exhaustive, and structured knowledge base designed to bridge fundamentals, advanced Python internals, system design patterns, and engineering best practices.

This module provides comprehensive theoretical notes, real-world executable code demonstrations (5 tailored examples per topic), and core technical interview questions across 18 specialized Python domains.

---

## 🗺️ Topic Tracker & Architecture Index

| # | Domain / Topic | Core Concepts Covered | Status | Directory Link |
|---|:---|:---|:---:|:---|
| 01 | **Basics Internals** | Variables, dynamic typing, type casting, I/O, control flow, loops, collections | `Completed` | [01_Basics](./01_Basics/) |
| 02 | **Functions & Closures** | `*args`/`**kwargs`, LEGB scope, closures, lambdas, decorators, recursion | `Completed` | [02_Functions](./02_Functions/) |
| 03 | **Modules & Packages** | Imports, `__init__.py`, custom packages, standard library deep dive | `Completed` | [03_Modules_and_Packages](./03_Modules_and_Packages/) |
| 04 | **OOP Architecture** | Classes, `@classmethod`, `@staticmethod`, inheritance, MRO, dunder methods | `Completed` | [04_OOP](./04_OOP/) |
| 05 | **Exception Architecture** | `try`/`except`/`else`/`finally`, custom errors, exception chaining, stack traces | `Completed` | [05_Exception_Handling](./05_Exception_Handling/) |
| 06 | **File Streams & I/O** | Text/binary streams, `with` internals, large file chunking, buffers | `Completed` | [06_File_Handling](./06_File_Handling/) |
| 07 | **DSA Fundamentals** | Arrays, two-pointer, sliding window, binary search, sorting algorithms | `Completed` | [07_DSA_Fundamentals](./07_DSA_Fundamentals/) |
| 08 | **Time Complexity & Big-O** | Asymptotic analysis, $O(1)$ to $O(2^n)$, space complexity, profiling | `Completed` | [08_Time_Complexity_and_Big_O](./08_Time_Complexity_and_Big_O/) |
| 09 | **Python Memory Management** | Reference counting, cyclic GC, `gc` module, object identity, shallow vs deep copy | `Completed` | [09_Python_Memory_Management](./09_Python_Memory_Management/) |
| 10 | **Context Managers** | `with` mechanics, `__enter__` & `__exit__`, `@contextmanager`, resource safety | `Completed` | [10_Context_Managers](./10_Context_Managers/) |
| 11 | **Iterators & Generators** | Iterator protocol (`__iter__`/`__next__`), `yield`, pipeline streams, `itertools` | `Completed` | [11_Iterators_and_Generators](./11_Iterators_and_Generators/) |
| 12 | **Testing & TDD** | `unittest`, `pytest`, fixtures, parameterized tests, mocking, assertions | `Completed` | [12_Testing](./12_Testing/) |
| 13 | **Regular Expressions** | Regex engine, quantifiers, capturing groups, lookahead/lookbehind, validations | `Completed` | [13_Regular_Expressions](./13_Regular_Expressions/) |
| 14 | **Type Hints & Static Typing** | PEP 484, `Optional`, `Union`, `TypeVar`, `Protocol`, `TypedDict` | `Completed` | [14_Type_Hints](./14_Type_Hints/) |
| 15 | **Virtual Envs & Packaging** | `venv`, dependency management, `requirements.txt`, `pyproject.toml`, wheels | `Completed` | [15_Virtual_Environments_and_Packaging](./15_Virtual_Environments_and_Packaging/) |
| 16 | **Data Structures from Scratch** | Linked Lists, Stack, Queue, Hash Map, Binary Search Tree, Graph | `Completed` | [16_Data_Structures_from_Scratch](./16_Data_Structures_from_Scratch/) |
| 17 | **Concurrency & Asynchrony** | Threading, Multiprocessing, Asyncio event loop, GIL trade-offs | `Completed` | [17_Concurrency](./17_Concurrency/) |
| 18 | **Databases with Python** | DB-API 2.0, `sqlite3`, parameterized queries, transactions (ACID) | `Completed` | [18_Databases_with_Python](./18_Databases_with_Python/) |
| 19 | **Git & GitHub Workflows** | Branching, rebase, semantic commits, PR workflows | `Planned` | *(Roadmap Addition)* |
| 20 | **Web Backend (Flask/FastAPI)** | WSGI/ASGI, routing, request/response, REST APIs | `Planned` | *(Roadmap Addition)* |

---

## 🏛️ Directory Architecture

Every topic folder follows an identical, rigorous three-part structure:

```text
08_intermediate_python/
├── XX_Topic_Name/
│   ├── notes.md                 # In-depth structured theoretical notes & internals
│   ├── examples/                # 5 runnable Python files demonstrating 5 distinct angles
│   │   ├── 01_basic_usage.py
│   │   ├── 02_edge_cases.py
│   │   ├── 03_real_world_use_case.py
│   │   ├── 04_common_mistakes_and_fixes.py
│   │   └── 05_advanced_idiomatic.py
│   └── interview_questions.md   # 5-8 high-yield technical interview questions with answers
```

---

## 🚀 How to Use This Knowledge Base

1. **Active Revision**: Check off each subtopic in [`progress_tracker.md`](./progress_tracker.md) as you master it.
2. **Read Notes**: Review `notes.md` to understand foundational theory, under-the-hood CPython mechanics, and pitfalls.
3. **Execute & Experiment**: Run every script inside `examples/`. Modify parameters and observe behavior.
4. **Mock Interview**: Attempt answering each prompt in `interview_questions.md` before reading the model answers.

---

## Next Step

👉 Ready to test your problem-solving skills against hundreds of exercises? Explore **[09_practice_and_assignments](../09_practice_and_assignments/)** and **[10_coding_challenges](../10_coding_challenges/)**!
