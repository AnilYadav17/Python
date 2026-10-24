# Lesson 05: Bitwise Operators and Bitmasks

## 1. What Are Bitwise Operators?
Computers store everything as binary bits (`0`s and `1`s). 

**Bitwise operators** allow you to manipulate individual binary bits directly:

| Operator | Name | What It Does | Example (Binary) |
| :--- | :--- | :--- | :--- |
| `&` | Bitwise AND | `1` only if both bits are `1` | `0b1100 & 0b1010 = 0b1000` |
| `\|` | Bitwise OR | `1` if at least one bit is `1` | `0b1100 \| 0b1010 = 0b1110` |
| `^` | Bitwise XOR | `1` if bits are DIFFERENT | `0b1100 ^ 0b1010 = 0b0110` |
| `~` | Bitwise NOT | Flips all bits | `~x = -(x + 1)` |
| `<<` | Left Shift | Shifts bits left (multiplies by $2^n$) | `5 << 1 = 10` |
| `>>` | Right Shift | Shifts bits right (divides by $2^n$) | `20 >> 2 = 5` |

---

## 2. Real-World Use Case: Permission Bitmasks

In systems programming (like Linux file permissions `rwxr-xr-x`), permissions are packed into single bits to save space:

```python
# Define permission flags using binary:
READ    = 0b100  # 4
WRITE   = 0b010  # 2
EXECUTE = 0b001  # 1

# 1. Grant Read and Write permission using Bitwise OR (|):
user_perms = READ | WRITE  # 0b110 (6)

# 2. Check if user has WRITE permission using Bitwise AND (&):
can_write = (user_perms & WRITE) != 0
print("Can write?", can_write)  # True

# 3. Check if user has EXECUTE permission:
can_exec = (user_perms & EXECUTE) != 0
print("Can execute?", can_exec)  # False
```

---

## 3. Fast Multiplication and Division with Shifts

- `x << 1`: Shifts binary bits 1 position to the left $\to$ **multiplies by 2**.
- `x << 2`: Shifts 2 positions $\to$ **multiplies by 4** ($2^2$).
- `x >> 1`: Shifts 1 position to the right $\to$ **divides by 2** (floor).

```python
print(15 << 1)  # 30
print(40 >> 2)  # 10
```

---

## 4. Quick Self-Test
1. What does `7 & 1` evaluate to, and why is this useful?
   - *Answer: `1`. Checking `n & 1` is a lightning-fast hardware-level check to see if a number is odd (returns 1) or even (returns 0).*
2. What does `5 ^ 5` evaluate to?
   - *Answer: `0` (XORing any number with itself always produces zero because identical bits cancel out).*
