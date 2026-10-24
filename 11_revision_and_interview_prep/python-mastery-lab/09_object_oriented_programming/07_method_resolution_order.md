# Lesson 07: Method Resolution Order (MRO) and `super()`

## 1. The Diamond Problem in Multiple Inheritance

In Python, a class can inherit from more than one parent:
```python
class A:
    def ping(self): print("A")

class B(A):
    def ping(self): print("B")

class C(A):
    def ping(self): print("C")

# Class D inherits from both B and C:
class D(B, C):
    pass
```

If you call `d = D(); d.ping()`, which `ping` gets called? `B`? `C`? Or `A`?

```
         A
       /   \
      B     C
       \   /
         D
```

This classic puzzle is called the **Diamond Problem**.

---

## 2. Python's Solution: C3 Linearization and MRO

Python solves this with mathematical precision using an algorithm called **C3 Linearization**.

It creates a linear, unambiguous search order called the **Method Resolution Order (MRO)**:
- Children are checked before their parents.
- Parents listed first in the class declaration are checked first.
- No class is visited twice.

You can inspect any class's MRO using **`Class.__mro__`**:
```python
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```
When `d.ping()` runs, Python walks this list from left to right:
1. Does `D` have `ping`? No.
2. Does `B` have `ping`? **Yes!** (Calls `B.ping` and stops).

---

## 3. Fascinating Fact: `super()` Does NOT Mean "Call My Parent"! 💡
> **Did you know?**
> The biggest misconception about `super()` is that it calls your immediate parent class.  
> **It does not!**  
> `super()` means: **"Call the NEXT class in the active instance's MRO chain!"**  
> In multiple inheritance, calling `super()` inside class `B` might actually call a method in class `C` (its sibling!), not class `A`! This cooperative behavior is what allows complex mixins and multi-inheritance frameworks to work without duplicate execution.

---

## 4. Quick Self-Test
1. How do you view the search path Python takes when looking up methods on a class?
   - *Answer: By checking `ClassName.__mro__` or calling `ClassName.mro()`.*
2. What algorithm does CPython use to compute the MRO?
   - *Answer: C3 Linearization (borrowed from the Dylan programming language in Python 2.3).*
