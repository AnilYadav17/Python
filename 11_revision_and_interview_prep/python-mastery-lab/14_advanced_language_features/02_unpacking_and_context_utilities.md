# Lesson 14.2: Extended Unpacking & Elegant Context Managers (`contextlib`)

## 1. What Is This in Simple Words?
1. **Extended Unpacking**: When extracting items from a list or tuple, Python lets you grab the first item, the last item, and bundle everything in the middle into a list using an asterisk `*`.
2. **`contextlib`**: Creating custom `with` statements by writing `__enter__` and `__exit__` dunder methods can be tedious. `contextlib.contextmanager` lets you turn any normal generator function into a full context manager using just one `yield` statement!

---

## 2. Extended Sequence Unpacking

### Catching the Middle (`*rest`)
```python
grades = [95, 88, 72, 91, 60, 99]

# Grab first, last, and bundle middle:
first, *middle, last = sorted(grades)
print(f"Lowest: {first}")   # 60
print(f"Middle: {middle}")  # [72, 88, 91, 95]
print(f"Highest: {last}")   # 99

# Dropping unneeded elements:
head, *_, tail = [1, 2, 3, 4, 5]
print(head, tail)  # 1 5
```

### Unpacking in Function Calls & Merging:
```python
default_settings = {"theme": "dark", "autosave": True, "font_size": 14}
user_settings = {"font_size": 18, "debug_mode": True}

# Dictionary merge with double asterisk (Python 3.5+):
merged = {**default_settings, **user_settings}
# In Python 3.9+, you can also simply use the union operator |:
merged_pipe = default_settings | user_settings

print(merged == merged_pipe)  # True
```

---

## 3. Creating Fast Context Managers with `@contextmanager`

Instead of creating a whole class with `__enter__` and `__exit__`:
```python
from contextlib import contextmanager
import time

@contextmanager
def execution_timer(label: str):
    start = time.perf_counter()
    print(f"[{label}] Started...")
    try:
        yield  # The code inside the 'with' block executes right here!
    finally:
        # This code is GUARANTEED to run, even if an exception crashes the with block!
        duration = (time.perf_counter() - start) * 1000
        print(f"[{label}] Finished in {duration:.2f} ms")

# How to use it:
with execution_timer("Heavy Loop"):
    total = sum(i ** 2 for i in range(100_000))
```

---

## 4. Mind-Blowing Facts! 💡

> **Fact 1: Starred Expressions Always Yield Lists!**  
> Even if you unpack a `tuple`, `set`, or `string`, the starred variable (`*rest`) is **always coerced into a Python `list`**:
> ```python
> a, *b = "Python"
> print(b)  # ['y', 't', 'h', 'o', 'n'] - it is a list!
> ```
>
> **Fact 2: Silent Error Suppression!**  
> `contextlib` has a built-in helper called `suppress`. Instead of writing an empty `try...except FileNotFoundError: pass`, you can write:
> ```python
> from contextlib import suppress
> import os
> 
> with suppress(FileNotFoundError):
>     os.remove("temporary_file.txt")
> ```
> Clean, readable, and pythonic!

---

## 5. Self-Test
1. **Question**: What happens if you put two starred targets in one unpacking statement, e.g., `*a, *b = [1, 2, 3]`?
   - *Answer*: Python raises a `SyntaxError: multiple starred expressions in assignment`. You can only have at most one starred target per unpacking expression.
