# Lesson 10: Closures (Functions with Memory)

## 1. What Is a Closure in Simple Words?
Normally, when a function finishes executing, all of its local variables are destroyed and thrown away.

A **Closure** is a special function that **"closes over" and remembers variables from its outer enclosing scope, even after the outer function has finished running and returned!**

---

## 2. A Crystal-Clear Example: The Multiplier Factory

```python
def make_multiplier(factor):
    # 'factor' is a local variable inside make_multiplier

    def multiply(number):
        # The inner function uses 'factor' from the outer function!
        return number * factor

    return multiply  # We return the inner function without calling it!

# Create two specialized functions:
double = make_multiplier(2)
triple = make_multiplier(3)

# Notice: make_multiplier() finished running long ago!
# Yet 'double' still remembers that factor was 2:
print(double(10))  # 20
print(triple(10))  # 30
```

---

## 3. How Does Python Do This Internally? (`__closure__`)

When Python detects that an inner function references an outer variable, it packs that variable into a special **Cell Object** and attaches it to the inner function's **`__closure__`** attribute:

```python
print(double.__closure__)
# Output: (<cell at 0x7f...: int object at 0x...>,)

# We can literally read the remembered value from the cell!
print("Remembered factor:", double.__closure__[0].cell_contents)
# Output: Remembered factor: 2
```

---

## 4. The 3 Conditions for a Closure
For a function to be a true closure, three things must be true:
1. There must be an **outer function** and an **inner nested function**.
2. The inner function must **reference a variable** from the outer function (a "free variable").
3. The outer function must **return the inner function**.

---

## 5. Quick Self-Test
1. What attribute on a function stores the closure's captured variables?
   - *Answer: `__closure__` (holding a tuple of Cell objects).*
2. Do closures keep enclosing variables alive even after the outer function finishes?
   - *Answer: Yes, the cell object maintains a reference, preventing garbage collection.*
