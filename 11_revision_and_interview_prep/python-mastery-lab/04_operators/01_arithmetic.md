# Lesson 01: Arithmetic Operators

## 1. What Are Arithmetic Operators?
Arithmetic operators perform mathematical calculations:

| Operator | Name | Example | Result |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | True Division | `10 / 4` | `2.5` (Always returns `float`) |
| `//` | Floor Division | `10 // 4` | `2` (Rounds down to integer) |
| `%` | Modulo (Remainder) | `10 % 4` | `2` |
| `**` | Exponentiation (Power) | `2 ** 3` | `8` ($2 \times 2 \times 2$) |

---

## 2. Modulo (`%`): The Clock Arithmetic Operator

The modulo operator `%` calculates the **remainder** after integer division:
```python
print(14 % 5)  # 4 (because 14 = 5 * 2 + 4)
```

### The 2 Most Useful Real-World Uses of `%`:

1. **Checking Even vs. Odd Numbers**:
   ```python
   def is_even(n):
       return n % 2 == 0
   ```

2. **Cycling / Wrapping Around (Like Hours on a Clock)**:
   ```python
   # If it is 10:00 AM, what time will it be in 5 hours on a 12-hour clock?
   hour = (10 + 5) % 12
   print("New hour:", hour)  # 3:00
   ```

---

## 3. Floor Division with Negative Numbers

Remember the negative floor division rule:
```python
print(-10 // 3)  # -4 (NOT -3!)
```
Because $-10 / 3 = -3.333...$, flooring rounds **down** towards $-\infty$, which gives **`-4`**.

---

## 4. Quick Self-Test
1. What does `11 % 3` evaluate to?
   - *Answer: `2` (because $3 \times 3 = 9$, remainder is $2$).*
2. What does `7 / 2` evaluate to vs `7 // 2`?
   - *Answer: `7 / 2` is `3.5` (float), `7 // 2` is `3` (int).*
