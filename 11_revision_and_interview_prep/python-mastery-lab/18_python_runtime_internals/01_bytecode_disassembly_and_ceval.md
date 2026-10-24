# Lesson 18.1: CPython Runtime Internals — Bytecode, Stack Machine & Adaptive Specialization

## 1. What Is This in Simple Words?
When you click "run" on a Python script, Python doesn't execute your text characters directly.  
1. It compiles your text into **Bytecode** (compact, numeric instructions).
2. It feeds that bytecode into a virtual processor loop written in C (called the **CPython Evaluation Loop** or `ceval.c`).
3. CPython acts like an imaginary CPU called a **Stack Machine**, pushing numbers onto an internal stack, doing math, and popping results.

---

## 2. Peeking Under the Hood with the `dis` Module

Python has a built-in disassembler (`dis`) that lets you see the exact machine instructions Python creates for your functions:

```python
import dis

def calculate(a, b):
    return a + b * 2

# Disassemble the function:
dis.dis(calculate)
```

### What the Disassembly Output Means:
```
  2           0 RESUME                   0
              2 LOAD_FAST                0 (a)
              4 LOAD_FAST                1 (b)
              6 LOAD_CONST               1 (2)
              8 BINARY_OP                5 (*)
             12 BINARY_OP                0 (+)
             16 RETURN_VALUE
```
- `LOAD_FAST 0 (a)`: Quick lookup of local variable `a` from the array of local variables (much faster than a dictionary lookup!).
- `LOAD_CONST 1 (2)`: Pushes number 2 onto the stack.
- `BINARY_OP 5 (*)`: Pops `b` and `2`, multiplies them, and pushes the result back.
- `BINARY_OP 0 (+)`: Pops `a` and the multiplication result, adds them.
- `RETURN_VALUE`: Returns whatever is at the top of the stack!

---

## 3. Dissecting the Code Object (`__code__`)

Every function in Python holds a compiled code object in its `__code__` attribute:
```python
def example(x, y=10):
    message = "Result:"
    return f"{message} {x + y}"

co = example.__code__

print("Variable names:", co.co_varnames)   # ('x', 'y', 'message')
print("Constants:", co.co_consts)           # (None, 10, 'Result:', ' ')
print("Raw bytecode bytes:", co.co_code)   # Raw binary bytes (opcodes + arguments)
```

---

## 4. Modern CPython: The Specializing Adaptive Interpreter (PEP 659)

Starting in Python 3.11, Python watches your code as it runs!
- When an instruction runs multiple times, Python asks: *"Is this instruction always working on integers?"* or *"Is this attribute lookup always accessing the exact same class slot?"*
- If yes, Python dynamically **rewrites its own bytecode in memory** into specialized "quickened" opcodes (e.g. `LOAD_ATTR` becomes `LOAD_ATTR_SLOT` or `BINARY_OP_ADD_INT`).
- This dynamic adaptation is why modern Python (3.11, 3.12, 3.13+) is **up to 60% faster** than Python 3.10!

---

## 5. Mind-Blowing Facts! 💡

> **Fact 1: Local Variables Don't Use Dictionaries!**  
> Beginners assume Python looks up variables in dictionaries. In global scope (`globals()`), it does. But inside functions, local variables (`LOAD_FAST`) are indexed into a simple, fixed-size C array of pointers! This is why local variables are **30% to 50% faster** than global variables!
>
> **Fact 2: Python Bytecode Opcodes Are 2 Bytes Each!**  
> Since Python 3.6, all bytecode instructions are exactly **2 bytes long**: 1 byte for the opcode name (0-255) and 1 byte for the argument! This is known as the **Wordcode** architecture, making bytecode parsing and cache alignment blazingly fast in the C evaluation loop.

---

## 6. Self-Test
1. **Question**: Why is accessing a local variable inside a function (`LOAD_FAST`) faster than accessing a global variable (`LOAD_GLOBAL`)?
   - *Answer*: `LOAD_FAST` uses direct offset indexing into a fixed C array, whereas `LOAD_GLOBAL` requires looking up a string key inside a hash dictionary (`__dict__`).
