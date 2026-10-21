# 01. Python Basics: Complete Reference

---

## 1. Variables and Object References

### What it is
- In Python, variables are not memory containers that hold data values directly; they are symbolic name labels (references or pointers) bound to objects in memory.
- Dynamic typing means you do not declare a variable's data type upfront; the type is an intrinsic attribute of the object itself, not the reference label.
- Assignment (`=`) binds a name in the current scope's namespace to a specific object address in heap memory.

### Why it matters
- Prevents redundant data duplication because multiple names can reference the exact same underlying object in memory.
- Dictates how mutation affects programs: mutating an object through one reference reflects across all references pointing to that exact object.
- Eliminates manual pointer management while retaining pointer-like reference behavior, preventing buffer overflows and segmentation faults.

### How it works (internals, if relevant)
- Every Python object is represented under the hood by a C structure called `PyObject` (or `PyVarObject` for variable-length items).
- `PyObject` contains at least two mandatory fields:
  - `ob_refcnt`: an integer tracking the number of active references pointing to this object.
  - `ob_type`: a pointer to the object's type descriptor struct (`PyTypeObject`), which defines allowed operations, size, and methods.
- When executing `x = 500`, CPython allocates a `PyLongObject` on the heap, initializes its value to 500, sets `ob_refcnt = 1`, and adds the key-value pair `('x', <pointer to 500>)` into the local namespace dictionary (`locals()`).

### Common mistakes / gotchas
- Assuming `b = a` copies the data: if `a` points to a mutable object (like a list), mutating `b` silently mutates `a` as well.
- Confusing variable re-assignment (`a = [1, 2]`) with in-place mutation (`a.append(3)`): re-assignment updates the pointer to a new object, leaving previous objects intact.
- Attempting to use a variable before assignment, triggering an `UnboundLocalError` or `NameError`.

### Connects to
- Memory Management (Topic 09) for reference counting mechanics, garbage collection, and object identity (`id()`, `is` vs `==`).
- Functions (Topic 02) for pass-by-object-reference parameter passing.

---

## 2. Primitive & Built-in Data Types

### What it is
- The core built-in data types in Python:
  - `int`: Signed integers with arbitrary precision (unlimited digits, constrained only by available host RAM).
  - `float`: Double-precision floating-point numbers conforming to the IEEE 754 standard (64-bit: 1 sign bit, 11 exponent bits, 53 mantissa bits).
  - `bool`: Subclass of `int` representing truth values (`True` equals 1, `False` equals 0).
  - `complex`: Numbers with real and imaginary floating-point components written as `z = a + bj`.
  - `NoneType`: A singleton type represented by `None`, signaling absence of a value or default uninitialized state.

### Why it matters
- Choosing the right primitive ensures arithmetic precision, numerical stability, and predictable conditional branching.
- Knowing numeric limits avoids silent overflow bugs commonly encountered in languages like C/Java (e.g., Python integers will never overflow to negative values).

### How it works (internals, if relevant)
- In CPython, `int` is represented via variable-length arrays of 30-bit digits (or 15-bit on 32-bit platforms) inside `PyLongObject`. Arithmetic operations dynamically reallocate more digits as the number grows.
- CPython caches small integers in the range `[-5, 256]` in a global lookup array at startup. Any reference to an integer in this range reuses the identical cached `PyObject` singleton pointer.
- `float` values are susceptible to binary fraction representation limits (e.g., `0.1 + 0.2 != 0.3` because `0.1` and `0.2` cannot be expressed as exact binary fractions).

### Common mistakes / gotchas
- Testing exact equality on floating-point numbers (`0.1 + 0.2 == 0.3` evaluates to `False`); use `math.isclose()` instead.
- Subclass trap: `isinstance(True, int)` is `True` because `bool` inherits from `int`.
- Writing `None = 5` raises `SyntaxError` because `None` is a reserved keyword and an immutable singleton.

### Connects to
- Type Casting (subtopic 4 below) and Python Memory Management (Topic 09).

---

## 3. Python Operators

