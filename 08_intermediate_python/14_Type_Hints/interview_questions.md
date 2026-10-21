# 14. Type Hints & Typing Module — Interview & Viva Questions

---

### Q1: Does Python enforce type hints at runtime?
**Model Answer:**
- **No.** Python remains an inherently dynamically typed language.
- The Python interpreter completely ignores type annotations during execution; they incur **zero runtime performance overhead**.
- Passing an incorrect type (such as passing a string to a parameter annotated `x: int`) will not raise a `TypeError` on invocation unless explicit runtime validation checks (`isinstance()`) or runtime libraries (such as Pydantic) are employed.
- Type hints exist exclusively for static analysis tools (Mypy, Pyright), IDE autocompletion, linters, and developer documentation.

---

### Q2: What is the modern syntax for `Union` and `Optional` types in Python 3.10+ (PEP 604)?
**Model Answer:**
- Prior to Python 3.10, developers imported `Union` and `Optional` from the `typing` module:
  - `Union[int, str]` (can be int or str).
  - `Optional[str]` (can be str or None; shorthand for `Union[str, None]`).
- Starting in Python 3.10 (PEP 604), the pipe operator `|` is natively supported for union types:
  - `int | str` replaces `Union[int, str]`.
  - `str | None` replaces `Optional[str]`.
- This syntax is cleaner, avoids importing from `typing`, and aligns with modern languages like TypeScript and Rust.

---

### Q3: What is the difference between nominal subtyping and structural subtyping (`typing.Protocol`)?
**Model Answer:**
- **Nominal Subtyping (Inheritance)**: Subtyping relationship is based strictly on explicit class declarations. Class `Dog` is a subtype of `Animal` only if `class Dog(Animal):` explicitly inherits from it.
- **Structural Subtyping (`typing.Protocol`, PEP 544)**: Subtyping relationship is based strictly on the structure and shape of the class (Static Duck Typing).
  - If a protocol defines `def close(self) -> None: ...`, any class that implements `close()` is automatically accepted by the type checker as satisfying the protocol, without needing to inherit from it.

---

### Q4: Why is `from __future__ import annotations` (PEP 563) useful?
**Model Answer:**
- By default in early Python versions, type annotations were evaluated as Python expressions at module definition time.
- This caused two major issues:
  1. **Forward References**: A method inside `class Node` returning `Node` raised `NameError: name 'Node' is not defined` because the class was not yet fully constructed.
  2. **Performance & Circular Imports**: Evaluating complex generic annotations at import time created unnecessary startup overhead and circular import locks.
- `from __future__ import annotations` defers evaluation by storing all annotations as raw strings in `__annotations__`, resolving forward references cleanly without needing quoted strings (`'Node'`).

---

### Q5: What is `TypedDict` and when should it be used over a `dataclass` or `namedtuple`?
**Model Answer:**
- `TypedDict` defines a type hint for standard Python dictionaries (`dict`) with a fixed set of keys and specific value types.
- At runtime, an object annotated with `TypedDict` remains an ordinary Python dictionary.
- **When to use**:
  - Use `TypedDict` when interacting with external JSON payloads, HTTP APIs, or databases where the data is naturally a dictionary and instantiating custom class instances (`dataclass`) would add unnecessary serialization/deserialization CPU overhead.
  - Use `dataclass` when you need methods, defaults, object identity, immutability, or validation.

---

### Q6: What is the difference between `Any` and `object` in Python's type system?
**Model Answer:**
- **`object`**: The root of Python's class hierarchy. Every object is an instance of `object`. The type checker allows you to assign anything to `object`, but restricts operations: you can only call methods that exist on `object` (like `__str__`, `__repr__`). Accessing arbitrary attributes raises a static type error.
- **`Any`**: An escape hatch that disables type checking entirely. The type checker permits assigning anything to `Any`, and allows calling any arbitrary method or accessing any attribute on it without reporting errors. Overusing `Any` undermines the integrity of static type analysis.

---

### Q7: How do Generics and `TypeVar` preserve type safety across function inputs and outputs?
**Model Answer:**
- If you write `def get_first(items: list[Any]) -> Any:`, the return type is lost; the caller receives `Any`, allowing subsequent invalid method calls to go undetected.
- By declaring `T = TypeVar('T')` and writing `def get_first(items: list[T]) -> T:`, you create a generic contract:
  - If the caller passes `list[int]`, `T` binds to `int`, and the return type is statically inferred as `int`.
  - If the caller passes `list[str]`, the return type is statically inferred as `str`.
- This preserves full type safety and IDE autocompletion downstream without sacrificing reusability.
