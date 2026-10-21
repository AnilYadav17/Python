# Day 13: Lambda, Map, Filter, Reduce

## Explanation
Functional programming tools in Python allow for concise and expressive data transformations.

## Key Concepts
- **Lambda**: Anonymous, single-expression functions. `lambda x: x + 1`.
- **`map(func, iter)`**: Applies a function to all items in an iterable.
- **`filter(func, iter)`**: Returns items where the function evaluates to True.
- **`reduce(func, iter)`**: Applies a rolling computation (requires `from functools import reduce`).

## Code Example
```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(squares, evens)
```

## Task
Given a list of strings, use `filter` and a `lambda` to extract only the strings that start with the letter 'A'.