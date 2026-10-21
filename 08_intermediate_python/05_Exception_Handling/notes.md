# 05. Exception Handling: Complete Reference

---

## 1. Exception Control Flow: `try`, `except`, `else`, `finally`

### What it is
- The fundamental construct for handling runtime errors gracefully:
  - `try`: Encloses code that may potentially raise an exception.
  - `except ExceptionType as err`: Catches and handles matching exceptions.
  - `else`: Executes **only** if the `try` block ran to completion *without* raising any exceptions.
  - `finally`: Executes unconditionally under **all** circumstances (whether an exception was raised, caught, re-raised, or a `return` statement was executed).

### Why it matters
- Prevents unhandled exceptions from crashing the application or process.
- The `else` block prevents accidentally catching exceptions raised by error-handling logic itself.
- The `finally` block guarantees reliable cleanup of external system resources (closing file descriptors, releasing locks, returning database connections to pools).

### How it works (internals, if relevant)
- When an exception occurs, CPython searches backwards through active stack frames for a matching exception handler table entry (`SETUP_FINALLY`).
- If an uncaught exception is raised inside a `finally` block, it suppresses previous exceptions (unless chained).
- If a `return` is placed inside `finally`, it will override and discard any `return` or unhandled exception raised in `try` or `except`!

### Common mistakes / gotchas
- Placing return statements inside `finally` blocks, which silently swallows raised exceptions:
  ```python
  def bad_func():
      try:
          raise ValueError("Fatal error!")
      finally:
          return 42 # Silently eats the ValueError!
  ```
- Putting too much code inside the `try` block instead of confining `try` strictly to the risky operation and placing subsequent code in `else`.

### Connects to
- Context Managers (Topic 10) which automate `try-finally` cleanup semantics.

---

## 2. Python Exception Hierarchy: `BaseException` vs `Exception`

### What it is
- All built-in exceptions in Python form an inheritance tree rooted at `BaseException`:
  - **`BaseException`**: Top-level root of all exceptions.
    - `SystemExit`: Raised by `sys.exit()`.
    - `KeyboardInterrupt`: Raised when user presses `Ctrl+C`.
    - `GeneratorExit`: Raised when a generator's `close()` is called.
    - **`Exception`**: The base class for all non-system-exiting exceptions (e.g. `ValueError`, `KeyError`, `TypeError`, `OSError`, `RuntimeError`).

### Why it matters
- Custom exceptions and application error handlers must **always** inherit from `Exception`, never from `BaseException`.
- Catching `BaseException` intercepts `KeyboardInterrupt` and `SystemExit`, preventing users from stopping the program or scripts from terminating properly.

### How it works (internals, if relevant)
- Python's `except Exception:` catches all standard programming errors while allowing system-level signals (`SIGINT` -> `KeyboardInterrupt`) to pass through unhindered.
- Bare `except:` is equivalent to `except BaseException:`, which is why it is an egregious antipattern in production software.

### Common mistakes / gotchas
- Using a bare `except:` or `except BaseException:`, making the process impossible to terminate with `Ctrl+C`.
- Catching an overly broad exception too high in the call stack, masking unexpected bugs like `NameError` or `AttributeError`.

### Connects to
- Best Practices (subtopic 7 below).

---

## 3. Catching Multiple Specific Exceptions

### What it is
- Handling multiple distinct exception types:
  - Separate blocks: handling each exception type with tailored remediation logic.
  - Combined tuple: `except (TypeError, ValueError, KeyError) as err:` handling multiple exceptions uniformly.

### Why it matters
- Keeps error recovery granular: a network timeout requires a retry; an invalid password requires an immediate authentication rejection.
- Grouping related errors into a tuple avoids duplicate error recovery blocks.

### How it works (internals, if relevant)
- Exception matching tests `isinstance(raised_exception, CaughtExceptionClass)`.
- Python evaluates `except` clauses top-to-bottom sequentially. The first matching block is executed; subsequent handlers are ignored.

### Common mistakes / gotchas
- Specifying multiple exceptions without parentheses: `except TypeError, ValueError:` is valid Python 2 syntax (binding `ValueError` to the name `TypeError`!), which raises `SyntaxError` in Python 3. Must use a tuple: `except (TypeError, ValueError):`.
- Putting a general parent exception before a specific child exception:
  ```python
  except LookupError: # Parent of KeyError and IndexError
      ...
  except KeyError:    # Dead code: never reached!
      ...
  ```

### Connects to
- Custom Exception Hierarchies (subtopic 4 below).

---

## 4. Custom Exception Hierarchies

### What it is
- User-defined exception classes designed specifically for an application's domain model.
- Always inherit from `Exception` (or a domain base exception):
  ```python
  class AppError(Exception):
      """Base exception for all application errors."""
      pass

  class ValidationError(AppError):
      def __init__(self, field, reason):
          super().__init__(f"Validation failed for '{field}': {reason}")
          self.field = field
          self.reason = reason
  ```

