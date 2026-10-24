# Python Standard Library Essential Quick Reference

Python's "Batteries Included" philosophy means the standard library has solutions for 95% of engineering tasks without external dependencies.

---

## 1. Data Structures & Algorithms
- **`collections.deque`**: Double-ended queue with $O(1)$ appends and pops from both ends (unlike list's $O(N)$ `pop(0)`).
- **`collections.Counter`**: Fast frequency hash table for counting hashable elements.
- **`collections.defaultdict`**: Dictionary that automatically invokes a factory for missing keys.
- **`heapq`**: Priority queue algorithm (min-heap) with $O(\log N)$ pushes and pops.
- **`itertools`**:
  - `chain(*iterables)`: Stream multiple collections sequentially.
  - `islice(it, start, stop)`: Slice any iterator without loading into memory.
  - `count(start, step)`: Infinite arithmetic progression.
  - `combinations(p, r)`, `permutations(p, r)`: Combinatorial generators.

---

## 2. Function Utilities & Caching
- **`functools.lru_cache(maxsize=128)`**: Thread-safe Least-Recently-Used memoization cache.
- **`functools.partial(func, *args, **kwargs)`**: Freezes selected function parameters.
- **`functools.wraps(wrapped)`**: Preserves `__name__`, `__doc__`, and metadata in decorators.

---

## 3. Files, Formats & System
- **`pathlib.Path`**: Object-oriented filesystem paths (`path / "subdir"`, `.read_text()`, `.glob("*.py")`).
- **`json`**: Native JSON encoder/decoder (`loads`, `dumps`).
- **`csv`**: Streaming CSV reader and writer (`DictReader`, `DictWriter`).
- **`subprocess.run(["cmd", "arg"], check=True, capture_output=True, text=True)`**: Modern, safe shell execution.
- **`sys`**: Runtime introspection (`sys.argv`, `sys.modules`, `sys.getsizeof`, `sys.platform`).

---

## 4. Cryptography, Math & Serialization
- **`secrets`**: Cryptographically secure random tokens and passwords (`token_hex`, `token_urlsafe`).
- **`math.isclose(a, b, rel_tol=1e-9)`**: Safe floating-point equality comparisons.
- **`dataclasses.dataclass`**: Automatic code generation for data classes (`__init__`, `__repr__`, `__eq__`).