### What it is
- Constructs that instruct the Python interpreter to perform specific mathematical, logical, relational, or bit-level operations:
  - **Arithmetic**: `+`, `-`, `*`, `/` (true float division), `//` (floor division), `%` (modulo), `**` (exponentiation).
  - **Comparison**: `==`, `!=`, `<`, `<=`, `>`, `>=`.
  - **Logical**: `and`, `or`, `not` (short-circuit boolean operators).
  - **Bitwise**: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT / bitwise inversion), `<<` (left shift), `>>` (right shift).
  - **Assignment**: Simple `=` and compound `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`, plus the walrus operator `:=`.
  - **Identity**: `is`, `is not` (checks memory address equality).
  - **Membership**: `in`, `not in` (checks membership within containers/iterables).

### Why it matters
- Form the foundational building blocks of all computational logic, state transitions, and branching conditions.
- Operators possess strict precedence rules that determine expression evaluation order without ambiguous behavior.

### How it works (internals, if relevant)
- Operators invoke special dunder methods on operands: `a + b` invokes `a.__add__(b)` (or `b.__radd__(a)` if `a` does not implement it).
- `and` and `or` use **short-circuit evaluation**:
  - `expr1 and expr2`: if `expr1` is falsy, it immediately returns `expr1` without evaluating `expr2`. If truthy, it returns `expr2`.
  - `expr1 or expr2`: if `expr1` is truthy, it immediately returns `expr1` without evaluating `expr2`. If falsy, it returns `expr2`.
- Python modulo `%` always takes the sign of the divisor (unlike C/C++, where `%` truncates towards zero): `-7 % 3 == 2` in Python, whereas `-7 % 3 == -1` in C.

### Common mistakes / gotchas
- Using `==` instead of `is` when comparing against `None`. PEP 8 dictates `x is None` because `==` can be overridden by `__eq__`.
- Chained comparison surprises: `1 < x < 10` is evaluated as `(1 < x) and (x < 10)`, evaluating `x` only once.
- Bitwise precedence: Bitwise operators (`&`, `|`, `^`) have lower precedence than comparison operators (`<`, `==`), so `x & 1 == 0` evaluates as `x & (1 == 0)`. Always parenthesize: `(x & 1) == 0`.

### Connects to
- Conditionals (subtopic 6) and OOP Magic Methods (Topic 04, e.g., `__add__`, `__eq__`).

---

## 4. Type Casting (Implicit vs Explicit)

### What it is
- **Implicit type casting (type coercion)**: Python automatically promotes operands to a common compatible type without user intervention (e.g., `int + float` results in `float`).
- **Explicit type casting**: The programmer explicitly transforms an object into another type using constructor functions like `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()`.
- **Truthiness**: Every Python object has an implicit boolean value evaluated via `bool(obj)`:
  - Falsy: `False`, `None`, `0`, `0.0`, `0j`, `""`, `[]`, `()`, `{}`, `set()`, `range(0)`.
  - Truthy: Any non-zero number, non-empty string, or non-empty container.

### Why it matters
- Python is strongly typed: it will never implicitly convert types across incompatible boundaries (e.g., `"5" + 2` raises a `TypeError`, unlike JavaScript).
- Proper type casting prevents runtime bugs when processing external raw inputs (strings from files, network sockets, or CLI).

### How it works (internals, if relevant)
- `bool(x)` internally invokes `x.__bool__()`. If `__bool__` is not implemented, Python falls back to `x.__len__()` (returning `False` if 0, `True` if > 0). If neither exists, the object evaluates to `True`.
- `int("123")` parses characters digit-by-digit in base 10 (or a specified radix), allocating a new `PyLongObject`.

### Common mistakes / gotchas
- Attempting `int("12.34")` directly raises `ValueError`; it must first be cast to `float` then to `int`: `int(float("12.34"))`.
- Assuming non-empty string `"False"` is falsy: `bool("False")` evaluates to `True` because the string is non-empty.
- Using `int()` on floats truncates towards zero; it does not perform standard arithmetic rounding (use `round()` instead).

### Connects to
- Object-Oriented Programming (Topic 04) for implementing `__int__`, `__float__`, and `__bool__` on custom classes.

---

## 5. Input and Output Formatting

