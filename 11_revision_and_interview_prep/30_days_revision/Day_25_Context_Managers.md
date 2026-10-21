# Day 25: Context Managers

## Explanation
Context managers handle setup and teardown logic automatically (like closing a file or a database connection). You use them with the `with` statement.

## Key Concepts
- **Dunder Methods**: Require `__enter__` and `__exit__`.
- **`contextlib`**: A standard library module to easily create context managers using the `@contextmanager` decorator.

## Code Example
```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileManager('test.txt') as f:
    f.write('Custom context manager!')
```

## Task
Create a custom context manager that prints "Entering..." when opened and "Exiting..." when closed.