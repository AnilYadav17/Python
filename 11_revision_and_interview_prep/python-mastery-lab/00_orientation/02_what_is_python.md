# Lesson 02: What Is Python?

## 1. Learning Objectives
- Formulate the precise technical classification of Python (typing discipline, execution paradigm, memory management).
- Contrast Python rigorously with C, C++, Java, and JavaScript.
- Deconstruct the critical distinction between **Dynamic Typing** and **Strong Typing**.
- Explain "Duck Typing" and structural polymorphism at runtime.
- Differentiate between the **Python Language Specification** and **Python Implementations**.

---

## 2. Technical Definition of Python

> **Python** is a high-level, dynamically-typed, strongly-typed, garbage-collected, multi-paradigm programming language with an expressive syntax designed for developer velocity, readable code, and rich extensibility via native C interfaces.

Let us unpack every term in that definition:
- **High-level**: Hides hardware specifics (registers, stack pointers, direct RAM addresses).
- **Dynamically-typed**: Types belong to *objects* in memory, not *names/variables*. Type checks occur at runtime during evaluation.
- **Strongly-typed**: Types are strictly respected; no implicit type coercion is performed across incompatible types (e.g., `'42' + 8` raises `TypeError`, unlike JavaScript which produces `'428'`).
- **Garbage-collected**: Programmers do not manually allocate (`malloc`) or deallocate (`free`) heap memory. Memory lifetime is managed automatically via reference counting and cyclic garbage collection.
- **Multi-paradigm**: Supports object-oriented, procedural, and functional programming styles.

---

## 3. The Typing Matrix: Dynamic vs. Static, Strong vs. Weak

Many developers conflate "dynamic" with "weak". Python is **dynamic** and **strong**:

```
                    TYPE ENFORCEMENT
               Weak                     Strong
       +-----------------------+-----------------------+
       |                       |                       |
Static |          C            |      Java, Rust,      |
       | (Pointers, unchecked  |        C++, Go        |
       |    type casts)        |                       |
       +-----------------------+-----------------------+
       |                       |                       |
Dynamic|      JavaScript,      |        Python,        |
       |       PHP, Perl       |       Ruby, Lisp      |
       | ('5' - 3 == 2)        | ('5' + 3 -> TypeError)|
       +-----------------------+-----------------------+
```

### Demonstration of Strong vs. Weak Typing:
In JavaScript (Weakly Typed):
```javascript
"5" + 2   // Evaluates to "52" (implicit coercion to string)
"5" - 2   // Evaluates to 3 (implicit coercion to number)
[] + {}   // Evaluates to "[object Object]"
```

In Python (Strongly Typed):
```python
>>> "5" + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> "5" - 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'
```
Python refuses to guess your intention. You must perform explicit conversion: `int("5") + 2` or `"5" + str(2)`.

---

## 4. Architectural Comparison: Python vs. C, Java, JavaScript

| Feature | Python (CPython) | C (ISO C17) | Java (OpenJDK JVM) | JavaScript (V8 Engine) |
| :--- | :--- | :--- | :--- | :--- |
| **Typing Discipline** | Dynamic & Strong | Static & Weak | Static & Strong | Dynamic & Weak |
| **Memory Management** | Automatic (Ref count + Cyclic GC) | Manual (`malloc`/`free`) | Automatic (Tracing Generational GC) | Automatic (Mark-and-Sweep GC) |
| **Compilation Model** | Interpreted VM bytecode (with optional JIT) | Ahead-Of-Time (AOT) to native machine code | Bytecode to JVM; heavy JIT compilation | Bytecode interpreted, aggressive multi-tier JIT |
| **Execution Speed** | Moderate to Slow (interpreted bytecode) | Maximum (bare-metal direct CPU execution) | High (optimized HotSpot JIT) | High (V8 machine code generation) |
| **Safety & Bounds** | Memory-safe; bounds-checked indexing | Unsafe; buffer overflows, dangling pointers | Memory-safe; array bounds checked | Memory-safe |
| **Concurrency Model** | Threads (GIL in standard build), AsyncIO, Processes | Native OS threads (pthreads), locks | Native OS threads, Virtual Threads (Project Loom) | Single-threaded event loop, Web Workers |

---

## 5. Duck Typing: "If it walks like a duck..."

In statically typed nominal languages like Java, a function requires an argument to inherit from a specific interface or class:
```java
// Java requires explicit nominal type
void render(Shape s) { s.draw(); }
```

In Python, the function only requires the object to support the required methods or attributes at the exact moment of invocation:
```python
def render(drawable):
    # Python checks if 'drawable' has a callable attribute named 'draw'
    drawable.draw()
```
If the object responds to `.draw()`, Python executes it. If it does not, a runtime `AttributeError` is raised. This is dynamic polymorphism.

---

## 6. Language Specification vs. Implementation

A critical conceptual distinction:

1. **The Python Language Specification**:
   - The formal grammar, syntax, built-in keywords, scoping rules, and standard library behavior documented at [docs.python.org/3/reference/](https://docs.python.org/3/reference/).
   - Written in English and formal grammar (EBNF / PEG grammar).
   - Maintained by the Python Software Foundation (PSF) and Python Core Developers via Python Enhancement Proposals (PEPs).

2. **The Python Implementation**:
   - The concrete piece of software that reads Python code and executes it on physical hardware.
   - **CPython**: The reference implementation written in C.
   - **PyPy**: Alternative implementation written in RPython with a tracing JIT compiler.
   - **Jython**: Runs on the Java Virtual Machine.
   - **IronPython**: Runs on the .NET CLR.

When someone says *"Python has a GIL"* or *"Python uses reference counting"*, they are describing **CPython**, not the abstract Python language specification!

---

## 7. Viva & Interview Questions

1. **Q: Why does Python raise a `TypeError` when adding an integer to a string, while JavaScript does not?**
   - *Answer*: Because Python is strongly typed, whereas JavaScript is weakly typed. Strong typing forbids implicit semantic coercions between incompatible operand types, requiring the programmer to declare intent explicitly.

2. **Q: Does Python have variables that hold data?**
   - *Answer*: No. Python has names that act as references (pointers) bound to heap-allocated objects. The variable name resides in a namespace table; the value resides in an allocated `PyObject` structure on the heap.

---

## 8. Mastery Checklist
- [ ] Can accurately categorize Python on the static/dynamic and strong/weak axes.
- [ ] Can explain the difference between nominal typing (Java) and duck typing (Python).
- [ ] Can articulate the difference between the Python language specification and CPython.
