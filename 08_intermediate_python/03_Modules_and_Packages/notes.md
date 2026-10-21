# 03. Modules & Packages: Complete Reference

---

## 1. Importing Machinery & The Python Import System

### What it is
- A **module** is any single `.py` file containing Python definitions, functions, classes, and executable statements.
- Syntax variations:
  - `import module_name`: Imports module and creates reference `module_name` in current namespace.
  - `from module_name import symbol`: Imports specific object directly into current namespace.
  - `from module_name import symbol as alias`: Imports symbol under an alternative identifier.
  - `from module_name import *`: Imports all names defined in module (or restricted to `__all__`). Discouraged due to namespace pollution.

### Why it matters
- Enables code reusability across files and projects, preventing monolithic, unmaintainable single-file applications.
- Allows logical separation of concerns into isolated domains and libraries.

### How it works (internals, if relevant)
- **Import Sequence**:
  1. Checks cache dictionary `sys.modules`. If already imported, returns existing module object immediately ($O(1)$).
  2. If not cached, invokes "Finders" (PEP 302/451) that search paths in `sys.path` (current working directory, `PYTHONPATH`, standard library, installed `site-packages`).
  3. Invokes "Loaders" to read source file, compile to bytecode (`.pyc`), allocate a new `module` object (`types.ModuleType`), and execute the module's top-level code in the module's own dictionary (`__dict__`).
  4. Stores the newly created module object in `sys.modules`.

### Common mistakes / gotchas
- **Circular Imports**: Module A imports Module B, while Module B imports Module A at top-level. If accessed before definitions compile, raises `ImportError: cannot import name ... from partially initialized module`.
- Naming a local script identical to a standard library module (e.g. creating a file named `math.py` or `random.py`), which shadows the standard library module when importing.
- Mutating `sys.path` dynamically without understanding directory resolution order.

### Connects to
- Package Structure and `__init__.py` (subtopic 2 below) and Virtual Environments (Topic 15).

---

## 2. Package Structure & `__init__.py`

### What it is
- A **package** is a directory containing one or more Python modules.
- **Regular Package**: A directory containing an `__init__.py` file.
- **Namespace Package** (PEP 420, Python 3.3+): A directory without `__init__.py` that can be split across multiple file-system directories or zip files.
- `__all__`: A module/package-level list of strings defining the public API exposed when a user runs `from package import *`.

### Why it matters
- Organizes related modules into hierarchical dot-notated namespaces (`package.subpackage.module`).
- `__init__.py` controls what is exported when the package is imported, providing a clean facade over internal implementations.

### How it works (internals, if relevant)
- When a package is imported, its `__init__.py` is executed automatically, and the resulting module object represents the package namespace.
- Without `__all__`, `from module import *` imports all public names (names not starting with an underscore `_`).
- Defining `__all__ = ["Client", "connect"]` restricts wildcard imports strictly to those symbols.

### Common mistakes / gotchas
- Placing heavy, slow computational logic or network calls inside `__init__.py`, making package import sluggish.
- Relying on implicit namespace packages accidentally by forgetting `__init__.py` in legacy code or tools that require regular packages.
- Overusing wildcard imports (`from pkg import *`), which causes symbol shadowing and makes tracing variable origins difficult.

### Connects to
- Building Custom Packages (subtopic 3 below).

---

## 3. Building a Custom Package

### What it is
- Structuring Python source code into a standard distributable directory tree:
  ```text
  my_project/
  ├── pyproject.toml         # Packaging build configuration (PEP 517/621)
  ├── README.md
  └── src/
      └── my_package/
          ├── __init__.py
          ├── core.py
          └── utils.py
  ```
- **Relative Imports**: Used *within* a package:
  - `from . import core` (same directory)
  - `from ..subpkg import helper` (parent directory)

### Why it matters
- The `src/` layout prevents accidental imports of uninstalled development code when running tests or scripts.
- Relative imports make packages self-contained and relocatable without hardcoding the root package name internally.

### How it works (internals, if relevant)
- Relative imports rely on the module's `__name__` and `__package__` attributes.
- If a script inside a package is executed directly via `python src/my_package/core.py`, its `__name__` becomes `"__main__"`, and `__package__` is set to `None`.
- Attempting relative imports in direct script execution raises `ImportError: attempted relative import with no known parent package`.
- Solution: Run packages from root using module flag: `python -m my_package.core`.

### Common mistakes / gotchas
- Running a package submodule directly as a standalone script and wondering why relative imports fail.
- Flat project layouts where tests import source files directly from the working directory instead of testing installed package artifacts.

### Connects to
- Virtual Environments and Packaging (Topic 15).

---

## 4. Package Management with `pip`

