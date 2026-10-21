# Python Mastery: Comprehensive Progress Tracker

Use this checklist to track your revision and mastery of every concept across the curriculum. Check items off as you complete them (`- [x]`).

---

## 01. Basics
- [ ] **Variables & Object References**: Names, memory addresses, dynamic typing, PyObject reference semantics
- [ ] **Data Types**: Integers (arbitrary precision), Floats (IEEE 754), Booleans, Complex numbers, NoneType
- [ ] **Operators**: Arithmetic, Comparison, Logical (`and`, `or`, `not`), Bitwise (`&`, `|`, `^`, `~`, `<<`, `>>`), Assignment, Identity (`is`, `is not`), Membership (`in`, `not in`)
- [ ] **Type Casting**: Implicit promotion, Explicit casting (`int()`, `float()`, `str()`, `bool()`), Falsy vs Truthy values
- [ ] **Input & Output**: `input()`, `print()` parameters (`sep`, `end`, `file`, `flush`), stdout flushing
- [ ] **Conditionals**: `if`, `elif`, `else`, nested conditions, ternary operator (`x if cond else y`), Structural Pattern Matching (`match-case`)
- [ ] **Loops & Flow Control**: `for` loops, `while` loops, `break`, `continue`, `pass`, `for-else` and `while-else` constructs
- [ ] **String Methods & Formatting**: Immutability, slicing `[start:stop:step]`, methods (`split`, `join`, `strip`, `replace`, etc.), f-strings, `str.format()`, `%`-formatting
- [ ] **Lists**: Dynamic array internals, indexing, slicing, methods (`append`, `extend`, `insert`, `pop`, `remove`, `sort`), list mutation
- [ ] **Tuples**: Immutability, tuple packing, sequence unpacking, extended unpacking (`*rest`), single-element tuple syntax
- [ ] **Sets**: Hash table backend, uniqueness, hashability requirement, mathematical set operations (union `|`, intersection `&`, difference `-`, symmetric difference `^`)
- [ ] **Dictionaries**: Key-value mapping, hash table lookup $O(1)$, key immutability, insertion order preservation, methods (`get`, `items`, `keys`, `values`, `setdefault`, `update`)
- [ ] **Comprehensions**: List comprehensions, Set comprehensions, Dict comprehensions, nested comprehensions, filtering conditionals

---

## 02. Functions
- [ ] **Function Declarations & Returns**: `def` keyword, return values, multiple return values as tuples, implicit `None`
- [ ] **Arguments & Parameters**: Positional arguments, keyword arguments, positional-only (`/`), keyword-only (`*`)
- [ ] **Default Arguments**: Evaluation at definition time, mutable default argument pitfall and the `None` sentinel pattern
- [ ] **Variadic Arguments**: Packing and unpacking with `*args` (positional tuple) and `**kwargs` (keyword dict)
- [ ] **Variable Scope & LEGB Rule**: Local, Enclosing, Global, Built-in namespaces; `global` and `nonlocal` keywords
- [ ] **Closures**: Nested functions, lexical scoping, free variables, `__closure__` cell objects
- [ ] **Lambda Functions**: Anonymous single-expression functions, limitations, functional pairing (`map`, `filter`, `sorted`)
- [ ] **Decorators**: First-class function mechanics, function decorators, `@functools.wraps` metadata preservation, parameterized decorators, decorator chaining
- [ ] **Recursion**: Recursive structure, base conditions, call stack execution, stack overflow prevention, `sys.getrecursionlimit()`

---

## 03. Modules & Packages
- [ ] **Importing Mechanics**: `import module`, `from module import name`, aliasing `as`, module caching in `sys.modules`, search path in `sys.path`
- [ ] **Package Structure & `__init__.py`**: Regular packages vs namespace packages, package initialization, exposing APIs via `__all__`
- [ ] **Building Custom Packages**: Folder layout, relative vs absolute imports (`.`, `..`), top-level execution traps
- [ ] **Package Management with `pip`**: Installing packages, dependency freezing (`pip freeze`), requirements files, wheel binaries
- [ ] **Standard Library — `os` & `sys`**: File path manipulation, environment variables, working directories, system exit, CLI arguments (`sys.argv`)
- [ ] **Standard Library — `math` & `random`**: Math constants and functions, pseudo-random number generation, seeding, choice, shuffle, sampling
- [ ] **Standard Library — `datetime`**: `date`, `time`, `datetime`, `timedelta`, timezone-aware vs naive timestamps, `strftime` and `strptime`
- [ ] **Standard Library — `collections`**: `namedtuple`, `deque` (double-ended queue), `Counter`, `defaultdict`, `OrderedDict`
- [ ] **Standard Library — `itertools`**: Infinite iterators (`count`, `cycle`, `repeat`), terminating iterators (`accumulate`, `chain`, `compress`, `islice`), combinatoric generators (`product`, `permutations`, `combinations`)

