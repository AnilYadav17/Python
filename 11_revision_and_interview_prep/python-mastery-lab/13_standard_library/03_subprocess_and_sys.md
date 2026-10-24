# Lesson 13.3: The Operating System Bridge (`subprocess`, `sys`, and `os`)

## 1. What Is This in Simple Words?
Python doesn't live in a bubble. It runs on top of your operating system (Linux, macOS, or Windows).  
- **`sys`**: Gives you direct information about Python itself (command-line arguments, installed modules, recursion limit, memory size of objects).
- **`os`**: Lets you talk to the operating system (environment variables, current working directory, process IDs).
- **`subprocess`**: Python's remote control to run other command-line applications (like `git`, `ffmpeg`, `ls`, or `curl`) from inside Python.

---

## 2. Power Tools in `sys` & `os`

### A. Inspecting Command Line Arguments (`sys.argv`)
When you run `python script.py hello 42`, `sys.argv` captures those words:
```python
import sys

print(f"Script name: {sys.argv[0]}")
# sys.argv is a list of strings
print(f"Arguments passed: {sys.argv[1:]}")
```

### B. Accurate Memory Measurement (`sys.getsizeof`)
Find out how many bytes a Python object takes in RAM:
```python
import sys

empty_list = []
empty_dict = {}
small_int = 42

print(f"Empty list size: {sys.getsizeof(empty_list)} bytes")  # ~56 bytes
print(f"Empty dict size: {sys.getsizeof(empty_dict)} bytes")  # ~64 bytes
print(f"Integer size: {sys.getsizeof(small_int)} bytes")      # ~28 bytes
```

### C. Environment Variables with `os.environ`
Always read sensitive API keys and secrets from the environment, NEVER hardcode them:
```python
import os

# Safely read with default fallback:
database_url = os.environ.get("DATABASE_URL", "sqlite:///dev.db")
print(f"Connecting to: {database_url}")
```

---

## 3. Running Commands Safely with `subprocess.run`

### The Golden Rule: Avoid `os.system()`!
`os.system()` passes strings straight to a shell, making it extremely vulnerable to command injection bugs. Always use `subprocess.run()` with a list of arguments and `check=True`:

```python
import subprocess

# Run a safe command:
result = subprocess.run(
    ["echo", "Hello from Python!"],
    capture_output=True,
    text=True,
    check=True  # Raises CalledProcessError if returncode != 0
)

print(f"Exit code: {result.returncode}")
print(f"Output: {result.stdout.strip()}")
```

---

## 4. Mind-Blowing & Interesting Facts! 💡

> **Fact 1: Python Integers Are Big!**  
> In C or C++, a 32-bit integer takes only 4 bytes. In Python, the number `0` takes **24 to 28 bytes** of RAM! Why? Because in Python, *everything is an object* containing a reference count header, a type pointer, and size metadata.
>
> **Fact 2: Shell Injection Trap!**  
> If you run `subprocess.run(f"cat {user_input}", shell=True)`, and a user types `file.txt; rm -rf /`, Python's shell executes the second command! Passing a list `["cat", user_input]` with `shell=False` completely neutralizes this attack because the operating system treats the entire string as a literal filename.

---

## 5. Self-Test & Exercises
1. **Question**: Why is `subprocess.run(["ls", "-l"], check=True)` better than `os.system("ls -l")`?
   - *Answer*: `subprocess.run` captures output, avoids shell injection vulnerabilities, and automatically raises an exception if the command fails.
2. **Exercise**: Write a snippet using `sys.platform` to print whether Python is running on `"linux"`, `"darwin"` (macOS), or `"win32"`.
