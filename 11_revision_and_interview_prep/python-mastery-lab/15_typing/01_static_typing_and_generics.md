# Lesson 15.1: Modern Static Typing, Generics & Protocols

## 1. What Is This in Simple Words?
Python is dynamically typed: you don't *have* to declare types. But in large production systems, static type hints (`x: int = 5`) act like a built-in safety shield.  
- **Type Annotations**: Tell your IDE, teammates, and static analysis tools (like `mypy` or `pyright`) what type of data a variable, parameter, or function returns.
- **Generics**: Let you write flexible functions that work with *any* type while preserving that exact type.
- **Protocols (Duck Typing formalized)**: "If it walks like a duck and quacks like a duck, it is a duck!" `Protocol` allows you to define what methods an object MUST have without forcing it to inherit from a base class.

---

## 2. Modern Type Hints (Python 3.10+)

### Clean Union & Optional Syntax (`|` operator):
In older Python versions, you needed `from typing import Union, Optional`. Modern Python uses the pipe symbol `|`:
```python
# 'name' is either a string or None:
def greet(name: str | None = None) -> str:
    if name is None:
        return "Hello, Guest!"
    return f"Hello, {name}!"

# Collections don't need imports either:
def summarize_scores(scores: list[float]) -> dict[str, float]:
    return {
        "min": min(scores),
        "max": max(scores),
        "avg": sum(scores) / len(scores)
    }
```

---

## 3. Generics with `TypeVar`

If you write a function that returns the first element of a list:
```python
from typing import TypeVar, Sequence

T = TypeVar("T")  # Represents any consistent type

def get_first_element(items: Sequence[T]) -> T | None:
    return items[0] if items else None

first_num: int | None = get_first_element([10, 20, 30])
first_str: str | None = get_first_element(["apple", "banana"])
```
The IDE knows that `first_num` is an `int` and `first_str` is a `str`!

---

## 4. Structural Subtyping with `Protocol` (Duck Typing Verified)

You don't need inheritance! Define the interface you need:
```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str:
        ...

# Any class that has a render() method automatically satisfies Renderable:
class UserCard:
    def __init__(self, username: str):
        self.username = username
    
    def render(self) -> str:
        return f"<div class='card'>{self.username}</div>"

def display(item: Renderable) -> None:
    print(item.render())

# UserCard never inherited from Renderable, yet static type checkers approve!
display(UserCard("Alice"))
```

---

## 5. Mind-Blowing Facts! 💡

> **Fact 1: Python Completely Ignores Type Hints at Runtime!**  
> Unless you explicitly use a validation library like Pydantic, Python's CPython interpreter **never** checks type hints while executing!
> ```python
> def add(a: int, b: int) -> int:
>     return a + b
> 
> print(add("Hello, ", "World!"))  # Works perfectly! Prints 'Hello, World!'
> ```
> Type hints are purely metadata for developers, documentation, and static linters!
>
> **Fact 2: `__annotations__` Dictionary!**  
> Python stores your type hints inside a special dictionary attribute on the function called `__annotations__`:
> ```python
> print(add.__annotations__)
> # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
> ```

---

## 6. Self-Test
1. **Question**: Does adding type annotations make Python code execute faster in standard CPython?
   - *Answer*: No. Type annotations are purely metadata in standard CPython and have zero impact on runtime bytecode execution speed. (However, tools like Cython or MypyC can compile typed code into ultra-fast C extensions!)
