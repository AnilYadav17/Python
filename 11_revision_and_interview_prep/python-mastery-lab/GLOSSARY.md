# Technical Glossary of Python & CPython Terms

This glossary provides precise, engineering-grade definitions. Memorize these distinctions; do not rely on colloquial or simplified interpretations.

---

### Object Model & Variables
- **Name (Identifier)**: A token in source code bound to an object reference within a specific namespace. Names do *not* have types or memory allocations; objects do.
- **Object (`PyObject`)**: A chunk of allocated heap memory consisting minimally of a reference count (`ob_refcnt`) and a pointer to its type object (`ob_type`).
- **Binding / Assignment**: The operation of associating a name in a namespace with a pointer to an existing object (`name = object`).
- **Rebinding**: Associating an existing name with a different object. This does *not* mutate the object previously referred to.
- **Aliasing**: The condition where two or more distinct names (or collection elements) point to the exact same object reference in memory.
- **Identity (`is`)**: Whether two pointers refer to the exact same memory address (`id(a) == id(b)` in CPython).
- **Equality (`==`)**: Whether two objects represent the same value according to the left operand's `__eq__` (or right operand's `__eq__` reflection).
- **Mutability**: The property of an object allowing its internal state/values to be altered in-place after instantiation without changing its `id`.
- **Immutability**: The property of an object whose state cannot be modified once instantiated (e.g., `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`).
- **Hashability**: An object is hashable if it has an immutable hash value that remains constant during its lifetime (`__hash__`) and can be compared for equality (`__eq__`).

---

### Type System
- **Dynamic Typing**: Types are associated with *values/objects* at runtime, not with *variable names* at compile time.
- **Strong Typing**: The runtime strictly enforces type operations; implicit type coercions across incompatible types (such as `"5" + 2`) are prohibited and raise `TypeError`.
- **Duck Typing**: A programming style where an object's suitability is determined by the presence of certain methods and properties rather than by explicit inheritance ("If it walks like a duck and quacks like a duck, it's a duck").
- **Structural Subtyping (`Protocol`)**: Static typing discipline (PEP 544) where type compatibility is determined by shape/interface matching rather than nominal subclassing.

---

### Execution & Compilation Pipeline
- **Lexing / Tokenization**: The process of transforming raw source code characters into discrete tokens (`NAME`, `NUMBER`, `INDENT`, `DEDENT`, `NEWLINE`).
- **Parsing**: Constructing an Abstract Syntax Tree (AST) from a sequence of tokens based on Python's PEG grammar.
- **AST (Abstract Syntax Tree)**: A hierarchical tree representation of the syntactic structure of Python source code (`ast` module).
- **Compilation**: The transformation of an AST into executable bytecode packed inside a **Code Object**.
- **Code Object (`types.CodeType`)**: An immutable C structure containing compiled bytecode instructions, constants, variable names, and line mappings.
- **Bytecode**: The compact, platform-independent instruction set executed by the CPython Virtual Machine (stack-based opcodes).
- **Frame Object (`PyFrameObject`)**: The runtime execution context for a code block (e.g., a function call), holding the local namespace array, value stack, evaluation pointer, and reference to the code object.
- **Evaluation Loop (`_PyEval_EvalFrameDefault`)**: The core C switch-loop in CPython that iterates through bytecode instructions and executes them on the value stack.
- **Specialized Adaptive Interpreter (PEP 659)**: CPython 3.11+ mechanism that inspects executing bytecode and dynamically replaces generic instructions with fast, monomorphic specialized opcodes (e.g., `BINARY_OP_ADD_INT`).

---

### Scopes & Namespaces
- **Namespace**: A mapping from names to object references (implemented as a Python `dict` or C array).
- **LEGB Rule**: The name resolution hierarchy: **L**ocal $\to$ **E**nclosing $\to$ **G**lobal $\to$ **B**uilt-in.
- **Closure**: A function object that retains references to variables in its enclosing lexical scope even after that enclosing scope has finished executing (`__closure__`).
- **Free Variable**: A variable used in a function that is not a local variable or parameter of that function, but is defined in an outer enclosing scope.

---

### Concurrency & Memory
- **GIL (Global Interpreter Lock)**: A mutex used in standard CPython to synchronize thread access to Python object memory and interpreter state, preventing simultaneous multi-core execution of Python bytecode within a single process.
- **Free-Threaded CPython (PEP 703)**: A CPython build mode (`python3.14t`) where the GIL is removed, utilizing biased reference counting and mimalloc thread-safe memory management.
- **Reference Counting**: The primary memory management mechanism in CPython: every object maintains an `ob_refcnt`. When it drops to zero, memory is freed immediately.
- **Cyclic Garbage Collector**: A generational background collector in CPython that detects and frees circular references unreachable from root namespaces.
