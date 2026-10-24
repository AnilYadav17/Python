# Lesson 10: Tuples (`tuple`)

## 1. What Is a Tuple in Simple Words?
A **tuple** is an ordered, **immutable** sequence of items.

Think of a tuple as a list that has been sealed in epoxy: once created, you cannot add, remove, or reorder elements.

```python
point = (10, 20)
rgb = (255, 128, 0)
```

---

## 2. The #1 Beginner Trap: Commas Create Tuples, Not Parentheses!

Look closely at this code:
```python
x = (42)
print(type(x))  # <class 'int'>! NOT A TUPLE!
```
Why? Because parentheses `()` are also used for math expressions like `(5 + 3)`.

> **Rule: In Python, the COMMA `,` makes a tuple, not the parentheses!**

To create a tuple with a single item, **you MUST add a trailing comma**:
```python
single_item_tuple = (42,)
print(type(single_item_tuple))  # <class 'tuple'>
```

---

## 3. Why Use a Tuple Instead of a List?

1. **Safety**: Nobody can accidentally modify your data.
2. **Hashable**: A tuple can be used as a **dictionary key** or stored in a **set** (as long as everything inside the tuple is also immutable). A list cannot!
   ```python
   # Valid dictionary key:
   locations = {(40.7128, -74.0060): "New York City"}
   ```
3. **Memory and Speed**: Tuples take less memory than lists because they don't need empty over-allocated slots.

---

## 4. Tuple Unpacking: A Clean Superpower

You can unpack tuple values directly into separate variable names in one line:

```python
user_info = ("Anil", "Engineer", "Ubuntu")

name, role, os_name = user_info
print(f"{name} is an {role} on {os_name}.")

# Swapping variables without a temporary variable:
a = 10
b = 20
a, b = b, a  # Under the hood, this packs (b, a) into a tuple and unpacks it!
```

---

## 5. Quick Self-Test
1. What is the type of `t = (100)`?
   - *Answer: `int` (to make it a tuple, write `(100,)`).*
2. Can a tuple containing a list `(1, [2, 3])` be used as a dictionary key?
   - *Answer: No! Even though the tuple is immutable, the list inside it is mutable, making the entire tuple unhashable.*
