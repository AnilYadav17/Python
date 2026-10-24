# Lesson 03: Instance, Class, and Static Methods

## 1. The 3 Types of Methods in Python

Inside a Python class, you can create three distinct flavors of methods:

```python
class Employee:
    # Class-level attribute (shared by all employees):
    company_name = "Tech Corp"

    def __init__(self, name: str, salary: float):
        # Instance attributes (unique to each employee):
        self.name = name
        self.salary = salary

    # 1. Instance Method: Takes 'self' (Manipulates individual instance data)
    def give_raise(self, amount: float):
        self.salary += amount

    # 2. Class Method: Takes 'cls' (Manipulates class-level data or acts as Factory)
    @classmethod
    def from_string(cls, emp_str: str):
        """Alternative constructor: creates an Employee from 'Anil,75000'"""
        name, salary_str = emp_str.split(",")
        return cls(name, float(salary_str))

    # 3. Static Method: Takes neither self nor cls (Pure utility function)
    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        return salary > 0
```

---

## 2. When to Use Which?

1. **Instance Method**: Use when you need to read or modify an object's specific variables (`self.name`, `self.salary`).
2. **Class Method (`@classmethod`)**: Use for **Alternative Constructors**! For example, `datetime.date.fromtimestamp(ts)` or `User.from_json(json_str)`. It receives the class itself (`cls`) as the first argument, so subclasses inherit the factory cleanly!
3. **Static Method (`@staticmethod`)**: Use when a function logically belongs inside the class namespace for organization, but doesn't need to read any class or instance data.

---

## 3. Quick Self-Test
1. What does the first parameter of a `@classmethod` receive?
   - *Answer: A reference to the Class itself (`cls`).*
2. What is the most common professional use case for `@classmethod`?
   - *Answer: Alternative constructors (factories that build instances from strings, dictionaries, or files).*