### What it is
- **Input**: `input(prompt)` pauses execution, reads a line of text from standard input (`sys.stdin`) until a newline is encountered, and returns it as a `str`.
- **Output**: `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)` converts objects to strings via `str()` and writes them to standard output.
- **String Formatting Mechanisms**:
  - `%`-formatting (printf style): legacy, C-style format strings (`"%s is %d" % ("Alice", 30)`).
  - `str.format()`: introduced in Python 2.6 / 3.0 (`"{} is {}".format("Alice", 30)`).
  - Formatted String Literals (**f-strings**): introduced in Python 3.6 (`f"{name} is {age}"`), evaluated at runtime.

### Why it matters
- F-strings are significantly faster than `%`-formatting and `.format()` because CPython optimizes them directly into specialized bytecode instructions (`FORMAT_VALUE` and `BUILD_STRING`).
- Proper output control (`sep`, `end`, `flush`) is crucial for command-line tools, progress bars, and streaming loggers.

### How it works (internals, if relevant)
- `print()` writes to the buffer of `sys.stdout`. By default, standard output is line-buffered when connected to a terminal and block-buffered when redirected to a file or pipe.
- Setting `flush=True` forces an immediate OS-level `write()` call, bypassing the stream buffer.
- F-strings support conversion flags (`!r` for `repr()`, `!s` for `str()`, `!a` for `ascii()`) and format specifiers (e.g., `f"{val:.2f}"`, `f"{num:>10}"`, `f"{date:%Y-%m-%d}"`, and Python 3.8+ debugging syntax `f"{x=}"`).

### Common mistakes / gotchas
- Forgetting that `input()` always returns a string, leading to string concatenation bugs instead of arithmetic addition: `"10" + "20" == "1020"`.
- Missing `flush=True` in loops using `print(..., end="")` for progress bars, causing delayed or missing terminal output until loop completion.
- Reusing variable names or expressions with backslashes inside f-string expressions in Python versions prior to 3.12.

### Connects to
- File Handling (Topic 06) for standard I/O redirection and stream buffers.

---

## 6. Conditionals & Branching

### What it is
- Mechanisms to control the execution flow based on runtime boolean conditions:
  - `if`, `elif`, `else` blocks.
  - **Ternary conditional operator**: `x = value_if_true if condition else value_if_false`.
  - **Structural Pattern Matching** (`match-case`), introduced in Python 3.10: pattern-based branching matching values, sequences, mappings, or object structures with optional guards (`if`).

### Why it matters
- Provides deterministic decision paths in software.
- `match-case` replaces complex nested `if-elif-else` chains and manual type/structure unpacking with declarative, readable patterns.

### How it works (internals, if relevant)
- Bytecode execution: `if` compiles to `POP_JUMP_FORWARD_IF_FALSE` or `POP_JUMP_BACKWARD_IF_FALSE`. The interpreter evaluates the condition's truthiness and updates the instruction pointer.
- `match-case` does not simply compare values like a C `switch`; it performs destructuring, sequence matching, and binding simultaneously via `MATCH_SEQUENCE`, `MATCH_MAPPING`, and `MATCH_CLASS` bytecode ops.

### Common mistakes / gotchas
- Using assignment `=` instead of equality `==` inside an `if` condition (syntax error unless using walrus operator `:=`).
- Overusing deeply nested `if-elif-else` instead of guard clauses or dictionary dispatching.
- In `match-case`, using a bare variable name like `case x:` acts as a catch-all wildcard that binds the value to `x`, instead of checking equality with an existing variable `x` (use `case _` for discard or literal/attribute match).

### Connects to
- Loops (subtopic 7 below) and Exception Handling (Topic 05) for control flow.

---

## 7. Loops and Flow Control

### What it is
- Iteration constructs:
  - `for item in iterable:` traverses items yielded by any object implementing the iterable protocol.
  - `while condition:` repeatedly executes as long as the boolean condition remains truthy.
  - `break`: immediately terminates the innermost enclosing loop.
  - `continue`: skips the remainder of the current iteration and jumps to the next cycle.
  - `pass`: a null statement placeholder where syntax requires a code block.
  - **Loop `else` clause**: executes only if the loop completes normally (i.e. did not terminate early via a `break` statement).

