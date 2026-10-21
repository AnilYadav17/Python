# 05. Exception Handling — Interview & Viva Questions

---

### Q1: What is the role of the `else` clause in a `try-except-else-finally` block?
**Model Answer:**
- The `else` block executes **only if the code in the `try` block completes successfully without raising any exceptions**.
- It is used to separate the dangerous operation (placed inside `try`) from the downstream code that depends on the operation's success.
- This prevents downstream code from accidentally raising exceptions that get caught by the same `except` block, avoiding misleading error reporting.

---

### Q2: Why is using a bare `except:` clause considered a severe antipattern in Python?
**Model Answer:**
- A bare `except:` clause catches `BaseException`, the root of all exceptions in Python.
- This intercepts not only standard runtime errors (`ValueError`, `KeyError`), but also critical system signals:
  - `KeyboardInterrupt` (triggered when the user presses `Ctrl+C` to terminate the program).
  - `SystemExit` (triggered by `sys.exit()`).
- As a result, the application cannot be stopped or cleanly shut down by the operating system or user.
- Best practice: Always catch `Exception` (`except Exception:`) to handle standard application errors while allowing system signals to propagate unhindered.

---

### Q3: What is the difference between `raise ... from original_exc` and `raise ... from None`?
**Model Answer:**
- **`raise NewError from original_exc` (Explicit Chaining)**: Sets `NewError.__cause__ = original_exc`. The traceback explicitly displays both errors: *"The above exception was the direct cause of the following exception:"*, preserving the root cause for debugging.
- **`raise NewError from None` (Context Suppression)**: Sets `__suppress_context__ = True`. It suppresses the prior exception's traceback entirely, presenting only `NewError` to the caller. This is used in clean public APIs to hide low-level internal implementation details.

---

### Q4: What happens if a `return` statement is executed inside a `finally` block?
**Model Answer:**
- A `finally` block is guaranteed to execute under all circumstances before the function exits.
- If a `return` statement is placed inside a `finally` block, it **overrides and discards** any return value or pending unhandled exception from the preceding `try` or `except` blocks.
- If an exception was raised in `try`, the `return` in `finally` silences and swallows the exception completely, causing silent failures that are notoriously difficult to debug.

---

### Q5: Explain the difference between EAFP and LBYL programming styles in Python.
**Model Answer:**
- **EAFP (Easier to Ask for Forgiveness than Permission)**: Execute the operation directly assuming success, and catch exceptions if it fails (e.g. `try: with open("data.txt") as f: ... except FileNotFoundError: ...`).
- **LBYL (Look Before You Leap)**: Check preconditions before executing an operation (e.g. `if os.path.exists("data.txt"): with open("data.txt") as f: ...`).
- **Why EAFP is preferred in Python**:
  1. Prevents TOCTOU (Time-of-Check to Time-of-Use) race conditions where system state changes between the check and the action.
  2. Faster in the common success path due to Python 3.11+ zero-cost exception tables (no overhead when no exception occurs).

---

### Q6: How should custom domain exceptions be structured in a production Python project?
**Model Answer:**
- Define a base application exception subclassing `Exception` (e.g. `class AppError(Exception): pass`).
- Define specific sub-exceptions inheriting from that base class (e.g. `class UserNotFoundError(AppError): pass`).
- Benefits:
  - Callers can catch high-level domain errors (`except AppError:`) or specific failures (`except UserNotFoundError:`).
  - Can store structured metadata in `__init__` (e.g. `status_code`, `error_code`, `retryable`).
  - Keeps external callers decoupled from third-party or internal library exception types.

---

### Q7: What are `ExceptionGroup` and `except*`, introduced in Python 3.11?
**Model Answer:**
- `ExceptionGroup` allows grouping multiple independent or concurrent exceptions into a single composite exception object.
- It is crucial for concurrent programming (such as `asyncio.TaskGroup`), where multiple asynchronous tasks running in parallel can fail simultaneously.
- The `except*` syntax allows selective pattern-matching against subsets of exceptions inside an `ExceptionGroup`. For instance, `except* ValueError:` handles all `ValueError` instances in the group while allowing other exceptions in the group to propagate or be handled by other `except*` clauses.
