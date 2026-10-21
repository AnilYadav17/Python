# Day 15: Modules and Packages

## Explanation
Modules are Python files containing code. Packages are directories containing multiple modules and an `__init__.py` file.

## Key Concepts
- **Importing**: `import math`, `from math import sqrt`, `import pandas as pd`.
- **Custom Modules**: You can import any `.py` file in the same directory.
- **`if __name__ == "__main__":`**: Ensures code only runs when the script is executed directly, not when imported.

## Code Example
```python
# in my_module.py
def greet():
    print("Hello")

if __name__ == "__main__":
    print("This runs only if executed directly.")
```

## Task
Create a new file `math_utils.py` with an addition function. Import and use this function in a separate script.