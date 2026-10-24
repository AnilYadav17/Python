# Lesson 02: Comparison Operators

## 1. What Are Comparison Operators?
Comparison operators compare two values and always return either **`True`** or **`False`**:

| Operator | Meaning | Example | Result |
| :--- | :--- | :--- | :--- |
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |
| `>` | Greater than | `7 > 10` | `False` |
| `>=` | Greater than or equal to | `10 >= 10` | `True` |

---

## 2. Comparing Strings (Lexicographical / Alphabetical Order)

When you compare strings with `<` or `>`, Python compares their Unicode codepoints character by character:

```python
print("apple" < "banana")  # True ('a' comes before 'b')
print("cat" < "car")       # False ('t' comes after 'r')
```

### The Capital Letter Trap:
In Unicode and ASCII, **all Capital letters come before lowercase letters**!
```python
print("Zebra" < "apple")  # True! ('Z' is code 90, 'a' is code 97!)
```
> **Tip**: If you want true case-insensitive alphabetical sorting, convert to lowercase first: `str1.lower() < str2.lower()`.

---

## 3. Chained Comparisons: Writing Code Like Mathematics

In Python, you can chain multiple comparisons naturally:
```python
score = 85

# Clean Pythonic style:
if 80 <= score <= 90:
    print("Grade B")

# Equivalent to: (80 <= score) and (score <= 90)
```

---

## 4. Quick Self-Test
1. What does `"10" < "2"` evaluate to?
   - *Answer: `True`! Because it compares strings character-by-character, and `'1'` comes before `'2'` in ASCII! Convert to integers first to compare numbers: `int("10") < int("2")`.*
