# Lesson 10: Operator Overloading and Dunder Methods

## 1. What Is Operator Overloading in Simple Words?
In Python, symbols like `+`, `-`, and `*` are not hardcoded to only work on numbers. 

When you write `a + b`, Python does not say: *"I only add numbers."*  
Instead, Python asks object `a`:
> **"Hey `a`, do you have a method named `__add__`? If so, pass `b` to it!"**

This means you can make the `+` operator do whatever makes sense for your own custom classes! This is called **Operator Overloading**.

Methods that start and end with two underscores (like `__add__`) are called **Dunder Methods** (short for Double Underscore).

---

## 2. The Operator-to-Dunder Mapping Table

| What You Type | What Python Actually Runs Behind the Scenes |
| :--- | :--- |
| `a + b` | `a.__add__(b)` |
| `a - b` | `a.__sub__(b)` |
| `a * b` | `a.__mul__(b)` |
| `a / b` | `a.__truediv__(b)` |
| `a // b` | `a.__floordiv__(b)` |
| `a == b` | `a.__eq__(b)` |
| `a < b` | `a.__lt__(b)` |
| `a in b` | `b.__contains__(a)` |
| `len(a)` | `a.__len__()` |
| `a[i]` | `a.__getitem__(i)` |

---

## 3. Real-World Example: Building a 2D `Vector` Class

Let's build a simple mathematical 2D point/vector class that supports `+`, `*`, and `==`:

```python
class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Define what '+' does:
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Define what '*' by a scalar number does:
    def __mul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar)

    # Define what '==' checks:
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Make it print nicely:
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

### Now Watch How Clean the Code Becomes:
```python
v1 = Vector(2, 3)
v2 = Vector(5, 7)

# We can use '+' naturally!
v3 = v1 + v2
print("v1 + v2 =", v3)  # Vector(7, 10)

# We can multiply by 2!
v4 = v1 * 2
print("v1 * 2 =", v4)   # Vector(4, 6)

# We can check equality!
print(v3 == Vector(7, 10))  # True!
```

---

## 4. Quick Self-Test
1. When you write `len("hello")`, what method is actually called?
   - *Answer: `"hello".__len__()`.*
2. What dunder method allows a custom object to support the `+` operator?
   - *Answer: `__add__(self, other)`.*
