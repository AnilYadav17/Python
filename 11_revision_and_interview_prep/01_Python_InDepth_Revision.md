# Comprehensive Python In-Depth Revision Guide 🐍

> **Concept:** Python is an interpreted, high-level, dynamically-typed, garbage-collected programming language created by Guido van Rossum. It balances clean syntax and readability with immense power, multi-paradigm architecture (functional, object-oriented, procedural), and a rich ecosystem for systems programming, data engineering, web backends, and artificial intelligence.
>
> **Official Sources & References:**
> - Official Documentation: [docs.python.org/3](https://docs.python.org/3/)
> - Python Standard Library: [docs.python.org/3/library](https://docs.python.org/3/library/)
> - Python Language Reference: [docs.python.org/3/reference](https://docs.python.org/3/reference/)
> - Real Python Guides: [realpython.com](https://realpython.com/)
> - PEP 8 Style Guide: [peps.python.org/pep-0008](https://peps.python.org/pep-0008/)

---

## Table of Contents
1. [Core Fundamentals, Memory Model & Assignment](#1-core-fundamentals-memory-model--assignment)
2. [Data Types, Mutability & Type Conversions](#2-data-types-mutability--type-conversions)
3. [Strings & Text Manipulation (Methods, Formatting, Slicing)](#3-strings--text-manipulation)
4. [Data Structures In-Depth (List, Tuple, Set, Dict & Complexities)](#4-data-structures-in-depth)
5. [Control Flow, Structural Pattern Matching & Operators](#5-control-flow-structural-pattern-matching--operators)
6. [Functions, Scopes (LEGB), Closures & Lambdas](#6-functions-scopes-legb-closures--lambdas)
7. [Object-Oriented Programming (OOP) Complete Mastery](#7-object-oriented-programming-oop-complete-mastery)
8. [Iterators, Generators & Protocols (`yield`, `yield from`)](#8-iterators-generators--protocols)
9. [Decorators & Context Managers](#9-decorators--context-managers)
10. [Exception Handling, Debugging & Logging](#10-exception-handling-debugging--logging)
11. [File I/O, Encodings & Serialization (`pathlib`, JSON, CSV)](#11-file-io-encodings--serialization)
12. [Essential Standard Library Modules](#12-essential-standard-library-modules)
13. [Modern Python Typing & Type Hints](#13-modern-python-typing--type-hints)
14. [Concurrency & Asynchronous Programming (GIL, Threads, Multiprocessing, AsyncIO)](#14-concurrency--asynchronous-programming)
15. [Master Cheat Sheet, Edge Cases & Common Pitfalls](#15-master-cheat-sheet-edge-cases--common-pitfalls)

---

## 1. Core Fundamentals, Memory Model & Assignment

### The CPython Memory Model
In Python, **variables are names (pointers/labels) bound to objects stored on the heap**. Variables do not hold raw data; they hold memory references to a `PyObject` structure.

```
Variable Names (Stack / Symbol Table)            Heap Memory (PyObject)
+-------+                                     +---------------------------+
|   a   | ----------------------------------> | Type: int                 |
+-------+                                     | Ref Count: 2              |
|   b   | ----------------------------------> | Value: 1000               |
+-------+                                     +---------------------------+
```

Every `PyObject` in CPython contains at least:
1. `ob_refcnt`: Reference count for automatic memory management.
2. `ob_type`: Pointer to the object's type structure.
3. Actual payload/data (e.g., integer value, string buffer, array pointers).

### Dynamic Typing & Re-binding
Because variables are references, their associated type is determined by the object they currently point to at runtime.
```python
x = 42          # x references an integer object
print(type(x))  # <class 'int'>

x = "Antigravity"  # x now references a string object; the previous int's ref count drops
print(type(x))  # <class 'str'>
```

### Assignment Mechanics & Unpacking
```python
# Multiple Assignment
a, b, c = 10, 20, 30

# Chained Assignment (all point to the exact same object in memory)
x = y = z = [1, 2, 3]
x.append(4)
print(z)  # [1, 2, 3, 4] -> modifying through x affects z!

# In-place Swapping (uses tuple packing & unpacking internally)
a, b = b, a

# Extended Unpacking with Asterisk (*)
first, *middle, last = [1, 2, 3, 4, 5, 6]
print(first)   # 1
print(middle)  # [2, 3, 4, 5] (always unpacked into a list)
print(last)    # 6

# Walrus Operator (Assignment Expression := ) [Python 3.8+]
# Assigns a value to a variable within an expression
if (n := len("Hello World")) > 5:
    print(f"Length is {n}")  # Length is 11
```

### Identity (`is`) vs Equality (`==`)
- `==` calls `__eq__()` to evaluate **value equivalence**.
- `is` checks **memory identity** (whether `id(a) == id(b)`).

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # True: Identical contents
print(list1 is list2)  # False: Distinct heap objects
print(id(list1) == id(list2))  # False

# None check convention: ALWAYS use 'is' with singletons
value = None
if value is None:
    print("Value is None")
```

### Integer Caching & String Interning
CPython pre-allocates and caches small integers in the range `[-5, 256]`. Any variable bound to an integer in this range references the exact same shared singleton:
```python
x = 250
y = 250
print(x is y)  # True (small integer cache)

x = 1000
y = 1000
print(x is y)  # False (allocated as distinct objects outside interactive repl blocks)
```

---

## 2. Data Types, Mutability & Type Conversions

### Built-in Types Summary Table

| Type | Classification | Mutable? | Ordered? | Hashable? | Syntax / Construction |
|---|---|---|---|---|---|
| `int`, `float`, `complex` | Numeric | ❌ Immutable | N/A | ✅ Yes | `42`, `3.14`, `2 + 3j` |
| `bool` | Numeric (`int` subclass) | ❌ Immutable | N/A | ✅ Yes | `True`, `False` |
| `str` | Text Sequence | ❌ Immutable | ✅ Yes | ✅ Yes | `"hello"`, `'world'` |
| `bytes` | Binary Sequence | ❌ Immutable | ✅ Yes | ✅ Yes | `b"binary\x00"` |
| `bytearray` | Binary Sequence | ✅ **Mutable** | ✅ Yes | ❌ No | `bytearray(b"abc")` |
| `list` | Sequence | ✅ **Mutable** | ✅ Yes | ❌ No | `[1, 2, "apple"]` |
| `tuple` | Sequence | ❌ Immutable | ✅ Yes | ✅ If all elements hashable | `(1, 2, 3)` |
| `range` | Sequence | ❌ Immutable | ✅ Yes | ✅ Yes | `range(0, 10, 2)` |
| `set` | Set Collection | ✅ **Mutable** | ❌ No | ❌ No | `{1, 2, 3}` |
| `frozenset` | Set Collection | ❌ Immutable | ❌ No | ✅ Yes | `frozenset([1, 2, 3])` |
| `dict` | Mapping | ✅ **Mutable** | ✅ Yes (3.7+) | ❌ No | `{"key": "value"}` |
| `NoneType` | Singleton | ❌ Immutable | N/A | ✅ Yes | `None` |

### Mutability vs Immutability Internals
```python
# Immutability: Mutating an immutable object creates a completely new object
s = "python"
initial_id = id(s)
s += "3"
print(id(s) == initial_id)  # False: A new string object was created

# Mutability: Modifying an in-place container preserves object identity
nums = [1, 2, 3]
list_id = id(nums)
nums.append(4)
print(id(nums) == list_id)  # True: Modified in-place in memory
```

### Hashability Rules
An object is **hashable** if it has a hash value that never changes during its lifetime (`__hash__()`), and can be compared to other objects (`__eq__()`).
- Keys in a `dict` and elements in a `set` **must be hashable**.
- All immutable built-in types (`int`, `str`, `tuple`, `frozenset`) are hashable (provided their elements are hashable).
- Mutable types (`list`, `dict`, `set`) are **unhashable** and raise `TypeError: unhashable type`.

### Truth Value Testing (Truthiness)
The following evaluate to `False` in boolean contexts:
- Constants: `None`, `False`
- Zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
- Empty sequences and collections: `""`, `()`, `[]`, `{}`, `set()`, `range(0)`
- Any custom object whose `__bool__()` or `__len__()` returns `False` or `0`.
- **All other values evaluate to `True`.**

---

## 3. Strings & Text Manipulation

Strings in Python are immutable sequences of Unicode code points.

### Slicing Mechanics: `[start : stop : step]`
- `start`: Inclusive lower bound (default: `0`).
- `stop`: Exclusive upper bound (default: `len(sequence)`).
- `step`: Stride length. Negative step reverses traversal.

```python
s = "PythonDeveloper"

print(s[0:6])       # "Python"
print(s[6:])        # "Developer"
print(s[:])         # "PythonDeveloper" (full slice copy)
print(s[::2])       # "PtoDveoe" (every second character)
print(s[::-1])      # "repoleveDnohtyP" (reversed string)
print(s[-9:-3])     # "Develo" (negative index slicing)
```

### String Formatting Mastery (f-strings)
Introduced in Python 3.6, formatted string literals (`f"..."`) evaluate at runtime and provide maximum speed and precision.

```python
user = "antigravity"
score = 87.6543
count = 7

# 1. Floating-point precision & rounding
print(f"Score: {score:.2f}")  # "Score: 87.65"

# 2. Number formatting with thousand-separators & zero padding
large_num = 1_000_000
print(f"Count: {large_num:,}")  # "Count: 1,000,000"
print(f"Padded: {count:05d}")    # "Padded: 00007"

# 3. String padding and alignment
print(f"{'Header':^20}")        # Centered: "       Header       "
print(f"{'Left':<15}|")         # Left-aligned: "Left           |"
print(f"{'Right':>15}|")        # Right-aligned: "          Right|"

# 4. In-line expressions & debugging helper (Python 3.8+)
x, y = 10, 20
print(f"{x * y = }")            # Prints: "x * y = 200"

# 5. Percentage formatting
ratio = 0.856
print(f"{ratio:.1%}")           # "85.6%"
```

### Essential String Methods
```python
raw = "   data:engineer:python   "

# Cleaning whitespace
clean = raw.strip()             # "data:engineer:python"

# Splitting and Joining
parts = clean.split(":")        # ['data', 'engineer', 'python']
reconstructed = " -> ".join(parts) # "data -> engineer -> python"

# Searching and Verification
print("python".startswith("py"))    # True
print("12345".isdigit())            # True
print("alpha".isalpha())            # True
print("user_id".isidentifier())     # True

# Transformation
print("hello world".title())        # "Hello World"
print("ß".casefold())               # "ss" (aggressive lowercasing for caseless matching)
print("item_old".replace("old", "new")) # "item_new"
```

### Encoding and Decoding (Unicode & UTF-8)
```python
text = "Antigravity 🚀"
# Encode str to bytes (UTF-8 encoding)
encoded_bytes = text.encode("utf-8")
print(encoded_bytes)  # b'Antigravity \xf0\x9f\x9a\x80'

# Decode bytes back to str
decoded_text = encoded_bytes.decode("utf-8")
print(decoded_text)   # "Antigravity 🚀"
```

---

## 4. Data Structures In-Depth

### Big-O Time Complexity Comparison

| Operation | List (`list`) | Double-Ended Queue (`deque`) | Set (`set`) | Dictionary (`dict`) |
|---|---|---|---|---|
| **Index Access `a[i]`** | $O(1)$ | $O(N)$ | N/A | $O(1)$ average |
| **Append (Right)** | $O(1)$ amortized | $O(1)$ | $O(1)$ (`add`) | $O(1)$ average (`d[k] = v`) |
| **Append (Left)** | $O(N)$ (`insert(0, v)`) | $O(1)$ (`appendleft`) | N/A | N/A |
| **Pop (Right)** | $O(1)$ | $O(1)$ | $O(1)$ (`pop()`) | $O(1)$ (`pop(k)`) |
| **Pop (Left)** | $O(N)$ (`pop(0)`) | $O(1)$ (`popleft`) | N/A | N/A |
| **Lookup `x in s`** | $O(N)$ | $O(N)$ | $O(1)$ average | $O(1)$ average (keys) |
| **Delete `del a[i]`** | $O(N)$ | $O(N)$ | $O(1)$ average (`remove`) | $O(1)$ average |

---

### 1. Lists (`list`)
Lists are variable-length dynamic array buffers holding object references. CPython over-allocates extra capacity to ensure amortized $O(1)$ append operations.

```python
items = ["apple", "banana", "cherry"]

# Mutating Operations
items.append("date")              # O(1) amortized
items.insert(1, "blueberry")      # O(N): shifts subsequent elements right
items.extend(["elderberry", "fig"])# Appends iterable contents
items.remove("banana")            # O(N): searches and removes first occurrence
popped = items.pop()              # O(1): removes and returns last item
items.reverse()                   # In-place reversal: O(N)

# Sorting: Timsort algorithm (hybrid merge-insertion sort, O(N log N))
items.sort(key=len, reverse=True) # In-place sort by string length
sorted_copy = sorted(items)       # Returns a NEW sorted list

# List Comprehensions (Faster than explicit for-loops due to bytecode optimization)
squares = [x**2 for x in range(10) if x % 2 == 0]
# Nested List Comprehension (Matrix flattening)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [val for row in matrix for val in row]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 2. Tuples (`tuple`)
Tuples are fixed-size, immutable sequence containers. They use less memory than lists and allow memory re-use optimization in CPython.
```python
point = (10, 20)

# Single element tuple syntax REQUIREMENT: trailing comma
not_a_tuple = (42)    # int
single_tuple = (42,)  # tuple

# Named Tuples (readability without class overhead)
from collections import namedtuple
Coordinate = namedtuple("Coordinate", ["x", "y", "z"])
p = Coordinate(x=10, y=20, z=30)
print(p.x, p.y, p.z)  # 10 20 30
```

### 3. Sets (`set` and `frozenset`)
Sets are unordered collections of unique, hashable objects implemented using open-addressing hash tables.
```python
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Mathematical Set Operations
print(set_a | set_b)  # Union: {1, 2, 3, 4, 5, 6, 7, 8}
print(set_a & set_b)  # Intersection: {4, 5}
print(set_a - set_b)  # Difference: {1, 2, 3}
print(set_a ^ set_b)  # Symmetric Difference: {1, 2, 3, 6, 7, 8}

# Subset & Superset tests
print({1, 2}.issubset(set_a))  # True

# frozenset: Immutable set usable as dictionary keys or set elements
frozen = frozenset([1, 2, 3])
valid_dict = {frozen: "immutable_set_key"}
```

### 4. Dictionaries (`dict`)
Since Python 3.6/3.7, dictionaries maintain insertion order using a compact array table layout.
```python
user = {"id": 101, "name": "Aarav", "role": "Engineer"}

# Safe Retrieval & Defaults
role = user.get("role", "Guest")
department = user.setdefault("dept", "Core Engineering")  # Inserts if key absent

# View Objects (Dynamic reflections of dict state)
keys_view = user.keys()
values_view = user.values()
items_view = user.items()

# Dictionary Merging (Python 3.9+)
default_settings = {"theme": "light", "notifications": True}
user_settings = {"theme": "dark"}
final_settings = default_settings | user_settings  # {'theme': 'dark', 'notifications': True}
default_settings |= user_settings                  # In-place merge update

# Dict Comprehension
word_lengths = {word: len(word) for word in ["python", "code", "fast"]}
# {'python': 6, 'code': 4, 'fast': 4}
```

### 5. Specialized Data Structures (`collections` module)
```python
from collections import deque, defaultdict, Counter

# deque: O(1) append and pop on BOTH ends (ideal for queues and stacks)
queue = deque(["task1", "task2"])
queue.append("task3")         # Enqueue right
queue.appendleft("task0")     # Enqueue left
task = queue.popleft()        # Dequeue left -> "task0"

# defaultdict: Automatically initializes missing keys
grouping = defaultdict(list)
grouping["fruits"].append("apple")  # No KeyError raised!

# Counter: Frequency table for elements
counts = Counter("antigravity")
print(counts.most_common(2))  # [('a', 2), ('t', 2)]
```

---

## 5. Control Flow, Structural Pattern Matching & Operators

### Short-Circuit Evaluation (`and`, `or`)
Python's logical operators return the **value of the deciding operand**, not strictly a boolean:
```python
# 'or' returns the first truthy value or the last falsy value
val = None or "default"
print(val)  # "default"

# 'and' returns the first falsy value or the last truthy value
result = "valid" and 42
print(result)  # 42
```

### Conditional Expressions (Ternary Operator)
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
```

### Loop `else` Clauses
The `else` block executes **if and only if the loop terminates normally without encountering a `break` statement**.
```python
def find_prime(limit):
    for n in range(2, limit):
        for factor in range(2, int(n**0.5) + 1):
            if n % factor == 0:
                break
        else:
            # Executes only if inner loop ran to completion without break
            print(f"Found prime: {n}")

find_prime(10)  # Prints primes: 2, 3, 5, 7
```

### Iteration Helpers: `enumerate` and `zip`
```python
languages = ["Python", "Rust", "Go"]
for idx, lang in enumerate(languages, start=1):
    print(f"Rank {idx}: {lang}")

names = ["Alice", "Bob"]
scores = [95, 88]
# zip with strict=True raises ValueError on length mismatch (Python 3.10+)
for name, score in zip(names, scores, strict=True):
    print(f"{name} scored {score}")
```

### Structural Pattern Matching (`match` / `case`) [Python 3.10+]
Pattern matching inspects the structure and shape of data, extracts components, and applies guard conditions.

```python
def process_command(cmd):
    match cmd:
        # Literal pattern
        case "quit":
            return "Exiting system"

        # OR pattern
        case "start" | "restart":
            return "Booting service"

        # Sequence pattern with unpacking & wildcard
        case ["load", filename]:
            return f"Loading file: {filename}"
        case ["move", x, y] if x >= 0 and y >= 0:  # Guard condition
            return f"Moving to non-negative coordinate ({x}, {y})"

        # Mapping (dictionary) pattern
        case {"type": "notification", "msg": message}:
            return f"Alert: {message}"

        # Capture pattern with class structure
        case _:
            return "Invalid command"

print(process_command(["move", 10, 20]))  # "Moving to non-negative coordinate (10, 20)"
print(process_command({"type": "notification", "msg": "Build success"}))
```

---

## 6. Functions, Scopes (LEGB), Closures & Lambdas

### Anatomy of Function Parameters
Python allows strict separation between positional-only, regular, keyword-only, arbitrary positional (`*args`), and arbitrary keyword (`**kwargs`) parameters:

```python
#  Positional-Only   Regular     Keyword-Only
#       vvvv         vvvvvvvv        vvvv
def configure(host, port=8080, /, debug=False, *, timeout=30, **extra):
    return {
        "host": host, "port": port, "debug": debug,
        "timeout": timeout, "extra": extra
    }

# Valid calls:
configure("127.0.0.1", 9000, True, timeout=60, retries=3)
# configure(host="127.0.0.1")  # ❌ TypeError: host is positional-only!
# configure("127.0.0.1", 8080, True, 60) # ❌ TypeError: timeout is keyword-only!
```

### The Default Mutable Argument Trap
Default parameter values are **evaluated exactly once when the function definition is executed**, not at each invocation.

```python
# ❌ INCORRECT: The list persists across subsequent invocations!
def append_item(item, target_list=[]):
    target_list.append(item)
    return target_list

print(append_item(1))  # [1]
print(append_item(2))  # [1, 2] -- UNEXPECTED SHARED STATE!

# ✅ CORRECT: Use None as default sentinel
def append_item_safe(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

print(append_item_safe(1))  # [1]
print(append_item_safe(2))  # [2]
```

### Variable Scopes & The LEGB Rule

```
+--------------------------------------------------------+
| Built-in Scope (len, print, range, Exception)          |
|  +--------------------------------------------------+  |
|  | Global Scope (Module level variables, imports)   |  |
|  |  +--------------------------------------------+  |  |
|  |  | Enclosing Scope (Outer function closure)   |  |  |
|  |  |  +--------------------------------------+  |  |  |
|  |  |  | Local Scope (Inside active function) |  |  |  |
|  |  |  +--------------------------------------+  |  |  |
|  |  +--------------------------------------------+  |  |
|  +--------------------------------------------------+  |
+--------------------------------------------------------+
```

Resolution searches inward-to-outward: **L**ocal $\rightarrow$ **E**nclosing $\rightarrow$ **G**lobal $\rightarrow$ **B**uilt-in.

```python
count = 0  # Global

def outer():
    count = 10  # Enclosing
    def inner():
        nonlocal count  # Targets the enclosing scope variable
        count += 5
        print("Inner count:", count)
    inner()
    print("Outer count:", count)

outer()
# Inner count: 15
# Outer count: 15
```

### Closures & First-Class Functions
A **closure** occurs when a nested function retains access to variables from its enclosing scope even after the outer function has finished executing.

```python
def make_multiplier(factor):
    def multiplier(number):
        return number * factor  # 'factor' is a free variable retained in closure
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30
# Inspecting closure cell
print(double.__closure__[0].cell_contents)  # 2
```

### Lambda Functions & Higher-Order Functions
```python
# Lambda: Small anonymous expression
add = lambda x, y: x + y
print(add(4, 5))  # 9

# High-Order Functions: map, filter, reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, numbers))      # [2, 4, 6]
doubled = list(map(lambda n: n * 2, evens))              # [4, 8, 12]
total_sum = reduce(lambda acc, n: acc + n, doubled, 0)   # 24
```

---

## 7. Object-Oriented Programming (OOP) Complete Mastery

Python is fully object-oriented. Classes are blueprints, and classes themselves are instances of `type` (metaclasses).

### Anatomy of a Complete Class
```python
class BankAccount:
    """Represents a secure bank account with encapsulated transactions."""

    # Class Attribute (shared across all instances)
    bank_name = "Global Apex Bank"
    _account_counter = 1000

    def __init__(self, owner: str, initial_balance: float = 0.0):
        # Instance Attributes (unique to each instance)
        BankAccount._account_counter += 1
        self.account_id = BankAccount._account_counter
        self.owner = owner
        self._balance = initial_balance   # Protected by convention
        self.__secret_pin = "4321"        # Private (Name-mangled to _BankAccount__secret_pin)

    # 1. Instance Method (receives 'self')
    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    # 2. Property Getter & Setter (Pythonic Encapsulation)
    @property
    def balance(self) -> float:
        """Read-only balance property accessor."""
        return self._balance

    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Balance cannot be set to a negative value.")
        self._balance = value

    # 3. Class Method (receives 'cls', acts on class state or alternative constructor)
    @classmethod
    def create_corporate_account(cls, company_name: str, starting_grant: float):
        return cls(owner=company_name, initial_balance=starting_grant)

    # 4. Static Method (independent utility; receives neither self nor cls)
    @staticmethod
    def is_valid_account_number(acc_num: int) -> bool:
        return acc_num >= 1000
```

### Inheritance & Method Resolution Order (MRO)
Python supports multiple inheritance and resolves method dispatch using the **C3 Linearization Algorithm**.

```
       Animal
      /      \
   Mammal   Bird
      \      /
       Bat (Diamond Problem)
```

```python
class A:
    def execute(self):
        print("Executing in A")

class B(A):
    def execute(self):
        print("Executing in B")
        super().execute()

class C(A):
    def execute(self):
        print("Executing in C")
        super().execute()

class D(B, C):
    def execute(self):
        print("Executing in D")
        super().execute()

d = D()
d.execute()
# Output follows MRO:
# Executing in D
# Executing in B
# Executing in C
# Executing in A

print([cls.__name__ for cls in D.__mro__])
# ['D', 'B', 'C', 'A', 'object']
```

### Abstract Base Classes (ABCs)
Enforces an interface contract on child classes at instantiation time:
```python
from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def save(self, entity: dict) -> bool:
        """Persist entity to store."""
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> dict:
        """Fetch entity by primary key."""
        pass

class SQLiteRepository(BaseRepository):
    def save(self, entity: dict) -> bool:
        print("Saving to SQLite...")
        return True

    def get_by_id(self, entity_id: int) -> dict:
        return {"id": entity_id, "status": "active"}

# Attempting to instantiate BaseRepository directly raises TypeError
# repo = BaseRepository() # ❌ TypeError: Can't instantiate abstract class
```

### Essential Dunder (Magic) Methods

| Magic Method | Purpose | Invocation Trigger |
|---|---|---|
| `__init__(self, ...)` | Instance Initializer | `obj = MyClass()` |
| `__repr__(self)` | Unambiguous official representation | `repr(obj)`, Interactive REPL |
| `__str__(self)` | Readable string representation | `str(obj)`, `print(obj)` |
| `__eq__(self, other)` | Value equality | `obj == other` |
| `__hash__(self)` | Hash value computation | `hash(obj)`, key in `dict`/`set` |
| `__len__(self)` | Container length | `len(obj)` |
| `__getitem__(self, k)` | Index / Key lookup | `obj[k]` |
| `__setitem__(self, k, v)`| Index / Key assignment | `obj[k] = v` |
| `__call__(self, ...)` | Callable object instance | `obj()` |
| `__enter__` / `__exit__` | Context management | `with obj:` |

```python
class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector2D({self.x!r}, {self.y!r})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
print(v1 + v2)    # "(4, 6)"
print(repr(v1))   # "Vector2D(3, 4)"
print(len(v1))    # 5
```

### Modern Dataclasses (`@dataclass`) [Python 3.7+]
Automatically generates `__init__`, `__repr__`, `__eq__`, and ordering methods:
```python
from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class ServerConfig:
    host: str
    port: int = 8080
    tags: tuple = field(default_factory=tuple)

# frozen=True makes instances immutable and hashable
cfg = ServerConfig(host="localhost", tags=("web", "prod"))
print(cfg)  # ServerConfig(host='localhost', port=8080, tags=('web', 'prod'))
# cfg.port = 9000  # ❌ FrozenInstanceError!
```

### Memory Optimization with `__slots__`
By default, Python instances store attributes in a dynamic dictionary `self.__dict__`. Defining `__slots__` bypasses `__dict__`, preventing dynamic attribute creation and drastically reducing memory overhead when instantiating millions of objects:
```python
class FastPoint:
    __slots__ = ("x", "y")  # Eliminates instance __dict__
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## 8. Iterators, Generators & Protocols

### The Iterator Protocol
1. **Iterable**: An object with an `__iter__()` method that returns an iterator.
2. **Iterator**: An object with a `__next__()` method that returns the next item or raises `StopIteration`.

```python
class Countdown:
    """Custom iterator implementing the Iterator Protocol."""
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(3):
    print(num)  # 3, 2, 1
```

### Generators & Lazy Evaluation (`yield`)
Generators are functions that produce items lazily on demand, pausing execution and maintaining stack state between `yield` expressions.

```python
def fibonacci_sequence(limit: int):
    """Memory-efficient infinite or bounded Fibonacci generator."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

gen = fibonacci_sequence(5)
print(list(gen))  # [0, 1, 1, 2, 3]
```

### Advanced Generator Mechanics: `send()` and `yield from`
```python
# 1. Two-way communication with send()
def cumulative_sum():
    total = 0
    while True:
        val = yield total
        if val is None:
            break
        total += val

collector = cumulative_sum()
next(collector)         # Prime generator to first yield -> 0
print(collector.send(10)) # 10
print(collector.send(25)) # 35

# 2. Delegation with 'yield from'
def sub_stream():
    yield "A"
    yield "B"

def main_stream():
    yield 1
    yield from sub_stream()  # Delegates iteration transparently
    yield 2

print(list(main_stream()))  # [1, 'A', 'B', 2]
```

---

## 9. Decorators & Context Managers

### 1. Decorators Deep Dive
A decorator is a callable that takes a function/class as input, enhances its behavior, and returns a callable.

```python
import functools
import time

# Robust timing decorator preserving metadata
def execution_timer(func):
    @functools.wraps(func)  # Crucial: Preserves docstrings, name, type hints
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        print(f"[{func.__name__}] executed in {duration:.6f} seconds")
        return result
    return wrapper

@execution_timer
def compute_sum(n: int) -> int:
    """Computes arithmetic series sum."""
    return sum(range(n))

print(compute_sum(1_000_000))
print(compute_sum.__name__)  # 'compute_sum' (preserved by @functools.wraps)
```

### Decorators with Arguments (3-Layer Pattern)
```python
def retry(max_attempts: int = 3, delay: float = 0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    attempts += 1
                    if attempts == max_attempts:
                        raise err
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.1)
def unstable_network_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network blip!")
    return "Payload received"
```

### Class-Based Decorators
```python
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CallCounter
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
greet("Bob")
```

---

### 2. Context Managers (`with` statement)
Guarantees cleanup and resource reclamation regardless of exceptions.

```python
# Custom Class-Based Context Manager
class ManagedResource:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"[ENTER] Acquiring resource: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[EXIT] Releasing resource: {self.name}")
        if exc_type is not None:
            # Handle specific error or log it
            print(f"Exception intercepted: {exc_val}")
            return True  # Returning True suppresses the exception
        return False     # False propagates exceptions upwards

with ManagedResource("ConnectionPool") as res:
    print(f"Working with {res.name}")
```

### Generator-Based Context Manager (`contextlib`)
```python
from contextlib import contextmanager

@contextmanager
def temporary_flag(obj, attribute, temporary_value):
    original_value = getattr(obj, attribute)
    setattr(obj, attribute, temporary_value)
    try:
        yield obj
    finally:
        # Guarantee restoration even on error
        setattr(obj, attribute, original_value)
```

---

## 10. Exception Handling, Debugging & Logging

### Python Exception Hierarchy
```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception (All user-facing exceptions inherit from here)
      ├── ArithmeticError (ZeroDivisionError, OverflowError)
      ├── LookupError (IndexError, KeyError)
      ├── TypeError
      ├── ValueError
      └── OSError (FileNotFoundError, PermissionError)
```

### The Full `try / except / else / finally` Flow
```python
def parse_and_divide(input_str: str, denominator: int) -> float:
    try:
        val = int(input_str)
        result = val / denominator
    except ValueError as ve:
        print(f"Parsing error: {ve}")
        raise
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return 0.0
    else:
        # Runs ONLY if the try block completed without raising any exception
        print("Calculation completed cleanly.")
        return result
    finally:
        # ALWAYS runs, even if return or unhandled exception occurs
        print("Cleanup operations finished.")
```

### Custom Exceptions & Explicit Exception Chaining
```python
class ApplicationError(Exception):
    """Base custom application error."""
    pass

class DatabaseConnectionError(ApplicationError):
    def __init__(self, message: str, host: str):
        super().__init__(f"{message} (Host: {host})")
        self.host = host

# Explicit Chaining with 'from'
try:
    raise ConnectionRefusedError("Port 5432 closed")
except ConnectionRefusedError as original_error:
    # Preserves full root-cause traceback via __cause__
    raise DatabaseConnectionError("DB Down", host="db.internal") from original_error
```

### Exception Groups [Python 3.11+]
```python
# Handling concurrent/multiple exceptions
try:
    raise ExceptionGroup("Batch tasks failed", [
        ValueError("Invalid format"),
        TypeError("Expected string")
    ])
except* ValueError as eg:
    print(f"Caught ValueErrors: {eg.exceptions}")
except* TypeError as eg:
    print(f"Caught TypeErrors: {eg.exceptions}")
```

### Debugging with `pdb` & `breakpoint()`
```python
def complex_algorithm(data):
    processed = [d * 2 for d in data]
    # breakpoint() drops into interactive PDB session (Python 3.7+)
    # Commands: 'n' (next), 's' (step into), 'c' (continue), 'p <var>' (print), 'q' (quit)
    # breakpoint()
    return sum(processed)
```

### Production Structured Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s"
)
logger = logging.getLogger("auth_service")

logger.info("Service initialized")
logger.warning("Rate limit reaching threshold: %d req/min", 85)
```

---

## 11. File I/O, Encodings & Serialization

### Safe File Reading & Writing
Always specify `encoding="utf-8"` and use context managers:
```python
# Writing UTF-8 Text
with open("dataset.txt", mode="w", encoding="utf-8") as f:
    f.write("Line 1: Python Revision\nLine 2: Fast & Clean\n")

# Reading Line-by-Line (Memory Efficient Generator)
with open("dataset.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### Modern Path Handling with `pathlib`
Replaces legacy `os.path` functions with an object-oriented API:
```python
from pathlib import Path

# Path construction using / operator
base_dir = Path.cwd() / "project_data"
base_dir.mkdir(parents=True, exist_ok=True)

target_file = base_dir / "records.json"

# Convenience Read/Write operations
target_file.write_text('{"status": "ok"}', encoding="utf-8")
content = target_file.read_text(encoding="utf-8")

# Path Inspection
print("Exists:", target_file.exists())
print("File suffix:", target_file.suffix)  # ".json"
print("Parent directory:", target_file.parent)
```

### JSON Serialization
```python
import json

payload = {
    "user_id": 42,
    "active": True,
    "scores": [98.5, 92.0],
    "metadata": None
}

# Python dict -> JSON formatted string
json_str = json.dumps(payload, indent=2, sort_keys=True)

# JSON formatted string -> Python dict
parsed = json.loads(json_str)
```

### CSV Processing with `csv.DictReader` & `csv.DictWriter`
```python
import csv
from io import StringIO

csv_buffer = StringIO()
fieldnames = ["id", "username", "role"]

# Writing CSV
writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({"id": 1, "username": "anil", "role": "admin"})

# Reading CSV
csv_buffer.seek(0)
reader = csv.DictReader(csv_buffer)
for row in reader:
    print(row["username"], "->", row["role"])
```

---

## 12. Essential Standard Library Modules

### 1. `itertools` (High-Performance Iteration)
```python
import itertools

# Infinite counters & cycles
counter = itertools.count(start=10, step=2)  # 10, 12, 14...
print([next(counter) for _ in range(3)])     # [10, 12, 14]

# Combinatorics
items = ["A", "B", "C"]
permutations = list(itertools.permutations(items, 2))  # [('A', 'B'), ('A', 'C'), ...]
combinations = list(itertools.combinations(items, 2))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
cartesian = list(itertools.product([1, 2], ["x", "y"])) # [(1, 'x'), (1, 'y'), ...]

# Chain: Flatten iterables seamlessly
combined = list(itertools.chain([1, 2], [3, 4], [5]))   # [1, 2, 3, 4, 5]
```

### 2. `functools` (Functional Programming Tools)
```python
from functools import lru_cache, partial

# 1. Least Recently Used (LRU) Cache Memoization
@lru_cache(maxsize=128)
def expensive_fib(n: int) -> int:
    if n < 2:
        return n
    return expensive_fib(n - 1) + expensive_fib(n - 2)

# 2. partial: Freezes specific function arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(square(5))  # 25
print(cube(5))    # 125
```

### 3. `re` (Regular Expressions)
```python
import re

text = "Contact: support@example.com or admin@antigravity.io"
email_pattern = r"([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

# findall: Returns all matches
matches = re.findall(email_pattern, text)
# [('support', 'example.com'), ('admin', 'antigravity.io')]

# sub: Search and replace
censored = re.sub(email_pattern, "[REDACTED]", text)
print(censored)  # "Contact: [REDACTED] or [REDACTED]"
```

### 4. `datetime` & `time`
```python
from datetime import datetime, timezone, timedelta

# Aware UTC Datetime
now_utc = datetime.now(timezone.utc)
formatted = now_utc.strftime("%Y-%m-%d %H:%M:%S %Z")

# Parsing strings to datetimes
dt = datetime.strptime("2026-10-24 15:30:00", "%Y-%m-%d %H:%M:%S")
future = dt + timedelta(days=7, hours=3)
```

---

## 13. Modern Python Typing & Type Hints

Type hints improve code documentation, IDE auto-completion, and static verification with `mypy`.

```python
from typing import Optional, Union, Callable, TypeVar, Generic
from collections.abc import Sequence, Mapping

# Modern Union Syntax with Pipe (|) [Python 3.10+]
def parse_id(raw: int | str) -> str:
    return str(raw).strip()

# Optional / Nullable Types (T | None)
def find_user(user_id: int) -> dict[str, str] | None:
    if user_id == 1:
        return {"name": "Admin"}
    return None

# Callable signature: Callable[[ArgTypes], ReturnType]
def execute_callback(data: list[int], action: Callable[[int], bool]) -> list[int]:
    return [x for x in data if action(x)]

# Generics & TypeVar
T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

int_stack: Stack[int] = Stack()
int_stack.push(10)
```

---

## 14. Concurrency & Asynchronous Programming

### Concurrency vs Parallelism in Python

```
Concurrency (AsyncIO / Threading)              Parallelism (Multiprocessing)
+------------------------------------+        +------------------------------------+
| Core 0: [Task 1] -> [Task 2] -> .. |        | Core 0: [Task 1 Running Full Speed]|
+------------------------------------+        +------------------------------------+
(Interleaved cooperative or preemptive)       | Core 1: [Task 2 Running Full Speed]|
                                              +------------------------------------+
```

### The Global Interpreter Lock (GIL)
CPython uses a **Global Interpreter Lock (GIL)** to protect memory management and reference counts (`ob_refcnt`) from race conditions.
- **I/O-Bound Tasks** (network calls, disk reading, database queries): The GIL is **released** during system calls. `threading` or `asyncio` is optimal.
- **CPU-Bound Tasks** (image processing, heavy mathematics, machine learning inference): The GIL prevents multiple threads from executing Python bytecode simultaneously on multiple cores. Use `multiprocessing` to bypass the GIL.

---

### 1. Multithreading (`threading`) - Best for I/O Concurrency
```python
import threading
import time

lock = threading.Lock()
shared_counter = 0

def worker():
    global shared_counter
    for _ in range(100_000):
        with lock:  # Protect shared state with mutex lock
            shared_counter += 1

threads = [threading.Thread(target=worker) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print("Shared counter:", shared_counter)  # Exactly 400,000
```

---

### 2. Multiprocessing (`multiprocessing`) - True Parallelism for CPU Work
Spawns separate OS processes, each with its own Python interpreter, heap, and independent GIL.
```python
from multiprocessing import Pool

def heavy_computation(x: int) -> int:
    return sum(i * i for i in range(x))

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(heavy_computation, [1_000_000, 2_000_000, 3_000_000])
        print("Parallel results calculated:", len(results))
```

---

### 3. Asynchronous Programming (`asyncio`) - Event-Driven Cooperative Multitasking
A single thread runs an **event loop** that pauses (`await`) during I/O operations and resumes when data is ready.

```python
import asyncio

async def fetch_api(endpoint: str, delay: int) -> dict:
    print(f"Fetching {endpoint}...")
    await asyncio.sleep(delay)  # Non-blocking pause; hands control back to event loop
    print(f"Received {endpoint}")
    return {"endpoint": endpoint, "status": 200}

async def main():
    # Run coroutines concurrently
    results = await asyncio.gather(
        fetch_api("/users", 2),
        fetch_api("/orders", 1),
        fetch_api("/inventory", 1)
    )
    print("All responses gathered:", len(results))

# Execution entrypoint
if __name__ == "__main__":
    asyncio.run(main())
```

---

## 15. Master Cheat Sheet, Edge Cases & Common Pitfalls

### 1. Late-Binding Closures in Loops
```python
# ❌ BUG: All functions reference the same final variable 'i'!
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]

# ✅ FIX: Bind default argument at definition time
funcs_fixed = [lambda i=i: i for i in range(3)]
print([f() for f in funcs_fixed])  # [0, 1, 2]
```

### 2. Modifying a List While Iterating Over It
```python
# ❌ BUG: Modifying size alters iteration indices, skipping elements!
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)

# ✅ FIX 1: Iterate over a shallow slice copy
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers[:]:
    if n % 2 == 0:
        numbers.remove(n)

# ✅ FIX 2 (Best): List comprehension
numbers = [n for n in numbers if n % 2 != 0]
```

### 3. Floating-Point Precision
Due to IEEE 754 binary representation, floats cannot represent base-10 fractions exactly.
```python
print(0.1 + 0.2 == 0.3)  # False! (0.30000000000000004)

# Solutions:
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True

from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True
```

### 4. Chained Comparison Evaluation
In Python, `a < b < c` translates to `(a < b) and (b < c)`, with `b` being evaluated only once:
```python
x = 5
print(1 < x < 10)     # True
print(10 < x < 20)    # False
```

### 5. Variable Shadowing Built-ins
Never name variables after built-in types or functions (`id`, `list`, `dict`, `str`, `max`, `min`, `sum`):
```python
# ❌ DON'T DO THIS:
# list = [1, 2, 3]
# new_list = list("abc") # ❌ TypeError: 'list' object is not callable!
```

### 6. `finally` Return Value Overwrite
A `return` inside a `finally` block suppresses and overrides any previous `return` or unhandled exception raised in `try` or `except`:
```python
def check_finally():
    try:
        return "TRY_RETURN"
    finally:
        return "FINALLY_OVERRIDE"

print(check_finally())  # "FINALLY_OVERRIDE"
```

### 7. Shallow Copy vs Deep Copy
```python
import copy

nested = [[1, 2], [3, 4]]

shallow = copy.copy(nested)
shallow[0].append(99)
print(nested[0])  # [1, 2, 99] -> Outer copied, but inner elements shared!

deep = copy.deepcopy(nested)
deep[0].append(100)
print(nested[0])  # [1, 2, 99] -> Completely isolated recursive copy
```

### 8. `__bool__` vs `__len__` Truthiness Evaluation
When evaluating the truth value of an object:
1. Python checks for `__bool__()`.
2. If `__bool__()` is not defined, Python falls back to `__len__()` (0 is `False`, >0 is `True`).
3. If neither is defined, the object is considered `True`.

---

*End of Comprehensive Python In-Depth Revision Guide. Master these principles to excel in interviews, architecture design, and production engineering.*
