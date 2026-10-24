# Lesson 03: Identity (`is`) vs. Equality (`==`)

## 1. The Real-World Analogy: Identical Twins

Imagine identical twin brothers: Peter and Paul.
- If you ask: *"Do they look identical and have the same DNA?"* $\to$ **YES** (`Peter == Paul` is `True`).
- If you ask: *"Are Peter and Paul the exact same single human being?"* $\to$ **NO!** If Peter gets a haircut, Paul's hair doesn't magically disappear! (`Peter is Paul` is `False`).

This is the exact difference between `==` and `is` in Python:

- **Equality (`==`)**: Checks if two objects hold the **same data/value**.
- **Identity (`is`)**: Checks if two variables point to the **exact same physical memory address** (`id(a) == id(b)`).

---

## 2. A Crystal-Clear Example

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2:", list1 == list2)  # True (they have the same contents)
print("list1 is list2:", list1 is list2)  # False (two distinct lists in memory!)

print("list1 == list3:", list1 == list3)  # True (same contents)
print("list1 is list3:", list1 is list3)  # True (list3 is an alias for list1!)
```

```
Memory Diagram:

  Address 0x100: [1, 2, 3]  <--- list1, list3 point here
  Address 0x200: [1, 2, 3]  <--- list2 points here
```

---

## 3. The Small Integer Cache Trap: Why `is` Breaks on Numbers!

Try running this inside Python:
```python
x = 100
y = 100
print(x is y)  # Output: True! (Wait, why?)

a = 1000
b = 1000
print(a is b)  # Output: False! (WHAT?!)
```

### Why Did 100 Work but 1000 Failed?
This is a **CPython implementation detail**:
- Because small integers are used constantly in loops and indexing, CPython creates an internal array of singleton objects for all numbers from **`-5` to `256`** when Python starts up.
- Whenever you type `100`, Python doesn't make a new object; it hands you the pre-existing singleton.
- But for `1000`, CPython allocates a brand-new integer object each time!

> **Critical Rule**: NEVER use `is` to compare numbers or strings! Always use `==`.

---

## 4. When SHOULD You Use `is`?

The keyword `is` should almost exclusively be used when checking for **`None`**:

```python
# The correct, professional Python way:
if result is None:
    print("No result found")

# The correct way to check not None:
if result is not None:
    print("Found result:", result)
```

### Why `is None` instead of `== None`?
1. **Speed**: `is None` compares two memory pointers in a single CPU cycle. It doesn't need to call any methods.
2. **Safety**: Custom classes can override `__eq__` and lie! `is None` cannot be tricked because it checks physical identity.

---

## 5. Quick Self-Test
1. What does `a == b` check?
   - *Answer: Whether `a` and `b` have the same value.*
2. What does `a is b` check?
   - *Answer: Whether `a` and `b` point to the exact same object in memory (`id(a) == id(b)`).*
3. Why does PEP 8 forbid writing `if x == None:`?
   - *Answer: Because a custom class might override `__eq__`, causing unexpected bugs, and `x is None` is faster and unambiguous.*
