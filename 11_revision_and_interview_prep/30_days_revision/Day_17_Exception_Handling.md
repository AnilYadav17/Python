# Day 17: Exception Handling

## Explanation
Exceptions are errors that occur during execution. Python lets you catch and handle them gracefully instead of crashing.

## Key Concepts
- **`try`**: Block of code to test for errors.
- **`except`**: Block to handle the error.
- **`else`**: Executes if NO exceptions were raised.
- **`finally`**: Executes regardless of whether an exception occurred (useful for cleanup).
- **`raise`**: Manually trigger an exception.

## Code Example
```python
try:
    res = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught error: {e}")
finally:
    print("Execution finished.")
```

## Task
Write a function that accepts two inputs from a user and divides them. Handle `ValueError` (non-numbers) and `ZeroDivisionError` gracefully.