# Lesson 04: Integers (`int`) and Arbitrary Precision

## 1. The Magic of Python Integers: No Overflow Ever!

In languages like C, C++, or Java:
- A 32-bit integer maxes out at `2,147,483,647`. If you add 1, it overflows and wraps around into a negative number (`-2,147,483,648`)!
- A 64-bit integer maxes out at $\approx 9 \times 10^{18}$.

> **In Python, integers NEVER overflow!**

Python uses **Arbitrary Precision Arithmetic** (often called "bignum"). An integer can have 10 digits, 100 digits, or 10,000 digits! It will grow to whatever size fits in your computer's RAM:

```python
# Calculate 2 to the power of 200:
huge_number = 2 ** 200
print(huge_number)
# Output: 1606938044258990275541962092341162602522202993782792835301376
# Perfectly calculated, zero overflow bugs!
```

---

## 2. Division: `/` vs. `//`

Python has two different division operators:

1. **True Division (`/`)**: Always returns a **`float`**, even if the numbers divide evenly:
   ```python
   print(10 / 2)   # 5.0 (float)
   print(7 / 2)    # 3.5 (float)
   ```

2. **Floor Division (`//`)**: Divides and rounds down to the nearest whole integer:
   ```python
   print(7 // 2)   # 3 (int)
   ```

---

## 3. The Negative Floor Division Trap

Look at this trap that trips up even experienced engineers:
```python
print(-7 // 2)
```
What is the answer? Is it `-3`?  
**The answer is `-4`!**

### Why?
Because "floor" in math means **round DOWN towards negative infinity**:
- $7 / 2 = 3.5 \to$ rounding down gives `3`.
- $-7 / 2 = -3.5 \to$ rounding down towards negative infinity gives **`-4`**!

---

## 4. Useful Built-in Integer Methods

Integers in Python are real objects with built-in methods:

```python
# 1. Find how many binary bits are needed to represent a number:
num = 255
print("Bits needed:", num.bit_length())  # 8 bits (11111111)

# 2. Convert an integer to raw bytes:
raw = (1024).to_bytes(2, byteorder='big')
print("Raw bytes:", raw)  # b'\x04\x00'
```

---

## 5. Quick Self-Test
1. Does Python crash with an integer overflow if you calculate `100 ** 100`?
   - *Answer: No, Python automatically allocates as much memory as needed.*
2. What does `-1 // 2` evaluate to?
   - *Answer: `-1` (because $-0.5$ floored down is $-1$).*
