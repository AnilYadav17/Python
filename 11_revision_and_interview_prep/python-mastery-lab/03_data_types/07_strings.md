# Lesson 07: Strings (`str`) and Unicode

## 1. What Is a String in Simple Words?
In Python 3, a **string (`str`)** is an **immutable sequence of Unicode characters**.

Unlike Python 2 (which treated strings as raw bytes), Python 3 natively understands every human language, emoji, and symbol:
```python
greeting = "Hello"
hindi = "नमस्ते"
japanese = "こんにちは"
emoji = "🚀🐍"
```

---

## 2. String Indexing and Slicing

Strings are 0-indexed sequences:

```
  String:  "P  y  t  h  o  n"
  Index:    0  1  2  3  4  5
 Negative: -6 -5 -4 -3 -2 -1
```

```python
s = "Python"

# 1. Direct Indexing:
print(s[0])   # 'P'
print(s[-1])  # 'n' (last character)

# 2. Slicing: [start : stop : step] (stop is EXCLUDED)
print(s[0:2])   # 'Py' (indexes 0 and 1)
print(s[2:])    # 'thon' (from index 2 to end)
print(s[:3])    # 'Pyt' (from start up to index 3)

# 3. Stepping and Reversing:
print(s[::2])   # 'Pto' (every 2nd letter)
print(s[::-1])  # 'nohtyP' (Reverse a string in one line!)
```

---

## 3. The 5 Most Important String Methods

1. **`.strip()`**: Removes leading and trailing whitespace.
   ```python
   raw = "   anil@example.com \n"
   clean = raw.strip()  # "anil@example.com"
   ```

2. **`.split()`**: Chops text into a list of words.
   ```python
   sentence = "Python is fast and fun"
   words = sentence.split(" ")  # ['Python', 'is', 'fast', 'and', 'fun']
   ```

3. **`.join()`**: Glues a list of strings together into one string.
   ```python
   tags = ["python", "coding", "linux"]
   result = ", ".join(tags)  # "python, coding, linux"
   ```

4. **`.replace()`**: Substitutes text.
   ```python
   msg = "I love Java"
   print(msg.replace("Java", "Python"))  # "I love Python"
   ```

5. **`.startswith()` and `.endswith()`**:
   ```python
   filename = "report_2026.pdf"
   print(filename.endswith(".pdf"))  # True
   ```

---

## 4. Performance Trap: Never Use `+` in a Loop to Build Strings!

Because strings are **immutable**, every `+` creates a brand-new string in memory and copies all previous characters:

```python
# SLOW: O(N^2) memory copying!
result = ""
for word in huge_word_list:
    result += word + " "

# FAST & IDIOMATIC: O(N) single-pass allocation!
result = " ".join(huge_word_list)
```

---

## 5. Quick Self-Test
1. Can you change a letter in a string using `s[0] = 'X'`?
   - *Answer: No, strings are immutable (`TypeError`).*
2. What is the fastest, cleanest way to reverse a string in Python?
   - *Answer: `s[::-1]`.*
