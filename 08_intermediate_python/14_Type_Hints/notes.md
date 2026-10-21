# 14. Type Hints & Typing Module: Complete Reference

---

## 1. Static Type Checking in Python & PEP 484

### What it is
- **Type Annotations (PEP 484)**: A standardized syntax allowing developers to explicitly annotate variable types, function parameter types, and return values:
  ```python
  def calculate_tax(amount: float, rate: float = 0.05) -> float:
      return amount * rate
  ```
- **Static Analysis Tools**: External type checkers like **Mypy**, **Pyright**, or IDE language servers that analyze code for type discrepancies *before* the code runs.
- **Runtime Performance Neutrality**: Python remains dynamically typed at runtime; type annotations are completely ignored by the Python interpreter during execution and incur **zero runtime performance penalty**.

### Why it matters
- **Self-Documenting Code**: Eliminates guessing parameter types or return structures in large codebases.
- **Catches Bugs Early**: Identifies `NoneType` errors, missing arguments, invalid types, and refactoring mistakes before reaching production.
- **Supercharged IDEs**: Powers accurate autocompletion, refactoring renames, and instant static error highlighting.

### How it works (internals, if relevant)
- Python stores type annotations in the `__annotations__` dictionary of functions, modules, and classes.
- Since Python 3.7 (and PEP 563), `from __future__ import annotations` stores annotations as lazy strings instead of evaluating them at module load time, eliminating circular import issues for type annotations.

### Common mistakes / gotchas
- Believing type hints enforce runtime validation: passing `"5"` to `def square(x: int): return x * x` will execute normally at runtime (and crash with `TypeError`), because Python does NOT validate types at runtime. For runtime validation, tools like Pydantic are used.

### Connects to
- Basic and Collection Type Hints (subtopic 2 below).

---

## 2. Basic & Collection Type Hints

### What it is
- **Primitive Types**: `int`, `float`, `str`, `bool`, `bytes`, `None`.
- **Return Type Annotations**: `-> None` for functions with no return; `-> int` for returned values.
- **Built-in Generics (PEP 585, Python 3.9+)**:
  - Lists: `list[str]` (a list containing strings).
  - Dictionaries: `dict[str, int]` (mapping string keys to integer values).
  - Sets: `set[int]`.
  - Tuples:
    - Fixed length: `tuple[int, str, float]` (heterogeneous 3-tuple).
    - Variable length: `tuple[int, ...]` (homogenous tuple of arbitrary length).

### Why it matters
- Modern Python 3.9+ deprecates importing capitalized collection types (`from typing import List, Dict, Set, Tuple`); standard built-ins can be used directly as generic types.

### How it works (internals, if relevant)
- Built-in types implement `__class_getitem__()` to return `types.GenericAlias` objects when indexed with brackets.

### Common mistakes / gotchas
- Writing `tuple[int]` and expecting it to mean a tuple of multiple integers: `tuple[int]` means a tuple of *exactly one* integer! For arbitrary numbers of integers, use `tuple[int, ...]`.
- Using legacy `typing.List` in modern Python 3.9+ code.

### Connects to
- Union and Optional Types (subtopic 3 below).

---

## 3. Union and Optional Types

### What it is
- **Union Type**: Signifies that a variable or parameter can accept one of several types.
  - Legacy syntax: `typing.Union[int, str]`
  - Modern syntax (PEP 604, Python 3.10+): `int | str`
- **Optional Type**: Signifies that a parameter can accept a specific type OR `None`.
  - Legacy syntax: `typing.Optional[str]`
  - Modern syntax: `str | None`

### Why it matters
- The single most common runtime bug in modern software is `AttributeError: 'NoneType' object has no attribute '...'`.
- Static type checkers force developers to explicitly guard against `None` before accessing attributes:
  ```python
  def greet(user: str | None) -> str:
      if user is None: # Type checker enforces this guard!
          return "Hello, Guest"
      return f"Hello, {user.upper()}"
  ```

### How it works (internals, if relevant)
- The binary `|` operator invokes `types.UnionType.__or__()`.
- `Optional[T]` is purely syntactic shorthand for `Union[T, None]`.

### Common mistakes / gotchas
- Assuming a default parameter `val=None` automatically makes it Optional: writing `def search(query: str = None)` is a type error in strict mode; you must annotate `query: str | None = None`.

### Connects to
- Advanced Typing Constructs (subtopic 4 below).

---

## 4. Advanced Typing Constructs (`Any`, `Callable`, `Literal`, `Final`)

