# Lesson 02: None and NoneType

## 1. What Is `None` in Simple Words?
`None` is Python's way of saying: **"There is no value here."**

It is equivalent to `null` in Java/C/JavaScript or `nil` in Ruby/Go.

```python
middle_name = None  # The user has no middle name
```

---

## 2. The 3 Golden Rules of `None`

1. **Rule 1: `None` is a Singleton.**
   - In your entire computer's RAM, there is only **one single instance** of `None`.
   - Every time you write `None`, Python points to that same exact memory address.
   - Because it is a singleton, **always use `is` to check for it**:
     ```python
     if result is None:
         print("Nothing was found")
     ```

2. **Rule 2: Functions without a `return` return `None` automatically.**
   ```python
   def print_message():
       print("Hello!")

   output = print_message()
   print("Output is:", output)  # Output is: None
   ```

3. **Rule 3: `None` is Falsy in boolean conditions.**
   ```python
   data = None
   if not data:
       print("Data is empty or None")  # Runs!
   ```

---

## 3. The Most Common Use Case: Safe Default Arguments

Never use a mutable list or dictionary as a default function argument! Use `None` as a sentinel:

```python
# DANGEROUS:
# def add_item(item, items=[]): ...

# PROFESSIONAL & SAFE:
def add_item(item, items=None):
    if items is None:
        items = []  # Creates a fresh list every call!
    items.append(item)
    return items
```

---

## 4. Quick Self-Test
1. What is the type of `None`?
   - *Answer: `NoneType` (`type(None)`).*
2. Why is `if val is None:` better than `if val == None:`?
   - *Answer: It is faster (single pointer check) and cannot be tricked by custom classes overriding `__eq__`.*
