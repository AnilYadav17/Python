# Day 5: Loops (For and While)

## Explanation
Loops let you execute a block of code multiple times.

## Key Concepts
- **`for` loop**: Iterates over a sequence (list, string, range).
- **`while` loop**: Repeats as long as a condition is True.
- **`range(start, stop, step)`**: Generates a sequence of numbers.
- **Loop Control**: `break` (exit loop), `continue` (skip to next iteration), `pass` (do nothing placeholder).
- **`else` in loops**: Executes if the loop finishes without hitting a `break`.

## Code Example
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

## Task
Use a `while` loop to print numbers from 10 down to 1. Use a `for` loop to print all even numbers between 1 and 20.