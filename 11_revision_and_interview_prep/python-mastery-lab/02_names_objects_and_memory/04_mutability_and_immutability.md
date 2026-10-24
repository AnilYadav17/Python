# Lesson 04: Mutability vs. Immutability

## 1. What Is This in Simple Words?
Every object in Python falls into one of two camps:

1. **Mutable Objects**: Can be changed in-place without moving to a new memory address. (Like a whiteboard: you can erase and write new words, but it's still the same whiteboard).
2. **Immutable Objects**: **CANNOT** be changed once created. (Like a carved stone tablet: if you want a different message, you have to carve a completely new tablet!).

---

## 2. Which Types Are Mutable and Which Are Immutable?

| Category | Types | What Happens When You "Modify" It |
| :--- | :--- | :--- |
| **Immutable** (Unchangeable) | `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`, `bool`, `None` | Python **allocates a brand-new object** in memory and rebinds the name. |
| **Mutable** (Changeable) | `list`, `dict`, `set`, `bytearray` | Python **modifies the existing object** in-place at the exact same memory address. |

---

## 3. String Immutability in Action

Let's try to change the first letter of a string:
```python
greeting = "hello"
greeting[0] = "H"
```

**Python Output:**
```
TypeError: 'str' object does not support item assignment
```
Python prevents this! Strings are immutable. If you want `"Hello"`, you must build a new string:
```python
greeting = "hello"
print("Old ID:", id(greeting))

greeting = "H" + greeting[1:]  # Creates a new string "Hello"
print("New ID:", id(greeting))
```
Notice that `id(greeting)` changed! It is a brand-new object.

---

## 4. List Mutability in Action

Now let's do the exact same thing with a list:
```python
letters = ["h", "e", "l", "l", "o"]
print("Old ID:", id(letters))

letters[0] = "H"  # In-place change!
print("New ID:", id(letters))
print("Result:", letters)
```

**Output:**
```
Old ID: 1404561280
New ID: 1404561280
Result: ['H', 'e', 'l', 'l', 'o']
```
Notice that `id(letters)` stayed **identical**! The list was modified right where it lives in memory.

---

## 5. Why Does Immutability Matter?

1. **Dictionary Keys**: Dictionaries use hash tables. If a dictionary key could change its value while inside a dictionary, the dictionary would lose track of where it stored the data! That's why **only immutable objects (strings, numbers, tuples) can be used as dictionary keys**.
2. **Safety Across Functions**: If you pass an immutable object (like a string or tuple) into a function, you have a 100% guarantee that the function cannot secretly alter your data behind your back.

---

## 6. Quick Self-Test
1. Is a `tuple` mutable or immutable?
   - *Answer: Immutable.*
2. Can you put a `list` as a key in a Python dictionary?
   - *Answer: No! Lists are mutable (unhashable), so Python raises a `TypeError: unhashable type: 'list'`.*
