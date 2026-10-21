# Day 14: Comprehensions

## Explanation
Comprehensions provide a concise way to create lists, sets, and dictionaries in a single readable line.

## Key Concepts
- **List Comprehension**: `[expr for item in iter if condition]`
- **Set Comprehension**: `{expr for item in iter}`
- **Dict Comprehension**: `{key_expr: value_expr for item in iter}`

## Code Example
```python
# List
squares = [x**2 for x in range(5)]
# Dict
word = "hello"
char_count = {char: word.count(char) for char in set(word)}
print(char_count)
```

## Task
Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.