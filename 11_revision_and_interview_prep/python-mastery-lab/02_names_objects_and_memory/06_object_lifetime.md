# Lesson 06: Object Lifetime and Reference Counting

## 1. When Is an Object Born, and When Does It Die?

In Python, you never have to write `free()` or `delete` like in C or C++. Memory management is automatic.

- **Birth**: An object is born the moment Python creates it in memory (e.g., `data = [1, 2, 3]`).
- **Life**: The object stays alive in RAM as long as **at least one name or container is pointing to it**.
- **Death**: The moment **zero names** point to it, Python frees its memory immediately.

---

## 2. Reference Counting: CPython's Memory Heartbeat

Inside CPython, every single `PyObject` has a hidden counter called **`ob_refcnt`** (Reference Count).

- Every time you bind a new name to the object: `refcount` goes **UP by 1**.
- Every time you put the object inside a list, tuple, or dictionary: `refcount` goes **UP by 1**.
- Every time a name goes out of scope (like when a function finishes): `refcount` goes **DOWN by 1**.
- Every time you rebind or remove a name: `refcount` goes **DOWN by 1**.

```
    refcount = 2                 refcount = 1                 refcount = 0
  Tag 'a' ---\                 Tag 'a' (deleted!)
              +-> [ Object ]                +-> [ Object ]     [ Object Destroyed! ]
  Tag 'b' ---/                 Tag 'b' -----/                  (Memory freed to OS)
```

The instant `refcount` hits **0**, CPython deallocates the object.

---

## 3. What Does `del` REALLY Do?

This is a favorite interview trick question:
> *"Does `del x` delete the object `x`?"*
> 
> **Answer: NO! `del x` does NOT delete objects.**

`del x` does only two things:
1. It deletes the name `'x'` from the namespace dictionary (it peels off the luggage tag).
2. It decreases the object's reference count by 1.

If another variable was pointing to that same object, the object **remains completely alive**!

```python
list1 = [10, 20, 30]
list2 = list1  # Refcount is now 2

del list1  # We delete the name list1! Refcount drops to 1.

# Is the list gone?
print(list2)  # Output: [10, 20, 30]  (Still alive!)
```

---

## 4. Inspecting Reference Counts with `sys.getrefcount()`

You can see an object's reference count using the standard library `sys` module:

```python
import sys

x = [1, 2, 3]
print("Ref count:", sys.getrefcount(x))
```
*Note: `sys.getrefcount(x)` will print `2` (not 1) because passing `x` into `getrefcount()` creates a temporary extra reference during the function call!*

---

## 5. Quick Self-Test
1. What triggers the immediate destruction of an object in CPython?
   - *Answer: When its reference count (`ob_refcnt`) reaches zero.*
2. If `a = [1]`, `b = a`, and you run `del a`, does the list get destroyed?
   - *Answer: No, because `b` is still holding a reference to it.*
