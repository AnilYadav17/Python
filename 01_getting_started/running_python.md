# ⚡ Running Python Code: Methods & Workflows

Python is an interpreted language, which means you have multiple flexible ways to write, test, and execute your code.

---

## 1. Method 1: The Interactive REPL (Read-Eval-Print Loop)

The REPL is an interactive Python terminal where you can type Python expressions and see immediate output. It is perfect for testing short snippets, mathematical calculations, and exploring built-in functions.

### Starting the REPL
Open your terminal and type:
```bash
python3
# On Windows:
python
```

You will see the Python prompt:
```python
Python 3.12.0 (main, Oct  2 2023, 12:00:00) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

### Try it out:
```python
>>> print("Hello from REPL!")
Hello from REPL!
>>> 25 * 4 + 10
110
>>> name = "Anil"
>>> f"Welcome, {name}!"
'Welcome, Anil!'
```

### Exiting the REPL:
Type `exit()` or press `Ctrl + D` (`Ctrl + Z` then `Enter` on Windows).

---

## 2. Method 2: Running a Python Script File (`.py`)

For real programs, you save your Python instructions in a text file with a `.py` extension and execute it via the interpreter.

### Step 1: Create a file named `hello.py`
```python
# hello.py
print("Hello, Python Learning Hub!")
```

### Step 2: Run it from the terminal
Navigate to the directory containing `hello.py`:
```bash
python3 hello.py
# or on Windows:
python hello.py
```

### Output:
```text
Hello, Python Learning Hub!
```

---

## 3. Method 3: Running Inside VS Code

If you use VS Code:
1. Open the project folder in VS Code (`code .`).
2. Open any `.py` file (e.g., `first_program.py`).
3. Click the **Play button ▶️** in the top-right corner, OR press `Ctrl + F5` (Run without Debugging).
4. The integrated terminal will open and show the output immediately.

---

## 4. Method 4: Virtual Environments (Best Practice)

When building projects or installing external libraries, always create an isolated virtual environment to prevent package version conflicts with your operating system:

```bash
# 1. Create a virtual environment named '.venv'
python3 -m venv .venv

# 2. Activate the virtual environment:
# On Linux / macOS:
source .venv/bin/activate

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

# On Windows (Command Prompt):
.venv\Scripts\activate.bat

# 3. Notice your prompt changes to: (.venv) user@machine:~$
# Now install packages safely:
pip install pytest

# 4. When done, deactivate:
deactivate
```

---

## 5. Summary Cheat Sheet

| Task | Terminal Command |
|:---|:---|
| Check Python Version | `python3 --version` |
| Launch Interactive Shell | `python3` |
| Run a Script File | `python3 filename.py` |
| Check Script Syntax without Running | `python3 -m py_compile filename.py` |
| Create Virtual Environment | `python3 -m venv .venv` |
| Activate Virtual Environment (Linux/macOS) | `source .venv/bin/activate` |

---

## 6. Next Step

Proceed to [first_program.py](./first_program.py) to examine basic structure, comments, variables, and Python conventions!