### What it is
- `pip` is the standard package installer for Python, interacting with the Python Package Index (PyPI).
- Key commands:
  - `pip install <package>`: Downloads and installs a package and its dependencies.
  - `pip install -r requirements.txt`: Installs all pinned dependencies listed in a file.
  - `pip freeze > requirements.txt`: Dumps all installed packages and their exact versions in the current environment.
  - `pip uninstall <package>`: Removes a package.

### Why it matters
- Manages external third-party libraries efficiently.
- `requirements.txt` ensures environment reproducibility across development, staging, and production environments.

### How it works (internals, if relevant)
- `pip` resolves dependency trees, downloads distribution archives (**Wheels** `.whl` or **Source Distributions** `.tar.gz`), and installs files into the environment's `site-packages` directory.
- Wheels are pre-compiled binary archives: they install rapidly without requiring a C/C++ compiler on the client machine.
- Source distributions (sdist) contain raw source code and run `setup.py` / build backend to compile extensions locally during installation.

### Common mistakes / gotchas
- Running `pip install` globally without an active virtual environment, polluting system Python and risking OS package manager corruption.
- Committing unpinned dependencies (e.g. `requests` instead of `requests==2.31.0`), leading to unexpected breaking changes when new major versions release.

### Connects to
- Virtual Environments (Topic 15) and Intro to Flask (Topic 20).

---

## 5. Standard Library Deep Dive: `os` & `sys`

### What it is
- `os`: Provides an interface to interact with the underlying Operating System:
  - Environment variables: `os.environ.get("KEY", default)`, `os.environ["KEY"] = val`.
  - Filesystem: `os.getcwd()`, `os.chdir()`, `os.listdir()`, `os.mkdir()`, `os.remove()`, `os.walk()`.
- `sys`: Provides access to variables and functions that interact directly with the Python runtime interpreter:
  - CLI arguments: `sys.argv` (list of command-line arguments passed to script).
  - Search path: `sys.path` (list of directories searched for modules).
  - Loaded modules: `sys.modules` (dictionary cache of active modules).
  - Exit: `sys.exit(code)` (terminates interpreter by raising `SystemExit`).
  - Standard streams: `sys.stdin`, `sys.stdout`, `sys.stderr`.

### Why it matters
- Crucial for writing portable CLI tools, configuring application environments via Twelve-Factor App principles, and inspecting runtime execution.

### How it works (internals, if relevant)
- `os` maps directly to POSIX or Windows C system calls (`stat`, `fork`, `exec`, `getenv`).
- `sys.exit(status)` does not forcefully crash the process at the OS level; it raises the `SystemExit` exception, allowing `try-finally` blocks and context manager cleanup handlers to run gracefully before process death.

### Common mistakes / gotchas
- Using `os.system("rm " + filename)` instead of `os.remove(filename)` or `subprocess.run()`, introducing severe command injection vulnerabilities.
- Forgetting that `os.environ` values are strictly strings; boolean or numeric environment variables must be explicitly cast.
- Relying on `sys.argv[1]` without checking `len(sys.argv)`, triggering `IndexError`.

### Connects to
- File Handling (Topic 06) and Memory Management (Topic 09, `sys.getrefcount`).

---

## 6. Standard Library Deep Dive: `math` & `random`

### What it is
- `math`: Provides access to mathematical functions defined by the C standard:
  - Constants: `math.pi`, `math.e`, `math.inf`, `math.nan`.
  - Rounding & comparison: `math.ceil()`, `math.floor()`, `math.trunc()`, `math.isclose()`.
  - Power & logs: `math.sqrt()`, `math.pow()`, `math.log()`, `math.log10()`.
  - Trigonometry: `math.sin()`, `math.cos()`, `math.radians()`.
- `random`: Implements pseudo-random number generators (PRNG) for various distributions:
  - Functions: `random.random()`, `random.randint(a, b)`, `random.choice(seq)`, `random.shuffle(list)`, `random.sample(seq, k)`, `random.seed(val)`.

### Why it matters
- High-performance numeric computations and statistical simulations.
- Understanding the difference between deterministic PRNG and Cryptographically Secure Pseudo-Random Number Generators (CSPRNG).

### How it works (internals, if relevant)
- `random` uses the **Mersenne Twister** algorithm (MT19937) with a period of $2^{19937}-1$. It is completely deterministic and fast.
- **Security Warning**: Because the internal state of the Mersenne Twister can be completely reconstructed after observing 624 outputs, `random` is **NOT cryptographically secure**.
- For security-sensitive data (passwords, tokens, cryptography keys), use Python's `secrets` module, which draws entropy directly from OS sources (`/dev/urandom` or Windows `CryptGenRandom`).

### Common mistakes / gotchas
- Using `random` for cryptographic tokens, API keys, or password resets instead of `secrets.token_hex()`.
- Mutating a sequence with `random.shuffle()` and expecting it to return the shuffled list (it shuffles in-place and returns `None`).
- Comparing floating-point numbers without `math.isclose()`.

