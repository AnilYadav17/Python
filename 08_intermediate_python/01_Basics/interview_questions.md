# 01. Basics — Interview & Viva Questions

---

### Q1: What is the difference between `is` and `==` in Python?
**Model Answer:**
- `==` checks for **value equality**: it evaluates whether the values represented by two objects are equal by calling the `__eq__()` magic method.
- `is` checks for **reference identity**: it evaluates whether two variables point to the exact same object in memory by comparing their memory addresses (`id(a) == id(b)`).
- Example: `[1, 2] == [1, 2]` is `True`, but `[1, 2] is [1, 2]` is `False` because two separate list instances are allocated on the heap.

---

### Q2: What happens under the hood when you write `[[0] * 3] * 3` in Python?
**Model Answer:**
- The inner expression `[0] * 3` allocates a single list of three zeros: `[0, 0, 0]`.
- The outer multiplier `* 3` creates a new list containing three references to that **exact same** inner list object (shallow repetition of pointers).
- Consequently, modifying an element in one row (e.g., `grid[0][0] = 1`) alters that element across all rows because every row points to the same underlying list. The correct approach is a comprehension: `[[0] * 3 for _ in range(3)]`.

---

### Q3: What is "small integer caching" in CPython?
**Model Answer:**
- At startup, CPython creates and caches singleton integer objects for all values in the range `[-5, 256]`.
- Whenever an integer within this range is referenced, CPython returns the pointer to the existing cached singleton rather than allocating a new `PyLongObject`.
- Therefore, for any two variables assigned integers within `[-5, 256]`, `a is b` evaluates to `True`. Beyond this range, distinct objects are dynamically allocated at runtime.

---

### Q4: Why can't a list be used as a dictionary key or set element in Python?
**Model Answer:**
- Dictionary keys and set elements require objects to be **hashable**. An object is hashable if it possesses a hash code that never changes during its lifetime (implements `__hash__()`) and can be compared for equality (`__eq__()`).
- Lists are **mutable**: their contents can be modified at any time. If a list's contents changed while serving as a hash key, its hash bucket position would change, making the entry permanently unretrievable in the hash table. Hence, lists raise `TypeError: unhashable type: 'list'`. Tuples containing only immutable objects should be used instead.

---

### Q5: How does Python's `for-else` and `while-else` construct work?
**Model Answer:**
- In Python, loops can have an optional `else` block.
- The `else` block executes **only if the loop completes normally without encountering a `break` statement**.
- If the loop terminates early via `break`, the `else` block is completely skipped. It also executes if the loop condition was initially false (e.g. iterating over an empty collection). It is commonly used for search loops to execute fallback logic when no target element was found.

---

### Q6: Why does `0.1 + 0.2 != 0.3` evaluate to `True` in Python, and how should floating-point numbers be compared?
**Model Answer:**
- Python floats are 64-bit IEEE 754 double-precision numbers. Floating-point numbers are represented in binary (base 2). Fractions like $0.1$ ($1/10$) and $0.2$ ($1/5$) are infinite repeating fractions in binary, just as $1/3$ is in decimal ($0.333\dots$).
- When converted to 53 bits of mantissa precision, rounding truncation introduces a tiny representation error: `0.1 + 0.2` becomes `0.30000000000000004`.
- Exact equality `==` fails. Floats should always be compared using `math.isclose(a, b)` or `pytest.approx()` with a tolerance threshold.

---

### Q7: What are dictionary views, and what set-like properties do they provide?
**Model Answer:**
- Calling `.keys()`, `.values()`, or `.items()` on a dictionary returns **view objects** (`dict_keys`, `dict_values`, `dict_items`).
- View objects provide dynamic, read-only reflection of the dictionary's contents without copying memory: if the underlying dictionary updates, the view immediately reflects the change.
- Crucially, `dict_keys` and `dict_items` implement the `collections.abc.Set` interface, allowing direct mathematical set operations (union `|`, intersection `&`, difference `-`, symmetric difference `^`) with other sets and dictionary views.
