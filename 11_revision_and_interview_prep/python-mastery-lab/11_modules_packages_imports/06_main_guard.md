# Lesson 06: The `if __name__ == "__main__":` Guard and Module Caching

## 1. What Is `__name__` in Simple Words?
Whenever Python runs a `.py` file, it automatically creates a special hidden variable called **`__name__`**:

- If you run the file **directly** from your terminal (`python3 script.py`):
  Python sets `__name__ = "__main__"`.
- If another file **imports** your file (`import script`):
  Python sets `__name__ = "script"` (the module's actual file name!).

---

## 2. Why Do We Use `if __name__ == "__main__":`?

Imagine you write a file with useful functions and some test code at the bottom:

```python
# math_utils.py

def add(a, b):
    return a + b

# Without the guard:
print("Testing add:", add(5, 5))
```

If another file writes `import math_utils`:
**Python would execute `print("Testing add: 10")` immediately!** That pollutes your terminal and runs tests when you just wanted the function!

### The Solution:
Wrap execution code inside the guard:
```python
# math_utils.py

def add(a, b):
    return a + b

if __name__ == "__main__":
    # This ONLY runs if you execute this file directly:
    print("Running standalone tests:", add(5, 5))
```

Now:
- Running `python3 math_utils.py` $\to$ Runs the test!
- Writing `import math_utils` in another script $\to$ Imports cleanly without running the test!

---

## 3. Fascinating Fact: `sys.modules` Caches Everything! 💡
> **Did you know?**
> When you write `import math`, Python does not read `math.py` from disk every single time you call it.  
> Python has an internal dictionary called **`sys.modules`**.  
> The first time you import a module, Python compiles it, executes it once, and caches the resulting module object inside `sys.modules["math"]`.  
> If 50 different files in your project write `import math`, Python simply looks up the cached pointer in `sys.modules` in $O(1)$ time—it **never executes the file twice**!

---

## 4. Quick Self-Test
1. What is the value of `__name__` when a file is executed directly?
   - *Answer: `"__main__"`.*
2. Where does Python cache already-imported modules to avoid reloading them?
   - *Answer: In `sys.modules`.*
