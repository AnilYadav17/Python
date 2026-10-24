# Lesson 03: Logical Operators and De Morgan's Laws

## 1. The 3 Logical Operators
Python uses plain English words for logic instead of cryptic symbols like `&&`, `||`, and `!`:

| Operator | Plain English Meaning |
| :--- | :--- |
| **`and`** | `True` only if **BOTH** sides are true. |
| **`or`** | `True` if **AT LEAST ONE** side is true. |
| **`not`** | Flips the boolean: `not True` is `False`, `not False` is `True`. |

---

## 2. De Morgan's Laws: Cleaning Up Ugly Conditions

Have you ever looked at a confusing `if` condition like this?
```python
# Confusing:
if not (has_license and has_insurance):
    print("Cannot drive")
```

**De Morgan's Laws** give you a simple mathematical formula to flip and simplify negative conditions:

> 1. `not (A and B)` is identical to `(not A) or (not B)`
> 2. `not (A or B)` is identical to `(not A) and (not B)`

### Applying It in Practice:
```python
# Before (hard to read):
if not (is_weekend or is_holiday):
    wake_up_early()

# After applying De Morgan's Law (clear & readable!):
if not is_weekend and not is_holiday:
    wake_up_early()
```

---

## 3. Quick Self-Test
1. What does `not not True` evaluate to?
   - *Answer: `True` (double negative cancels out).*
2. How can you simplify `not (is_admin and is_verified)`?
   - *Answer: `not is_admin or not is_verified`.*
