# Project 1: Safe CLI Calculator

## 1. Problem Statement
Many command-line utilities require evaluating user-supplied mathematical formulas. A naive beginner implementation uses Python's built-in `eval(expression)`. 

However, `eval()` executes arbitrary Python code. If an attacker inputs `__import__('os').system('rm -rf /')`, the system is destroyed! 

The objective of this project is to build an industrial-grade, fully secure command-line calculator that parses, validates, and computes arithmetic expressions using Python's **Abstract Syntax Tree (AST)** module without ever executing untrusted user input.

---

## 2. Requirements & Scope
- **Supported Operations**:
  - Addition (`+`), Subtraction (`-`)
  - Multiplication (`*`), Division (`/`)
  - Floor Division (`//`), Modulo (`%`)
  - Exponentiation (`**`)
  - Parenthesized grouping: `( )`
  - Unary positive (`+x`) and negative (`-x`)
- **Execution Modes**:
  - One-shot command line: `python3 calculator.py "10 + 5 * 2"`
  - Interactive REPL loop: `python3 calculator.py`
- **Security Constraint**: **Zero usage of `eval()` or `exec()`**. Only whitelist-approved AST nodes are visited.

---

## 3. Architecture & Design

```
+─────────────────────────────────────────────────────────────+
| User Input String: "(10 + 5) * 2"                           |
+──────────────────────────────┬──────────────────────────────+
                               | ast.parse(mode='eval')
                               v
+─────────────────────────────────────────────────────────────+
| Abstract Syntax Tree (AST):                                 |
| BinOp(left=BinOp(Add), op=Mult, right=Constant(2))          |
+──────────────────────────────┬──────────────────────────────+
                               | SafeEvaluator (ast.NodeVisitor)
                               v
+─────────────────────────────────────────────────────────────+
| Strict Whitelist Validation:                                |
|   - Add, Sub, Mult, Div, Mod, Pow -> Approved!              |
|   - Call, Import, Attribute -> REJECTED (InvalidExpression)  |
+──────────────────────────────┬──────────────────────────────+
                               | Recursive Arithmetic Evaluation
                               v
+─────────────────────────────────────────────────────────────+
| Result: 30                                                  |
+─────────────────────────────────────────────────────────────+
```

---

## 4. Security Analysis
If an attacker attempts a code injection attack:
```bash
python3 calculator.py "__import__('os').system('whoami')"
```
1. `ast.parse()` parses the text into an AST `Call` node.
2. `SafeEvaluator` visits the node. Because `Call` is not on the whitelist of approved arithmetic visitors, it hits `generic_visit()`.
3. It immediately raises `InvalidExpressionError: Unsupported operation or security violation: Call`.
4. The system is completely protected.

---

## 5. Setup & Running Instructions

```bash
# Run interactively:
python3 28_projects/01_cli_calculator/calculator.py

# Run one-shot:
python3 28_projects/01_cli_calculator/calculator.py "100 / (2 + 3) ** 2"

# Run project unit tests:
python3 -m unittest 28_projects/01_cli_calculator/test_calculator.py
```

---

## 6. Code Review Checklist
- [x] Zero usage of `eval()` or `exec()`.
- [x] Division by zero handled gracefully (`DivisionByZeroError`).
- [x] Operator precedence preserved naturally by AST parser.
- [x] Both integer and floating-point inputs supported.
- [x] Comprehensive test suite with edge cases.
