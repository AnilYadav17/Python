# Lesson 11: Ranges (`range`) and Lazy Sequences

## 1. What Is a `range` in Simple Words?
A **`range`** represents an immutable sequence of numbers, commonly used for looping a specific number of times:

```python
# Print numbers from 0 to 4 (stop is EXCLUDED):
for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4
```

---

## 2. The 3 Forms of `range()`

```python
range(stop)               # Starts at 0, steps by 1
range(start, stop)        # Starts at 'start', steps by 1
range(start, stop, step)  # Starts at 'start', steps by 'step'
```

### Examples:
```python
print(list(range(2, 6)))        # [2, 3, 4, 5]
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]  (Even numbers)
print(list(range(5, 0, -1)))    # [5, 4, 3, 2, 1]  (Counting down)
```

---

## 3. The Miracle of Lazy Evaluation: $O(1)$ Memory!

In Python 2, `range(1000000)` created a list of 1 million numbers in RAM, consuming megabytes.

In Python 3, `range()` is **lazy**:
- It does **not** store numbers in memory!
- It only stores three tiny numbers: `start`, `stop`, and `step`.
- It calculates each number on the fly as the loop asks for it.

```python
import sys

small_range = range(10)
huge_range = range(1_000_000_000_000)  # 1 Trillion numbers!

print("Size of small range:", sys.getsizeof(small_range), "bytes")
print("Size of huge range: ", sys.getsizeof(huge_range), "bytes")
```
**Output:**
```
Size of small range: 48 bytes
Size of huge range:  48 bytes
```
Both take **48 bytes**! A range of 1 trillion numbers takes zero extra memory.

---

## 4. The Hidden Superpower: `in` on a Range Is $O(1)$ Fast!

If you check if a number is inside a list of 1 million items:
```python
999_999 in list_of_million_items  # SLOW! Must inspect all 1 million items one by one!
```

If you check if a number is inside a `range`:
```python
999_999 in range(1_000_000_000)  # INSTANT ($O(1)$)!
```
Why? Because Python doesn't loop! It uses basic grade-school math:
`start <= x < stop and (x - start) % step == 0`.

---

## 5. Quick Self-Test
1. What does `range(1, 5)` produce?
   - *Answer: 1, 2, 3, 4 (the stop number 5 is excluded).*
2. Does `range(10_000_000)` take more RAM than `range(10)`?
   - *Answer: No, both take 48 bytes because range computes values lazily.*
