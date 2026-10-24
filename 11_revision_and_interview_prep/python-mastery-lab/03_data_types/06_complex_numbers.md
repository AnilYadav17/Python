# Lesson 06: Complex Numbers (`complex`)

## 1. What Is a Complex Number in Simple Words?
In basic math, you cannot take the square root of a negative number like $\sqrt{-1}$.  
In advanced mathematics and electrical engineering, mathematicians invented the imaginary number $i = \sqrt{-1}$ to make these calculations possible.

Python has built-in support for complex numbers! In Python, we use the letter **`j`** (standard in electrical engineering) instead of $i$:

```python
z = 3 + 4j  # 3 is the Real part, 4 is the Imaginary part
```

---

## 2. Inspecting and Operating on Complex Numbers

```python
z = 3 + 4j

# 1. Access parts:
print("Real part:     ", z.real)  # 3.0 (always a float)
print("Imaginary part:", z.imag)  # 4.0 (always a float)

# 2. Conjugate (flips the sign of the imaginary part: 3 - 4j):
print("Conjugate:     ", z.conjugate())  # (3-4j)

# 3. Magnitude (Absolute value: sqrt(3^2 + 4^2) = 5.0):
print("Magnitude:     ", abs(z))  # 5.0
```

---

## 3. Math with Complex Numbers
You can add, subtract, multiply, and divide them like normal numbers:
```python
z1 = 2 + 3j
z2 = 1 - 2j

print(z1 + z2)  # (3+1j)
print(z1 * z2)  # (8-1j)
```

---

## 4. Quick Self-Test
1. What character does Python use to indicate the imaginary component of a complex number?
   - *Answer: `j` (or `J`).*
2. What does `abs(3 + 4j)` return?
   - *Answer: `5.0` (calculates $\sqrt{3^2 + 4^2} = \sqrt{25} = 5.0$).*
