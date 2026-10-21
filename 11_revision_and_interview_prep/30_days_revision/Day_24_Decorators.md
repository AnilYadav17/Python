# Day 24: Decorators

## Explanation
Decorators allow you to modify or enhance the behavior of a function without permanently modifying the function itself. They wrap a function inside another function.

## Key Concepts
- **Functions as First-Class Citizens**: You can pass functions as arguments.
- **Syntax**: Uses the `@decorator_name` symbol above the function definition.
- **Wrapper**: The inner function that adds functionality.

## Code Example
```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello world"

print(say_hello()) # HELLO WORLD
```

## Task
Create a `@timer` decorator that calculates and prints how long a function takes to execute (use the `time` module).