# 🚀 01_Getting_Started: Onboarding & First Steps

## Overview
Welcome to the starting line of your Python journey! This directory is designed for absolute beginners who have never touched Python before. Here, you will learn how to install Python on any operating system, understand how the interpreter processes instructions, run code through multiple workflows, and execute your very first Python program.

---

## Learning Objectives
By completing this module, you will:
1. Verify and install Python 3.10+ on Windows, macOS, or Linux.
2. Understand the difference between the interactive REPL and executing `.py` script files.
3. Learn how to configure Visual Studio Code with the official Python extension.
4. Understand basic output with `print()`, comments (`#`), and variables.
5. Learn the importance of isolated virtual environments (`venv`).

---

## Prerequisites
* None! Just a computer running Windows, macOS, or Linux, and a desire to learn.

---

## Learning Path

```text
Step 1: Installation & PATH setup
   │     └── Read: installation.md
   ▼
Step 2: Understand Execution Modes (REPL vs Script)
   │     └── Read: running_python.md
   ▼
Step 3: Run Your First Executable Program
   │     └── Run: first_program.py
   ▼
Step 4: Move to Fundamentals
         └── Next: 02_python_fundamentals
```

---

## Guide & Examples

| File | Type | Description |
|:---|:---:|:---|
| 📄 **[installation.md](./installation.md)** | Guide | Step-by-step installation instructions for Linux, macOS, and Windows. |
| 📄 **[running_python.md](./running_python.md)** | Guide | Explaining the REPL, running `.py` files, VS Code setup, and virtual environments. |
| 🐍 **[first_program.py](./first_program.py)** | Script | Executable beginner program covering comments, print, types, and math. |

---

## How to Run the Example

Open your terminal, navigate to this folder, and run:

```bash
cd 01_getting_started
python3 first_program.py
```

Expected output:
```text
==================================================
  🚀 Welcome to Python Learning Hub!
==================================================
Hello, World! You are writing Python code.

Learning: Python (Major Version: 3)
Satisfaction Rating: 9.9/10 | Fun?: True
...
✅ Program executed successfully!
```

---

## Common Beginner Mistakes

1. **Forgetting to check "Add Python to PATH" on Windows:**
   * *Problem:* Running `python` in Command Prompt yields `'python' is not recognized as an internal or external command`.
   * *Fix:* Re-run the installer, click "Modify", and check the PATH checkbox, or add Python's installation folder to your System Environment Variables manually.

2. **Mixing Python 2 and Python 3 commands:**
   * *Problem:* On many Linux/macOS systems, `python` might still point to legacy Python 2.7 or fail entirely.
   * *Fix:* Always use `python3` and `pip3` in your terminal commands.

3. **Case Sensitivity:**
   * *Problem:* Writing `Print("hello")` or `true` instead of `print("hello")` and `True`.
   * *Fix:* Python is strictly case-sensitive. Keywords and built-ins must match exact casing.

4. **Confusing single/double quote mismatches:**
   * *Problem:* `print("Hello')` results in `SyntaxError: unterminated string literal`.
   * *Fix:* Strings must start and end with the matching quotation mark.

---

## Next Step

👉 Head over to **[02_python_fundamentals](../02_python_fundamentals/)** to learn about Variables, Data Types, Type Casting, Operators, Control Flow, and Loops!
