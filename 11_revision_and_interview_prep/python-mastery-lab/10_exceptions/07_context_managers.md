# Lesson 07: Context Managers and the `with` Statement

## 1. What Is a Context Manager in Simple Words?
Think of renting a hotel room:
- **Check-in (`__enter__`)**: You get the keycard and the lights turn on.
- **Your Stay (inside `with`)**: You sleep and work in the room.
- **Check-out (`__exit__`)**: You return the keycard, and the room is cleaned—**even if an emergency happened during your stay!**

In Python, a **Context Manager** guarantees that resources (like open files, network connections, or database locks) are automatically and cleanly closed when you are done with them.

```python
# The with statement automatically closes the file when the block exits!
with open("notes.txt", "w") as f:
    f.write("Learning Python Mastery!")
# The file is 100% closed right here, even if f.write() had crashed!
```

---

## 2. Building a Custom Context Manager from Scratch

To make any custom class work with `with`, implement two methods:
1. **`__enter__(self)`**: Sets up the resource and returns it.
2. **`__exit__(self, exc_type, exc_val, exc_tb)`**: Cleans up the resource.

```python
import time

class PerformanceTimer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self  # Can be bound using 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"[TIMER] Block took {self.elapsed:.6f} seconds")
        # Return False to let any exceptions bubble up normally:
        return False

# Use our custom timer with 'with':
with PerformanceTimer():
    total = sum(i ** 2 for i in range(500_000))
```

---

## 3. The Modern Shortcut: `@contextlib.contextmanager`

Don't want to create a full class with `__enter__` and `__exit__`?  
Python lets you turn a **generator with `yield` into a context manager**:

```python
from contextlib import contextmanager

@contextmanager
def temporary_heading(title: str):
    print(f"\n--- START {title} ---")
    try:
        yield  # Code inside the 'with' block runs right here!
    finally:
        print(f"--- END {title} ---\n")

with temporary_heading("DATABASE SYNC"):
    print("Writing records...")
    print("Flushing buffers...")
```
**Output:**
```
--- START DATABASE SYNC ---
Writing records...
Flushing buffers...
--- END DATABASE SYNC ---
```

---

## 4. Quick Self-Test
1. What two methods make an object a Context Manager?
   - *Answer: `__enter__()` and `__exit__()`.*
2. How can an `__exit__` method suppress an exception that happened inside the `with` block?
   - *Answer: By returning `True` from `__exit__`.*
