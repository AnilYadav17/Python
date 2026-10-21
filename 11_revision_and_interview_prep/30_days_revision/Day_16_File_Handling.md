# Day 16: File Handling

## Explanation
Python can read from and write to files on your system natively using the `open()` function.

## Key Concepts
- **Modes**: `'r'` (read), `'w'` (write, truncates), `'a'` (append), `'r+'` (read/write).
- **Context Managers (`with`)**: Automatically handles closing the file, even if errors occur. ALWAYS use this.
- **Methods**: `.read()`, `.readlines()`, `.write()`.

## Code Example
```python
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

## Task
Write a script that appends 3 lines of text to a file named `log.txt`, then reads the file and prints each line prefixed with its line number.