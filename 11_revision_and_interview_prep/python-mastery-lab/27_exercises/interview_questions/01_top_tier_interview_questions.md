# Top-Tier Python Technical Interview Questions

These 10 in-depth interview questions test real architectural understanding, memory mechanics, and runtime knowledge.

---

### Q1: What actually happens in memory when you execute `a = [1, 2, 3]` followed by `b = a`?
**Answer**:  
Python allocates a list `PyListObject` on the heap containing pointers to small integer singletons `1, 2, 3`. The name `a` is bound to the memory address of that list object. Executing `b = a` does NOT copy the list; it simply binds the name `b` to the identical memory address (incrementing the list object's `ob_refcnt` reference count by 1). Modifying `b.append(4)` mutates the shared heap object.

---

### Q2: What is the Python Global Interpreter Lock (GIL), why was it created, and how is it evolving?
**Answer**:  
The GIL is a mutual exclusion lock in CPython that ensures only one native OS thread executes Python bytecode at any given moment. It was created in the 1990s to make memory management (specifically non-thread-safe reference counting) simple, safe, and fast for single-threaded code. In Python 3.13+ (PEP 703), experimental "free-threaded Python" introduces mimalloc-based thread-safe reference counting, allowing true multi-core parallel thread execution.

---

### Q3: What is the difference between `__new__` and `__init__` in Python?
**Answer**:  
`__new__(cls, *args, **kwargs)` is the actual **constructor**; it allocates the memory for the new instance and returns it. `__init__(self, *args, **kwargs)` is the **initializer**; it receives the already-created instance as `self` and sets up initial attributes. You override `__new__` when subclassing immutable types (like `int`, `str`, `tuple`) or implementing the Singleton pattern.

---

### Q4: Explain the C3 Linearization Algorithm (MRO).
**Answer**:  
Method Resolution Order (MRO) defines the exact order Python traverses inheritance hierarchies to look up methods. Python uses C3 Linearization to guarantee:
1. Children precede their parents.
2. Order of classes listed in inheritance is preserved.
3. Monotonicity: if class A precedes B in one class's MRO, it will precede B in all subclasses.  
Accessible on any class via `ClassName.mro()` or `ClassName.__mro__`.

---

### Q5: How does Python's Garbage Collector detect and clean cyclic references?
**Answer**:  
CPython's primary memory management is **reference counting** (immediate deallocation when `ob_refcnt == 0`). However, reference counting cannot free cyclic references (e.g. object A points to B, and B points to A). To fix this, Python runs a **generational cyclic garbage collector** (Generations 0, 1, 2). It tracks all container objects in doubly-linked lists, temporarily decrements reference counts to isolate self-referencing cycles, and frees unreferenced islands of objects.

---

### Q6: What is a Python descriptor, and how does `@property` use it?
**Answer**:  
A descriptor is an object that defines at least one of `__get__`, `__set__`, or `__delete__`. When accessed as a class attribute, Python delegates attribute access to the descriptor's methods instead of a standard dictionary lookup. `@property` is simply a built-in descriptor that delegates `obj.attr` to a getter function.

---

### Q7: Why is `is` different from `==`? Give an example where `a == b` is True, but `a is b` is False.
**Answer**:  
- `==` tests **equality of value** (calls `__eq__`).
- `is` tests **object identity** (`id(a) == id(b)`, the physical memory address).
```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True (equal contents)
print(list1 is list2)  # False (different objects in memory)
```

---

### Q8: What are generator functions, and what are their architectural advantages?
**Answer**:  
Generators are functions that use `yield` instead of `return`. Calling a generator returns an iterator object without executing the function body. Execution proceeds only when `next()` is called, pausing at `yield` and preserving its local stack frame state (`f_locals`).  
*Advantage*: Extremely low memory footprint ($O(1)$ constant memory), enabling lazy stream processing of multi-gigabyte files.

---

### Q9: What happens when an exception is raised inside a generator?
**Answer**:  
The generator's execution pauses, and the exception bubbles out through the caller's call stack unless caught inside a `try...except` within the generator itself. If the generator runs out of items or returns, it raises `StopIteration`.

---

### Q10: How does `collections.defaultdict` differ from `dict.setdefault()`?
**Answer**:  
`defaultdict(default_factory)` calls the factory function automatically whenever a missing key is accessed via `d[key]`. In contrast, `dict.setdefault(key, default_val)` evaluates `default_val` on every invocation (even if the key exists), which can be slow if creating the default value is computationally expensive or allocates new objects.
