# Lesson 05: Modern Filesystem Operations with `pathlib`

## 1. Why `os.path` and String Paths Are Obsolete

In old Python code, working with file paths meant clumsy string manipulation:
```python
# The Clunky Old Way (os.path):
import os
filepath = os.path.join(os.path.expanduser("~"), "documents", "data.csv")
```
If you accidentally concatenate with `+ "/"`, your code breaks on Windows (which uses backslashes `\`).

Modern Python (PEP 428) introduces **`pathlib.Path`**, which represents paths as **real objects with methods, not raw strings**:

```python
from pathlib import Path

# The Modern, Clean Way:
base_dir = Path.home() / "documents"
filepath = base_dir / "data.csv"
print(filepath)
```

---

## 2. Fascinating Fact: Overloading the Division Operator `/` for Paths! 💡
> **Did you know?**
> How does `base_dir / "data.csv"` work?  
> Python's `Path` class overloads the mathematical division operator via **`__truediv__`**!  
> When you divide a `Path` object by a string, Python joins them into a cross-platform path, automatically handling Windows backslashes `\` and Linux forward slashes `/` seamlessly!

---

## 3. Reading and Writing Files in One Line

With `pathlib`, you don't even need `with open(...)` for simple files:

```python
from pathlib import Path

notes = Path("notes.txt")

# 1. Write text in one line:
notes.write_text("Hello from pathlib!", encoding="utf-8")

# 2. Read text in one line:
content = notes.read_text(encoding="utf-8")
print("Read:", content)

# 3. Check properties instantly:
print("Exists?    ", notes.exists())
print("File name: ", notes.name)       # "notes.txt"
print("Extension: ", notes.suffix)     # ".txt"
print("Parent dir:", notes.parent)     # "."

# Cleanup:
notes.unlink()  # Deletes the file!
```

---

## 4. Quick Self-Test
1. What operator does `pathlib.Path` overload to join path segments?
   - *Answer: The division operator (`/`).*
2. What method on a `Path` object deletes a file?
   - *Answer: `.unlink()`.*
