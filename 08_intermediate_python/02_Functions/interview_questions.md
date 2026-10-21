# 02. Functions — Interview & Viva Questions

---

### Q1: Why should you never use a mutable object (like a list or dictionary) as a default parameter in Python?
**Model Answer:**
- Default parameter values in Python are evaluated **once at function definition time**, when the `def` statement is compiled, NOT every time the function is called.
- The evaluated default object reference is stored in the function's `__defaults__` attribute.
- If a mutable object like `[]` or `{}` is used as a default, all invocations of the function that omit that argument will share and mutate the **exact same object** across calls.
- The idiomatic fix is to set the default parameter to `None` and conditionally assign a newly instantiated mutable object inside the function body (`if arg is None: arg = []`).

---

### Q2: Explain the LEGB rule and what triggers an `UnboundLocalError`.
**Model Answer:**
- The LEGB rule defines Python's namespace search hierarchy for identifier resolution:
  1. **L**ocal: Names defined within the current function.
  2. **E**nclosing: Names in outer enclosing functions (closures).
  3. **G**lobal: Module-level variables or names declared with `global`.
  4. **B**uilt-in: Python built-in namespace (`len`, `range`, `Exception`, etc.).
- Python determines variable scope **at compile time**. If a variable is assigned anywhere inside a function (e.g. `x = 10`), Python marks `x` as local to that function for its entire scope.
- If the function attempts to read `x` before the assignment line executes (e.g., `print(x); x = 10`), Python sees that local `x` has not yet been assigned a value and raises `UnboundLocalError`.

---

### Q3: What is a closure in Python, and how does CPython implement it internally?
**Model Answer:**
- A closure is an inner function that retains access to variables in its outer enclosing scope even after the outer function has finished executing and its stack frame has been destroyed.
- Internally, when CPython detects an inner function referencing an outer variable (a "free variable"), it creates a `cell` object.
- The cell object lives on the heap and contains a pointer to the variable's value (`cell_contents`).
- The inner function stores a tuple of these cell objects in its `__closure__` attribute, allowing it to read and mutate the outer variable across independent calls.

---

### Q4: Why is `@functools.wraps` essential when writing custom decorators?
**Model Answer:**
- When a function is wrapped by a decorator, the decorator returns a new wrapper function.
- Without `@functools.wraps`, the decorated function loses its original identity: its `__name__`, `__doc__`, `__module__`, and `__annotations__` are replaced by those of the inner `wrapper` function.
- This breaks introspection, automated documentation generators (Sphinx), debuggers, IDE tooltips, and testing frameworks.
- Applying `@functools.wraps(original_func)` to the wrapper automatically copies all metadata from the original function onto the wrapper.

---

### Q5: What is the late-binding closure trap in Python loops?
**Model Answer:**
- In Python, closures capture variables by **reference (name binding)**, not by value at the moment the closure is created.
- In a loop like `funcs = [lambda: i for i in range(3)]`, all lambdas capture the identical variable name `i`.
- When the functions are called later, the loop has already completed, and `i` has its final value `2`. Therefore, calling every function returns `2`.
- Solution: Force early binding using default argument evaluation: `lambda i=i: i`. Because default arguments are evaluated when the lambda is defined, each function captures the current iteration value.

---

### Q6: What are positional-only (`/`) and keyword-only (`*`) parameters, and why are they used?
**Model Answer:**
- Introduced in PEP 570 (Python 3.8), parameters before `/` are **positional-only**; callers cannot pass them as `name=value`.
- Parameters after a bare `*` (or after `*args`) are **keyword-only**; callers must pass them explicitly using `name=value`.
- Use cases:
  - Positional-only parameters prevent API consumers from depending on internal parameter names, allowing maintainers to rename parameters in future releases without breaking backwards compatibility.
  - Keyword-only parameters enforce clarity at the call site for boolean flags or configuration options (e.g. `open_connection(timeout=30)` instead of `open_connection(30)`).

---

### Q7: Does Python support Tail-Call Optimization (TCO), and what happens during unbounded recursion?
**Model Answer:**
- Python **does not** support Tail-Call Optimization (TCO). Guido van Rossum intentionally omitted TCO to preserve complete stack traces for debugging and inspection.
- Every recursive call creates a new stack frame (`PyFrameObject`) on the CPython call stack.
- To prevent C-level stack overflow crashes, Python imposes a recursion limit (default 1000).
- If recursive depth exceeds this limit, Python raises `RecursionError: maximum recursion depth exceeded`.
- Algorithms requiring deep recursion should either be rewritten iteratively using an explicit list-based stack or memoized to avoid redundant frames.
