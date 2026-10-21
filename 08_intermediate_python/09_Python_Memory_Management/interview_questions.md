# 09. Python Memory Management — Interview & Viva Questions

---

### Q1: How does Python manage memory at runtime?
**Model Answer:**
- Python employs a two-layer hybrid memory management strategy:
  1. **Reference Counting (Primary)**: Every object has an `ob_refcnt` header tracking active references. When an object's reference count drops to zero, it is deallocated immediately.
  2. **Generational Cyclic Garbage Collector (Secondary)**: Handles cyclic references that reference counting alone cannot reclaim (e.g. `a.partner = b; b.partner = a`). It divides container objects into three generations (0, 1, 2) and periodically runs trial decrement scans to isolate and collect unreachable cyclic reference islands.
- Low-level allocations are managed by **PyMalloc**, a specialized memory allocator that groups small objects ($\le 512$ bytes) into pools and arenas to prevent OS heap fragmentation.

---

### Q2: Why does `sys.getrefcount(obj)` return a count that is 1 higher than expected?
**Model Answer:**
- When you call `sys.getrefcount(obj)`, the argument `obj` is passed into the function by object reference.
- Passing the object into the function creates an active local reference parameter on the function's stack frame.
- Consequently, `sys.getrefcount()` counts its own temporary argument reference along with all pre-existing references, returning $N + 1$. Once the function returns, this temporary reference is immediately destroyed.

---

### Q3: What is a reference cycle, and why can't reference counting alone collect it?
**Model Answer:**
- A reference cycle occurs when two or more objects reference each other, either directly (`a.b = b; b.a = a`) or indirectly through a chain of references.
- Even after deleting the external variable names (`del a; del b`), each object still retains an incoming reference from the other object in the cycle (`ob_refcnt >= 1`).
- Because neither reference count ever reaches zero, standard reference counting can never trigger deallocation, causing an orphaned memory leak.
- CPython's cyclic GC is required to detect that these objects are reachable only from within the isolated cycle and break them.

---

### Q4: Explain the difference between `copy.copy()` and `copy.deepcopy()`.
**Model Answer:**
- **`copy.copy()` (Shallow Copy)**: Constructs a new outer compound object (e.g. a new list or dict), but populates it with **references** to the objects found in the original. If the original object contains nested mutable structures (e.g. lists within a list), modifying the inner list through the copy also modifies the inner list in the original.
- **`copy.deepcopy()` (Deep Copy)**: Constructs a new outer compound object and then **recursively clones copies** of all nested child objects found within it. It maintains an internal `memo` dictionary to prevent infinite recursion on circular object graphs. Modifications to any level of the clone have zero effect on the original.

---

### Q5: What is object interning in Python, and why is it used?
**Model Answer:**
- Interning is an optimization where CPython ensures that only one unique instance of an immutable object is kept in memory and shared globally across all variables that reference that value.
- **Small Integers**: CPython pre-allocates singletons for integers in the range `[-5, 256]`.
- **Strings**: CPython automatically interns string literals resembling valid Python identifiers. Developers can manually intern arbitrary strings using `sys.intern(string)`.
- **Benefits**:
  1. Memory savings: eliminates duplicate copies of identical strings across large datasets.
  2. Performance: interned strings can be compared in constant $O(1)$ time using pointer identity (`a is b`) instead of $O(n)$ character comparisons (`a == b`).

---

### Q6: What is `weakref.WeakValueDictionary`, and what problem does it solve?
**Model Answer:**
- A standard Python `dict` creates **strong references** to its values. If an object is placed in a dictionary cache, its reference count will never drop to zero as long as the dictionary exists, causing unbounded memory growth (a cache memory leak).
- `weakref.WeakValueDictionary` stores **weak references** to its values. A weak reference allows accessing the object without incrementing its `ob_refcnt`.
- As soon as all external strong references to a cached object are deleted, Python deallocates the object, and the entry is **automatically removed from the dictionary**, creating a zero-maintenance, self-evicting memory-safe cache.

---

### Q7: Why does a Python process's RAM usage (in `top` or Task Manager) often not decrease after deleting large objects?
**Model Answer:**
- Small objects ($\le 512$ bytes) are managed by CPython's **PyMalloc** allocator, which allocates large contiguous 256 KB memory chunks (arenas) from the operating system.
- Arenas are partitioned into 4 KB pools, which are subdivided into fixed-size blocks.
- When an object is freed, PyMalloc returns the block to the pool's internal free list for fast reuse by future Python allocations rather than releasing it back to the OS via `free()`.
- An arena can only be released back to the operating system if **every single block across all pools in that 256 KB arena is simultaneously empty**, which rarely happens in long-running processes due to heap fragmentation.
