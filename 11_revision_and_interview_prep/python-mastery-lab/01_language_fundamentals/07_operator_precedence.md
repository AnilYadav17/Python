# Lesson 07: Operator Precedence and Associativity

## 1. What Is This in Simple Words?
When you have a calculation with multiple operators:
```python
result = 10 + 5 * 2
```
Does Python calculate `(10 + 5) * 2 = 30`, or `10 + (5 * 2) = 20`?

Python calculates **`20`** because multiplication has higher **precedence** than addition.

**Precedence** defines the priority of operators (which operator gets calculated first).  
**Associativity** defines the direction of calculation (left-to-right vs right-to-left) when operators have the *exact same* precedence.

---

## 2. Complete Operator Precedence Table (High to Low)

| Priority | Operator Symbol | Description | Associativity |
| :--- | :--- | :--- | :--- |
| **1 (Highest)** | `()` | Parentheses (grouping) | Inner first |
| **2** | `x[i]`, `x.attr`, `f()` | Indexing, attribute access, function call | Left-to-Right |
| **3** | `**` | Exponentiation (power) | **Right-to-Left** |
| **4** | `+x`, `-x`, `~x` | Unary positive, negative, bitwise NOT | Right-to-Left |
| **5** | `*`, `/`, `//`, `%` | Multiply, float divide, floor divide, modulo | Left-to-Right |
| **6** | `+`, `-` | Addition, Subtraction | Left-to-Right |
| **7** | `<<`, `>>` | Bitwise shifts | Left-to-Right |
| **8** | `&` | Bitwise AND | Left-to-Right |
| **9** | `^` | Bitwise XOR | Left-to-Right |
| **10** | `\|` | Bitwise OR | Left-to-Right |
| **11** | `==`, `!=`, `<`, `<=`, `>`, `>=`, `in`, `is` | Comparisons, identity, membership | Chained |
| **12** | `not` | Boolean NOT | Right-to-Left |
| **13** | `and` | Boolean AND | Left-to-Right |
| **14** | `or` | Boolean OR | Left-to-Right |
| **15 (Lowest)**| `:=` | Walrus assignment expression | Right-to-Left |

---

## 3. The Power Trap: Exponentiation Associativity

Almost all operators in Python calculate from **left to right**. 
The major exception is **`**` (power)**, which calculates from **right to left**:

```python
result = 2 ** 3 ** 2
```
What is the answer?
- Left to right would be: `(2 ** 3) ** 2` $\to$ `8 ** 2` = `64`.
- **Right to left is: `2 ** (3 ** 2)` $\to$ `2 ** 9` = `512`!**

Python evaluates this as **512**.

---

## 4. Chained Comparisons: A Python Superpower

In most languages like Java or C, writing `1 < x < 10` is an error or produces broken logic.

In Python, **chained comparisons work just like math**:
```python
x = 5
if 1 < x < 10:
    print("x is between 1 and 10")
```

Internally, Python automatically translates `1 < x < 10` into:
```python
(1 < x) and (x < 10)
```
**Important**: Python is smart—it only evaluates `x` once!

---

## 5. The Professional Engineering Rule
> **Never make your teammates guess precedence.**
> If an expression has more than two operators, always use parentheses `()` to make your intent crystal clear:
> 
> ```python
> # Bad (hard to scan quickly):
> if not active and score > 100 or role == "admin":
> 
> # Good (crystal clear intent):
> if ((not active) and (score > 100)) or (role == "admin"):
> ```
