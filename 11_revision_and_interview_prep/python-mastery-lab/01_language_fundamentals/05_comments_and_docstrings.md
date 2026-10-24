# Lesson 05: Comments and Docstrings

## 1. What Is This in Simple Words?
When writing code, you need a way to leave notes for humans (including yourself 6 months from now).

Python gives you two distinct ways to document your code:
1. **Comments** (`#`): Notes for developers reading the raw source code. Python completely throws them away before running.
2. **Docstrings** (`"""..."""`): Official documentation strings that Python keeps in memory so users can inspect them using `help()`.

---

## 2. Comments (`#`)

A comment starts with a hash symbol `#` and lasts until the end of the line:

```python
# Calculate discount for prime members
discount = 0.20  # 20% discount rate
```

### The Golden Rule of Comments:
> **Explain WHY, not WHAT.**
> 
> Good: `# We add 1 millisecond buffer to prevent race conditions on slow disks`
> 
> Bad: `# Add 1 to time` (The code already says that!)

---

## 3. Docstrings (Documentation Strings)

A **docstring** is a string literal that occurs as the **very first statement** inside a function, class, or module. It uses triple quotes `"""`:

```python
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate the Body Mass Index (BMI).
    
    Arguments:
        weight_kg: Weight in kilograms (e.g., 70.5).
        height_m: Height in meters (e.g., 1.75).
        
    Returns:
        The calculated BMI as a float.
    """
    return weight_kg / (height_m ** 2)
```

---

## 4. The Critical Difference: Memory and Runtime

This is a classic Python interview question:

| Feature | Comment (`#`) | Docstring (`"""..."""`) |
| :--- | :--- | :--- |
| **Where it lives** | Only in the `.py` text file. | Inside the compiled Code Object in RAM. |
| **Compiler behavior** | Stripped and ignored by the lexer. | Preserved and attached to the `__doc__` attribute. |
| **Accessible at runtime?** | **No**. Cannot be read by running code. | **Yes**. Readable via `func.__doc__` or `help(func)`. |

### Try It in Python:
```python
def greet(name):
    """Return a warm greeting message."""
    # This comment disappears completely!
    return f"Hello, {name}!"

# You can read the docstring directly from Python!
print(greet.__doc__)
# Output: Return a warm greeting message.
```

---

## 5. Quick Self-Test
1. If you place a triple-quoted string in the middle of a function, is it a docstring?
   - *Answer: No! A string is only a docstring if it is the first statement of the module, class, or function. In the middle of a function, it is just an unused string literal.*
2. How does the `help()` command find what to display for a function?
   - *Answer: It reads the function's `__doc__` attribute.*
