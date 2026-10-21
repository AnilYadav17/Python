# Day 27: Advanced Collections

## Explanation
The `collections` module provides specialized container datatypes beyond the built-in dict, list, set, and tuple.

## Key Concepts
- **`Counter`**: Dict subclass for counting hashable objects.
- **`defaultdict`**: Dict that calls a factory function to supply missing values.
- **`namedtuple`**: Tuple subclass with named fields.

## Code Example
```python
from collections import Counter, namedtuple

# Counter
words = ['apple', 'banana', 'apple', 'orange']
counts = Counter(words)
print(counts) # Counter({'apple': 2, 'banana': 1, 'orange': 1})

# NamedTuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x) # 10
```

## Task
Use a `Counter` to find the top 3 most common words in a long string of text.