# 02. Python Functions: Complete Reference

---

## 1. Function Declarations, Signatures, and Return Values

### What it is
- Functions in Python are first-class citizens declared using the `def` keyword followed by a function name, formal parameter list, and an indented body.
- Return values:
  - If an explicit `return <value>` is executed, the function immediately terminates and yields that value to the caller.
  - Multiple comma-separated values (`return x, y`) automatically pack into a single `tuple`.
  - If a function reaches the end of its block without a `return` or calls a bare `return`, it implicitly returns `None`.

### Why it matters
- Encapsulates reusable units of execution, fostering modularity, abstraction, and the DRY (Don't Repeat Yourself) principle.
- Being first-class objects means functions can be assigned to variables, passed as arguments to other functions, stored in data structures, and returned from other functions.

### How it works (internals, if relevant)
- When Python compiles a `def` block, it constructs a `code` object containing bytecode instructions, constants, and variable names (`co_code`, `co_consts`, `co_varnames`).
- At runtime, executing the `def` statement instantiates a `function` object (`PyFunctionObject`), binding the code object to the current module/scope namespace dictionary.
- Calling a function pushes a new stack frame (`PyFrameObject`) onto CPython's execution call stack, establishing a fresh local namespace.

### Common mistakes / gotchas
- Expecting a function to return a value when it only prints output (resulting in unintended `None` in callers).
- Overwriting built-in function names (e.g. defining `def list(): ...` shadows Python's built-in `list` constructor in that scope).
- Putting statements after `return`, which become unreachable dead code.

### Connects to
- Variable Scope and LEGB Rule (subtopic 5 below) and Call Stack execution in Recursion (subtopic 9).

---

## 2. Arguments & Parameters: Positional, Keyword, Positional-Only, and Keyword-Only

### What it is
- **Parameters**: Variable names listed in the function definition.
- **Arguments**: Actual values or references passed into the function upon invocation.
- Argument types:
  - **Positional arguments**: Bound to parameters by position/order from left to right.
  - **Keyword arguments**: Bound by explicit parameter name (`func(name="Alice")`), independent of position.
  - **Positional-only parameters** (Python 3.8+): Defined before a forward slash `/`. Cannot be passed as keyword arguments.
  - **Keyword-only parameters**: Defined after a bare asterisk `*` (or after `*args`). Must be passed explicitly by keyword.

### Why it matters
- Keyword arguments improve code clarity at call sites.
- Positional-only parameters prevent callers from coupling to internal parameter names that might change during refactoring.
- Keyword-only parameters enforce explicit intent and prevent ambiguous function calls (e.g. boolean flag arguments like `process_data(data, validate=True)`).

### How it works (internals, if relevant)
- CPython parses parameters using specialized slot layouts.
- Parameters before `/` are stored in `co_posonlyargcount`.
- Parameters between `/` and `*` are standard positional/keyword parameters counted in `co_argcount`.
- Parameters after `*` are stored in `co_kwonlyargcount`.
- The interpreter performs fast C-level validation of arguments before creating the local frame.

### Common mistakes / gotchas
- Passing a positional argument after a keyword argument (`func(a=1, 2)` raises `SyntaxError: positional argument follows keyword argument`).
- Supplying both positional and keyword arguments for the same parameter (`func(10, a=10)` raises `TypeError: got multiple values for argument 'a'`).
- Trying to pass a positional-only argument using its keyword name.

### Connects to
- Variadic arguments (subtopic 4 below).

---

## 3. Default Arguments & The Mutable Default Argument Trap

### What it is
- Parameters can specify default fallback values used when the caller omits corresponding arguments (`def connect(host="localhost", port=5432): ...`).
- Default values must always appear *after* parameters without defaults in the definition signature.

### Why it matters
- Simplifies APIs by making common configuration settings optional for the caller.
- However, misunderstanding default argument evaluation time is one of the single most infamous gotchas in all of Python.

### How it works (internals, if relevant)
- **Default arguments are evaluated once at function definition time**, when the `def` statement executes, NOT at function call time.
- The evaluated default object references are stored permanently in the function object's `__defaults__` tuple attribute (or `__kwdefaults__` dictionary).
- If a default argument is a mutable object (such as a `list`, `dict`, or `set`), all function calls that rely on the default share the **exact same mutable instance** across the entire lifetime of the program.

### Common mistakes / gotchas
- Defining `def append_to(item, target_list=[]): target_list.append(item); return target_list`. Every call without passing `target_list` mutates and accumulates into the identical list stored in `__defaults__`.
- **The Idiomatic Fix**: Always use `None` as the sentinel default value, and instantiate the mutable object inside the function body:
  ```python
  def append_to(item, target_list=None):
      if target_list is None:
          target_list = []
      target_list.append(item)
      return target_list
  ```

### Connects to
- Closures (subtopic 6) and Python Memory Management (Topic 09).

---

## 4. Variadic Arguments (`*args` and `**kwargs`)

### What it is
- Constructs allowing functions to accept an arbitrary, unspecified number of arguments:
  - `*args`: Packs extra positional arguments into a `tuple`.
  - `**kwargs`: Packs extra keyword arguments into a `dict`.
- Argument unpacking at call sites:
  - `*iterable` unpacks sequence elements into positional arguments.
  - `**dict` unpacks mapping pairs into keyword arguments.

### Why it matters
- Enables flexible function interfaces that accept variable arguments (e.g., `print(*items)`, `min()`, `max()`).
- Crucial for implementing transparent function wrappers, decorators, and subclass constructors that delegate unknown arguments up to parent classes (`super().__init__(*args, **kwargs)`).

### How it works (internals, if relevant)
- CPython sets flags in the function's code object: `CO_VARARGS` (0x0004) for `*args` and `CO_VARKEYWORDS` (0x0008) for `**kwargs`.
- When called, any excess positional arguments are allocated into a new `tuple` bound to the `args` parameter name.
- Any excess keyword arguments are inserted into a new `dict` bound to the `kwargs` parameter name.

### Common mistakes / gotchas
- Placing standard positional arguments after `*args` without making them keyword-only.
- Forgetting that inside the function body, the identifiers are referenced without asterisks: `args` is a tuple and `kwargs` is a dictionary.
- Passing duplicate keys when unpacking `**kwargs` that conflict with explicit keyword parameters.

### Connects to
- Decorators (subtopic 8 below) and OOP `super()` method calls (Topic 04).

---

## 5. Variable Scope and the LEGB Rule

### What it is
- Variable scope defines the visibility and lifetime of variable bindings within Python code blocks.
- **The LEGB Rule**: When resolving an identifier name, Python searches namespaces strictly in this order:
  1. **L — Local**: Names assigned inside the currently executing function.
  2. **E — Enclosing**: Names in the local scope of any enclosing/outer functions (closures).
  3. **G — Global**: Names assigned at the top level of the current module file, or declared with `global`.
  4. **B — Built-in**: Pre-loaded Python names (`len`, `range`, `ValueError`, etc.).
- **Scope Modifiers**:
  - `global <var>`: Binds the identifier in the local scope to the module-level global namespace.
  - `nonlocal <var>`: Binds the identifier to the nearest outer enclosing function namespace (excluding global).

### Why it matters
- Prevents functions from unintentionally corrupting variables outside their intended boundaries.
- Distinguishes modular local state from shared global application state.

### How it works (internals, if relevant)
- Python determines variable scope **at compile time**, not at runtime.
- If a variable is assigned anywhere within a function body without a `global` or `nonlocal` declaration, Python marks it as a local variable for the *entire* function.
- CPython optimizes local variable lookups via indexed array slots using `LOAD_FAST` bytecode, whereas global lookups require dictionary hashing via `LOAD_GLOBAL`.

### Common mistakes / gotchas
- **The `UnboundLocalError`**: Reading a global variable before assigning to it locally:
  ```python
  x = 10
  def foo():
      print(x) # Raises UnboundLocalError: local variable 'x' referenced before assignment!
      x = 20
  ```
  Because `x = 20` assigns to `x`, Python flagged `x` as local to `foo` at compile time.
- Overusing `global` variables, introducing hidden coupling and breaking concurrency safety.

### Connects to
- Closures (subtopic 6 below) and Concurrency (Topic 17).

---

## 6. First-Class Functions and Closures

### What it is
- **First-Class Functions**: Functions are standard objects that can be assigned to variables, passed as parameters, returned from functions, and stored in lists/dictionaries.
- **Closure**: A closure is an inner function that retains access to variables in its outer enclosing lexical scope even after the outer function has completed execution and returned.

### Why it matters
- Enables functional programming paradigms: higher-order functions, function factories, partial applications, and event handlers.
- Forms the foundational mathematical and linguistic prerequisite for Python **decorators**.
- Provides data hiding / state encapsulation without requiring full OOP class boilerplate.

### How it works (internals, if relevant)
- When an inner function references an enclosing variable (a "free variable"), CPython does not discard the outer frame's variable when the outer function returns.
- Instead, the free variable is wrapped in a special `cell` object stored in the inner function's `__closure__` attribute.
- Each cell contains `cell_contents` pointing to the object reference on the heap, keeping it alive across subsequent invocations.

### Common mistakes / gotchas
- **The Late-Binding Closure Trap in Loops**:
  ```python
  funcs = [lambda: i for i in range(3)]
  # Calling [f() for f in funcs] produces [2, 2, 2], NOT [0, 1, 2]!
  ```
  Because closures bind to the variable *name* `i`, not its value at creation. When the lambda executes later, `i` has reached 2.
- **Fix**: Bind default argument at creation time: `lambda i=i: i`.

### Connects to
- Decorators (subtopic 8 below) and OOP vs Closures (Topic 04).

---

## 7. Lambda Functions

### What it is
- Small, anonymous, inline functions created with the syntax `lambda arguments: single_expression`.
- Cannot contain statements, assignments, loops, or multiple expressions; automatically returns the evaluated result of the single expression.

### Why it matters
- Ideal for short, disposable callbacks passed as inline arguments to higher-order functions like `sorted(key=...)`, `map()`, `filter()`, and `min()`/`max()`.

### How it works (internals, if relevant)
- A lambda compiles to an ordinary code object with the name `<lambda>`.
- Identical in execution mechanics and performance to a standard function defined via `def`, except for having no formal statement body and carrying `<lambda>` in tracebacks.

### Common mistakes / gotchas
- Assigning a lambda to a variable (`f = lambda x: x * 2`). PEP 8 explicitly discourages this; use `def f(x): return x * 2` instead to preserve meaningful traceback identifiers.
- Trying to write multi-line complex logic or exception handling inside a lambda; if it exceeds one simple expression, use `def`.

### Connects to
- Iterators & Generators (Topic 11) and Comprehensions (Topic 01).

---

## 8. Decorators (Basic, Parameterized, and Class Decorators)

### What it is
- A decorator is a callable that takes a function as an input, wraps or transforms it, and returns a callable (wrapper).
- Syntactic sugar `@decorator` placed above a function definition:
  ```python
  @my_decorator
  def target(): ...
  # Equivalent to: target = my_decorator(target)
  ```
- **Parameterized Decorators**: Functions that take arguments and return a decorator (three nested functions).
- **Metadata Preservation**: Using `@functools.wraps(func)` copies the original function's name (`__name__`), docstring (`__doc__`), and annotations over to the wrapper.

### Why it matters
- Implements Aspect-Oriented Programming (AOP): separates cross-cutting concerns (logging, timing, authentication, caching, rate limiting, validation) from core business logic.
- Eliminates boilerplate repetition across dozens or hundreds of endpoint functions.

### How it works (internals, if relevant)
- When CPython compiles `@dec`, it invokes `dec(target)` immediately when the module is loaded and rebinds the symbol `target` to the returned wrapper.
- Decorator chaining:
  ```python
  @dec_a
  @dec_b
  def func(): ...
  # Evaluated from bottom to top: func = dec_a(dec_b(func))
  ```

### Common mistakes / gotchas
- Forgetting `@functools.wraps(func)` on the wrapper function: causes `func.__name__` to become `'wrapper'`, breaking introspective tools, debuggers, and test runners.
- Parameterized decorator nesting confusion: forgetting that a parameterized decorator requires an extra outer function layer to accept the parameters.
- Wrapper argument mismatches: always write wrappers as `def wrapper(*args, **kwargs): return func(*args, **kwargs)` to accept arbitrary function signatures.

### Connects to
- Context Managers (Topic 10) and Flask routes (Topic 20).

---

## 9. Recursion

### What it is
- A computational pattern where a function solves a problem by calling itself on smaller sub-problems.
- Mandatory components:
  1. **Base Case(s)**: Terminating conditions that return a value without making further recursive calls.
  2. **Recursive Step**: Calling the function with reduced/decomposed inputs progressing towards the base case.

### Why it matters
- Natural and elegant solution for hierarchical structures: trees, graphs, nested JSON, directory traversal, and divide-and-conquer algorithms (Merge Sort, Quick Sort).

### How it works (internals, if relevant)
- Each recursive call creates and pushes a new `PyFrameObject` onto the CPython call stack, consuming stack memory.
- CPython **does NOT perform Tail-Call Optimization (TCO)**.
- CPython sets a default recursion depth limit (typically 1000 frames) to prevent C-level stack overflow crashes.
- Exceeding the depth raises `RecursionError: maximum recursion depth exceeded`.
- Limit can be inspected with `sys.getrecursionlimit()` and modified with `sys.setrecursionlimit(n)`.

### Common mistakes / gotchas
- Missing or incorrectly bounded base cases, triggering infinite recursion and immediate `RecursionError`.
- Exponential time complexity on naive recursive solutions (e.g. naive Fibonacci $O(2^n)$) without memoization (`@functools.lru_cache`).
- Relying on recursion for deeply nested data that exceeds the recursion limit instead of using an explicit iterative stack.

### Connects to
- DSA Fundamentals (Topic 07) and Data Structures from Scratch (Topic 16).
