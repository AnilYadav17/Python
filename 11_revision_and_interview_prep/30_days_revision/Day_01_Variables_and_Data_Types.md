# Day 1: Variables and Data Types

## Explanation
Variables store data in memory. Python is dynamically typed, meaning you don't declare the type of variable explicitly. The main primitive types are `int`, `float`, `str`, and `bool`.

## Key Concepts
- **Dynamic Typing**: `x = 5` then `x = 'hello'` is valid.
- **Type Casting**: `int('5')`, `str(10)`.
- **`type()` function**: Used to check the data type of a variable.

## Code Example
```python
x = 10        # int
y = 3.14      # float
name = "Dev"  # str
is_valid = True # bool
print(f"{name} is {x} years old. Type of x: {type(x)}")
```

## Task
Declare variables for your name, age, and a boolean indicating if you like Python. Print a sentence combining them. Then, change your age variable to a string and check its type.