### Why it matters
- Allows API consumers to catch either all application-level errors using `except AppError:` or specific sub-failures using `except ValidationError:`.
- Attaches domain-specific structured metadata (HTTP status codes, error field names, user IDs) directly to the exception object.

### How it works (internals, if relevant)
- Exception objects store arguments passed to `__init__` in the `args` tuple attribute.
- Custom exceptions can override `__str__` or define custom serialization methods (e.g. `.to_dict()`) for JSON API error responses.

### Common mistakes / gotchas
- Inheriting directly from `BaseException` instead of `Exception`.
- Failing to create a domain base exception, forcing users of a library to catch dozens of unrelated individual exception classes.

### Connects to
- Testing (Topic 12) for verifying custom exceptions with `pytest.raises`.

---

## 5. Exception Chaining & Context (`raise ... from ...`)

### What it is
- Mechanisms for preserving original root cause errors when wrapping or translating exceptions across architectural layers:
  - **Explicit Chaining**: `raise NewException(...) from original_exc` (sets `__cause__`).
  - **Implicit Chaining**: If an exception is raised while handling another exception in an `except` or `finally` block, Python automatically records the prior exception (sets `__context__`).
  - **Suppression**: `raise NewException(...) from None` (suppresses the original context from appearing in traceback).

### Why it matters
- Prevents loss of diagnostic debugging information when translating low-level errors (e.g. `sqlite3.OperationalError`) into high-level business errors (`DatabaseConnectionError`).
- Suppressing context (`from None`) cleans up user-facing tracebacks by hiding irrelevant internal implementation failures.

### How it works (internals, if relevant)
- When `raise NewException from orig` runs:
  - `NewException.__cause__` is set to `orig`.
  - Python's traceback printer outputs: `"The above exception was the direct cause of the following exception:"`.
- When an exception occurs naturally inside an `except` handler without `from`:
  - `NewException.__context__` is set to the handled exception.
  - Traceback printer outputs: `"During handling of the above exception, another exception occurred:"`.

### Common mistakes / gotchas
- Swallowing the original exception by raising a new exception without chaining, destroying the original root cause stack trace and line numbers.
- Confusing `from None` (intentional context suppression) with accidental context loss.

### Connects to
- Databases with Python (Topic 18) for translating driver exceptions into ORM exceptions.

---

## 6. Re-raising Exceptions (`raise` vs `raise e`)

### What it is
- Re-raising an exception after performing partial handling (e.g. logging an audit entry or cleaning up state):
  - **Bare `raise`**: Re-raises the active exception currently being handled.
  - **`raise err`**: Re-raises the captured exception variable.

### Why it matters
- Bare `raise` preserves the **exact original traceback and stack frame position** where the error originated.
- Calling `raise err` can sometimes mutate or reset the traceback frame in subtle edge cases.

### How it works (internals, if relevant)
- CPython maintains the currently active exception in thread-local storage (`_PyErr_GetRaisedException`).
- A bare `raise` statement accesses this active exception directly without reconstructing or altering the traceback object.

### Common mistakes / gotchas
- Catching an exception, logging it, and forgetting to re-raise, silently allowing faulty execution to proceed.
- Using `raise sys.exc_info()[1]` (legacy syntax) instead of a simple bare `raise`.

### Connects to
- Exception Groups in Python 3.11+ (subtopic 7 below).

---

## 7. Best Practices, EAFP vs LBYL, and Exception Groups

### What it is
- **EAFP (Easier to Ask for Forgiveness than Permission)**: Python's standard idiomatic style: execute code assuming success, and catch exceptions if it fails (`try-except`).
- **LBYL (Look Before You Leap)**: Checking preconditions before performing an action (e.g. `if os.path.exists(f): open(f)`). Vulnerable to Race Conditions (Time-Of-Check to Time-Of-Use / TOCTOU).
- **Exception Groups** (`ExceptionGroup` / `TaskGroup`) and `except*` (Python 3.11+): Enables handling multiple concurrent exceptions simultaneously (used heavily in `asyncio`).

### Why it matters
- EAFP is faster in the typical success path because no pre-checks are performed, and eliminates race conditions.
- `except*` provides language-level support for managing aggregate errors in parallel workflows.

### How it works (internals, if relevant)
- In CPython, `try` blocks have **zero runtime overhead** when no exception occurs (Zero-Cost Exceptions since Python 3.11 via compiler lookup tables).
- Pre-checking (`os.path.exists()`) requires an explicit OS system call; if the file is deleted immediately after the check, the subsequent `open()` crashes anyway. EAFP handles this atomically.

### Common mistakes / gotchas
- Using bare `except: pass` (the "black hole" antipattern), which hides all syntax errors, typos, and memory issues.
- Using exceptions for routine loop termination or standard control flow where a boolean check is more readable.

### Connects to
- Concurrency and Asyncio (Topic 17) for `TaskGroup` and `ExceptionGroup`.
