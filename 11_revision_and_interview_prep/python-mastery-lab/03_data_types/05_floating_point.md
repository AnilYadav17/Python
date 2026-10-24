# Lesson 05: Floating-Point Numbers (`float`) and Precision

## 1. The Classic Shock: `0.1 + 0.2 != 0.3`

Type this into any Python terminal:
```python
print(0.1 + 0.2 == 0.3)
```
What does Python print?  
**`False`!**

If you print the actual result:
```python
print(0.1 + 0.2)
# Output: 0.30000000000000004
```

### Is Python Broken?
**No!** Every modern computer and programming language (C, Java, JavaScript, Rust) behaves this exact same way.

---

## 2. Why Does This Happen? (Base 10 vs. Base 2)

- In our human decimal system (base 10), we cannot write $1/3$ cleanly: it becomes an infinite repeating fraction: `0.3333333...`.
- Computers do math in **binary (base 2)**. In binary, numbers like $1/10$ (`0.1`) and $1/5$ (`0.2`) become **infinite repeating fractions**:
  $$0.0001100110011001100..._2$$
- Because computers only have 64 bits to store a float (the IEEE 754 standard), they must cut off the repeating fraction at 53 bits.
- That microscopic rounding difference creates `0.30000000000000004`.

---

## 3. How to Compare Floats Safely: `math.isclose()`

> **Rule**: NEVER compare two floating-point numbers with `==`!

Instead, use Python's built-in **`math.isclose()`**:

```python
import math

a = 0.1 + 0.2
b = 0.3

# DANGEROUS:
print(a == b)  # False!

# PROFESSIONAL:
print(math.isclose(a, b))  # True! (Checks if they are equal within a tiny tolerance)
```

---

## 4. How to Handle Money and Banking: `decimal.Decimal`

If you are writing software that handles currency, bank accounts, or financial transactions, **never use `float`**.

Use Python's built-in **`decimal`** module, which performs exact human decimal arithmetic:

```python
from decimal import Decimal

# Always pass numbers as STRINGS to Decimal!
price1 = Decimal("0.1")
price2 = Decimal("0.2")

total = price1 + price2
print("Exact total:", total)  # 0.3
print(total == Decimal("0.3"))  # True! 100% exact!
```

---

## 5. Quick Self-Test
1. Why does `0.1 + 0.2` equal `0.30000000000000004` instead of `0.3`?
   - *Answer: Because 0.1 cannot be represented as a finite fraction in binary (base 2), leading to a microscopic rounding cutoff in 64-bit IEEE 754 float representation.*
2. How should you compare two floats in scientific or gaming code?
   - *Answer: Using `math.isclose(a, b)`.*
3. What standard library module should you use for exact money calculations?
   - *Answer: `from decimal import Decimal`.*
