# Lesson 07: `break`, `continue`, and `pass`

## 1. What Are These Statements?
These three keywords give you fine-grained control inside loops and blocks:

| Keyword | What It Does |
| :--- | :--- |
| **`break`** | Exits (terminates) the loop **immediately**. No more iterations run. |
| **`continue`** | Skips the rest of the **current iteration** and jumps directly to the next cycle. |
| **`pass`** | Does **nothing at all**. It is a syntactic placeholder where code is expected. |

---

## 2. Examples in Action

### 1. `break`: Finding a Target and Stopping Early
```python
numbers = [10, 25, 42, 60, 80]

for n in numbers:
    if n == 42:
        print("Found the target 42! Stopping search.")
        break
    print("Checking:", n)
```

### 2. `continue`: Skipping Unwanted Items
```python
for n in range(6):
    if n % 2 == 0:
        continue  # Skip even numbers!
    print("Odd number:", n)
# Output: 1, 3, 5
```

### 3. `pass`: An Empty Placeholder
In Python, you cannot leave a function or loop completely empty (it causes an `IndentationError`). Use `pass`:
```python
def todo_later():
    pass  # Will implement tomorrow! Code runs without errors.
```

---

## 3. Quick Self-Test
1. What is the difference between `break` and `continue`?
   - *Answer: `break` kills the entire loop completely; `continue` skips only the current iteration and keeps the loop running.*
