# Lesson 10: Comprehensions (List, Dict, and Set)

## 1. What Is a Comprehension in Simple Words?
A **comprehension** is a concise, expressive way to transform or filter a collection in a single, readable line of code.

Instead of writing a 4-line loop with an empty list and `.append()`:
```python
# The Traditional Way (4 lines):
squares = []
for x in range(5):
    squares.append(x ** 2)

# The List Comprehension Way (1 clean line!):
squares = [x ** 2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]
```

---

## 2. Adding a Filter Condition (`if`)

You can filter items by putting an `if` at the end:
```python
# Formula: [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Only square the EVEN numbers:
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
```

---

## 3. Set and Dictionary Comprehensions

Comprehensions are not just for lists!

### 1. Set Comprehension:
```python
# Use curly brackets {} to collect unique items:
names = ["alice", "bob", "alice", "charlie"]
unique_lengths = {len(name) for name in names}
print(unique_lengths)  # {3, 5, 7}
```

### 2. Dictionary Comprehension:
```python
# Use key: value inside curly brackets:
users = ["Anil", "Bob", "Charlie"]
user_id_map = {name: index for index, name in enumerate(users, start=1)}
print(user_id_map)
# {'Anil': 1, 'Bob': 2, 'Charlie': 3}
```

---

## 4. Why Comprehensions Are Faster Than Loops
In CPython, a list comprehension runs significantly faster than a manual `for` loop with `list.append()`.  
Why? Because `list.append` has to look up the `.append` method on the list object on every single iteration. Comprehensions use a specialized C-level bytecode instruction (`LIST_APPEND`) that bypasses method lookup entirely!

---

## 5. Quick Self-Test
1. What does `[x for x in range(5) if x > 2]` produce?
   - *Answer: `[3, 4]`.*
2. How do you write a dictionary comprehension mapping numbers 1 to 3 to their cubes?
   - *Answer: `{x: x**3 for x in range(1, 4)}`.*
