# Lesson 13.1: Collections & Itertools (Supercharging Data Manipulation)

## 1. What Is This in Simple Words?
Python comes with "batteries included" — you don't need to install external libraries for everyday data heavy-lifting. The `collections` and `itertools` modules provide high-speed, specialized tools written in optimized C to count, group, loop, and organize data without messy boilerplate code.

---

## 2. Essential Tools from `collections`

### A. `Counter`: Instant Frequency Counting
Instead of writing a loop with `if item in counts: counts[item] += 1`:
```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)

print(counts["apple"])           # 3
print(counts.most_common(2))     # [('apple', 3), ('banana', 2)]
```

### B. `defaultdict`: Never See a `KeyError` Again
A `defaultdict` automatically supplies a default value when you access a key that doesn't exist yet:
```python
from collections import defaultdict

# Group people by department
teams = defaultdict(list)  # default value factory is list()

teams["Engineering"].append("Anil")
teams["Engineering"].append("Sarah")
teams["Design"].append("Elena")

# No KeyError! Accessing an unused key returns [] automatically:
print(teams["Marketing"])  # []
```

### C. `namedtuple`: Lightweight Readable Tuples
Tuples with named fields that behave like lightweight, immutable objects without the overhead of a full class:
```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)  # 10 20 (Accessed by name instead of p[0], p[1])
```

---

## 3. Power Tools from `itertools`

`itertools` generates efficient memory-saving iterators implemented in C.

### A. `itertools.islice`: Slice Any Generator
You cannot slice a generator with `[0:10]` because it has no fixed length. `islice` lets you slice any stream without loading it into RAM:
```python
import itertools

# Infinite counter starting at 100
numbers = itertools.count(100, step=5)

# Take only the first 5 items:
first_five = list(itertools.islice(numbers, 5))
print(first_five)  # [100, 105, 110, 115, 120]
```

### B. `itertools.chain`: Glue Iterables Without Memory Allocation
Instead of creating a giant new list with `list_a + list_b`, `chain` yields items sequentially:
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for num in itertools.chain(list1, list2):
    print(num, end=" ")  # 1 2 3 4 5 6
```

---

## 4. Fascinating Fact 💡
> **The Secret of `defaultdict`'s `__missing__` Dunder**:
> When a standard Python dictionary cannot find a key, it checks if the class defines a special dunder method called **`__missing__(key)`**.  
> If `__missing__` exists, Python calls it instead of raising `KeyError`!  
> You can even subclass `dict` and define your own `__missing__` method to create custom auto-populating dictionaries without importing anything!

---

## 5. Quick Self-Test
1. Which collection class should you use to find the top 3 most frequent words in a text file?
   - *Answer: `collections.Counter.most_common(3)`.*
2. Why is `itertools.chain(a, b)` better than `a + b` for huge collections?
   - *Answer: `a + b` allocates a brand-new list in RAM copying all elements, while `chain()` iterates lazily in $O(1)$ memory.*
