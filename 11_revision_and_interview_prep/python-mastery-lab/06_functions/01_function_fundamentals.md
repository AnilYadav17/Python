# Lesson 01: Function Fundamentals and First-Class Citizens

## 1. What Is a Function in Simple Words?
A **function** is a reusable block of code that takes inputs (arguments), does some work, and returns an output:

```python
def calculate_tax(price: float, tax_rate: float = 0.05) -> float:
    """Calculate the total price including sales tax."""
    return price + (price * tax_rate)
```

---

## 2. Functions Are "First-Class Citizens" in Python!

In many languages (like C or old Java), functions are special grammar constructs that only exist to be called.

In Python, **functions are real objects**—just like integers, strings, or lists!
- You can store a function in a variable.
- You can pass a function as an argument to another function.
- You can return a function from another function.
- You can store functions inside lists or dictionaries!

### Demonstration:
```python
def shout(text):
    return text.upper() + "!"

# 1. Assign the function to another variable:
loud = shout  # Notice: NO parentheses! We are passing the function itself, not calling it!
print(loud("hello"))  # HELLO!

# 2. Store functions inside a dictionary (A Dispatch Table!):
operations = {
    "uppercase": str.upper,
    "lowercase": str.lower,
    "capitalize": str.capitalize
}

print(operations["uppercase"]("python"))  # PYTHON
```

---

## 3. Quick Self-Test
1. What is the difference between `my_func` and `my_func()`?
   - *Answer: `my_func` refers to the function object itself; `my_func()` calls/executes the function.*
2. What does a function return if it has no `return` statement?
   - *Answer: `None`.*
