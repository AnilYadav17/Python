# Day 30: Type Hinting & Best Practices

## Explanation
Type hints make your code more readable and allow tools like `mypy` to catch errors before runtime. Best practices ensure your code is maintainable and Pythonic.

## Key Concepts
- **Type Hints**: `def func(name: str) -> int:`
- **`typing` module**: `List`, `Dict`, `Optional`, `Union` (or `|` in Python 3.10+).
- **PEP 8**: The style guide for Python (naming conventions, spacing).
- **Virtual Environments**: Always isolate project dependencies using `venv`.

## Code Example
```python
from typing import List, Optional

def process_scores(scores: List[int], name: Optional[str] = None) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
```

## Task
Review a piece of code you wrote on Day 1. Add type hints to all functions and variables. Ensure it follows PEP 8 standards (4 spaces, snake_case for variables).

## Congratulations! 
You have completed the 30 Days of Python Revision Challenge. You are now officially a Python Pro! 🎉