---

## 04. Object-Oriented Programming (OOP)
- [ ] **Classes & Instances**: Class definition, object instantiation, instance attributes vs class attributes, `self` parameter
- [ ] **Constructor Mechanics**: `__new__` (object allocator) vs `__init__` (object initializer)
- [ ] **Method Types**: Instance methods (`self`), Class methods (`@classmethod` with `cls`), Static methods (`@staticmethod`)
- [ ] **Encapsulation**: Access conventions: public, protected (`_attr`), private (`__attr` name mangling), property getters/setters (`@property`)
- [ ] **Inheritance**: Single inheritance, multilevel inheritance, multiple inheritance, Method Resolution Order (MRO, C3 linearization), `super()` mechanics
- [ ] **Polymorphism**: Duck typing ("if it quacks like a duck"), method overriding, operator overloading
- [ ] **Abstraction**: Abstract Base Classes (`abc.ABC`), `@abstractmethod` decorator, interface contract enforcement
- [ ] **Dunder / Magic Methods**: String representation (`__str__`, `__repr__`), comparison (`__eq__`, `__lt__`), container protocol (`__len__`, `__getitem__`), callable objects (`__call__`)
- [ ] **Composition vs Inheritance**: Is-A vs Has-A relationship modeling, loose coupling, delegation pattern

---

## 05. Exception Handling
- [ ] **Exception Control Flow**: `try`, `except`, `else` (runs on success), `finally` (always runs for cleanup)
- [ ] **Exception Hierarchy**: `BaseException` vs `Exception`, catching multiple specific exceptions, avoiding broad/bare `except:`
- [ ] **Custom Exception Classes**: Subclassing `Exception`, custom error attributes, standardized error formatting
- [ ] **Exception Chaining**: Explicit chaining (`raise NewException from orig_exc`), implicit chaining, inspecting `__cause__` and `__context__`
- [ ] **Best Practices & Robustness**: EAFP (Easier to Ask for Forgiveness than Permission) vs LBYL (Look Before You Leap), re-raising exceptions (`raise`), logging exceptions

---

## 06. File Handling
- [ ] **File Modes & Open Semantics**: Modes (`r`, `w`, `a`, `x`, `b`, `+`), text vs binary decoding, encoding specification (`utf-8`)
- [ ] **Reading & Writing Operations**: `read()`, `readline()`, `readlines()`, `write()`, `writelines()`, file pointer navigation (`seek()`, `tell()`)
- [ ] **Context Management**: Resource safety with `with open(...)`, automatic file closing on exceptions
- [ ] **Structured Text Data — CSV**: `csv.reader`, `csv.writer`, `csv.DictReader`, `csv.DictWriter`, delimiters and quote handling
- [ ] **Structured Text Data — JSON**: Serialization (`dump`, `dumps`), deserialization (`load`, `loads`), custom encoders via `json.JSONEncoder`
- [ ] **Path Operations**: Legacy `os.path` vs modern `pathlib.Path`, path resolution, file existence, parent directories, glob patterns

---

## 07. Data Structures & Algorithms Fundamentals
- [ ] **Array & String Fundamentals**: In-place mutation, prefix sums, palindrome checking, anagram detection
- [ ] **Searching Algorithms**: Linear search $O(n)$, Binary search $O(\log n)$ (iterative and recursive), Python `bisect` module
- [ ] **Sorting Algorithms**: Bubble Sort $O(n^2)$, Merge Sort $O(n \log n)$ (divide and conquer), Quick Sort $O(n \log n)$ average
- [ ] **Recursion Patterns**: Call stack trace, Fibonacci, Factorial, Subsets generation
- [ ] **Two-Pointer Technique**: Left and right pointers (sum pairs, container with most water), slow and fast pointers (cycle detection)
- [ ] **Sliding Window Technique**: Fixed window size (max sum subarray of size k), dynamic window size (longest substring without repeating characters)

---

## 08. Time Complexity & Big-O Analysis
- [ ] **Asymptotic Analysis**: Big-O ($O$), Big-Omega ($\Omega$), Big-Theta ($\Theta$), worst-case vs average-case vs best-case
- [ ] **Complexity Classes**: $O(1)$ Constant, $O(\log n)$ Logarithmic, $O(n)$ Linear, $O(n \log n)$ Linearithmic, $O(n^2)$ Quadratic, $O(2^n)$ Exponential
- [ ] **Space Complexity**: Memory allocation, auxiliary space, recursive call stack space
- [ ] **Python Operation Complexities**: Time complexity of list, dict, and set operations in CPython
- [ ] **Amortized Analysis**: Dynamic array resizing and $O(1)$ amortized append
- [ ] **Code Profiling**: Measuring real runtime with `timeit`, profiling bottlenecks with `cProfile`

