# Lesson 03: The Boolean Type (`bool`)

## 1. What Is a Boolean?
A **Boolean** represents a binary truth value. In Python, there are exactly two boolean objects:
- `True`
- `False`

Notice they **must be capitalized**! `true` and `false` are not recognized keywords and will cause a `NameError`.

---

## 2. The Secret: `bool` Is a Subclass of `int`!

In Python, `bool` is literally a child class of `int`:
```python
print(issubclass(bool, int))  # True!
```

Because of this:
- `True` has the numerical value **`1`**.
- `False` has the numerical value **`0`**.

You can actually do math with booleans (though you rarely should in practice!):
```python
print(True + True)   # 2
print(True * 50)     # 50
print(False - 5)     # -5
print(True == 1)     # True!
print(False == 0)    # True!
```

### Why Did Python Design It This Way?
Historical compatibility! Before Python 2.3, Python had no dedicated `bool` type at all; programmers just used `0` and `1`. When Guido added `bool` in PEP 285, making it inherit from `int` ensured that millions of lines of existing code wouldn't break.

---

## 3. A Clever Real-World Trick: Counting Trues with `sum()`

Because `True == 1` and `False == 0`, you can count how many conditions passed using `sum()`:

```python
scores = [85, 92, 45, 78, 99, 61]

# Count how many students scored 80 or higher:
passed_count = sum(score >= 80 for score in scores)
print("Students with A/B grade:", passed_count)
# Output: 3
```

---

## 4. Quick Self-Test
1. What does `True == 1` evaluate to?
   - *Answer: `True`.*
2. Does `True is 1` evaluate to `True`?
   - *Answer: `False`! They have equal numerical values (`==`), but they are different objects in memory with different types (`bool` vs `int`).*