### What it is
- Specialized typing constructs from `typing`:
  - **`Any`**: Opts out of static type checking; allows any operation without type checker complaints.
  - **`Callable[[Arg1Type, Arg2Type], ReturnType]`**: Annotates functions, lambdas, or callable objects.
  - **`Literal["RED", "GREEN", "BLUE"]`**: Enforces that a variable can only equal specific exact values.
  - **`Final`**: Marks a variable or attribute as constant that cannot be reassigned or overridden.
  - **`TypeAlias`**: Explicitly declares a type alias for complex signatures.

### Why it matters
- `Literal` provides type-safe enumeration replacements for string flags (e.g. `mode: Literal["r", "w"]`).
- `Callable` ensures callback functions match expected signatures in higher-order architectures.

### How it works (internals, if relevant)
- Type checkers enforce `Literal` matching during AST scanning; at runtime, `Literal` is an instance of `_SpecialForm`.

### Common mistakes / gotchas
- Overusing `Any`: defeats the entire purpose of static typing (the "any virus" spreads through downstream code).
- Misunderstanding `Final`: Python will not prevent re-assignment at runtime; only static type checkers like Mypy will flag the violation.

### Connects to
- Generics and Type Variables (subtopic 5 below).

---

## 5. Generics & Type Variables (`TypeVar`)

### What it is
- Mechanism for writing parameterized, reusable functions and classes that preserve type relationships across inputs and outputs.
- **`TypeVar("T")`**: Represents a generic type placeholder.
  ```python
  from typing import TypeVar

  T = TypeVar("T")

  def first_element(items: list[T]) -> T:
      return items[0]
  ```
- **Bounded TypeVars**: `T = TypeVar("T", bound=Comparable)` restricts types to subclasses.

### Why it matters
- Without `TypeVar`, writing `def first_element(items: list[Any]) -> Any` destroys type information: the caller receives `Any` instead of the original type.
- Enables building generic data structures (e.g. `class Stack[T]` or `class Repository[T]`).

### How it works (internals, if relevant)
- When a generic function is called, the static type checker binds `T` to the concrete argument type and infers the return type accordingly.
- Since Python 3.12 (PEP 695), Python introduces native generic syntax: `def first[T](` `items: list[T]) -> T: ...`.

### Common mistakes / gotchas
- Re-using a single `TypeVar` across independent unrelated parameters when they should be separate type variables (`T1`, `T2`).

### Connects to
- Structural Subtyping with Protocols (subtopic 6 below).

---

## 6. Structural Subtyping with `typing.Protocol`

### What it is
- **Static Duck Typing (PEP 544)**: Defines interfaces based on structure/methods rather than nominal class inheritance:
  ```python
  from typing import Protocol

  class Renderable(Protocol):
      def render(self) -> str: ...
  ```
- Any class that implements `def render(self) -> str:` is automatically considered a valid subtype of `Renderable` without needing to inherit from it!

### Why it matters
- Eliminates tight coupling: libraries can define protocols without forcing downstream consumers to inherit from library-specific base classes.
- Brings formal static type checking to Python's classic duck typing philosophy.

### How it works (internals, if relevant)
- Static type checkers verify that classes supply all methods and attributes defined in the `Protocol`.
- Can be decorated with `@typing.runtime_checkable` to allow runtime `isinstance(obj, Renderable)` validation.

### Common mistakes / gotchas
- Forgetting that `@runtime_checkable` only verifies method *existence*, NOT method signatures or return types at runtime!

### Connects to
- Structured Dictionaries with TypedDict (subtopic 7 below).

---

## 7. Structured Dictionaries (`TypedDict`)

### What it is
- Subclass of `dict` that enforces static type annotations on dictionary keys and values:
  ```python
  from typing import TypedDict

  class UserPayload(TypedDict):
      id: int
      username: str
      is_active: bool
  ```

### Why it matters
- Provides type safety and autocompletion for raw JSON/dictionary payloads common in REST APIs, without the overhead of instantiating full OOP classes.
- Validates required vs optional keys using `total=False`.

### How it works (internals, if relevant)
- At runtime, an instance of `UserPayload` is just a standard Python dictionary `dict`.
- Static type checkers verify that required keys exist and match declared types.

### Common mistakes / gotchas
- Expecting `TypedDict` to perform runtime type casting: initializing `UserPayload(id="not-an-int", ...)` does not raise an error at runtime.
- Attempting to use `isinstance(data, UserPayload)`: raises `TypeError` unless handled carefully.

### Connects to
- Intro to Flask (Topic 20) for typed request/response handlers.
