# Day 19: OOP - Types of Methods

## Explanation
Classes can have different types of methods depending on what data they need to access.

## Key Concepts
- **Instance Methods**: Take `self`. Can modify object state and class state.
- **Class Methods**: Take `cls`. Annotated with `@classmethod`. Can modify class state (applies to all instances).
- **Static Methods**: Don't take `self` or `cls`. Annotated with `@staticmethod`. Like regular functions grouped within the class namespace.

## Code Example
```python
class Employee:
    company_name = "TechCorp"

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    @staticmethod
    def is_workday(day):
        return day.weekday() < 5
```

## Task
Create a `MathOperations` class with a static method `add(a, b)` and test it without instantiating the class.