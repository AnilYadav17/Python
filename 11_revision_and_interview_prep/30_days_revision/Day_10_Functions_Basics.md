# Day 10: Functions Basics

## Explanation
Functions allow you to reuse code blocks. They help in keeping your code modular, readable, and DRY (Don't Repeat Yourself).

## Key Concepts
- **Defining**: Use the `def` keyword.
- **Parameters & Arguments**: Passing data to functions.
- **Return Statement**: Sending a result back from a function. If omitted, the function returns `None`.
- **Default Arguments**: Providing fallback values `def greet(name="Guest"):`.

## Code Example
```python
def add_numbers(a, b=10):
    return a + b

print(add_numbers(5))     # 15
print(add_numbers(5, 20)) # 25
```

## Task
Write a function called `calculate_area` that takes `length` and `width` as parameters (with a default width of 1) and returns the area of a rectangle.