# Lesson 11: Properties (`@property`) and Pythonic Encapsulation

## 1. Why Java Style Getters and Setters Look Silly in Python

In Java or C++, developers are taught to never expose public variables. You must write ugly boilerplate:
```java
// Verbose Java style:
public int getAge() { return this.age; }
public void setAge(int age) { this.age = age; }
```

In Python, the philosophy is different:
> **Start simple. If you just have data, use a plain public attribute: `self.age = age`.**

What if, 6 months later, business rules change and you need to validate that `age` cannot be negative?  
Do you have to break everyone's code and force them to call `.setAge()`?

**No! You simply turn the attribute into a `@property`!**

---

## 2. The `@property` Pattern (Getters and Setters)

```python
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        # Calls the setter automatically during initialization!
        self.balance = balance

    # 1. The Getter (Accessed like a plain variable: account.balance)
    @property
    def balance(self) -> float:
        return self._balance

    # 2. The Setter (Called automatically on assignment: account.balance = 500)
    @balance.setter
    def balance(self, amount: float):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = amount
```

### Look How Clean Caller Code Remains:
```python
acc = BankAccount("Anil", 1000)

# Looks like reading a simple variable, but runs the getter function!
print("Current balance:", acc.balance)

# Looks like a simple assignment, but runs the setter validation!
acc.balance = 1500
print("New balance:", acc.balance)

# Invalid assignment raises an error automatically!
try:
    acc.balance = -200
except ValueError as e:
    print("Caught error:", e)  # Balance cannot be negative!
```

---

## 3. Quick Self-Test
1. Why does Python avoid writing explicit `get_x()` and `set_x()` methods from day one?
   - *Answer: Because any public attribute can later be upgraded to a `@property` without changing the external syntax or breaking existing callers.*
2. How do you create a read-only attribute in Python?
   - *Answer: Define a method with `@property` and do not provide a `@<name>.setter`.*