---

## 09. Python Memory Management
- [ ] **Reference Counting**: `PyObject` structure, `ob_refcnt`, increment and decrement triggers, deallocation
- [ ] **Cyclic Reference Detection**: Why reference counting fails on circular references, Generational Garbage Collector
- [ ] **Generational GC Mechanics**: Generation 0, 1, 2; collection frequency, collection thresholds, `gc` module API
- [ ] **Reference Inspection**: `sys.getrefcount()`, weak references with `weakref`
- [ ] **Object Identity vs Value Equality**: `id()` memory address, `is` pointer comparison vs `==` `__eq__` equality
- [ ] **CPython Interning**: Small integer caching (-5 to 256), string interning
- [ ] **Object Copying**: Assignment vs Shallow Copy (`copy.copy()`) vs Deep Copy (`copy.deepcopy()`)

---

## 10. Context Managers (Deep Dive)
- [ ] **Context Manager Protocol**: The `__enter__` and `__exit__` dunder methods
- [ ] **Exception Handling in `__exit__`**: Exception types, values, tracebacks; suppressing exceptions with `return True`
- [ ] **Contextlib Utilities**: Creating context managers via generators with `@contextmanager`, `contextlib.closing`, `contextlib.suppress`, `contextlib.ExitStack`
- [ ] **Real-World Patterns**: Database connection pools, execution timers, file locks, atomic file writes

---

## 11. Iterators & Generators
- [ ] **The Iterable & Iterator Protocol**: `__iter__()` returning iterator, `__next__()` returning items and raising `StopIteration`
- [ ] **Custom Iterator Classes**: Designing stateful custom iterators, iterator exhaustion
- [ ] **Generators & `yield`**: Generator functions, execution pause/resume, frame state persistence
- [ ] **Generator Expressions**: Memory savings compared to list comprehensions, lazy pipelines
- [ ] **Advanced Generator Communication**: Passing data into generators with `.send()`, handling `.throw()`, cleanup with `.close()`
- [ ] **Itertools Power Tools**: Infinite streams, grouping with `groupby()`, chained iterations

---

## 12. Testing
- [ ] **Testing Foundations**: Unit tests, integration tests, Test-Driven Development (TDD) cycle (Red-Green-Refactor)
- [ ] **The `unittest` Framework**: `TestCase`, test lifecycle (`setUp`, `tearDown`, `setUpClass`, `tearDownClass`), assertions
- [ ] **The `pytest` Framework**: Test discovery conventions, assertion rewriting, running tests
- [ ] **Pytest Fixtures**: Fixture definitions, dependency injection, fixture scopes, teardown logic with `yield`
- [ ] **Parametrization**: Running a single test against multiple inputs using `@pytest.mark.parametrize`
- [ ] **Mocking with `unittest.mock`**: `Mock` vs `MagicMock`, `@patch` decorator, mocking network requests, asserting call arguments

---

## 13. Regular Expressions
- [ ] **Regex Foundations**: Pattern matching engine, regex compilation with `re.compile()`
- [ ] **Regex Functions**: `re.search()`, `re.match()`, `re.fullmatch()`, `re.findall()`, `re.finditer()`, `re.sub()`, `re.split()`
- [ ] **Metacharacters & Character Classes**: `^`, `$`, `.`, `\d`, `\D`, `\w`, `\W`, `\s`, `\S`, ranges `[a-z]`
- [ ] **Quantifiers**: Greedy quantifiers (`*`, `+`, `?`, `{m,n}`) vs Lazy quantifiers (`*?`, `+?`, `??`)
- [ ] **Grouping & Capturing**: Capture groups `(...)`, named capture groups `(?P<name>...)`, non-capturing groups `(?:...)`
- [ ] **Lookaround Assertions**: Positive lookahead `(?=...)`, negative lookahead `(?!...)`, positive lookbehind `(?<=...)`, negative lookbehind `(?<!...)`
- [ ] **Real-World Patterns**: Email validation, phone extraction, markdown/HTML parsing, log line scraping

---

## 14. Type Hints & Typing
- [ ] **Type Annotation Foundations**: PEP 484, type hints syntax for variables, parameters, and return types
- [ ] **Built-in & Generic Collections**: Modern built-in generics (`list[str]`, `dict[str, int]`, `tuple[int, ...]`)
- [ ] **Union and Optional**: `Union[A, B]` and modern `A | B`, `Optional[T]` as shorthand for `T | None`
- [ ] **Advanced Typing Types**: `Any`, `Callable`, `Literal`, `Final`, `TypeVar`, `Generic`
- [ ] **Structural Typing with Protocols**: `typing.Protocol` for compile-time duck typing
- [ ] **Structured Dictionaries**: `typing.TypedDict`, type narrowing with `TypeGuard` / `isinstance`

