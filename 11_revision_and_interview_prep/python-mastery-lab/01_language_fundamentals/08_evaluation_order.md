# Lesson 08: Evaluation Order and Short-Circuiting

## 1. Precedence vs. Evaluation Order (The Big Distinction)

Many programmers confuse these two concepts:
- **Operator Precedence** tells Python how to group operators into a tree (e.g., multiplication binds tighter than addition).
- **Evaluation Order** tells Python **which piece of code runs first in time**.

> **Python's Universal Law**: Python evaluates expressions strictly **from Left to Right**.

Let's verify this with a clear experiment:
```python
def first():
    print("1. Running first()")
    return 10

def second():
    print("2. Running second()")
    return 20

def third():
    print("3. Running third()")
    return 5

# Notice: multiplication has higher precedence than addition,
# but which function executes first?
total = first() + second() * third()
```

**Output:**
```
1. Running first()
2. Running second()
3. Running third()
```
Even though `second() * third()` must be multiplied before adding to `first()`, Python still evaluates `first()` **first in time** because it appears on the left!

---

## 2. Short-Circuit Evaluation: `and` and `or`

When evaluating logical conditions, Python is lazy in a very smart way:

### 1. The `and` Operator:
`A and B` needs **both** sides to be True.
- If `A` is False, Python doesn't even look at `B`! It immediately stops and returns `A`.
- If `A` is True, it evaluates and returns `B`.

### 2. The `or` Operator:
`A or B` needs **at least one** side to be True.
- If `A` is True, Python doesn't even look at `B`! It immediately stops and returns `A`.
- If `A` is False, it evaluates and returns `B`.

---

## 3. The Secret: `and` and `or` Return Objects, Not Just Booleans!

In many languages (like Java or C++), `&&` and `||` strictly return the boolean values `true` or `false`.

**In Python, `and` and `or` return the actual object that decided the outcome:**

```python
# 'or' returns the first Truthy value:
name = "" or "Guest"
print(name)  # Prints: "Guest" (because "" is falsy)

username = "Alice" or "Guest"
print(username)  # Prints: "Alice" (stops immediately at "Alice"!)

# 'and' returns the first Falsy value (or the last value if all are truthy):
val1 = 0 and "apple"
print(val1)  # Prints: 0 (stops immediately because 0 is falsy)

val2 = "apple" and "banana"
print(val2)  # Prints: "banana" (both are truthy, returns the last one evaluated)
```

---

## 4. How to Use Short-Circuiting Safely (Guards)

Because Python stops evaluating immediately when the result is known, you can protect against crashes:

```python
user = None

# If user is None, 'user is not None' is False.
# Python stops right there and NEVER calls user.get_name()!
# This prevents an AttributeError crash!
if user is not None and user.get_name() == "Admin":
    print("Welcome Admin")
```

---

## 5. Quick Self-Test
What will each of the following expressions return?
1. `"" or [] or 42 or "Hello"`
2. `True and 10 and None and "Python"`

**Answers:**
1. `42` (It skips the empty string and empty list because they are falsy, and stops at `42` which is truthy).
2. `None` (It evaluates `True` and `10` which are truthy, then hits `None` which is falsy, stopping immediately and returning `None`).
