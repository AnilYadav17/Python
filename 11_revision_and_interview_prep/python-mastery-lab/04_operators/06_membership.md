# Lesson 06: Membership Operators (`in` and `not in`)

## 1. What Are Membership Operators?
Membership operators test whether a value is **contained inside a sequence or collection**:

- **`x in collection`**: Returns `True` if `x` is found.
- **`x not in collection`**: Returns `True` if `x` is NOT found.

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("orange" not in fruits)  # True
```

---

## 2. The Dictionary Gotcha: `in` Checks KEYS, Not Values!

Look at this common mistake:
```python
scores = {"Alice": 95, "Bob": 80}

print("Alice" in scores)  # True (Checks keys!)
print(95 in scores)       # False!
```

> **Rule: In dictionaries, `in` checks the KEYS by default.**

If you want to search values, you must explicitly search `.values()`:
```python
print(95 in scores.values())  # True!
```

---

## 3. String Substring Search with `in`

In strings, `in` checks for complete contiguous substrings:
```python
text = "The quick brown fox"
print("quick" in text)  # True
print("quiet" in text)  # False
```

---

## 4. Performance: $O(1)$ vs. $O(N)$ Search

Always remember:
- `in` on a **`set`** or **`dict`**: **$O(1)$ instant hash lookup**.
- `in` on a **`list`** or **`tuple`**: **$O(N)$ linear scan** (must check every single item one by one).

```python
# If you have 500,000 email addresses to check:
banned_emails_set = set(large_banned_list)

# Lightning fast ($O(1)$):
if email in banned_emails_set:
    block_user()
```

---

## 5. Quick Self-Test
1. What does `"cat" in "caterpillar"` evaluate to?
   - *Answer: `True`.*
2. Why is searching a set faster than searching a list?
   - *Answer: Sets use hash tables ($O(1)$) instead of scanning through items sequentially ($O(N)$).*
