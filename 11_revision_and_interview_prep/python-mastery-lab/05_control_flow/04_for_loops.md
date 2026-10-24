# Lesson 04: For Loops, `enumerate()`, and `zip()`

## 1. What Is a For Loop in Python?
In languages like C or Java, a for loop is an arithmetic counter:
`for (int i = 0; i < 10; i++)`.

In Python, a **for loop is a Foreach Iterator**. It iterates directly over the items of any iterable (list, string, dictionary, file):

```python
languages = ["Python", "Rust", "Go"]
for lang in languages:
    print(f"I write {lang}")
```

---

## 2. The #1 For Loop Sin: Never Use `range(len(items))`!

A very common beginner habit from other languages:
```python
# UGLY & UNPYTHONIC:
items = ["apples", "bananas", "cherries"]
for i in range(len(items)):
    print(f"{i}: {items[i]}")
```

### The Clean Python Way: `enumerate()`
The built-in function `enumerate()` automatically gives you **both the index and the item** cleanly:

```python
# CLEAN & IDIOMATIC:
for i, item in enumerate(items, start=1):
    print(f"Item #{i}: {item}")
```

---

## 3. Pairing Two Lists Together: `zip()`

What if you have two related lists that you want to loop over simultaneously?

```python
students = ["Anil", "Alice", "Bob"]
scores = [95, 88, 92]

# zip() pairs items from both lists together:
for name, score in zip(students, scores):
    print(f"{name} scored {score}%")
```

---

## 4. Quick Self-Test
1. What does `enumerate(["a", "b"])` yield on each iteration?
   - *Answer: Tuples of `(index, item)`: `(0, 'a')`, then `(1, 'b')`.*
2. How does `zip()` handle lists of unequal lengths?
   - *Answer: It stops as soon as the shortest list runs out of items (use `itertools.zip_longest` if you want to keep going).*
