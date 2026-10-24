# Lesson 08: Unary Operators

## 1. What Is a Unary Operator?
Most operators (like `+`, `-`, `*`) are **binary operators** because they operate on two things: `5 + 3`.

A **unary operator** acts on **one single operand**:

| Unary Operator | Name | Example | Explanation |
| :--- | :--- | :--- | :--- |
| `+` | Unary Positive | `+x` | Returns `x` as-is (rarely used, but calls `__pos__`). |
| `-` | Unary Negative | `-x` | Negates the number (`-5`, calls `__neg__`). |
| `~` | Bitwise NOT | `~x` | Inverts bits: `-(x + 1)` (calls `__invert__`). |
| `not` | Logical NOT | `not x` | Inverts truthiness: `not True` is `False`. |

---

## 2. The Curious Case of `~` (Bitwise Invert)

In Python, numbers are represented using Two's Complement.  
When you invert a number with `~`:
$$\sim x = -(x + 1)$$

```python
print(~0)   # -1
print(~5)   # -6
print(~-1)  # 0
```

---

## 3. Quick Self-Test
1. What does `-(-10)` evaluate to?
   - *Answer: `10`.*
2. What method does `-x` trigger on custom objects?
   - *Answer: `x.__neg__()`.*
