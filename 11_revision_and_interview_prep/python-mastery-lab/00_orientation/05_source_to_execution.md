# Lesson 05: From Source Code to Execution

## 1. Learning Objectives
- Trace the lifecycle of a Python program from UTF-8 source text to machine execution.
- Dissect the roles of the Lexer (Tokenizer), Parser (PEG), Compiler, and Virtual Machine.
- Inspect the Abstract Syntax Tree (AST) using the standard library `ast` module.
- Demystify `.pyc` files, the `__pycache__` directory, and the `marshal` format.
- Understand the structure of a **Code Object** (`types.CodeType`) and an execution **Frame** (`PyFrameObject`).

---

## 2. The Complete Pipeline Diagram

```
+---------------------------------------------------------------+
| Source Code (.py file / UTF-8 string)                         |
| "total = count * 2"                                           |
+------------------------------┬--------------------------------+
                               | Lexing (Tokenizer)
                               v
+---------------------------------------------------------------+
| Stream of Tokens:                                             |
| [NAME 'total', EQUAL '=', NAME 'count', STAR '*', NUMBER '2'] |
+------------------------------┬--------------------------------+
                               | Parsing (PEG Parser)
                               v
+---------------------------------------------------------------+
| Abstract Syntax Tree (AST):                                   |
| Assign(targets=[Name('total')], value=BinOp(...))             |
+------------------------------┬--------------------------------+
                               | Bytecode Compiler
                               v
+---------------------------------------------------------------+
| Code Object (types.CodeType):                                 |
| - co_code: b'e\x00d\x01\x14\x00Z\x02'                         |
| - co_consts: (None, 2)                                        |
| - co_names: ('count', 'total')                                |
| - Bytecode: LOAD_NAME 0 (count), LOAD_CONST 1 (2),            |
|             BINARY_OP 5 (*), STORE_NAME 1 (total)             |
+------------------------------┬--------------------------------+
                               | Serialization (Import only)
                               v
+---------------------------------------------------------------+
| Cache File (__pycache__/module.cpython-314.pyc)               |
| [Magic Number (4B) | Timestamp (4B) | Serialized Code Object] |
+------------------------------┬--------------------------------+
                               | CPython Virtual Machine
                               v
+---------------------------------------------------------------+
| Execution Frame (PyFrameObject on C Call Stack):              |
| - Value Stack (operand evaluation)                            |
| - Local / Global / Builtin Namespace Dictionaries             |
| - Evaluation Loop: _PyEval_EvalFrameDefault() in C            |
+---------------------------------------------------------------+
```

---

## 3. Detailed Stage Breakdown

### Stage 1: Lexing (Tokenizing)
The Lexer reads raw UTF-8 characters and groups them into atomic units called **Tokens**.
- Whitespace and indentation are converted into structural tokens: `INDENT` and `DEDENT`.
- Newlines in logical statements emit `NEWLINE` tokens.
- Comments are stripped from the execution stream.

You can inspect Python's tokenizer using the standard library module:
```python
import io
import tokenize

code = "total = count * 2"
tokens = list(tokenize.tokenize(io.BytesIO(code.encode("utf-8")).readline))
for tok in tokens:
    print(f"{tok.type:<4} {tokenize.tok_name[tok.type]:<12} {tok.string!r}")
```

### Stage 2: Parsing (Constructing the AST)
Python 3.9+ uses a **PEG (Parsing Expression Grammar)** parser. It processes the stream of tokens and constructs an **Abstract Syntax Tree (AST)**—a tree structure representing the grammatical hierarchy of the program.

Inspect with the `ast` module:
```python
import ast

tree = ast.parse("total = count * 2")
print(ast.dump(tree, indent=4))
```
Output:
```python
Module(
    body=[
        Assign(
            targets=[
                Name(id='total', ctx=Store())],
            value=BinOp(
                left=Name(id='count', ctx=Load()),
                op=Mult(),
                right=Constant(value=2)))],
    type_ignores=[])
```

### Stage 3: Compilation into Code Objects
The compiler walks the AST and translates high-level syntactic structures into a flat stream of virtual machine instructions (bytecode), encapsulated inside a **Code Object** (`types.CodeType`):
- `co_code`: The raw bytes representing VM opcodes and operands.
- `co_consts`: Tuple of literal values used in the code (e.g., `(None, 2)`).
- `co_names`: Tuple of global and attribute names referenced.
- `co_varnames`: Tuple of local variable names.
- `co_filename`, `co_firstlineno`, `co_lnotab` / `co_linetable`: Debugging and traceback mapping information.

Code objects are completely immutable. They contain no state or variable values—only instructions and constants.

### Stage 4: Bytecode Caching (`.pyc` Files)
When a module is imported, CPython avoids recompiling it on subsequent executions by serializing the Code Object using the internal `marshal` format and writing it to `__pycache__/<name>.<interpreter-tag>.pyc`.
- **Header**: Contains a 4-byte Magic Number (specific to the CPython version), bit flags, and the source file timestamp or SHA-256 hash.
- If the source `.py` file timestamp or hash matches the header, CPython skips tokenizing, parsing, and compiling, loading the marshalled code object directly into memory in milliseconds.

### Stage 5: Execution in the CPython Virtual Machine
When Python executes a code object:
1. It allocates a **Frame Object** (`PyFrameObject`).
2. The frame provides:
   - A **Value Stack** (an array of `PyObject*` where intermediate evaluation results are pushed and popped).
   - Pointers to **Local**, **Global**, and **Built-in** namespaces.
   - An instruction pointer (`f_lasti`) pointing to the current bytecode offset.
3. The CPython evaluation loop (`_PyEval_EvalFrameDefault`) enters a high-speed C `switch` statement, popping operands from the value stack, invoking C operations, and pushing results back onto the stack.

---

## 4. Viva & Interview Questions

1. **Q: Why does running a standalone script directly (`python3 script.py`) not create a `.pyc` file in `__pycache__` by default, whereas importing it (`import script`) does?**
   - *Answer*: CPython is optimized under the assumption that top-level command-line scripts are frequently modified by developers during editing and rapid iteration, whereas imported library modules are relatively static. Therefore, CPython only caches imported modules in `__pycache__` to accelerate subsequent startup times, avoiding the disk I/O overhead of writing `.pyc` files for one-off scripts unless explicitly forced (e.g., via `python -m compileall`).

2. **Q: What is the relationship between a Code Object and a Frame Object?**
   - *Answer*: A Code Object is a static, immutable description of instructions, constants, and variable names generated at compile time. A Frame Object is a dynamic, heap-allocated runtime instance created on the call stack each time that code object is executed (such as each invocation of a function). If a recursive function calls itself 10 times, there is **1** Code Object, but **10** distinct Frame Objects.

---

## 5. Mastery Checklist
- [ ] Can describe the 5 stages from source text to evaluation.
- [ ] Can explain the role and components of an Abstract Syntax Tree (AST).
- [ ] Can identify what is stored inside a Code Object vs a Frame Object.
