# Lesson 01: Classes and Objects (The Blueprint Model)

## 1. What Is a Class in Simple Words?
- A **Class** is an architectural blueprint (like the blueprint for a sports car).
- An **Object (Instance)** is the actual, physical car built in memory from that blueprint.

You can use one blueprint to manufacture thousands of individual cars:

```python
class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

# Build two separate cars in memory:
car1 = Car("Tesla", "Model 3")
car2 = Car("Porsche", "911")

print(car1.brand)  # Tesla
print(car2.brand)  # Porsche
```

---

## 2. Fascinating Fact: `__init__` Is NOT the Constructor! 💡
> **Did you know?**
> Almost every tutorial claims that `__init__` is Python's constructor. **That is technically false!**  
> In Python:
> 1. **`__new__(cls, ...)`** is the **real Constructor**. Its job is to allocate the raw memory chunk and create the brand-new instance.
> 2. **`__init__(self, ...)`** is the **Initializer**. By the time `__init__` runs, the object already exists in RAM! `__init__` merely populates attributes on `self`.
> 
> You only need to override `__new__` when subclassing immutable types (like `int` or `tuple`) or creating Singletons!

---

## 3. Why Does Python Require Explicit `self`?

In C++ or Java, the current instance pointer (`this`) is hidden and injected implicitly behind your back.

In Python:
```python
def drive(self):
    print(f"Driving {self.brand}")
```
Why must we write `self` explicitly as the first parameter?
1. **Explicit is better than implicit** (The Zen of Python). You can clearly see that `drive` needs access to instance data.
2. Under the hood, when you type `car1.drive()`, Python translates it directly into:
   ```python
   Car.drive(car1)  # Passing the instance as the first argument!
   ```

---

## 4. Fascinating Fact: `self` Is Not Even a Keyword! 💡
> **Did you know?**
> `self` is not a reserved Python keyword!  
> You could literally write:
> ```python
> class Robot:
>     def beep(me):
>         print("Beep beep!")
> ```
> And Python runs it without any syntax error! However, using anything other than `self` breaks PEP 8 and confuses teammates. Always use `self`.

---

## 5. Quick Self-Test
1. What is the difference between `__new__` and `__init__`?
   - *Answer: `__new__` creates and returns the object in memory; `__init__` initializes its attributes.*
2. What does `my_car.honk()` actually translate to in CPython?
   - *Answer: `Car.honk(my_car)`.*
