# Day 4: Control Flow (Conditionals)

## Explanation
Conditionals allow your code to make decisions based on certain conditions.

## Key Concepts
- `if`, `elif`, `else` blocks.
- **Ternary Operator**: `x if condition else y`.
- **Truthy & Falsy**: Empty sequences (`""`, `[]`), `0`, and `None` evaluate to `False`.

## Code Example
```python
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'
print(f"Grade: {grade}")
```

## Task
Write a program that determines if a given year is a leap year. (Divisible by 4, but not 100 unless also divisible by 400).