# Predict The Output: 5 Mind-Bending Python Quirks

Can you predict what each snippet outputs before opening the solution?

---

### Challenge 1: Chained Comparisons
```python
print(False == False in [False])
```
<details>
<summary>Click to reveal answer</summary>

**Output**: `True`  
**Why**: Python chains comparisons! `False == False in [False]` does **NOT** evaluate as `(False == False) in [False]` (which would be `True in [False]` -> False). Instead, Python evaluates it as:  
`(False == False) and (False in [False])`  
Both expressions are `True`, so `True and True` returns `True`!
</details>

---

### Challenge 2: The List Multiplication Identity Trap
```python
grid = [[0] * 3] * 3
grid[0][0] = 99
print(grid)
```
<details>
<summary>Click to reveal answer</summary>

**Output**: `[[99, 0, 0], [99, 0, 0], [99, 0, 0]]`  
**Why**: The outer `* 3` does not copy the inner list; it creates a list with 3 references to the **exact same inner list** in memory (`grid[0] is grid[1] is grid[2]`). Modifying one modifies all three!  
*Correct idiom*: `grid = [[0] * 3 for _ in range(3)]`.
</details>

---

### Challenge 3: Boolean Arithmetic
```python
print(True + True)
print(isinstance(True, int))
```
<details>
<summary>Click to reveal answer</summary>

**Output**:
```
2
True
```
**Why**: In Python, `bool` is a direct subclass of `int` (`issubclass(bool, int) is True`). `True` is an integer `1` and `False` is an integer `0`.
</details>

---

### Challenge 4: Short-Circuit Return Values
```python
print([] or 42)
print("apple" and "banana")
```
<details>
<summary>Click to reveal answer</summary>

**Output**:
```
42
banana
```
**Why**: Python's `and` and `or` logical operators do **not** return boolean `True` or `False`. They return the actual operand that determined the truth value! For `or`, it returns the first truthy value. For `and`, if the left side is truthy, it returns the right side.
</details>

---

### Challenge 5: Scope Shadowing Inside Functions
```python
x = 10
def test():
    print(x)
    x = 20

test()
```
<details>
<summary>Click to reveal answer</summary>

**Output**: `UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`  
**Why**: Python inspects function bodies at compile time. Because `x = 20` assigns to `x`, Python marks `x` as a local variable for the entire function scope. When `print(x)` runs before the assignment, Python refuses to fall back to the global `x` and raises `UnboundLocalError`!
</details>
