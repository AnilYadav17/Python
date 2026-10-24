# Lesson 13.2: Functools & Regular Expressions

## 1. What Is This in Simple Words?
- **`functools`**: Tools for working with and modifying functions. It includes automatic caching (memoization) and partial function pre-filling.
- **`re` (Regular Expressions)**: A mini-programming language inside Python for pattern searching, validating emails, phone numbers, and extracting text.

---

## 2. Power Tools in `functools`

### A. `@lru_cache`: Turn Slow Recursive Functions into Instant Miracles
LRU stands for **Least Recently Used**. It saves function outputs in a fast hash table in memory.
```python
import functools
import time

# Without cache: Fibonacci(35) takes seconds.
# With @lru_cache: It takes milliseconds!
@functools.lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

start = time.perf_counter()
print(fibonacci(50))  # 12586269025
print(f"Elapsed: {(time.perf_counter() - start) * 1000:.3f} ms")
```

### B. `functools.partial`: Freeze Arguments
Freeze a few arguments of a function to create a simpler specialized helper:
```python
from functools import partial

def multiply(x: int, y: int) -> int:
    return x * y

# Create a specialized double function
double = partial(multiply, 2)

print(double(5))   # 10
print(double(10))  # 20
```

---

## 3. Regular Expressions with `re`

### A. Core Pattern Matching
```python
import re

text = "Contact us at support@example.com or admin@python.org"

# Extract all email addresses
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)
print(emails)  # ['support@example.com', 'admin@python.org']
```

### B. Compiling Patterns for Speed
If you match a regex inside a loop, always use `re.compile()` once outside the loop:
```python
pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")  # YYYY-MM-DD
if pattern.match("2026-10-23"):
    print("Valid date format!")
```

---

## 4. Fascinating Fact 💡
> **The Catastrophic Backtracking Trap**:
> Python's `re` module uses an NFA (Nondeterministic Finite Automaton) engine. If you write an ambiguous regex with nested quantifiers like `r"(a+)+$"` and test it against `"aaaaaaaaaaaaaaaaaaaaX"`, Python's regex engine attempts millions of combinations before failing.  
> This can freeze your entire CPU core—a classic denial of service vulnerability known as **ReDoS (Regular Expression Denial of Service)**!

---

## 5. Quick Self-Test
1. What does `@lru_cache` require from function arguments?
   - *Answer: All arguments must be **hashable** (immutable), because the cache stores them as dictionary keys.*
2. Why is raw string notation `r"..."` recommended when writing regular expressions in Python?
   - *Answer: It prevents Python from interpreting backslashes like `\n` or `\b` as escape sequences, letting the regex engine receive literal backslashes.*
