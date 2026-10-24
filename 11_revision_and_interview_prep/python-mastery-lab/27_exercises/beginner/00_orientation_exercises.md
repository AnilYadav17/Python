# Orientation Exercises (Module 00)

---

## Exercise 1: Predict the Output (Without Running Code)

Analyze the following snippets. For each snippet, state:
1. Does it succeed or raise an exception?
2. If it succeeds, what is the printed value and its type?
3. If it raises an exception, what is the exact exception type?

### Snippet A:
```python
x = 7 / 2
print(x, type(x).__name__)
```

### Snippet B:
```python
val = "100" + 25
print(val)
```

### Snippet C:
```python
import sys
code = compile("x = 42", "<string>", "exec")
print(type(code).__name__)
```

---

## Exercise 2: Find the Bug & Explain the Mechanism

A junior developer wrote the following function intended to safely combine user input:

```python
def format_user_id(prefix, id_number):
    # Intent: returns "USR-101" when passed ("USR", 101)
    return prefix + "-" + id_number
```

1. What error occurs when calling `format_user_id("USR", 101)`?
2. Why does Python raise this error, whereas a language like JavaScript would silently return `"USR-101"`?
3. Rewrite the function using idiomatic modern Python.

---

## Exercise 3: Code Object Inspection Task

Write a 5-line Python script that:
1. Takes the expression: `result = (base_rate * multiplier) + 5000`.
2. Compiles it into a Code Object using `compile()`.
3. Prints the tuple of referenced names (`co_names`).
4. Prints the tuple of constants (`co_consts`).
5. Prints whether `base_rate` is considered a constant or a name.

---

## Exercise 4: Viva Interview Drill

Be prepared to answer these three questions without looking at notes:
1. *"Python is an interpreted language, so it executes source code directly from top to bottom without any compiler."* How do you refute this statement using concrete CPython architectural components?
2. *"What is a .pyc file, what two pieces of information does its header store, and why doesn't running a one-off script produce one?"*
3. *"Explain the difference between Python's strong typing and static typing."*

---

<details>
<summary><strong>Click to View Complete Solutions & Explanations</strong></summary>

### Solution to Exercise 1:
- **Snippet A**: Succeeds. Prints: `3.5 float`. Python 3 implements true mathematical division for `/`. Floor division requires `//`.
- **Snippet B**: Raises `TypeError: can only concatenate str (not "int") to str`. Python is strongly typed and refuses implicit coercion between `str` and `int`.
- **Snippet C**: Succeeds. Prints: `code`. `compile()` returns a first-class `types.CodeType` object holding compiled bytecode.

### Solution to Exercise 2:
1. Raises `TypeError: can only concatenate str (not "int") to str`.
2. Python enforces strong typing at runtime. In JavaScript, the `+` operator has implicit type coercion semantics that silently cast numbers to strings if either operand is a string. In Python, operand types must match or implement compatible dunder methods (`__add__`).
3. Idiomatic fix:
   ```python
   def format_user_id(prefix: str, id_number: int) -> str:
       return f"{prefix}-{id_number}"
   ```

### Solution to Exercise 3:
```python
expr = "result = (base_rate * multiplier) + 5000"
code_obj = compile(expr, "<exercise>", "exec")
print("Names:    ", code_obj.co_names)    # ('base_rate', 'multiplier', 'result')
print("Constants:", code_obj.co_consts)  # (5000, None)
print("base_rate is in co_names:", 'base_rate' in code_obj.co_names)
```

</details>
