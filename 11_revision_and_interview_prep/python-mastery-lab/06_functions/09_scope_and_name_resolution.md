# Lesson 09: Scope, Name Resolution (LEGB), and `nonlocal`

## 1. What Is Scope in Simple Words?
**Scope** is the area of your code where a variable name is recognized and can be used.

If you create a variable inside a function, that variable only exists while that function is running. Once the function finishes, its local variables vanish!

---

## 2. The LEGB Rule: How Python Looks Up Names

Whenever Python encounters a variable name (like `x`), it searches for it in this strict, 4-step order:

```
  1. Local (L)      -> Inside the current function
         │
         ▼
  2. Enclosing (E)  -> Inside outer nested functions (closures)
         │
         ▼
  3. Global (G)     -> At the top level of the .py module
         │
         ▼
  4. Built-in (B)   -> Python's built-in namespace (len, print, range)
```

If Python checks all 4 layers and cannot find the name, it raises a **`NameError: name 'x' is not defined`**.

---

## 3. The Classic `UnboundLocalError` Trap

Look at this very common bug:
```python
counter = 0

def increment():
    counter += 1  # We want to add 1 to the global counter!
    print(counter)

increment()
```
**Python Output:**
```
UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
```

### Why Did This Crash?
1. Before running the function, Python **compiles** it.
2. The compiler sees `counter += 1` (which has an assignment `=`).
3. Python decides: *"Aha! `counter` is being assigned to inside this function, so `counter` MUST be a **Local variable**!"*
4. At runtime, when Python executes `counter += 1`, it tries to read the local `counter` to add 1 to it.
5. But the local `counter` hasn't been given a value yet! $\to$ **CRASH!**

---

## 4. How to Fix It: `global` vs. `nonlocal`

### 1. The `global` Keyword:
Tells Python: *"Don't create a local variable. Use the module's top-level global variable!"*
```python
counter = 0

def increment():
    global counter  # Explicitly declare intent
    counter += 1
    print(counter)

increment()  # 1
```

### 2. The `nonlocal` Keyword (For Nested Functions):
Tells Python: *"Look in the outer enclosing function, not global!"*
```python
def make_counter():
    count = 0

    def step():
        nonlocal count  # Modifies count in the enclosing make_counter()
        count += 1
        return count

    return step

counter_fn = make_counter()
print(counter_fn())  # 1
print(counter_fn())  # 2
```

---

## 5. Quick Self-Test
1. In the LEGB lookup rule, what does the 'E' stand for?
   - *Answer: Enclosing scope (outer nested function).*
2. What keyword allows an inner function to modify a variable in its outer enclosing function?
   - *Answer: `nonlocal`.*
