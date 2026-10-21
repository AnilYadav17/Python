# Day 9: Dictionaries

## Explanation
Dictionaries store data in **key-value pairs**. They are ordered (as of Python 3.7) and mutable. Keys must be immutable (strings, numbers, tuples).

## Key Concepts
- **Creating**: `my_dict = {'key': 'value'}`.
- **Accessing**: `my_dict['key']` (throws error if missing) vs `my_dict.get('key')` (returns None).
- **Methods**: `.keys()`, `.values()`, `.items()`, `.update()`, `.pop()`.

## Code Example
```python
student = {"name": "John", "age": 22}
student["grade"] = "A"

for key, value in student.items():
    print(f"{key}: {value}")
```

## Task
Create a dictionary representing a book (title, author, year). Add a 'genre' key. Iterate over the dictionary and print all key-value pairs.