### Connects to
- DSA Fundamentals (Topic 07) and Time Complexity (Topic 08).

---

## 7. Standard Library Deep Dive: `datetime`

### What it is
- Supplies classes for manipulating dates, times, and intervals:
  - `datetime.date`: Year, month, day.
  - `datetime.time`: Hour, minute, second, microsecond, tzinfo.
  - `datetime.datetime`: Combination of date and time.
  - `datetime.timedelta`: Duration expressing difference between two dates/times.
  - `datetime.timezone`: UTC and fixed-offset timezones.

### Why it matters
- Handling timestamps, logging events, scheduling background tasks, calculating service SLAs, and parsing temporal API payloads.

### How it works (internals, if relevant)
- **Naive vs Aware Datetimes**:
  - **Naive**: Contains no timezone information (`tzinfo=None`). Ambiguous across daylight saving transitions and global timezones.
  - **Aware**: Contains an explicit `tzinfo` (e.g. `datetime.timezone.utc` or `zoneinfo.ZoneInfo("UTC")`).
- Formatting & Parsing:
  - `dt.strftime(format)`: Datetime to string (**f**ormat string).
  - `datetime.strptime(string, format)`: String to datetime (**p**arse string).

### Common mistakes / gotchas
- Comparing or subtracting a naive datetime with an aware datetime raises `TypeError: can't subtract offset-naive and offset-aware datetimes`.
- Using `datetime.datetime.now()` without UTC timezone awareness in server backends. Always use `datetime.datetime.now(datetime.timezone.utc)`.
- Using legacy `datetime.datetime.utcnow()` which is deprecated in Python 3.12+ because it returns a naive datetime representing UTC time.

### Connects to
- Databases with Python (Topic 18) and Flask APIs (Topic 20).

---

## 8. Standard Library Deep Dive: `collections`

### What it is
- Provides specialized high-performance container alternatives to Python's general-purpose built-ins:
  - `namedtuple`: Factory function for creating tuple subclasses with named fields.
  - `deque`: Double-ended queue with $O(1)$ appends and pops from both ends.
  - `Counter`: Dict subclass for counting hashable objects.
  - `defaultdict`: Dict subclass that calls a factory function to supply missing values.
  - `OrderedDict`: Dict subclass that remembers order (and provides specialized `.move_to_end()`).

### Why it matters
- Significantly simplifies code: removes manual key-initialization checks and provides memory-efficient, self-documenting data structures.
- `deque` provides $O(1)$ FIFO queue operations, whereas `list.pop(0)` is $O(n)$.

### How it works (internals, if relevant)
- `deque` is implemented in C as a doubly-linked list of fixed-size blocks (64 elements per block). It never requires memory reallocation of the entire buffer.
- `Counter` optimizes multi-set operations: supports addition (`+`), subtraction (`-`), intersection (`&`), and union (`|`).
- `defaultdict` overrides `__missing__(key)`. When a key is absent, it executes the provided default factory, inserts the result, and returns it.

### Common mistakes / gotchas
- Using `list` as a FIFO queue with `list.pop(0)` in high-throughput applications, degrading performance to quadratic $O(n^2)$.
- Passing an argument to the factory of `defaultdict` (e.g. `defaultdict(list())` instead of `defaultdict(list)`), raising `TypeError`.

### Connects to
- Iterators & Generators (Topic 11) and Data Structures from Scratch (Topic 16).

---

## 9. Standard Library Deep Dive: `itertools`

### What it is
- Provides a suite of fast, memory-efficient functions that construct iterators for efficient looping:
  - **Infinite Iterators**: `count(start, step)`, `cycle(iterable)`, `repeat(elem, [n])`.
  - **Terminating Iterators**: `accumulate(seq, [func])`, `chain(*iterables)`, `compress(data, selectors)`, `dropwhile()`, `takewhile()`, `islice(iterable, start, stop[, step])`.
  - **Combinatoric Iterators**: `product(*iterables, repeat=1)`, `permutations(iterable, r)`, `combinations(iterable, r)`, `combinations_with_replacement(iterable, r)`.

### Why it matters
- Allows processing massive or infinite streams without loading entire collections into memory (lazy evaluation).
- Written in optimized C, executing loop combinations drastically faster than nested Python `for` loops.

### How it works (internals, if relevant)
- Every function in `itertools` returns an iterator object yielding one element at a time on each `__next__()` call.
- Memory consumption remains constant $O(1)$ regardless of how many elements are iterated.

### Common mistakes / gotchas
- Converting an infinite iterator (like `count()` or `cycle()`) directly to a list (`list(itertools.cycle([1, 2]))`), which exhausts available RAM and causes an `OutOfMemoryError`.
- Forgetting that `itertools` objects are consumable iterators: once consumed, they cannot be rewound or reused without re-instantiation.

### Connects to
- Iterators & Generators (Topic 11) and DSA Fundamentals (Topic 07).
