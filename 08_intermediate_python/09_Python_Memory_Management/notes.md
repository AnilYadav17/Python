# 09. Python Memory Management: Complete Reference

---

## 1. Reference Counting Mechanics

### What it is
- The primary memory management mechanism in CPython.
- Every Python object tracks how many active references currently point to it via an internal counter field (`ob_refcnt`).
- Whenever a reference is created, `ob_refcnt` is incremented (+1):
  - Assignment: `b = a`
  - Argument passing: `func(a)`
  - Container insertion: `my_list.append(a)`
- Whenever a reference is destroyed, `ob_refcnt` is decremented (-1):
  - Variable goes out of scope when a function returns.
  - Explicit deletion: `del a`
  - Reassignment: `a = None`
  - Container element removal: `my_list.clear()`
- **Immediate Deallocation**: As soon as an object's reference count drops to zero (`ob_refcnt == 0`), its memory is immediately deallocated and reclaimed.

### Why it matters
- Provides deterministic, instantaneous memory reclamation for the vast majority of objects without requiring a full stop-the-world garbage collection pause.

### How it works (internals, if relevant)
- Implemented in C via macros `Py_INCREF(op)` and `Py_DECREF(op)`.
- When `Py_DECREF` reduces the count to zero, it calls the object's type deallocator function `tp_dealloc`, which frees child references and releases the memory block back to CPython's memory allocator.

### Common mistakes / gotchas
- Assuming `del variable` deletes the object from memory: `del variable` only destroys the *name binding* and decrements the reference count by 1. The object is only freed if no other references point to it.
- Inability to reclaim circular references on its own (requires cyclic GC).

### Connects to
- The Cyclic Garbage Collector (subtopic 2 below).

---

## 2. The Cyclic Garbage Collector (Generational GC)

### What it is
- A complementary garbage collector that detects and reclaims isolated reference cycles that reference counting alone cannot reclaim.
- **Reference Cycle**: A situation where two or more objects reference each other (e.g. object A references B, and B references A). Even if all external references to A and B are deleted, their reference counts never drop to 0 (`ob_refcnt >= 1`), creating an orphaned memory leak.

### Why it matters
- Prevents memory leaks caused by circular object graphs, doubly linked lists, parent-child tree nodes, and closures referencing outer frames.

### How it works (internals, if relevant)
- CPython's cyclic GC is **generational**, based on the weak generational hypothesis (most objects die young):
  - **Generation 0**: Newly allocated container objects. Collected most frequently.
  - **Generation 1**: Objects surviving Generation 0 collections.
  - **Generation 2**: Long-lived objects surviving Generation 1 collections. Collected least frequently.
- **Cycle Detection Algorithm**:
  1. The GC tracks container objects using a doubly linked list of `PyGC_Head` headers.
  2. For each tracked container, the GC copies its reference count into a trial field `gc_refs`.
  3. The GC visits all reachable sub-objects via their `tp_traverse` slot and decrements the target object's `gc_refs`.
  4. Any objects whose `gc_refs` drops to 0 are referenced *only* from within the isolated cycle (unreachable from the outside).
  5. The GC marks these objects as unreachable, breaks the cycle, and frees them.

### Common mistakes / gotchas
- Believing non-container types (like `int`, `str`, `float`) are tracked by the cyclic GC: they are never tracked because they cannot contain references to other objects.
- Disabling the cyclic GC without understanding that reference cycles will continuously leak memory.

### Connects to
- The `gc` Module (subtopic 3 below).

---

## 3. The `gc` Module

### What it is
- Standard library interface for inspecting and configuring CPython's cyclic garbage collector:
  - `gc.collect(generation=2)`: Triggers a manual full garbage collection cycle.
  - `gc.disable()` / `gc.enable()`: Turns off or on automatic cyclic GC.
  - `gc.isenabled()`: Returns boolean status of automatic collection.
  - `gc.get_threshold()` / `gc.set_threshold()`: Gets or sets the allocation threshold triggers for generations (0, 1, 2).
  - `gc.get_stats()`: Returns diagnostic statistics for each generation.
  - `gc.garbage`: List of objects that the collector found unreachable but could not free.

### Why it matters
- High-performance, latency-sensitive services (e.g. game loops, high-frequency trading, batch ETL) often disable automatic GC during critical sections to prevent latency spikes and manually invoke `gc.collect()` during idle periods.

### How it works (internals, if relevant)
- Default thresholds: `(700, 10, 10)`:
  - Gen 0 runs when the net number of allocations minus deallocations exceeds 700.
  - Gen 1 runs when Gen 0 has been collected 10 times.
  - Gen 2 runs when Gen 1 has been collected 10 times.

### Common mistakes / gotchas
- In Python 3.3 and earlier, objects with `__del__` methods in a cycle were permanently uncollectable and stored in `gc.garbage`. Since Python 3.4 (PEP 442), `__del__` methods are safely executed by the GC.
- Manually invoking `gc.collect()` too frequently in tight loops, which destroys performance.

### Connects to
- Reference Inspection (subtopic 4 below).

---

## 4. Reference Inspection (`sys.getrefcount` & `weakref`)

### What it is
- **`sys.getrefcount(obj)`**: Returns the current reference count of an object.
- **`weakref` Module**: Allows creating references to objects without increasing their reference count (`weakref.ref()`, `weakref.WeakValueDictionary`).

