# 📦 03_Python_Collections: Lists, Dictionaries, Sets & Matrices

## Overview
Collections are composite data structures designed to store, manage, and manipulate groups of related items. Python provides powerful built-in collections with distinct mutability, ordering, and indexing characteristics:

* **Lists:** Ordered, mutable sequences allowing duplicate elements.
* **Dictionaries (Hash Maps):** Key-value mappings offering average $O(1)$ lookup, insertion, and deletion.
* **Sets:** Unordered collections of unique, hashable elements supporting mathematical set operations (union, intersection, difference).
* **2D Lists / Matrices:** Nested lists used to represent multidimensional grids, image buffers, and coordinate matrices.

This directory focuses on real-world algorithms, interview-frequently-asked patterns (matrix math, frequency hashing, anagram detection, pair sums), and efficient lookups.

---

## Learning Objectives
By studying this module, you will understand:
1. When to choose a List vs. Set vs. Dictionary based on performance complexity ($O(1)$ vs. $O(n)$).
2. Frequency counting and hash map grouping (`grp_words_by_length`, `occurance_vowels`, `reoccurance_word`).
3. Set operations for uniqueness checks, first non-repeating character detection, and duplicates elimination.
4. Matrix algorithms: 2D array representation, nested indexing, row/column traversals, matrix addition, and matrix multiplication ($O(N^3)$).
5. Two-pointer and pair-sum searching strategies on lists.

---

## Prerequisites
* **[02_python_fundamentals](../02_python_fundamentals/)** (Variables, loops, conditionals, and range).

---

## Learning Path

```text
1. Lists & Sequences
   └── Indexing, Slicing, Appending, Removing, Two-Pointer Pair Sums
       ▼
2. 2D Lists & Matrices
   └── Traversal, Row/Column Access, Matrix Addition, Matrix Multiplication
       ▼
3. Dictionaries (Hash Maps)
   └── Key-Value pairs, .get(), Dict Inversion, Frequency Counters, Grouping
       ▼
4. Sets & Hash Tables
   └── Uniqueness, Membership Testing, Deduplication, Character Frequency
```

---

## Repository Contents & Examples

| Folder | Topic | Key Files & Concepts Demonstrated |
|:---|:---|:---|
| 📁 **[List](./List)** | Lists & Matrices | `01_matrix.py` (2D basics), `02_Matrix_addition.py`, `03_Matrix_multiplication.py`, `matrix_accessing.py`, `matrix_sum.py`, `duplicates_in_list.py`, `pair_array_sum.py`, `common_in_lists.py` |
| 📁 **[Dictionary](./Dictionary)** | Hash Mappings & Grouping | `merge_dict.py`, `grp_words_by_length.py`, `count_vowels.py`, `occurance_vowels.py`, `reoccurance_word.py`, `logins_time.py`, `demos/` |
| 📁 **[Set](./Set)** | Uniqueness & Hashing | `first_np_char.py`, `is_unique_chars.py`, `unique_words.py` |

---

## How to Run the Programs

```bash
# Matrix Multiplication:
python3 03_python_collections/List/03_Matrix_multiplication.py

# Grouping words by length using Dictionaries:
python3 03_python_collections/Dictionary/grp_words_by_length.py

# Unique character verification using Sets:
python3 03_python_collections/Set/is_unique_chars.py
```

---

## Practice & Assignments

Solve the comprehensive collection assignment suites in **`09_practice_and_assignments/01_Basics/`**:
* **[07_Lists_and_Arrays](../09_practice_and_assignments/01_Basics/07_Lists_and_Arrays/)** — Traversals, mountain arrays, comprehensions, 2D matrices.
* **[08_Tuples_and_NamedTuples](../09_practice_and_assignments/01_Basics/08_Tuples_and_NamedTuples/)** — Immutability, pairs with difference K, namedtuple analysis.
* **[09_Sets](../09_practice_and_assignments/01_Basics/09_Sets/)** — Student club memberships, set difference and intersection.
* **[10_Dictionaries](../09_practice_and_assignments/01_Basics/10_Dictionaries/)** — Shopping cart management, hospital patient records.

---

## Common Beginner Mistakes

1. **Using a Mutable Default Argument:**
   * Writing `def append_to(element, target=[]):` creates a persistent list across calls! Always use `target=None` and initialize inside the function.
2. **Accessing a Non-Existent Dictionary Key:**
   * `my_dict["missing_key"]` raises a `KeyError`. Use `my_dict.get("missing_key", default_value)` to safely retrieve optional keys.
3. **Modifying a Collection While Iterating Over It:**
   * Calling `.remove()` on a list while looping over it skips elements due to index shifting. Iterate over a copy (`for item in my_list[:]:`) or use a list comprehension.
4. **Expecting Sets to Preserve Order:**
   * Standard sets do not preserve insertion order and cannot be accessed via indexing (`my_set[0]` raises `TypeError`).

---

## Next Step

👉 Advance to **[04_functions](../04_functions/)** to organize code into reusable blocks, master scopes, lambda expressions, recursion, and decorators!
