# Lesson 02: Assignment, Binding, and Rebinding

## 1. What Does `=` Really Do in Python?
In Python, the equals sign `=` is called the **assignment operator**, but its real name is **Name Binding**:

> **Assignment does NOT copy values. Assignment binds a name to an existing object.**

When Python executes `x = 500`:
1. It creates an integer object `500` in memory.
2. It takes the label `'x'` and binds it to that object.

---

## 2. Rebinding vs. Mutating

What happens when you run this?
```python
x = 10
x = 20
```
Did the number `10` transform into `20`? **No!**
- First, the tag `'x'` was attached to object `10`.
- Then, the tag `'x'` was peeled off and stuck onto a new object `20`.
- This is called **rebinding**. The old object `10` is left behind in memory (and cleaned up if nothing else points to it).

---

## 3. The Chained Assignment Trap: `a = b = []`

A common beginner mistake is writing:
```python
# You think you created two separate empty shopping carts:
cart1 = cart2 = []

# You add an apple to cart1:
cart1.append("apple")

# Now look at cart2:
print(cart2)  # Prints: ['apple']! Why?!
```

### Why Did This Happen?
Because `cart1 = cart2 = []` evaluated `[]` **only once**. Both names were bound to the exact same list in memory!

```
   cart1 -----\
               +----> [ 'apple' ]
   cart2 -----/
```

### The Correct Way:
If you want two separate lists, create them separately:
```python
cart1 = []
cart2 = []
cart1.append("apple")
print(cart2)  # Prints: [] (completely safe!)
```

---

## 4. Augmented Assignment: `+=` on Numbers vs. Lists

Does `x += y` mean `x = x + y`? **Not always!**

1. **For immutable objects (Numbers, Strings, Tuples)**:
   ```python
   x = 5
   x += 1  # Rebinds x to a brand-new integer 6
   ```

2. **For mutable objects (Lists)**:
   ```python
   items = [1, 2, 3]
   items += [4]  # Does NOT create a new list! It calls items.extend([4]) in-place!
   ```

---

## 5. The Ultimate Python Trap: Modifying a List Inside a Tuple

Can you modify an item inside a tuple? Tuples are immutable! Look at this bizarre experiment:

```python
t = (1, 2, [10, 20])

try:
    t[2] += [30]
except TypeError as e:
    print("Caught error:", e)

print("What is inside t now?", t)
```

**Output:**
```
Caught error: 'tuple' object does not support item assignment
What is inside t now? (1, 2, [10, 20, 30])
```

### Why Did It Crash AND Still Modify the List?!
Here is what happened under the hood:
1. `t[2]` points to the mutable list `[10, 20]`.
2. Python executes `+= [30]` in-place on that list object $\to$ the list becomes `[10, 20, 30]`. (Success!)
3. Then Python tries to reassign the result back to `t[2]`.
4. But `t` is a tuple, and tuples forbid assignment! So Python raises a `TypeError`!
5. **Result**: The list in memory WAS updated, but an exception was still thrown.

---

## 6. Quick Self-Test
1. In `a = [1]`, `b = a`, `b = b + [2]`, does `a` change?
   - *Answer: No! `b + [2]` creates a brand-new list `[1, 2]` and rebinds `b` to it. `a` still points to `[1]`.*
2. In `a = [1]`, `b = a`, `b += [2]`, does `a` change?
   - *Answer: YES! `+=` on a list mutates the object in-place. Both `a` and `b` will show `[1, 2]`!*
