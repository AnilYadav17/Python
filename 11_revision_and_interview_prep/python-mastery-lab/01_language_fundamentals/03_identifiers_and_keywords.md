# Lesson 03: Identifiers and Keywords

## 1. What Is an Identifier?
An **identifier** is simply a name that you (the programmer) invent to label something in your code—like a variable, a function, or a class.

```python
user_age = 25          # 'user_age' is an identifier
def calculate_area():  # 'calculate_area' is an identifier
    pass
```

---

## 2. The 5 Strict Rules for Naming Identifiers
Python will reject your code with a `SyntaxError` if you break any of these rules:

1. **Rule 1: Can only contain letters (`a-z`, `A-Z`), digits (`0-9`), and underscores (`_`).**
   - No spaces, no hyphens (`-`), and no special symbols (`@`, `$`, `%`, `!`).
   - `user_name` (Valid)
   - `user-name` (Invalid! Python thinks you are subtracting `name` from `user`).

2. **Rule 2: Cannot start with a digit.**
   - `player1` (Valid)
   - `1player` (Invalid! Raises `SyntaxError`).

3. **Rule 3: Case-sensitive.**
   - `score`, `Score`, and `SCORE` are **three completely different variables** in Python. Be careful with typos!

4. **Rule 4: Cannot be a reserved keyword.**
   - You cannot name a variable `for`, `while`, `class`, or `def` because Python needs those words for its own grammar.

5. **Rule 5: Can start with an underscore (`_`).**
   - `_hidden` or `__secret` are valid. In Python, a starting underscore is a convention that tells other developers: *"This is private or internal, don't touch it directly."*

---

## 3. What Are Keywords?
**Keywords** are Python’s reserved vocabulary. They have fixed, built-in meanings and cannot be used as variable names.

You can see all of them anytime inside Python:
```python
import keyword

print("Total Python Keywords:", len(keyword.kwlist))
print(keyword.kwlist)
```

In modern Python, there are 35 keywords:
```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

### Notice:
Only three keywords start with a Capital letter:
1. `True`
2. `False`
3. `None`
All other keywords are completely lowercase.

---

## 4. PEP 8 Naming Conventions (Professional Style)
In the Python community, we follow official guidelines (PEP 8) so everyone's code looks clean and uniform:

| Category | Style | Example |
| :--- | :--- | :--- |
| **Variables** | `snake_case` (lowercase with underscores) | `item_count`, `total_price` |
| **Functions** | `snake_case` | `calculate_discount()`, `fetch_user()` |
| **Classes** | `PascalCase` (Capitalize each word) | `UserProfile`, `BankAccount` |
| **Constants** | `UPPER_CASE` (All capitals) | `MAX_CONNECTIONS = 100`, `PI = 3.14159` |

---

## 5. Quick Self-Test
Which of the following variable names are **invalid** in Python and why?
1. `first_name`
2. `2nd_place`
3. `user-email`
4. `class`
5. `total_`

**Answers:**
- `2nd_place` is invalid (starts with a number).
- `user-email` is invalid (contains a hyphen `-`).
- `class` is invalid (it is a reserved keyword).
- `first_name` and `total_` are 100% valid.
