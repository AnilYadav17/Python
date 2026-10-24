# Lesson 03: Sorting, Key Functions, and Timsort

## 1. Sorting in Python: `list.sort()` vs. `sorted()`

Python gives you two ways to sort data:

1. **`list.sort()`**: Sorts the list **in-place** at the same memory address. Returns `None`.
   ```python
   numbers = [5, 2, 9, 1]
   numbers.sort()
   print(numbers)  # [1, 2, 5, 9]
   ```

2. **`sorted(iterable)`**: Leaves the original data untouched and returns a **brand-new sorted list**. Works on any iterable (tuples, dicts, sets, strings):
   ```python
   original = (5, 2, 9, 1)
   new_list = sorted(original)
   print("Original tuple:", original)  # (5, 2, 9, 1)
   print("New sorted list:", new_list)  # [1, 2, 5, 9]
   ```

---

## 2. Custom Sorting with `key=` Functions

In many languages, you have to write complex comparator functions comparing two elements: `compare(a, b)`.

Python uses a much faster, cleaner concept: **Key Functions (`key=`)**:
You supply a function that transforms each item into a sorting key. Python extracts the key once and sorts by it!

```python
# 1. Sort words by their length:
words = ["elephant", "cat", "dog", "hippopotamus"]
words.sort(key=len)
print("Sorted by length:", words)
# ['cat', 'dog', 'elephant', 'hippopotamus']

# 2. Sort users by age:
users = [
    {"name": "Anil", "age": 28},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 35}
]

# Sort by age ascending:
users.sort(key=lambda u: u["age"])
for u in users:
    print(f"{u['name']}: {u['age']}")
```

---

## 3. Fascinating Fact: The Legend of Timsort 💡
> **Did you know?**
> The sorting algorithm inside Python is called **Timsort**, created in 2002 by Python core developer **Tim Peters**.  
> Before Timsort, standard sorting algorithms (QuickSort, MergeSort) performed poorly on real-world data because real data is rarely completely random—it usually contains stretches of already-sorted numbers (called "runs").  
> Timsort was so shockingly fast and intelligent (adaptive hybrid of MergeSort and InsertionSort) that **Sun Microsystems replaced the default sorting algorithm in Java 7 with Timsort**! Google also made Timsort the official sorting engine inside the **Android Operating System** and the **V8 JavaScript engine**!

---

## 4. Timsort Is "Stable": What Does That Mean?

A sorting algorithm is **Stable** if items with equal keys preserve their original relative order.

For example, imagine you have employees already sorted alphabetically by Name:
```python
employees = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Charlie", "Engineering")
]

# Now sort by Department:
employees.sort(key=lambda e: e[1])
print(employees)
# Output:
# [('Alice', 'Engineering'), ('Charlie', 'Engineering'), ('Bob', 'Sales')]
```
Notice that inside `Engineering`, `Alice` is **still before `Charlie`**! Because Timsort is stable, you can perform multi-level sorting by sorting least-significant keys first!

---

## 5. Quick Self-Test
1. What does `list.sort()` return?
   - *Answer: `None` (it sorts the list in-place).*
2. What algorithm powers Python's `.sort()` and `sorted()`?
   - *Answer: Timsort (invented by Tim Peters).*
