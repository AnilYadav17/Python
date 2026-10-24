# Lesson 07: Identity Operators (`is` and `is not`)

## 1. What Are Identity Operators?
Identity operators check whether two variables point to the **exact same physical memory address in RAM**:

- **`a is b`**: Returns `True` if `id(a) == id(b)`.
- **`a is not b`**: Returns `True` if `id(a) != id(b)`.

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True (y points to x)
print(x is z)      # False (z is a separate object with the same values)
print(x is not z)  # True
```

---

## 2. When to Use `is` vs. `==` (Summary)

- **Use `==` when comparing values/data**:
  - `name == "Anil"`
  - `count == 10`
  - `items == [1, 2, 3]`

- **Use `is` ONLY when checking singletons**:
  - `result is None`
  - `flag is True`
  - `status is not None`

---

## 3. Quick Self-Test
1. Why does `[1] == [1]` evaluate to `True`, while `[1] is [1]` evaluates to `False`?
   - *Answer: Because `==` checks value equality (both lists contain the number 1), while `is` checks memory identity (they are two separate lists allocated at different RAM addresses).*
