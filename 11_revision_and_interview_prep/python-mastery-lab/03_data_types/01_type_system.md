# Lesson 01: Python's Type System

## 1. What Is This in Simple Words?
In Python, **everything is an object, and every object has a type**.

When you write:
```python
x = 42
```
The variable name `x` does **not** have a type. The object `42` has the type (`int`).

You can check any object's type using the built-in function `type()`:
```python
print(type(42))          # <class 'int'>
print(type("hello"))     # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>
```

---

## 2. Dynamic vs. Strong Typing (Revisited)

1. **Dynamic Typing**: You don't have to declare types when making variables. Python determines the type automatically when the code runs. You can rebind a name to an entirely different type:
   ```python
   data = 100        # data is pointing to an int
   data = "Python"   # now data is pointing to a str (completely valid!)
   ```

2. **Strong Typing**: Python strictly enforces type rules. It will NEVER guess or convert incompatible types behind your back:
   ```python
   result = "5" + 2  # CRASH! TypeError: can only concatenate str (not "int") to str
   ```

---

## 3. How to Check Types Properly: `type()` vs. `isinstance()`

This is an important professional rule:
- `type(x) == int`: Checks for the **exact** type. (Does not consider inheritance).
- `isinstance(x, int)`: Checks if `x` is an instance of `int` **OR any subclass of `int`**.

### The Boolean Example:
Did you know that in Python, **`bool` is a subclass of `int`**?
```python
flag = True

print(type(flag) == int)      # False! (Exact type is bool)
print(isinstance(flag, int))  # True! (Because bool inherits from int!)
```

> **Professional Best Practice**: Always use `isinstance(x, SomeType)` unless you strictly need to reject subclasses.

---

## 4. Quick Self-Test
1. In `val = 3.14`, does the name `val` have a type, or does the object `3.14` have a type?
   - *Answer: The object `3.14` has the type (`float`). Names in Python have no types.*
2. Why is `isinstance(x, (int, float))` useful?
   - *Answer: It checks if `x` is either an integer OR a float in a single, clean check.*
