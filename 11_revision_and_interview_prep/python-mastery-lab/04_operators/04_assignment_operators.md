# Lesson 04: Augmented Assignment and the Walrus Operator

## 1. What Is Augmented Assignment?
Instead of writing `x = x + 5`, Python lets you combine the arithmetic operator with the equals sign:
`x += 5`.

Python supports augmented assignments for all operations:
`+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.

---

## 2. Under the Hood: `__iadd__` vs. `__add__`

Why does this matter so much? Look at this huge performance difference on lists:

### Method 1: `list_a = list_a + [4]` (Slow)
```python
a = [1, 2, 3]
print("Old ID:", id(a))

a = a + [4]  # Calls __add__(): Allocates a BRAND-NEW list and copies all items!
print("New ID:", id(a))  # ID CHANGED!
```

### Method 2: `list_a += [4]` (Fast)
```python
a = [1, 2, 3]
print("Old ID:", id(a))

a += [4]     # Calls __iadd__(): Extends the EXISTING list in-place!
print("New ID:", id(a))  # ID IS IDENTICAL!
```
> **Rule**: For mutable collections like lists, `+=` modifies the object in-place without allocating a new list.

---

## 3. The Walrus Operator (`:=`) in Real Life

The walrus operator `:=` assigns a value to a variable **inside an expression**:

### Cleaning Up Regex / Pattern Matching:
```python
import re

text = "User ID: 94821"

# Without walrus:
match = re.search(r"\d+", text)
if match:
    print("Found ID:", match.group())

# With walrus:
if match := re.search(r"\d+", text):
    print("Found ID:", match.group())
```

---

## 4. Quick Self-Test
1. In `items = [1, 2]`, does `items += [3]` create a new list in memory?
   - *Answer: No, it mutates the existing list in-place via `__iadd__`.*
2. Why is `:=` nicknamed the Walrus operator?
   - *Answer: Because the colon and equals sign `:=` look like the eyes and tusks of a walrus sideways!*
