# Lesson 07: Positional-Only (`/`) and Keyword-Only (`*`) Parameters

## 1. Controlling How Callers Pass Arguments

In basic Python, any argument can be passed positionally OR by keyword:
```python
def greet(name, age):
    pass

greet("Alice", 25)          # Positional
greet(name="Alice", age=25) # Keyword
```

Modern Python gives you two special boundary markers to enforce strict rules:
1. **`/` (Slash)**: Enforces **Positional-Only** parameters (everything BEFORE `/` CANNOT use keywords).
2. **`*` (Asterisk)**: Enforces **Keyword-Only** parameters (everything AFTER `*` MUST use keywords).

---

## 2. The Universal Parameter Syntax Diagram

```
def func(pos_only1, pos_only2, /, standard, *, kw_only1, kw_only2):
         |__________________|      |           |________________|
           Positional-Only       Standard         Keyword-Only
         (Keywords forbidden!)  (Either way)   (Must use keyword!)
```

---

## 3. Why Use Keyword-Only Parameters (`*`)?

Consider this function call:
```python
# Unclear: What does True mean here?!
create_user("anil", "secret_pass", True, False)
```
Nobody reading this code knows what `True` and `False` do without opening the documentation.

### The Fix: Force Keywords with `*`
```python
def create_user(username, password, *, is_admin=False, send_welcome_email=True):
    pass

# Calling with positional arguments raises TypeError!
# create_user("anil", "secret_pass", True, False) # TypeError!

# Callers are FORCED to be explicit:
create_user("anil", "secret_pass", is_admin=True, send_welcome_email=False)
```
Now the code is 100% self-documenting and safe!

---

## 4. Why Use Positional-Only Parameters (`/`)?

1. **Parameter names don't matter**: In math functions like `pow(x, y)` or `abs(x)`, the parameter name `x` is meaningless. Forcing positional-only prevents callers from locking in on the arbitrary name `x=...`.
2. **Freedom to rename**: If callers cannot use `func(my_arg=5)`, you can safely rename `my_arg` in future library updates without breaking any user code!

```python
def calculate_vat(amount, rate, /):
    return amount * rate

# Valid:
calculate_vat(100, 0.20)

# Invalid!
# calculate_vat(amount=100, rate=0.20)
# TypeError: calculate_vat() got some positional-only arguments passed as keyword arguments
```

---

## 5. Quick Self-Test
1. In `def f(a, /, b, *, c):`, which argument is keyword-only?
   - *Answer: `c` (because it appears after the `*`).*
2. Which argument in `def f(a, /, b, *, c):` is positional-only?
   - *Answer: `a` (because it appears before the `/`).*