### Why it matters
- `sys.getrefcount` enables debugging memory leaks and verifying whether objects are being retained unintentionally.
- `weakref` enables building memory-safe in-memory caches, listener registries, and circular tree structures that automatically clean up when no strong references remain.

### How it works (internals, if relevant)
- **The Extra Reference Trap in `sys.getrefcount`**:
  `sys.getrefcount(obj)` always returns a value that is **1 higher** than you expect!
  Why? Because passing `obj` into `sys.getrefcount()` creates a new local reference on the function's stack frame for the duration of the call.
- Weak references point to an object's weak reference list (`tp_weaklist`). When the object's strong `ob_refcnt` hits 0, CPython notifies all registered weak references to invalidate themselves and set their target to `None`.

### Common mistakes / gotchas
- Creating a cache using a standard `dict`, which retains strong references permanently, creating an accidental memory leak. Use `weakref.WeakValueDictionary` instead!
- Attempting to create a weak reference to built-in types like `list` or `dict` (raises `TypeError`; standard built-ins do not support weakrefs without subclassing).

### Connects to
- Object Identity vs Equality (subtopic 5 below).

---

## 5. Object Identity vs Equality & Interning

### What it is
- **`id(obj)`**: Returns the integer identity of the object (in CPython, this is the exact virtual memory address of the `PyObject` struct).
- **`a is b`**: Tests whether `id(a) == id(b)` (pointer identity).
- **`a == b`**: Tests whether values are equal by calling `a.__eq__(b)` (value equality).
- **Interning**: Optimization technique where only one unique copy of an immutable object is kept in memory and shared across references.

### Why it matters
- Understanding identity prevents bugs when checking singletons like `None`.
- Interning saves massive amounts of memory and speeds up dictionary lookups by allowing string comparisons via fast pointer equality ($O(1)$) instead of character-by-character scans ($O(n)$).

### How it works (internals, if relevant)
- **Small Integer Interning**: CPython automatically interns all integers in the range `[-5, 256]` at startup into a static array.
- **String Interning**: CPython automatically interns string literals that look like valid Python identifiers (letters, digits, underscores).
- **Manual Interning**: The `sys.intern(string)` function forces CPython to insert any string into the global interned string dictionary.

### Common mistakes / gotchas
- Using `is` for value comparisons (e.g. `x is 1000` or `s1 is s2`): this may evaluate to `True` in test scripts due to compiler constant folding, but fail unpredictably at runtime! Always use `==` for values, and reserve `is` for singletons (`None`, `True`, `False`, `sentinel_object`).

### Connects to
- Shallow vs Deep Copy (subtopic 6 below).

---

## 6. Shallow Copy vs Deep Copy

### What it is
- The standard library `copy` module:
  - **Assignment (`b = a`)**: Creates a new reference pointing to the exact same object address.
  - **Shallow Copy (`copy.copy(a)` or `a.copy()` or `a[:]`)**: Constructs a new compound object and inserts *references* to the objects found in the original.
  - **Deep Copy (`copy.deepcopy(a)`)**: Constructs a new compound object and recursively creates copies of all child objects found in the original.

### Why it matters
- Mutating a nested collection inside a shallow copy inadvertently mutates the original collection.
- Deep copying is essential when cloning complex hierarchical state (trees, nested configurations, game state snapshots).

### How it works (internals, if relevant)
- `copy.deepcopy()` maintains an internal memo dictionary (`memo={}`) mapping original object IDs to their newly cloned counterparts.
- This memo dictionary prevents infinite loops when deep-copying objects that contain circular references!
- Objects can customize copying behavior by implementing `__copy__()` and `__deepcopy__(memo)`.

### Common mistakes / gotchas
- Assuming `list.copy()` or `dict.copy()` creates a deep copy: they are strictly shallow copies!
- Deep-copying objects with references to external OS resources (file streams, network sockets, database connections) will raise `TypeError` or produce corrupted handles.

### Connects to
- Python Allocator Architecture (subtopic 7 below).

---

## 7. Python Allocator Architecture (PyMalloc)

### What it is
- CPython's tiered memory allocation subsystem managing memory layout between the OS and Python objects.
- Tiers:
  1. **OS Layer**: Standard C library allocator (`malloc`, `free`).
  2. **PyMem Layer**: General-purpose memory allocator for raw buffers.
  3. **PyObject / PyMalloc Layer**: Specialized small object allocator for objects $\le 512$ bytes.

### Why it matters
- Small objects are created and destroyed by the millions in Python. Calling standard OS `malloc()` for every small object causes severe heap fragmentation and system call overhead.
- PyMalloc groups small objects into pre-allocated memory pools, dramatically increasing cache locality and speed.

### How it works (internals, if relevant)
- **Arenas**: 256 KB memory chunks allocated from the OS via `malloc`.
- **Pools**: 4 KB blocks within an arena, dedicated to objects of a specific size class (in multiples of 8 bytes: 8, 16, 24, ..., 512 bytes).
- **Blocks**: The actual slots within a pool that store objects.
- When an object $\le 512$ bytes is freed, PyMalloc returns the block to its pool free list rather than returning memory to the OS immediately, which is why Python process memory may not visibly decrease in `top` after freeing objects.

### Common mistakes / gotchas
- Expecting OS-level memory (`top` or `ps`) to drop immediately after running `del big_list` and `gc.collect()`. Memory is recycled internally by PyMalloc for future Python allocations.

### Connects to
- Context Managers (Topic 10).
