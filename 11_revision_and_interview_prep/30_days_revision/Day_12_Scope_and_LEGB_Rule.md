# Day 12: Scope and LEGB Rule

## Explanation
Scope determines the visibility and lifetime of a variable. Python follows the **LEGB** rule: Local, Enclosing, Global, and Built-in.

## Key Concepts
- **Local**: Inside the current function.
- **Enclosing**: Inside enclosing functions (nested functions).
- **Global**: Defined at the top level of the script.
- **Built-in**: Python's pre-defined names (e.g., `len`, `print`).
- **`global` keyword**: Used to modify a global variable inside a function.

## Code Example
```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer() # Prints 'local'
```

## Task
Create a global variable `counter = 0`. Write a function that uses the `global` keyword to increment the counter by 1 every time it's called.