---

## 15. Virtual Environments & Packaging
- [ ] **Virtual Environments**: Need for isolation, `venv` module creation (`python -m venv .venv`), activation scripts
- [ ] **Environment Architecture**: `pyvenv.cfg`, isolated `site-packages`, `sys.prefix` vs `sys.base_prefix`
- [ ] **Dependency Management**: `requirements.txt`, pin operators (`==`, `>=`, `~=`), transitive dependencies
- [ ] **Modern Packaging Standards**: PEP 517 / 518, declarative build configuration in `pyproject.toml`
- [ ] **Package Distribution**: Source distribution (`sdist`) vs Binary wheel distribution (`bdist_wheel`), publishing with `twine`

---

## 16. Data Structures from Scratch
- [ ] **Singly Linked List**: Node class, append, prepend, delete by value, search, reverse
- [ ] **Doubly Linked List**: Bidirectional pointers (`prev`, `next`), constant-time tail operations
- [ ] **Stack**: Array-based and node-based LIFO data structure, push, pop, peek, is_empty
- [ ] **Queue**: FIFO data structure, enqueue, dequeue, circular array vs linked nodes
- [ ] **Hash Map**: Direct hashing, collision handling via separate chaining, dynamic load factor rehashing
- [ ] **Binary Search Tree (BST)**: Node insertion, binary search property, tree traversals (In-order, Pre-order, Post-order, Level-order)
- [ ] **Graph**: Adjacency list representation, Breadth-First Search (BFS), Depth-First Search (DFS)

---

## 17. Concurrency
- [ ] **Concurrency Fundamentals**: Concurrency vs Parallelism, I/O-bound vs CPU-bound tasks
- [ ] **The Global Interpreter Lock (GIL)**: What GIL is, why it exists in CPython, implications for threading
- [ ] **Multithreading**: `threading.Thread`, thread synchronization with `threading.Lock`, thread pools (`concurrent.futures.ThreadPoolExecutor`)
- [ ] **Multiprocessing**: `multiprocessing.Process`, bypassing the GIL, process communication with `Queue`, `ProcessPoolExecutor`
- [ ] **Asynchronous Programming (`asyncio`)**: The event loop, coroutines (`async def`), `await` syntax, `asyncio.gather()`, `asyncio.run()`

---

## 18. Databases with Python
- [ ] **Python DB-API 2.0 (PEP 249)**: Connection objects, Cursor objects, SQL execution, fetching results (`fetchone`, `fetchall`)
- [ ] **SQLite Integration (`sqlite3`)**: In-memory and disk-based databases, table schema creation, CRUD operations
- [ ] **SQL Injection Prevention**: Parameterized queries with `?` or named placeholders, avoiding string interpolation
- [ ] **Transaction Control**: Atomic commit and rollback, auto-commit modes, handling integrity errors
- [ ] **Object-Relational Mapping (ORM)**: Introduction to SQLAlchemy, declarative models, mapping classes to tables, Session querying

---

## 19. Git & GitHub for Real Projects
- [ ] **Git Architecture**: Working tree, Staging area, Git repository, object model (blobs, trees, commits, tags)
- [ ] **Branching & Workflows**: Creating branches, switching branches, Feature-branch workflow, Gitflow
- [ ] **Merging & Rebasing**: Fast-forward merge, 3-way merge commits, interactive rebasing (`git rebase -i`), squashing commits
- [ ] **Merge Conflict Resolution**: Conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), manual resolution, staging and completing rebase
- [ ] **Commit Hygiene**: Conventional Commits standard (`feat:`, `fix:`, `docs:`, `refactor:`), imperative mood commit messages
- [ ] **GitHub Collaboration**: Forking, cloning remotes, creating upstream tracking, opening Pull Requests, contributing to open source

---

## 20. Intro to Flask
- [ ] **Web Foundations & WSGI**: HTTP request/response cycle, WSGI specification, web server to application interface
- [ ] **Flask Application Basics**: App initialization, route decorators (`@app.route`), HTTP methods (`GET`, `POST`, `PUT`, `DELETE`)
- [ ] **Request & Response Handling**: Query parameters (`request.args`), form data (`request.form`), JSON payload (`request.get_json()`), response objects, HTTP status codes
- [ ] **Jinja2 Templating**: Template rendering (`render_template`), variable substitution, control loops, template inheritance (`{% extends %}`, `{% block %}`)
- [ ] **Database Integration**: SQLite integration in Flask, lifecycle hooks (`@app.teardown_appcontext`), persistent state
- [ ] **Production Structure**: Modular architecture with Flask Blueprints, Application Factory pattern (`create_app`)
