# 10. Context Managers: Complete Reference

---

## 1. The `with` Statement Mechanics & Bytecode

### What it is
- The `with` statement is Python's dedicated syntax for resource management, formalizing the RAII (Resource Acquisition Is Initialization) pattern.
- Syntax:
  ```python
  with expression as target:
      # protected block
  ```
- Evaluates `expression` to obtain a context manager object, enters runtime context, executes the block, and guarantees clean exit handling.

### Why it matters
- Eliminates resource leaks (unclosed files, orphaned locks, dangling sockets, uncommitted database transactions).
- Replaces verbose, error-prone `try-finally` boilerplate with declarative, readable code.

### How it works (internals, if relevant)
- CPython compiles `with` statements into specialized bytecode instructions:
  - Calls `type(mgr).__enter__(mgr)`. The return value is bound to the `as target` identifier.
  - Registers the exception handler via `SETUP_WITH`.
  - Executes the inner block.
  - If the block exits normally: calls `mgr.__exit__(None, None, None)`.
  - If an exception occurs: pushes `exc_type`, `exc_val`, and `exc_tb` onto stack, executes `WITH_EXCEPT_START`, and invokes `mgr.__exit__(exc_type, exc_val, exc_tb)`.
  - If `__exit__` returns a truthy value (`True`), the exception is **suppressed**; otherwise, it is re-raised.

### Common mistakes / gotchas
- Assuming `target` receives the context manager object itself: `target` receives whatever value `__enter__()` returns (e.g. `open()` returns the file object, but custom managers may return `self`, an integer, or `None`).
- If an exception is raised inside `__enter__()`, the `with` block is aborted and `__exit__()` is **NEVER called**!

### Connects to
- Class-Based Context Managers (subtopic 2 below).

---

## 2. Class-Based Context Managers (`__enter__` & `__exit__`)

### What it is
- Any Python class that implements the context manager protocol:
  - `__enter__(self)`: Prepares the runtime environment or acquires a resource. Returns the value bound to the `as` variable.
  - `__exit__(self, exc_type, exc_val, exc_tb)`: Tears down the environment or releases the resource.

### Why it matters
- Encapsulates lifecycle setup and teardown logic cleanly into an object-oriented abstraction.
- Highly reusable across multiple parts of a codebase and easily configured via `__init__`.

### How it works (internals, if relevant)
- The arguments passed to `__exit__`:
  - If no exception occurred: `(None, None, None)`.
  - If an exception occurred:
    - `exc_type`: The exception class (e.g. `<class 'ValueError'>`).
    - `exc_val`: The exception instance (e.g. `ValueError("invalid input")`).
    - `exc_tb`: The traceback object (`<traceback object at ...>`).

### Common mistakes / gotchas
- Defining `__exit__` with fewer than 4 arguments (forgetting `self, exc_type, exc_val, exc_tb`), raising `TypeError` when exiting the `with` block.
- Mutating traceback objects inside `__exit__`.

### Connects to
- Exception Suppression (subtopic 3 below).

---

## 3. Exception Handling & Suppression in `__exit__`

### What it is
- The mechanism allowing a context manager to decide whether an exception raised within its block should be swallowed or propagated to the outer scope:
  - **Propagate (Default)**: Return `False` (or `None`). Python will re-raise the exception up the call stack.
  - **Suppress**: Return `True`. Python silences the exception and resumes normal execution immediately after the `with` statement.

### Why it matters
- Enables building specialized error-handling utilities, such as `contextlib.suppress(FileNotFoundError)` or resilient circuit breakers that swallow non-fatal exceptions while logging them.

### How it works (internals, if relevant)
- Bytecode `WITH_EXCEPT_START` inspects the boolean truthiness of `__exit__`'s return value.
- If truthy, the exception state is cleared from the virtual machine frame; if falsy, Python re-raises the exception.

### Common mistakes / gotchas
- Accidentally suppressing all exceptions by having `__exit__` return a truthy value unintentionally (e.g. `return self` or `return True` unconditionally), masking critical bugs like `NameError` or `TypeError`.
- Never suppress unexpected exceptions: only suppress specific expected exception types:
  ```python
  def __exit__(self, exc_type, exc_val, exc_tb):
      if exc_type is not None and issubclass(exc_type, FileNotFoundError):
          return True # Suppress only FileNotFoundError
      return False    # Propagate everything else
  ```

### Connects to
- Generator-Based Context Managers (subtopic 4 below).

---

## 4. Generator-Based Context Managers (`@contextmanager`)

### What it is
- A decorator from the `contextlib` module that turns a Python generator function into a context manager without writing a full class:
  ```python
  from contextlib import contextmanager

  @contextmanager
  def managed_resource():
      # Setup code (equivalent to __enter__)
      resource = acquire()
      try:
          yield resource # Value bound to 'as' target
      finally:
          # Teardown code (equivalent to __exit__)
          release(resource)
  ```

