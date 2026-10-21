# 🛡️ 07_Error_and_File_Handling: Resilience, Exceptions & Streams

## Overview
Real-world software interacts with unpredictable external environments: files can be missing, network connections drop, disk storage fills up, and users type invalid input. Writing production-grade software requires **defensive programming**—anticipating errors gracefully and managing persistent files safely.

This module combines two tightly related disciplines:
1. **Exception Handling:** Using `try`, `except`, `else`, and `finally` to intercept runtime errors, prevent crashes, and create custom domain exceptions.
2. **File Handling:** Interacting with persistent storage using file modes (`r`, `w`, `a`, `r+`, `w+`, `x`), stream pointers (`seek`, `tell`), and safe resource management using Python's `with` statement (**Context Managers**).

---

## Learning Objectives
By studying this module, you will understand:
1. The difference between **Syntax Errors** (compile time) and **Exceptions** (runtime events).
2. Catching specific built-in exceptions: `ZeroDivisionError`, `ValueError`, `TypeError`, `IndexError`, `KeyError`, `NameError`, and `FileNotFoundError`.
3. The complete lifecycle of `try -> except -> else -> finally`.
4. Designing domain-specific Custom Exception classes inheriting from Python's base `Exception`.
5. Edge cases: How `return` statements interact with `finally`, and why `os._exit(0)` terminates execution without executing `finally`.
6. File I/O modes and behaviors:
   * `'r'` — Read mode (default; requires file to exist).
   * `'w'` — Write mode (creates file or truncates existing content).
   * `'a'` — Append mode (adds data at the end without truncation).
   * `'r+'` — Read and write mode (file must exist; overwrites at pointer).
   * `'w+'` — Write and read mode (truncates file and allows read).
   * `'x'` — Exclusive creation mode (fails if file already exists).
7. Context managers: How `with open(...) as f:` guarantees file descriptor closure even when exceptions occur.

---

## Prerequisites
* **[02_python_fundamentals](../02_python_fundamentals/)** (Basic syntax, data types)
* **[05_object_oriented_programming](../05_object_oriented_programming/)** (Class inheritance for custom exceptions)

---

## Learning Path

```text
1. Exception Handling Fundamentals (exception_handling/)
   └── try-except blocks, handling multiple exception types
       ▼
2. Control Flow with else & finally (exception_handling/)
   └── Cleanup logic, return in finally, os._exit behavior
       ▼
3. Custom Domain Exceptions (exception_handling/)
   └── Inheriting from Exception, Email & Banking validation
       ▼
4. File Operations & Modes (file_handling/)
   └── open(), read(), write(), append(), r+, w+, x modes
       ▼
5. Safe Stream Management (file_handling/)
   └── Context managers ('with open'), cursor positioning ('seek', 'tell')
```

---

## Repository Contents & Examples

### 🛡️ Exception Handling (`exception_handling/`)

| File | Focus | Description |
|:---|:---|:---|
| `01_zero_division_try_except.py` | Basic Catching | Intercepting division by zero gracefully. |
| `02_multiple_except_blocks.py` | Multi-Type Catching | Handling distinct error types with separate responses. |
| `03_type_error_handling.py` | Type Safety | Catching string concatenation vs. integer arithmetic errors. |
| `04_index_error_handling.py` | Sequence Bounds | Preventing out-of-bounds list index crashes. |
| `05_key_error_handling.py` | Hash Map Bounds | Handling missing keys in dictionaries cleanly. |
| `06_name_error_nested_try.py` | Scopes & Nesting | Handling undefined variables and nested try blocks. |
| `07_generic_exception_base.py` | Inheritance | Catching the general `Exception` base class. |
| `08_value_error_handling.py` | Input Parsing | Inspecting exception instances using `as v`. |
| `09_try_finally_return_behavior.py` | Finally Mechanics | Verifying that `finally` runs even when `try` returns early. |
| `10_os_exit_and_finally.py` | Process Termination | Demonstrating how `os._exit(0)` bypasses `finally`. |
| `custom_exception_email_validator.py` | Custom Errors | Defining `DotException` and `AteTheRateException`. |
| `custom_exception_bank_account.py` | Custom Errors | Defining `InsufficientBalance` and `NegativeDepositException`. |
| `Theory/Exception_Keywords.md` | Reference Notes | Summary of `try`, `except`, `else`, and `finally` keywords. |

### 📁 File Handling (`file_handling/`)

| File | Mode / Concept | Description |
|:---|:---|:---|
| `01_file_open_syntax.py` | Syntax & Defaults | Syntax of `open()`, reading text, default mode `'r'`. |
| `02_file_read_and_close.py` | Manual Descriptors | Explicit `file.read()` and `file.close()`. |
| `03_context_manager_with_open.py` | Context Managers | Using `with open()` and verifying `file.closed`. |
| `append_mode_demo.py` | Append `'a'` | Appending lines without clearing existing content. |
| `read_write_rplus_mode.py` | Read/Write `'r+'` | Dual reading and writing with existing files. |
| `write_read_wplus_mode.py` | Write/Read `'w+'` | Truncating, writing, seeking (`seek(0)`), and reading. |
| `exclusive_creation_x_mode.py` | Exclusive `'x'` | Safe creation that errors if the target file already exists. |
| `file_modes_notes.md` | Reference Notes | Comparative summary of file mode flags. |

---

## How to Run Examples

```bash
# Test custom banking exception:
python3 07_error_and_file_handling/exception_handling/custom_exception_bank_account.py

# Test context manager and file closure verification:
python3 07_error_and_file_handling/file_handling/03_context_manager_with_open.py

# Test write and read with w+ mode:
python3 07_error_and_file_handling/file_handling/write_read_wplus_mode.py
```

---

## Practice & Real-World Projects

Put these concepts to work in real applications:
* **[Student Result Processor](../13_mini_projects/02_student_result_processor/)** — A complete application that parses student data, validates marks, writes results, and logs invalid records to an `error_log.txt` stream.

---

## Common Beginner Mistakes

1. **Bare `except:` Catch-All:**
   * Writing `except:` catches everything, including `KeyboardInterrupt` (Ctrl+C) and `SystemExit`, making it difficult to stop scripts. Always catch specific exceptions or `except Exception:` at minimum.
2. **Forgetting to Flush or Close Files:**
   * When opening files manually without `with`, data might sit in Python's internal I/O buffer and not be written to disk if the script crashes before `file.close()`. Always use `with open(...)`!
3. **Reading After Writing in `'w+'` Mode Without `seek(0)`:**
   * After writing data to a file, the stream position pointer is at the very end. Calling `.read()` immediately returns an empty string `""` unless you rewind with `file.seek(0)`.
4. **Treating Exceptions as Normal Control Flow:**
   * Don't use `try-except` for conditions that can be easily checked with a standard `if` statement (e.g. checking `if key in my_dict:` is faster and cleaner than catching `KeyError` in hot loops).

---

## Next Step

👉 Advance to **[08_intermediate_python](../08_intermediate_python/)** to master advanced Python internals: Concurrency, Iterators & Generators, Context Managers, Type Hints, and System Design!
