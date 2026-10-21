# Day 3: Strings and Formatting

## Explanation
Strings are immutable sequences of characters. Python provides powerful ways to manipulate and format them.

## Key Concepts
- **Indexing & Slicing**: `text[start:stop:step]`.
- **Methods**: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.replace()`, `.join()`.
- **Formatting**: f-strings (introduced in Python 3.6), `.format()`.

## Code Example
```python
text = "  Python Programming  "
clean_text = text.strip().upper()
print(f"Cleaned: {clean_text}")
print("Reversed:", clean_text[::-1])
```

## Task
Create a string holding a full name. Use string slicing to extract the first name. Then, format a greeting using an f-string.