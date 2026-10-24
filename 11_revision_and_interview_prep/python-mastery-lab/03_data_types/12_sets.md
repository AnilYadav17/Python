# Lesson 12: Sets (`set`) and Frozensets (`frozenset`)

## 1. What Is a Set in Simple Words?
A **set** is an unordered collection of **unique, hashable elements**.

Think of a set as a bag of items where:
1. **Duplicates are automatically thrown away.**
2. **Items have no index order** (you cannot do `my_set[0]`).
3. **Checking if an item exists (`x in my_set`) is practically instantaneous ($O(1)$)**.

```python
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)  # Output: {1, 2, 3, 4}  (Duplicates removed automatically!)
```

---

## 2. The #1 Set Trap: The Empty Set Syntax

How do you create an empty set?

```python
empty = {}  # WARNING: THIS CREATES AN EMPTY DICTIONARY!
print(type(empty))  # <class 'dict'>
```
Because dictionaries were invented first in Python, `{}` is reserved for empty dicts.

> **Rule: To create an empty set, you MUST call `set()`:**
```python
real_empty_set = set()
print(type(real_empty_set))  # <class 'set'>
```

---

## 3. Mathematical Set Operations (Venn Diagrams in Code)

Python sets have built-in operators that correspond to mathematical set theory:

```python
team_python = {"Anil", "Alice", "Bob"}
team_rust = {"Bob", "Charlie", "Dave"}

# 1. Union (|): Everyone in either team
print(team_python | team_rust)
# {'Anil', 'Alice', 'Bob', 'Charlie', 'Dave'}

# 2. Intersection (&): People in BOTH teams
print(team_python & team_rust)
# {'Bob'}

# 3. Difference (-): In Python team, but NOT in Rust team
print(team_python - team_rust)
# {'Anil', 'Alice'}

# 4. Symmetric Difference (^): In ONE team, but NOT in both
print(team_python ^ team_rust)
# {'Anil', 'Alice', 'Charlie', 'Dave'}
```

---

## 4. Why Sets Are 10,000x Faster Than Lists for Lookups

If you need to check whether an ID exists in a collection of 1,000,000 users:

```python
# In a list: O(N) linear scan
target in user_list  # Must compare with up to 1,000,000 items!

# In a set: O(1) hash table lookup
target in user_set   # Instantaneous! Jumps directly to memory address!
```

---

## 5. What Is a `frozenset`?

A regular `set` is mutable (you can `.add()` or `.remove()`).  
Because it is mutable, you cannot put a set inside another set!

A **`frozenset`** is the immutable version of a set:
```python
# You can put frozensets inside a regular set:
group_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
```

---

## 6. Quick Self-Test
1. What does `type({})` evaluate to?
   - *Answer: `<class 'dict'>` (use `set()` for an empty set).*
2. What is the time complexity of `item in my_set`?
   - *Answer: $O(1)$ constant time on average.*
