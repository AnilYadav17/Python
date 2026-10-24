# Lesson 07: Garbage Collection and Reference Cycles

## 1. The Fatal Flaw of Reference Counting: Circular References

Reference counting is lightning fast, but it has one major weakness: **Circular References (Cycles)**.

Imagine two objects that point to each other:
```python
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbor = None

node_a = Node("A")
node_b = Node("B")

# Make them point to each other in a circle:
node_a.neighbor = node_b
node_b.neighbor = node_a
```

Now, what happens if we delete both variable names?
```python
del node_a
del node_b
```
- Can our program reach `Node A` or `Node B` anymore? **No!** We lost all variable names pointing to them.
- But what are their reference counts?  
  `Node A` still has `node_b.neighbor` pointing to it (`refcount = 1`).  
  `Node B` still has `node_a.neighbor` pointing to it (`refcount = 1`).
- **The Problem**: Because their reference counts never drop to 0, reference counting alone would leave them stranded in RAM forever—a **memory leak**!

```
      +------------+   neighbor   +------------+
      |   Node A   | -----------> |   Node B   |
      | (refcnt=1) | <----------- | (refcnt=1) |
      +------------+   neighbor   +------------+
        ^                           ^
        |                           |
   (del node_a)                (del node_b)
```

---

## 2. Python's Solution: The Cyclic Garbage Collector (`gc`)

To fix circular references, CPython has a second, background memory cleaner called the **Cyclic Garbage Collector**.

The cyclic GC periodically scans container objects in memory (lists, dicts, custom class instances). It performs graph-cycle detection:
1. It looks for groups of objects that point to each other.
2. It asks: *"Is any object in this group reachable from outside variables (like global names or the current function)?"*
3. If the entire cluster is an isolated island with no outside connections, the GC breaks the cycle and frees all of them!

---

## 3. The 3 Generations of Garbage Collection

Scanning every single object in memory takes CPU time. To keep Python fast, the GC uses a smart heuristic called **Generational Garbage Collection**:

> **The Theory**: Most objects in a program are born and die very quickly (temporary loop variables, strings). If an object survives multiple garbage collections, it is probably a long-lived configuration or cache that will stay alive for a long time.

CPython divides objects into **3 Generations**:
- **Generation 0 (Youngest)**: All newly created container objects start here. This generation is scanned very frequently.
- **Generation 1 (Middle-aged)**: Objects that survive a Gen 0 collection get promoted to Gen 1. Scanned less often.
- **Generation 2 (Oldest)**: Long-lived objects (like loaded modules or global configs) live here. Scanned very rarely.

---

## 4. Controlling the GC Yourself (`import gc`)

You can inspect and control the garbage collector directly using Python’s built-in `gc` module:

```python
import gc

# 1. Check how many objects are tracked in each generation:
print("GC Counts:", gc.get_count())

# 2. Force an immediate garbage collection sweep:
unreachable_count = gc.collect()
print(f"Freed {unreachable_count} circular unreachable objects!")

# 3. Check if GC is enabled:
print("Is GC active?", gc.isenabled())
```

---

## 5. Quick Self-Test
1. If CPython already has reference counting, why does it need a garbage collector?
   - *Answer: To find and clean up circular references (reference cycles) that reference counting alone cannot reclaim.*
2. How many generations does CPython's generational garbage collector use?
   - *Answer: Three generations: Gen 0, Gen 1, and Gen 2.*
