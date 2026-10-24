# Lesson 12: Free-Threaded CPython (PEP 703: The Death of the GIL)

## 1. The Historic Milestone: Python Without the GIL!

For over 30 years, removing the GIL from CPython was considered the "Holy Grail" of Python engineering.  
Previous attempts failed because removing the GIL made ordinary single-threaded Python code 30% to 50% slower.

In **Python 3.13 and 3.14**, under **PEP 703 (Making the Global Interpreter Lock Optional in CPython)** by Sam Gross, Python achieved the impossible:

> **Free-Threaded CPython allows true multi-core parallel execution of Python bytecode across all CPU cores without the GIL!**

---

## 2. Fascinating Fact: How Did They Finally Eliminate the GIL? 💡
> **Did you know?**
> To kill the GIL without slowing Python down, three revolutionary computer science breakthroughs were implemented in CPython:
> 1. **Biased Reference Counting**: When an object is only accessed by the thread that created it, Python modifies its ref count with ultra-fast non-atomic operations. Only when shared across multiple threads does it fall back to atomic operations!
> 2. **`mimalloc` Thread-Safe Allocator**: Developed by Microsoft Research, `mimalloc` provides thread-local memory allocation pools with zero lock contention.
> 3. **Immortal Objects (PEP 683)**: Built-in singletons (like `None`, `True`, `False`, small integers, and core type definitions) have their reference counts marked as "immortal"—their reference counts are **never incremented or decremented**, eliminating cache line bouncing across CPU cores!

---

## 3. Running Free-Threaded Python

On systems with free-threaded builds installed, the binary is typically named `python3.14t` (with a `t` for threaded):

```bash
# Check if the current interpreter has the GIL disabled:
python3 -c "import sys; print('GIL active?', getattr(sys, '_is_gil_enabled', lambda: True)())"
```

In standard builds, this prints `True`. In free-threaded builds with `--disable-gil`, it prints `False`!

---

## 4. Quick Self-Test
1. What PEP formalizes the removal of the GIL in modern CPython?
   - *Answer: PEP 703.*
2. What are "Immortal Objects" in Python?
   - *Answer: Objects whose reference counts are fixed and never change, preventing CPU cache bouncing in multi-threaded execution.*
