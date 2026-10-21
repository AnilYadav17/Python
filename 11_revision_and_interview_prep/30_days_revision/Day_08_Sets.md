# Day 8: Sets

## Explanation
Sets are unordered collections of **unique** elements. They are highly optimized for checking if an item exists.

## Key Concepts
- **Creating**: `my_set = {1, 2, 3}` or `set([1, 2, 2, 3])` (removes duplicates).
- **Methods**: `.add()`, `.remove()`, `.discard()`.
- **Mathematical Operations**: Union (`|`), Intersection (`&`), Difference (`-`), Symmetric Difference (`^`).

## Code Example
```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a & set_b)  # Intersection: {3, 4}
print(set_a | set_b)  # Union: {1, 2, 3, 4, 5, 6}
```

## Task
Take a list with duplicate elements. Convert it to a set to remove duplicates, then add a new element to the set.