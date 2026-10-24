# Lesson 11: Control Flow Traps and Misconceptions

## 1. The Deadly Trap: Mutating a List While Looping Over It!

Look at this innocent-looking code. We want to remove all even numbers from a list:

```python
numbers = [1, 2, 4, 5, 6]

for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)

print("Result:", numbers)
```
What is the result? You would expect `[1, 5]`.  
**Actual Result: `[1, 4, 5]`! The number 4 was completely skipped! Why?!**

### The Mechanism:
- Under the hood, Python keeps an index counter: `0, 1, 2, ...`
- At index 1, Python sees `2` and removes it.
- When `2` is removed, the remaining numbers **shift one slot to the left**: `4` moves into index 1!
- On the next cycle, the loop counter advances to **index 2** (which now holds `5`), completely stepping over `4`!

```
Iteration 0: index 0 is 1. (Keep)
Iteration 1: index 1 is 2. (Remove 2! List becomes [1, 4, 5, 6])
Iteration 2: index 2 is 5! (4 was at index 1, so it was never inspected!)
```

### The 2 Correct Ways to Fix This:

1. **Iterate over a shallow copy (`[:]`)**:
   ```python
   for n in numbers[:]:  # Loops over the snapshot, mutates the original
       if n % 2 == 0:
           numbers.remove(n)
   ```

2. **Use a List Comprehension (Fastest & Cleanest)**:
   ```python
   numbers = [n for n in numbers if n % 2 != 0]
   ```

---

## 2. Modifying a Dictionary During Iteration

What happens if you try to delete or add keys to a dictionary while looping over it?

```python
data = {"a": 1, "b": 2, "c": 3}

for key in data:
    if key == "b":
        del data[key]
```
**Python Output:**
```
RuntimeError: dictionary changed size during iteration
```
Python explicitly forbids changing a dictionary's size while looping over it!

### The Fix:
Loop over a copy of the keys using `list(data.keys())`:
```python
for key in list(data.keys()):
    if key == "b":
        del data[key]
```

---

## 3. Quick Self-Test
1. Why did `numbers.remove(n)` skip elements during a `for n in numbers:` loop?
   - *Answer: Because removing an element shifts the remaining elements to the left, while the loop's internal index continues moving to the right.*
2. What error is raised if you delete a key from a dict while iterating over it directly?
   - *Answer: `RuntimeError: dictionary changed size during iteration`.*
