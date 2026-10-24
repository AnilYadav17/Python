# Lesson 03: `try`, `except`, `else`, and `finally`

## 1. The Complete 4-Part Structure

```python
try:
    # 1. Code that might fail
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    # 2. Runs ONLY if FileNotFoundError happened
    print("File was missing!")
else:
    # 3. Runs ONLY if NO error occurred in try!
    print(f"Successfully read {len(content)} characters.")
finally:
    # 4. ALWAYS runs no matter what (even on crashes or return statements!)
    print("Cleanup complete.")
```

---

## 2. Fascinating Fact: `finally` Executes Even If You `return`! 💡
> **Did you know?**
> What does this function return?
> ```python
> def mysterious():
>     try:
>         return 1
>     finally:
>         return 2
> ```
> Believe it or not, it returns **`2`**!  
> Python guarantees that `finally` MUST execute before the function frame can be popped from the call stack. The `return 2` in `finally` overrides the `return 1`!

---

## 3. Why Use the `else:` Block in Exception Handling?

Many developers put everything inside the `try:` block. That is a bad habit!
```python
# Bad: If calculate_total() crashes with a ValueError, we might mistakenly
# think it was the int() conversion that failed!
try:
    val = int(user_input)
    total = calculate_total(val)
except ValueError:
    print("Invalid input")
```

### The Clean Pythonic Way:
Keep `try:` as small as possible, and put the rest in `else:`:
```python
try:
    val = int(user_input)  # ONLY wrap the dangerous line!
except ValueError:
    print("Please enter a valid number.")
else:
    # Runs only if conversion succeeded:
    total = calculate_total(val)
    print("Total is:", total)
```

---

## 4. Quick Self-Test
1. When does the `else:` block of a `try` statement run?
   - *Answer: Only when the `try` block completes without raising any exceptions.*
2. Is code inside `finally:` guaranteed to run even if an exception occurs?
   - *Answer: Yes, `finally` always runs (unless the computer loses power or the OS kills the process with SIGKILL).*
