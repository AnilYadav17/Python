# Lesson 06: Expressions and Statements

## 1. What Is This in Simple Words?
Understanding the difference between an **expression** and a **statement** is one of the most important concepts in programming:

- **An Expression evaluates to a value.** (Think of it as a question: *"What does this calculate to?"*)
- **A Statement executes an action.** (Think of it as a command: *"Do this!"*)

---

## 2. Expressions: Anything That Produces a Value

If you can print it, assign it to a variable, or pass it to a function, it is an **expression**:

```python
5 + 3             # Evaluates to 8
len("hello")      # Evaluates to 5
x > 10            # Evaluates to True or False
"apple".upper()   # Evaluates to "APPLE"
```

Because every expression produces a value, you can nest expressions inside other expressions:
```python
total = (5 + 3) * len("cat")  # (8) * 3 = 24
```

---

## 3. Statements: Complete Instructions That Do Something

A **statement** is an entire instruction that changes program state or controls the flow of execution:

```python
x = 10            # Assignment statement (stores 10 in x)
if x > 5:         # If statement (makes a decision)
    print("Big")  
for i in range(3):# Loop statement (repeats actions)
    print(i)
import math       # Import statement (loads a module)
```

A statement does **not** evaluate to a value. For example, you cannot do this:
```python
# INVALID PYTHON:
print(x = 10)     # SyntaxError! An assignment is a statement, not a value.
```

### Why Did Python Make Assignment a Statement?
In languages like C or JavaScript, assignment `=` is an expression. This leads to dangerous bugs where a developer accidentally types one `=` instead of two `==`:
```c
// Dangerous C code: accidentally assigns 0 to x instead of checking equality!
if (x = 0) { ... } 
```
Python makes this mistake impossible! If you type `if x = 0:` in Python, the compiler stops immediately with a `SyntaxError: invalid syntax. Maybe you meant '==' or ':='?`.

---

## 4. The Bridge: The Walrus Operator (`:=`)

What if you *want* to assign a value AND use it as an expression at the same time?

In Python 3.8, the **Walrus Operator** (`:=`) was introduced as an **assignment expression**:

```python
# Without walrus operator (two steps):
line = input("Enter something: ")
while line != "quit":
    print(f"You typed: {line}")
    line = input("Enter something: ")

# With walrus operator (one step!):
while (line := input("Enter something: ")) != "quit":
    print(f"You typed: {line}")
```
Here, `(line := input(...))` assigns the input to `line` AND immediately returns the value so it can be compared to `"quit"`.

---

## 5. Summary Table

| Concept | What It Does | Can You Print It? | Examples |
| :--- | :--- | :--- | :--- |
| **Expression** | Calculates and returns a value | **Yes** (`print(5 + 3)`) | `5 + 3`, `x > 2`, `func()` |
| **Statement** | Performs an action or instruction | **No** (`print(if x: ...)` is invalid) | `x = 10`, `if/else`, `for`, `import` |
