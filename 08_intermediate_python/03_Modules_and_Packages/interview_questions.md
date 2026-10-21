# 03. Modules & Packages — Interview & Viva Questions

---

### Q1: Describe the step-by-step process of how Python imports a module.
**Model Answer:**
1. **Cache Check (`sys.modules`)**: Python checks if the module has already been imported and cached in the `sys.modules` dictionary. If found, the existing module reference is returned immediately ($O(1)$).
2. **Finding (`sys.meta_path` & Finders)**: If not cached, Python queries finder objects configured in `sys.meta_path` to locate the module spec across paths listed in `sys.path` (current directory, `PYTHONPATH`, standard library, `site-packages`).
3. **Loading**: Python uses an appropriate loader (e.g. `SourceFileLoader`) to read the file, compile it to bytecode (`.pyc`), allocate a new module object, and execute the module's top-level code within the module's own dictionary namespace.
4. **Caching**: The module object is inserted into `sys.modules`, and the symbol is bound to the importing scope's namespace.

---

### Q2: What causes a circular import in Python, and how can it be resolved?
**Model Answer:**
- A circular import occurs when Module A imports Module B while Module B imports Module A at module top-level.
- When Module A begins executing, it enters `sys.modules` in an uncompleted state. When it reaches `import B`, Python pauses A and begins executing B. When B tries to import a specific attribute from A (`from A import foo`), `foo` has not yet been defined in A because A's execution was paused. Python raises `ImportError: cannot import name ... from partially initialized module`.
- **Solutions**:
  1. **Refactor**: Extract shared types, classes, or utilities into a separate, third leaf module (e.g. `models.py` or `common.py`).
  2. **Deferred / Local Import**: Move `from A import foo` inside the specific function in B where `foo` is needed, deferring the import until runtime when A has completely finished initializing.

---

### Q3: What is the purpose of `__init__.py` and the `__all__` variable in a package?
**Model Answer:**
- `__init__.py` marks a directory as a regular Python package and executes automatically upon importing the package. It is used to initialize package-level state and expose a consolidated public API interface.
- `__all__` is a list of strings defined at the module or package level. When a user executes wildcard import `from package import *`, Python imports *only* the names explicitly listed in `__all__`. If `__all__` is omitted, `import *` imports all names that do not begin with an underscore `_`.

---

### Q4: Why is `collections.deque` preferred over a standard `list` for implementing queues?
**Model Answer:**
- Python's `list` is implemented as a contiguous dynamic array of pointers. While appending and popping from the *right* end is $O(1)$ amortized, removing an item from the *front* (`list.pop(0)`) requires shifting all $n-1$ remaining pointers in memory, costing $O(n)$ time complexity. Processing $n$ elements yields $O(n^2)$ total runtime.
- `collections.deque` (double-ended queue) is implemented as a doubly-linked list of fixed-size blocks (64 elements each). Both `append()` and `popleft()` operate by adjusting block pointers in constant $O(1)$ time regardless of collection size.

---

### Q5: What is the difference between naive and aware `datetime` objects, and what error occurs if they are mixed?
**Model Answer:**
- A **naive** `datetime` object does not contain timezone information (`tzinfo=None`); it simply represents numbers for year, month, day, hour, etc., without reference to a geographical timezone or UTC.
- An **aware** `datetime` object contains an explicit timezone implementation (e.g. `datetime.timezone.utc` or a `zoneinfo.ZoneInfo` instance).
- Attempting to compare, subtract, or calculate a `timedelta` between a naive datetime and an aware datetime raises `TypeError: can't subtract offset-naive and offset-aware datetimes`. Server systems should always standardize on UTC-aware timestamps.

---

### Q6: Why should you never use the `random` module for generating passwords or authentication tokens?
**Model Answer:**
- Python's `random` module uses the **Mersenne Twister** algorithm (MT19937), which is a deterministic pseudo-random number generator designed for modeling and simulations, not cryptography.
- An attacker who observes 624 consecutive 32-bit outputs from the Mersenne Twister can completely reconstruct its internal 2.5 KB state array and accurately predict all past and future generated values.
- For security-sensitive applications (session tokens, password resets, crypto keys), developers must use the `secrets` module, which draws non-deterministic entropy from operating system CSPRNG sources (`/dev/urandom`).

---

### Q7: What are the primary advantages of `itertools` functions over standard loops and list comprehensions?
**Model Answer:**
- **Memory Efficiency (Lazy Evaluation)**: `itertools` functions return iterator objects that compute elements on-demand one by one during iteration, requiring $O(1)$ auxiliary memory even when processing millions of items or infinite streams.
- **C-Level Performance**: The algorithms (`chain`, `islice`, `permutations`, `product`) are implemented in optimized C, executing with significantly less interpreter overhead than equivalent nested Python loops.
- **Composable Pipelines**: Iterators can be chained together into memory-frugal streaming data pipelines.
