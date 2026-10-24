# Lesson 16: Descriptors (The Secret Engine of Python OOP)

## 1. What Is a Descriptor in Simple Words?
Have you ever wondered:
- How does `@property` intercept attribute access?
- How does `@classmethod` pass `cls` automatically?
- How do ORMs like SQLAlchemy and Django validate table columns when you assign `user.age = 25`?

The answer to all of them is **Descriptors**!

> **A Descriptor is an object that customizes what happens when an attribute is accessed (`.`), assigned (`=`), or deleted (`del`).**

An object is a descriptor if it defines at least one of these three methods:
1. **`__get__(self, instance, owner)`**
2. **`__set__(self, instance, value)`**
3. **`__delete__(self, instance)`**

---

## 2. A Real-World Example: A Reusable Type-Validator Descriptor

Imagine you want to ensure that `age`, `salary`, and `score` are always positive numbers, without copy-pasting the same `@property` validation three times!

```python
class PositiveNumber:
    """A descriptor that enforces positive numeric values."""
    def __set_name__(self, owner, name):
        # Automatically remembers the variable name ('age', 'salary')
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name} cannot be negative!")
        instance.__dict__[self.name] = value

class Profile:
    # Use our descriptor to protect these attributes:
    age = PositiveNumber()
    points = PositiveNumber()

p = Profile()
p.age = 25       # Calls PositiveNumber.__set__()!
p.points = 100   # Calls PositiveNumber.__set__()!

print(f"Age: {p.age}, Points: {p.points}")

try:
    p.age = -5   # Raises ValueError: age cannot be negative!
except ValueError as e:
    print("Caught error:", e)
```

---

## 3. Fascinating Fact: Functions Are Actually Descriptors! 💡
> **Did you know?**
> Every standard Python function is literally a descriptor!  
> When you define a function inside a class:
> ```python
> class Dog:
>     def bark(self): pass
> ```
> The function object `bark` implements `__get__`!  
> When you call `d = Dog(); d.bark()`, accessing `d.bark` triggers `bark.__get__(d, Dog)`.  
> That `__get__` call is what binds `d` to `self` and returns a **`MethodType`**! Without descriptors, Python methods with `self` could not exist!

---

## 4. Quick Self-Test
1. What three methods make up the descriptor protocol?
   - *Answer: `__get__`, `__set__`, and `__delete__`.*
2. How does accessing an instance method `obj.method` pass `self` automatically?
   - *Answer: Python functions implement `__get__`, which returns a bound method with the instance pre-filled as the first argument.*
