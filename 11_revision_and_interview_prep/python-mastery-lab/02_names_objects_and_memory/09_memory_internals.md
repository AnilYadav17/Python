# Lesson 09: Memory Internals (PyMalloc, Arenas, and Sizing)

## 1. Why Python Doesn't Call `malloc()` for Every Object

In operating systems like Linux or Windows, asking the OS kernel for memory using the standard C `malloc()` function is relatively slow. 

If Python asked the OS kernel for a few bytes every single time you created a number, a string, or a variable, Python would grind to a halt!

To make memory blazing fast, CPython has its own built-in memory manager called **PyMalloc**.

---

## 2. The 3 Layers of PyMalloc (Arenas, Pools, and Blocks)

For all small objects (objects of size **512 bytes or smaller**, which includes almost all integers, strings, and floats):

1. **Arenas (256 Kilobytes)**: Python asks the operating system for large chunks of 256 KB memory at a time.
2. **Pools (4 Kilobytes)**: Each Arena is carved into 4 KB Pools. Each pool handles objects of a specific size (e.g., one pool handles 16-byte objects, another handles 32-byte objects).
3. **Blocks (8 to 512 Bytes)**: Each Pool is divided into tiny fixed-size blocks where your actual Python objects sit.

```
+-------------------------------------------------------------+
|               Arena (256 KB from Linux Kernel)              |
|  +-----------------------+  +----------------------------+  |
|  |     Pool 1 (4 KB)     |  |       Pool 2 (4 KB)        |  |
|  | [16B][16B][16B][16B]  |  |   [32B][32B][32B][32B]     |  |
|  +-----------------------+  +----------------------------+  |
+-------------------------------------------------------------+
```

Because Python manages this memory itself, allocating a new small object takes only a few CPU instructions!

---

## 3. Why Doesn't Python Return RAM to the OS Immediately?

Have you ever noticed this in Python?
1. Your script creates a huge list of 10 million numbers. RAM usage spikes to 1 GB.
2. You run `del huge_list` and `gc.collect()`.
3. In your Linux System Monitor / Task Manager, the Python process **still shows 1 GB of RAM in use**!

### Why?
Because PyMalloc keeps that memory inside its Arenas so it can instantly reuse it for future Python objects without having to ask the operating system again. The memory is free for *Python*, even if the OS hasn't reclaimed it yet.

---

## 4. Measuring Object Size: `sys.getsizeof()`

You can check how many bytes an object takes up using `sys.getsizeof()`:

```python
import sys

print("Integer 0:       ", sys.getsizeof(0), "bytes")
print("Integer 100:     ", sys.getsizeof(100), "bytes")
print("Empty String:    ", sys.getsizeof(""), "bytes")
print("Empty List:      ", sys.getsizeof([]), "bytes")
print("Empty Dict:      ", sys.getsizeof({}), "bytes")
```

### Notice:
Why does the integer `0` take **28 bytes**, when in C an `int` is only 4 bytes?  
Because in Python, an integer is not a raw number! It is a complete `PyObject` with:
- An 8-byte reference count (`ob_refcnt`)
- An 8-byte type pointer (`ob_type`)
- An 8-byte size indicator for arbitrary precision (`ob_size`)
- Plus the actual number data!

---

## 5. The Container Trap with `sys.getsizeof()`

`sys.getsizeof()` only measures the **outer container**, NOT the objects inside it!

```python
import sys

items = [1, 2, 3]
print("Size of list:", sys.getsizeof(items))

# Now put 3 huge strings inside:
items_huge = ["A" * 10_000_000, "B" * 10_000_000, "C" * 10_000_000]
print("Size of huge list:", sys.getsizeof(items_huge))
```
Both lists will report almost the exact same size (~88 bytes)!  
Why? Because `items_huge` only holds 3 pointers (8 bytes each). To measure real memory consumption, use the standard library **`tracemalloc`** module.

---

## 6. Quick Self-Test
1. What internal CPython system handles allocations for objects $\le 512$ bytes?
   - *Answer: PyMalloc (using Arenas, Pools, and Blocks).*
2. Why is `sys.getsizeof(my_list)` misleading for nested data?
   - *Answer: Because it only measures the memory of the pointer array, not the objects pointed to.*
