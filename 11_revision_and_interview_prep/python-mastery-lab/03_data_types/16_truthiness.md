# Lesson 16: Truthiness and Truth-Value Testing

## 1. What Is "Truthiness" in Simple Words?
In Python, you don't only pass `True` or `False` to an `if` statement. You can pass **any object**!

When you write:
```python
if cart:
    print("You have items in your cart!")
```
Python automatically converts `cart` into a boolean. This concept is called **Truthiness**.

---

## 2. The Complete List of All "Falsy" Values in Python

Memorize this short list. Everything on this list evaluates to **`False`**:

1. **Constants**:
   - `None`
   - `False`
2. **Zero Numbers**:
   - `0` (integer zero)
   - `0.0` (float zero)
   - `0j` (complex zero)
3. **Empty Sequences and Collections**:
   - `""` (empty string)
   - `[]` (empty list)
   - `()` (empty tuple)
   - `{}` (empty dictionary)
   - `set()` (empty set)
   - `range(0)` (empty range)

> **The Universal Rule**: **EVERYTHING ELSE in Python evaluates to `True`!**  
> Any non-zero number (`-5`, `42`) is True. Any collection with at least one item is True.

---

## 3. Writing Clean, Idiomatic Python (PEP 8 Style)

Pythonic developers take advantage of truthiness to write elegant conditions:

### Example 1: Checking if a list is not empty
```python
# Beginner style (verbose):
if len(users) > 0:
    process_users()

# Pythonic style (clean & fast):
if users:
    process_users()
```

### Example 2: Checking if a string is empty
```python
# Beginner style:
if name == "":
    print("Name is required")

# Pythonic style:
if not name:
    print("Name is required")
```

---

## 4. The Dangerous Trap: When Zero Is a Valid Value!

Be very careful when an input could legitimately be `0`:

```python
discount = 0  # 0% discount is valid!

# BUGGY: 0 evaluates to False, so it mistakenly applies default 10%!
if not discount:
    discount = 10

print("Discount applied:", discount)  # Applied 10% instead of 0%!
```

### The Fix: Check for `None` explicitly!
```python
discount = 0

if discount is None:
    discount = 10

print("Discount applied:", discount)  # Correctly keeps 0%!
```

---

## 5. Quick Self-Test
1. What does `bool([0])` evaluate to?
   - *Answer: `True`! Even though the item inside is 0, the list itself is NOT empty!*
2. What does `bool("0")` evaluate to?
   - *Answer: `True`! Because the string is not empty.*