### Why it matters
- Python does not have a traditional C-style index-based `for(int i=0; i<n; i++)` loop; all `for` loops in Python iterate over sequences/iterables directly.
- The `else` clause eliminates the need for boolean flag variables when searching through collections for an element.

### How it works (internals, if relevant)
- When a `for` loop runs on iterable `obj`, CPython compiles bytecode `GET_ITER`, which calls `iter(obj)` to obtain an iterator object.
- Each iteration executes `FOR_ITER`, which calls `next(iterator)`.
- When `next()` raises `StopIteration`, CPython traps the exception internally and jumps to the loop's `else` block (if present) or proceeds past the loop.

### Common mistakes / gotchas
- Modifying a list while iterating over it (e.g., removing elements in `for x in my_list: my_list.remove(x)` causes skipped elements because the internal index counter increments regardless of deletions).
- Misunderstanding the loop `else` block: expecting it to run when a loop breaks, whereas it runs exclusively when the loop does NOT break.
- Creating infinite `while` loops due to missing condition increment/decrement statements.

### Connects to
- Iterators and Generators (Topic 11) for under-the-hood iteration mechanics and custom iterables.

---

## 8. String Methods and Formatting

### What it is
- In Python, strings (`str`) are immutable sequences of Unicode code points.
- Core string capabilities:
  - **Indexing & Slicing**: `s[start:stop:step]` with negative indices supported.
  - **Transformation**: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.capitalize()`, `.title()`.
  - **Inspection**: `.startswith()`, `.endswith()`, `.find()`, `.index()`, `.isalpha()`, `.isdigit()`, `.isalnum()`.
  - **Splitting & Joining**: `.split(sep)`, `.rsplit()`, `.splitlines()`, and `sep.join(iterable)`.

### Why it matters
- Text processing is ubiquitous in software engineering (data ingestion, parsing protocols, web scraping, sanitization).
- String immutability guarantees thread safety, safe dictionary keys (hash stability), and optimization opportunities.

### How it works (internals, if relevant)
- Immutability: any string operation that appears to modify a string actually allocates a completely new `PyUnicodeObject` in memory.
- CPython uses PEP 393 (Flexible String Representation): strings are stored using the most compact encoding suitable for the data:
  - 1 byte per character (Latin-1) if max code point < 256.
  - 2 bytes per character (UCS-2) if max code point < 65536.
  - 4 bytes per character (UCS-4) if code points exceed 65535 (e.g. emojis).
- Concatenating strings in a loop with `s += chunk` is $O(n^2)$ due to repeated buffer allocation; using `''.join(list_of_strings)` is $O(n)$ because Python pre-calculates total required memory upfront.

### Common mistakes / gotchas
- Calling `s.replace("a", "b")` and assuming `s` was modified in-place without capturing the returned new string (`s = s.replace(...)`).
- Using `.index()` which raises `ValueError` when a substring is missing, instead of `.find()` which returns `-1`, or using the `in` operator.
- Using `+` in large loops instead of `"".join()` leading to severe performance degradation.

### Connects to
- Regular Expressions (Topic 13) for complex pattern searching and text manipulation.

---

## 9. Lists

### What it is
- Lists (`list`) are ordered, mutable, heterogenous sequences of arbitrary Python objects.
- Supported operations:
  - Access: $O(1)$ random access by index (`lst[i]`).
  - Slicing: `lst[start:stop:step]` (creates a shallow copy of the specified slice).
  - Modification: `.append(x)`, `.extend(iterable)`, `.insert(idx, x)`, `.pop(idx)`, `.remove(val)`, `.reverse()`, `.sort()`, `clear()`.

### Why it matters
- The primary general-purpose workhorse sequence in Python used across virtually all applications.
- Provides dynamic resizing without requiring the programmer to manage manual memory buffers.

### How it works (internals, if relevant)
- Implemented as dynamic arrays of pointers (`PyObject**`) inside `PyListObject`.
- **Over-allocation strategy**: When the allocated buffer is full, CPython reallocates the array with an over-allocation growth factor: approximately `new_allocated = (newsize >> 3) + (newsize < 9 ? 3 : 6) + newsize`.
- Appending to the end of a list is $O(1)$ amortized time complexity.
- Inserting or deleting at index 0 or in the middle requires shifting all subsequent pointers by one position, costing $O(n)$ time.

### Common mistakes / gotchas
- Creating a list of lists via `[[0] * 3] * 3`: this repeats the *same* inner list reference three times. Modifying `grid[0][0] = 1` modifies all three rows! Use `[[0 for _ in range(3)] for _ in range(3)]` instead.
- Confusing `.sort()` (in-place modification, returns `None`) with `sorted()` (creates and returns a new sorted list, leaves original untouched).
- Using `lst.extend([item])` vs `lst.append([item])`: `.append()` adds the list as a single nested element; `.extend()` unpacks its elements into the outer list.

### Connects to
- Tuples (subtopic 10 below) for immutable counterparts and DSA Fundamentals (Topic 07).

---

## 10. Tuples

### What it is
- Tuples (`tuple`) are ordered, immutable sequences of heterogeneous Python objects.
- Key properties:
  - Defined using parentheses `(1, 2, 3)` or simply comma-separated values `1, 2, 3`.
  - Single-element tuple requires a trailing comma: `(42,)` (without comma, `(42)` is evaluated as an integer).
  - Supports sequence unpacking: `a, b, c = (1, 2, 3)` and extended unpacking with starred expression: `first, *middle, last = numbers`.

### Why it matters
- Immutability guarantees write-safety: once instantiated, elements cannot be added, removed, or replaced.
- Hashability: If all elements inside a tuple are hashable (immutable), the tuple itself is hashable and can be used as a dictionary key or set element.
- Memory efficiency: Tuples consume less memory than lists and are optimized by CPython.

### How it works (internals, if relevant)
- Implemented as a fixed-size `PyTupleObject` containing an array of `PyObject*` pointers.
- Because their size is fixed at instantiation, CPython does not allocate extra capacity for growth buffers.
- CPython maintains a free list of recycled tuple structures for tuples of length up to 20 to avoid repeated heap allocation overhead.
- Note: A tuple is immutable in its references, but if an element inside a tuple is mutable (e.g., a list `t = ([1, 2], 3)`), the contents of that list can still be mutated!

### Common mistakes / gotchas
- Forgetting the trailing comma for single-element tuples: `x = ("hello")` creates a `str`, not a `tuple`. Must be `x = ("hello",)`.
- Attempting in-place addition on a mutable item inside a tuple: `t = ([1, 2], 3); t[0] += [4]` mutates the list but then raises `TypeError: 'tuple' object does not support item assignment` because `+=` attempts to re-assign the reference back to `t[0]`.
- Unpacking mismatch: `a, b = (1, 2, 3)` raises `ValueError: too many values to unpack`.

### Connects to
- Functions (Topic 02) for returning multiple values and `*args` packing.

---

## 11. Sets

### What it is
- A set (`set` and immutable `frozenset`) is an unordered collection of unique, hashable Python objects.
- Syntax: `{1, 2, 3}`, or `set()` for an empty set (`{}` creates an empty dictionary).
- Core mathematical operations:
  - Union: `a | b` or `a.union(b)`
  - Intersection: `a & b` or `a.intersection(b)`
  - Difference: `a - b` or `a.difference(b)`
  - Symmetric Difference: `a ^ b` or `a.symmetric_difference(b)`
  - Subset / Superset: `a <= b`, `a >= b`

### Why it matters
- Membership testing (`x in my_set`) runs in average $O(1)$ time complexity compared to $O(n)$ in lists or tuples.
- Eliminates duplicate entries from collections effortlessly with `list(set(items))` (note: does not preserve order).

### How it works (internals, if relevant)
- Implemented using a hash table similar to dictionaries, but storing only keys without associated values (`PySetObject`).
- When an object is added, Python computes its hash code via `hash(obj)`. The hash determines the bucket index.
- If a hash collision occurs, CPython resolves it using open addressing with quadratic probing / perturbation.
- Only **hashable** objects (objects with a fixed hash code across their lifetime, implementing `__hash__` and `__eq__`) can be added to a set. Mutable objects like lists or dicts cannot be set elements.

### Common mistakes / gotchas
- Creating an empty set with `{}`: this creates an empty `dict`. To create an empty set, you must use `set()`.
- Adding unhashable types: `{ [1, 2] }` raises `TypeError: unhashable type: 'list'`.
- Relying on set iteration order: sets are mathematically unordered; order is an implementation detail and may change between Python runs due to hash randomization (salt).

### Connects to
- Dictionaries (subtopic 12 below) and Python Memory Management (Topic 09).

---

## 12. Dictionaries

### What it is
- A dictionary (`dict`) is a mutable mapping structure storing key-value pairs (`{key: value}`).
- Properties:
  - Keys must be unique and hashable.
  - Values can be any arbitrary Python object.
  - Guaranteed to preserve insertion order (standard language feature since Python 3.7).
- Methods: `.get(key, default)`, `.keys()`, `.values()`, `.items()`, `.pop(key)`, `.popitem()`, `.setdefault(key, default)`, `.update(other)`.

### Why it matters
- The cornerstone of Python itself: modules, classes, instances, and local/global variable namespaces are all implemented internally as dictionaries.
- Provides constant-time $O(1)$ average lookups, insertions, updates, and deletions by key.

### How it works (internals, if relevant)
- Since Python 3.6 (compact dict design):
  - Instead of a sparse table holding hash, key, and value in each entry, Python uses a dense array of entries: `entries = [ [hash, key_ptr, val_ptr], ... ]`.
  - A separate small hash indices table maps hash buckets to indices in the dense `entries` table.
  - This architecture reduces memory footprint by 20–25% and naturally preserves insertion order.
- Dictionary views: `.keys()`, `.values()`, and `.items()` return dynamic view objects that reflect changes made to the dictionary in real-time without copying data.

### Common mistakes / gotchas
- Direct key access `d[key]` on a non-existent key raises `KeyError`. Use `d.get(key, default)` or `collections.defaultdict` instead.
- Modifying a dictionary while iterating over it: `for k in d: del d[k]` raises `RuntimeError: dictionary changed size during iteration`. Iterate over a list copy instead: `for k in list(d): del d[k]`.
- Using mutable keys: dictionaries require immutable keys. If an object is mutated after being used as a key, its hash code changes, making it permanently inaccessible in the hash table.

### Connects to
- Comprehensions (subtopic 13 below) and Data Structures from Scratch (Topic 16).

---

## 13. Comprehensions (List, Dict, Set)

### What it is
- A concise, declarative syntactic construct to build new collections by transforming and filtering elements from an existing iterable:
  - **List comprehension**: `[expr for item in iterable if condition]`
  - **Set comprehension**: `{expr for item in iterable if condition}`
  - **Dict comprehension**: `{k_expr: v_expr for item in iterable if condition}`
  - **Nested comprehensions**: `[val for row in matrix for val in row]`

### Why it matters
- Replaces verbose multi-line `for` loops and `append()` calls with clear, readable, single-line declarations.
- Faster execution: comprehensions run at C-speed in CPython because they emit specialized bytecode instructions (`LIST_APPEND`, `MAP_ADD`, `SET_ADD`) that bypass python-level function lookup overhead.

### How it works (internals, if relevant)
- In Python 3, list, set, and dict comprehensions execute in their own isolated local function scope. Loop variables do not leak into the surrounding scope (unlike Python 2).
- When a comprehension executes, CPython pre-allocates an accumulator and uses dedicated fast append instructions directly in the virtual machine loop.

### Common mistakes / gotchas
- Over-complicating comprehensions: nesting more than 2 loops or adding multiple nested ternary operators produces unreadable "spaghetti" code. If readability suffers, use a standard loop.
- Nesting order confusion: `[x for row in matrix for x in row]` mirrors the exact nesting order of traditional loops:
  ```python
  for row in matrix:
      for x in row:
          ...
  ```
- Confusing generator expressions with list comprehensions: `(x for x in data)` creates a lazy generator object, not a tuple or list.

### Connects to
- Functions (Topic 02) for functional equivalents (`map`, `filter`) and Iterators & Generators (Topic 11).
