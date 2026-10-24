# Lesson 08: Shallow Copy vs. Deep Copy

## 1. The Problem: Duplicating Data Safely

Earlier we learned that writing `b = a` does **not** copy a list—it just creates a second name (alias) for the same list.

So how do you actually make a real copy of a list or dictionary?

Python gives you two types of copies:
1. **Shallow Copy**
2. **Deep Copy**

---

## 2. Shallow Copy: Copying the Outer Shell

A **shallow copy** creates a brand-new outer container, but **copies references to the items inside it**.

You can make a shallow copy using:
- `.copy()` method on lists or dicts: `b = a.copy()`
- The slice operator: `b = a[:]`
- The `copy` module: `import copy; b = copy.copy(a)`

### Where Shallow Copy Works Perfectly (Flat Lists):
```python
original = [1, 2, 3]
shallow = original.copy()

shallow.append(99)
print("Original:", original)  # [1, 2, 3] (Safe!)
print("Shallow: ", shallow)   # [1, 2, 3, 99]
```

### The Shallow Copy Trap (Nested Lists):
Look what happens when the list contains another list inside it!
```python
cart = [["Apples", 5], ["Bread", 2]]
shallow_cart = cart.copy()

# Modify the nested list (change Apples quantity from 5 to 100):
shallow_cart[0][1] = 100

print("Original Cart:", cart)
# Output: [['Apples', 100], ['Bread', 2]]  <- OOPS! Original changed too!
```

### Why Did That Happen?
Because a shallow copy only made a new outer list. The items inside `cart[0]` still pointed to the **exact same inner list**!

```
Original Cart ----> [ Address A, Address B ]
                          |           |
                          v           v
                    ['Apples', 5]  ['Bread', 2]
                          ^
                          |
Shallow Cart  ----> [ Address A, Address B ]
```

---

## 3. Deep Copy: Copying Everything All the Way Down

A **deep copy** creates a new outer container AND recursively creates new copies of **every single nested object inside it**.

Use the standard library `copy.deepcopy()`:

```python
import copy

cart = [["Apples", 5], ["Bread", 2]]
deep_cart = copy.deepcopy(cart)

# Now modify the deep copy:
deep_cart[0][1] = 999

print("Original Cart:", cart)
# Output: [['Apples', 5], ['Bread', 2]]  <- 100% UNTOUCHED AND SAFE!

print("Deep Cart:    ", deep_cart)
# Output: [['Apples', 999], ['Bread', 2]]
```

```
Original Cart ----> [ Address A ] ----> ['Apples', 5]

Deep Cart     ----> [ Address X ] ----> ['Apples', 999]
```

---

## 4. Summary Table

| Method | Syntax | Outer Container | Nested Objects |
| :--- | :--- | :--- | :--- |
| **Reference Assignment** | `b = a` | Shared (Same ID) | Shared |
| **Shallow Copy** | `b = a.copy()` | **New Object** | Shared |
| **Deep Copy** | `b = copy.deepcopy(a)` | **New Object** | **New Objects (Recursively duplicated)** |

---

## 5. Quick Self-Test
1. If you have a simple list of numbers `nums = [10, 20, 30]`, is a shallow copy enough to be safe?
   - *Answer: Yes, because numbers are immutable.*
2. When MUST you use `copy.deepcopy()`?
   - *Answer: When your data structure contains nested mutable objects (e.g., lists of lists, dicts containing lists).*
