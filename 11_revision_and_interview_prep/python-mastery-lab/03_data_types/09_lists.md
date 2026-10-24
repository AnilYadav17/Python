# Lesson 09: Lists (`list`) and Dynamic Arrays

## 1. What Is a List in Simple Words?
A **list** is an ordered, mutable collection of items. 

In Python, a list can hold items of any type—even mixed types:
```python
mixed = [10, "Python", True, 3.14, [1, 2]]
```

---

## 2. CPython Internals: Lists Are Dynamic Arrays, NOT Linked Lists!

Many beginners think a Python list is a linked list where nodes point to the next node.  
**It is not!**

Inside CPython, a list is a **Dynamic Array of Pointers**:
- It is a contiguous block of memory holding 8-byte pointers (`PyObject*`).
- Because it is an array, looking up any element by index (`items[5]`) takes **$O(1)$ constant time** (instant direct memory offset calculation).

```
   PyListObject
   +--------------------+
   | ob_size = 3        |
   | allocated = 4      |
   | ob_item -----------> [ Ptr to 10 | Ptr to 20 | Ptr to 30 | (empty slot) ]
   +--------------------+
```

---

## 3. The Over-Allocation Strategy: Why `.append()` Is Fast

When you call `items.append(x)`:
- Does Python allocate memory for 1 new item? **No!**
- Python allocates room for **multiple extra slots ahead of time** (e.g., 4, 8, 16, 25 slots).
- This means most `.append()` calls simply write a pointer into an already-allocated empty slot!
- This gives `append()` an **amortized $O(1)$ time complexity**.

---

## 4. Key List Methods and Their Performance

| Method | What It Does | Time Complexity | Note |
| :--- | :--- | :--- | :--- |
| `list.append(x)` | Adds item to the very end | **$O(1)$** | Blazing fast! |
| `list.pop()` | Removes and returns the last item | **$O(1)$** | Fast stack operation |
| `list.insert(0, x)` | Adds item to the front | **$O(N)$** | **SLOW!** Must shift all $N$ items to the right |
| `list.pop(0)` | Removes the first item | **$O(N)$** | **SLOW!** Must shift all $N$ items to the left |
| `list.extend(iter)` | Adds all items from another collection | $O(K)$ | Much faster than appending in a loop |
| `list.sort()` | Sorts items in-place using Timsort | $O(N \log N)$ | Highly optimized hybrid sort |

> **Performance Tip**: If you need to frequently add and remove items from the *front* of a list, do not use `list`. Use `collections.deque` (Double-Ended Queue), which does front operations in $O(1)$!

---

## 5. Quick Self-Test
1. Why is `my_list.insert(0, "first")` slow on a list with 1 million items?
   - *Answer: Because Python must shift all 1 million existing pointers one slot to the right in memory ($O(N)$ time).*
2. What is the time complexity of looking up `items[999]`?
   - *Answer: $O(1)$ constant time, because lists are contiguous pointer arrays.*
