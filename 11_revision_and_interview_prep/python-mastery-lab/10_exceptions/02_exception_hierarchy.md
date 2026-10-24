# Lesson 02: The Exception Hierarchy and the Bare `except` Bug

## 1. What Is the Exception Hierarchy?
Exceptions in Python are not loose error codes. They form an organized tree of classes inheriting from a common root:

```
                      BaseException
                            │
     ┌──────────────────────┼──────────────────────┬──────────────────────┐
     ▼                      ▼                      ▼                      ▼
SystemExit          KeyboardInterrupt        GeneratorExit            Exception
(sys.exit())          (Ctrl + C)           (Generator cleanup)            │
                                                                   ┌──────┴──────┐
                                                                   ▼             ▼
                                                             ArithmeticError  LookupError
                                                                   │             │
                                                           ZeroDivisionError  IndexError / KeyError
```

---

## 2. Fascinating Fact: Why `KeyboardInterrupt` Does NOT Inherit from `Exception`! 💡
> **Did you know?**
> When you press `Ctrl + C` in your terminal to kill a runaway script, Python raises a `KeyboardInterrupt`.  
> Why doesn't it inherit from `Exception`?  
> Because if it did, every lazy developer who wrote `except Exception:` would accidentally trap the `Ctrl + C` signal, making it **impossible to kill or stop their script**!  
> By placing `KeyboardInterrupt` and `SystemExit` directly under `BaseException`, Python guarantees that standard exception handlers cannot trap them.

---

## 3. The Deadly Bug: The Bare `except:`
Never write a bare `except:` without an error type:

```python
# DANGEROUS CODE:
try:
    infinite_loop()
except:  # Traps BaseException!
    print("Caught an error!")
```
If you press `Ctrl + C`, the script **refuses to exit**!  
It catches your attempt to terminate the program and keeps running!

> **The Golden Rule**: Always catch specific exceptions: `except ValueError:`, or at most `except Exception:`. Never catch bare `except:`.

---

## 4. Quick Self-Test
1. What is the root class of all exceptions in Python?
   - *Answer: `BaseException`.*
2. Why should you write `except Exception:` instead of `except BaseException:`?
   - *Answer: To avoid accidentally catching `KeyboardInterrupt` (Ctrl+C) and `SystemExit`.*