### Why it matters
- Reduces 20 lines of class boilerplate down to a simple 6-line generator function.
- The standard, idiomatic way to write lightweight context managers in modern Python.

### How it works (internals, if relevant)
- `@contextmanager` wraps the generator inside a `_GeneratorContextManager` object.
- Upon entering `with`: advances generator to the `yield` statement via `next(gen)`.
- Upon exiting `with`:
  - If no exception: advances generator past `yield` to completion (`next(gen)`).
  - If exception occurred: injects the exception into the generator at the `yield` point using `gen.throw(exc_type, exc_val, exc_tb)`.
  - If the generator catches or suppresses the exception and terminates normally, the exception is suppressed in the caller.

### Common mistakes / gotchas
- Forgetting the `try-finally` block around `yield`: if an exception is raised inside the `with` block, the exception is thrown into the generator. Without `finally`, the cleanup code after `yield` will **never execute**!
- Yielding more than once: a `@contextmanager` generator must yield **exactly once**. Yielding zero times or multiple times raises `RuntimeError`.

### Connects to
- Iterators & Generators (Topic 11) for generator mechanics and `throw()`.

---

## 5. Standard Library `contextlib` Utilities

### What it is
- Powerful pre-built context utilities in `contextlib`:
  - **`contextlib.suppress(*exceptions)`**: Silences specified exceptions cleanly:
    ```python
    with contextlib.suppress(FileNotFoundError):
        os.remove("temp.txt")
    ```
  - **`contextlib.ExitStack()`**: Dynamically enters and manages an arbitrary number of context managers programmatically.
  - **`contextlib.closing(thing)`**: Ensures objects with a `.close()` method (sockets, urllib streams) are closed.
  - **`contextlib.redirect_stdout(stream)`**: Temporarily redirects `sys.stdout` to a file or `io.StringIO` buffer.
  - **`contextlib.ContextDecorator`**: Base class enabling a context manager to also be used as a function decorator (`@my_context`).

### Why it matters
- `ExitStack` solves the complex problem of opening a variable number of files or acquiring dynamic locks without deeply nested, unmaintainable `with` indentations.
- `suppress` replaces 5 lines of `try-except-pass` with a clean, expressive one-liner.

### How it works (internals, if relevant)
- `ExitStack` maintains an internal LIFO stack of cleanup callbacks and `__exit__` methods.
- When `ExitStack` exits, it invokes the callbacks in reverse order, properly threading exceptions through each registered exit handler.

### Common mistakes / gotchas
- Using `contextlib.suppress()` too broadly (e.g. `suppress(Exception)`), which silences genuine programming bugs.
- Forgetting that `ExitStack` unwinds callbacks in LIFO (Last-In, First-Out) order.

### Connects to
- Real-World Applications (subtopic 7 below).

---

## 6. Reentrant vs Reusable Context Managers

### What it is
- **Reusable**: A context manager instance that can be passed to multiple `with` statements sequentially:
  ```python
  mgr = MyContext()
  with mgr: ...
  with mgr: ... # Reused
  ```
- **Reentrant**: A context manager that can be nested within itself simultaneously:
  ```python
  with mgr:
      with mgr: # Re-entered
          ...
  ```

### Why it matters
- Many custom context managers (especially those using `@contextmanager`) are single-use only: once consumed, re-entering them raises `RuntimeError: generator didn't yield`.
- Synchronization locks (`threading.RLock`) and timers must be designed with reentrancy in mind.

### How it works (internals, if relevant)
- Generators decorated with `@contextmanager` cannot be re-entered because a generator can only be iterated once.
- Class-based context managers can be made reusable by resetting internal state in `__enter__`, or reentrant by tracking an internal nesting depth counter (`self.depth`).

### Common mistakes / gotchas
- Passing a generator-based context manager instance to multiple `with` blocks instead of re-invoking the factory function (`with get_context(): ...`).

### Connects to
- Concurrency (Topic 17) for `threading.Lock` vs `threading.RLock`.

---

## 7. Real-World Applications & Patterns

### What it is
- Standard production patterns:
  - **Execution Timer**: Benchmarking code blocks and logging latencies.
  - **Transactional Unit of Work**: Database transactions where operations are committed on success or rolled back on error.
  - **Temporary Environment Override**: Temporarily altering `os.environ` or `sys.path` and restoring original values upon exit.
  - **File Locking**: Acquiring OS advisory locks (`fcntl.flock`) for cross-process concurrency safety.

### Why it matters
- Provides deterministic state restoration even under catastrophic unexpected errors.
- Separates infrastructure concerns (locking, connection pooling, rollback) from application business logic.

### How it works (internals, if relevant)
- The context manager records pre-state in `__enter__`.
- In `__exit__`, inspects `exc_type`: if `None`, commits changes; if an exception occurred, executes rollback procedures and lets the exception propagate.

### Common mistakes / gotchas
- Rolling back state but accidentally swallowing the exception, misleading callers into thinking the operation succeeded.

### Connects to
- Databases with Python (Topic 18) and Testing (Topic 12).
