# 10. Context Managers — Interview & Viva Questions

---

### Q1: What is the method signature of `__exit__`, and what do its parameters represent?
**Model Answer:**
- The signature is `def __exit__(self, exc_type, exc_val, exc_tb):`.
- Parameters:
  - `exc_type`: The exception class (e.g. `ZeroDivisionError`) if an exception was raised, or `None` if the block succeeded.
  - `exc_val`: The exception instance containing the error message and arguments, or `None`.
  - `exc_tb`: The traceback object detailing the call stack frame at the point the exception occurred, or `None`.
- If no exception occurred in the `with` block, all three parameters are passed as `None`.

---

### Q2: How do you suppress an exception inside `__exit__` versus allowing it to propagate?
**Model Answer:**
- To **suppress** an exception: Return a truthy value (`return True`) from `__exit__`. Python will clear the exception state and resume normal execution immediately after the `with` statement.
- To **propagate** an exception: Return `False` (or let the method return `None` by default). Python will automatically re-raise the exception up the call stack.
- Warning: You should only return `True` for expected, handled exceptions; returning `True` unconditionally will accidentally mask programming errors like `NameError` or `TypeError`.

---

### Q3: What happens if an exception is raised inside `__enter__`?
**Model Answer:**
- If an exception occurs during the execution of `__enter__()`, the runtime context has not been successfully established.
- Consequently, the protected block inside the `with` statement is aborted, and the context manager's `__exit__()` method is **NEVER called**.
- If resource cleanup is required upon an acquisition failure, the acquisition logic inside `__enter__()` must handle its own exceptions internally using standard `try-except-finally`.

---

### Q4: Why must code inside `@contextmanager` generator functions always wrap `yield` in a `try-finally` block?
**Model Answer:**
- When an exception is raised inside a `with` block managed by `@contextmanager`, the decorator catches the exception and re-injects it into the generator function at the exact point of the `yield` statement using `generator.throw()`.
- If the `yield` statement is not enclosed in a `try-finally` (or `try-except-finally`) block, the injected exception immediately crashes out of the generator function.
- As a result, any cleanup code placed after `yield` is completely skipped, causing resource leaks. Wrapping `yield` in `try-finally` guarantees cleanup execution under all error conditions.

---

### Q5: What is `contextlib.ExitStack`, and what problem does it solve?
**Model Answer:**
- `contextlib.ExitStack` allows managing a dynamic or variable number of context managers and arbitrary cleanup callbacks programmatically.
- Standard `with` syntax requires nesting or comma-separation of a fixed number of known managers. If you need to open an arbitrary list of $N$ files based on user input, standard `with` statements cannot easily express it without recursion.
- `ExitStack.enter_context(mgr)` registers managers onto an internal LIFO stack and guarantees that all registered managers have their `__exit__` methods called in reverse order when the stack exits.

---

### Q6: What is the difference between a reusable and a reentrant context manager?
**Model Answer:**
- **Reusable**: The same context manager instance can be used in multiple separate `with` statements sequentially (`with mgr: ...; with mgr: ...`).
- **Reentrant**: The same context manager instance can be nested within itself simultaneously (`with mgr: with mgr: ...`).
- Most class-based context managers that reset state in `__enter__` are reusable. Reentrant managers (like `threading.RLock`) maintain state (such as acquisition depth counters) to allow safe re-entry without deadlocks. Generators decorated with `@contextmanager` are generally neither, because generators cannot be iterated multiple times.

---

### Q7: How does `contextlib.ContextDecorator` allow a class to serve as both a context manager and a function decorator?
**Model Answer:**
- Inheriting from `contextlib.ContextDecorator` equips a context manager class with the ability to decorate functions (`@MyManager()`).
- Under the hood, `ContextDecorator` wraps the decorated function's execution inside its own `with self: return func(*args, **kwargs)` block.
- This allows a single class (such as an execution timer, audit logger, or temporary environment switcher) to be used either around an isolated code block (`with Timer(): ...`) or around an entire function (`@Timer() def run(): ...`).
