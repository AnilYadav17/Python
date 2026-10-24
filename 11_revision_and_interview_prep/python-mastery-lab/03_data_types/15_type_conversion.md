# Lesson 15: Type Conversion (Casting) and Common Gotchas

## 1. What Is Type Conversion?
Converting data from one type into another:
- Converting text input `"42"` into an integer `42`.
- Converting a number `19.99` into a string `"19.99"`.

---

## 2. The 3 Biggest Type Conversion Gotchas

### Gotcha 1: `bool("False")` Is `True`!
Look at this code:
```python
user_setting = "False"
is_active = bool(user_setting)
print(is_active)  # Outputs: True!
```
Why? Because `bool(any_string)` does not read the English word inside the string! It simply checks: *"Is this string non-empty?"* Since `"False"` has 5 characters, it is truthy!

**The Proper Fix**:
```python
is_active = user_setting.lower() in ("true", "1", "yes")
```

### Gotcha 2: `int("3.14")` Crashes!
```python
int("3.14")
# CRASH! ValueError: invalid literal for int() with base 10: '3.14'
```
The `int()` function refuses to parse decimal points in a string directly.

**The Fix**: Convert to float first, then int:
```python
val = int(float("3.14"))  # 3
```

### Gotcha 3: Converting Binary or Hex Strings to Numbers
You can pass the base as the second argument to `int()`:
```python
print(int("1010", 2))   # 10 (Binary base 2)
print(int("FF", 16))    # 255 (Hex base 16)
```

---

## 3. Quick Self-Test
1. What does `bool("")` evaluate to?
   - *Answer: `False` (empty string is falsy).*
2. What does `bool(" ")` evaluate to?
   - *Answer: `True` (a string with a space is NOT empty!).*
