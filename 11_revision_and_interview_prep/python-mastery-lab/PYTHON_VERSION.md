# Python Target Version & Environment Specification

## 1. Active Environment
- **Host OS**: Ubuntu Linux (Kernel `7.0.0-38-generic`, `x86_64`)
- **Active Python Interpreter**: CPython `3.14.4`
- **Compiler**: GCC / Clang on GNU/Linux
- **Standard Baseline**: Code examples target Python `3.12+` compatibility while highlighting `3.13` and `3.14` developments (e.g., Free-Threaded CPython / PEP 703, Tier-2 JIT compiler, refined error tracebacks, improved interactive REPL).

---

## 2. Universal Language Guarantees vs. CPython Implementation Details

A critical skill in Python mastery is distinguishing between what the **Python Language Specification** guarantees versus what is specific to **CPython**:

| Aspect | Language Specification Guarantee (All Compliant Pythons) | CPython Implementation Detail (May vary or change) |
| :--- | :--- | :--- |
| **Object Model** | Everything is an object; names bind to object references. | `id(obj)` returns the memory address (`PyObject*`). |
| **Memory Cleanup** | Unreachable objects are eventually collected. | Immediate deterministic reclamation via reference counting; cyclic GC handles reference cycles. |
| **Small Integers** | Integers have arbitrary precision; `==` compares mathematical values. | Pre-allocated singleton array for integers `[-5, 256]`; `is` returns `True` for these. |
| **String Interning** | Strings are immutable sequences of Unicode codepoints. | Identifiers and short ASCII strings are interned; `is` may return `True` for identical literals. |
| **Dict Ordering** | Key insertion order is preserved (guaranteed since Python 3.7). | Compact dict layout (split table with 8-byte hash/key/value entries + dense index array). |
| **Concurrency & Execution** | Python threads execute standard OS threads. | Global Interpreter Lock (GIL) serializes bytecode execution unless running on free-threaded builds (`python3.14t`). |
| **Bytecode & Execution** | Source code is compiled and evaluated according to semantics. | Stack-based Virtual Machine bytecode (`LOAD_FAST`, `CALL`, `STORE_NAME`), code objects (`co_code`), frame objects (`PyFrameObject`). |

---

## 3. Version Compatibility Matrix (Key Milestones)

- **Python 3.8**: Assignment expressions (Walrus `:=`), Positional-only parameters (`/`).
- **Python 3.9**: Dict union operators (`|`, `|=`), Type hinting generics in standard collections (`list[str]`).
- **Python 3.10**: Structural Pattern Matching (`match / case`), explicit Union operator (`int | str`), enhanced syntax error messages.
- **Python 3.11**: Fine-grained error locations in tracebacks, Exception Groups & `except*`, `Self` type, Faster CPython project (Specializing Adaptive Interpreter).
- **Python 3.12**: Type parameter syntax (PEP 695 `type Alias[T] = ...`), f-string syntax formalization (arbitrary nesting & quotes), isolated subinterpreters with per-interpreter GIL.
- **Python 3.13**: Experimental Free-Threaded build (disable GIL with PEP 703), experimental JIT compiler (PEP 744), enhanced interactive REPL (Pygments-based highlighting, multi-line editing).
- **Python 3.14**: Deferred annotation evaluation adjustments, further interpreter specialization optimizations, template strings / annotation transformations.

---

## 4. Verification Policy
All executable experiments in `26_experiments/` and automated tests in `tests/` are run directly against the active environment's interpreter. No output is claimed without local execution or strict cross-referencing with official documentation ([docs.python.org/3/](https://docs.python.org/3/)).
