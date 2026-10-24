# PEP Standards & Modern Typing Architecture Guide

Python Enhancement Proposals (PEPs) define the evolution of the language. Here is a guide to the PEPs that every senior Python engineer should know.

---

## 1. Landmark PEPs
- **PEP 8**: Style Guide for Python Code (indentation, naming conventions, import ordering).
- **PEP 20**: The Zen of Python (`import this`).
- **PEP 249**: Python Database API Specification v2.0 (DB-API 2.0).
- **PEP 257**: Docstring Conventions.
- **PEP 484**: Type Hints (foundation of Python's static typing ecosystem).
- **PEP 517 / 518**: Build system independent format for source trees (`pyproject.toml`).
- **PEP 572**: Assignment Expressions (The Walrus Operator `:=`).
- **PEP 604**: Union syntax using the pipe operator (`int | str` instead of `Union[int, str]`).
- **PEP 634**: Structural Pattern Matching (`match / case`).
- **PEP 659**: Specializing Adaptive Interpreter (Faster CPython project).
- **PEP 703**: Making the Global Interpreter Lock (GIL) Optional in CPython (Free-threaded Python).

---

## 2. Modern Typing Matrix (Python 3.10+)

| Type Feature | Modern Syntax (3.10+) | Legacy Syntax (< 3.10) |
| :--- | :--- | :--- |
| **Union Types** | `int | str` | `Union[int, str]` |
| **Nullable / Optional** | `str | None` | `Optional[str]` |
| **Standard Collections** | `list[int]`, `dict[str, Any]` | `List[int]`, `Dict[str, Any]` |
| **Generics** | `def first[T](l: list[T]) -> T:` (3.12+) | `T = TypeVar("T")` |
| **Structural Duck Typing**| `class P(Protocol): ...` | Class inheritance |
| **Callable Signatures** | `Callable[[int, int], bool]` | `Callable[..., Any]` |

---

## 3. Best Practices for Professional Python
1. **Never use bare `except:`**: Always catch explicit exceptions (`except KeyError:` or `except Exception:`).
2. **Favor composition and Protocols over deep inheritance hierarchies**: Keep classes small and cohesive.
3. **Use linters in CI**: Enforce strict Ruff checks (`ruff check .` and `ruff format .`) on every commit.
4. **Isolate dependencies**: Use dedicated virtual environments (`python3 -m venv .venv`).
