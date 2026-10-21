# Day 22: OOP - Encapsulation & Abstraction

## Explanation
Encapsulation hides the internal state of an object and requires all interaction to be performed through an object's methods. Abstraction hides complex implementation details.

## Key Concepts
- **Private attributes**: Prefix with `__` (e.g., `__balance`). Python uses name mangling to restrict access.
- **Protected attributes**: Prefix with `_` (convention only).
- **Properties**: `@property` decorator allows accessing a method like an attribute, useful for getters/setters.

## Code Example
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private
        
    @property
    def balance(self):
        return self.__balance
```

## Task
Create a `User` class with a private `__password` attribute. Create a method to verify the password, ensuring the password itself cannot be accessed directly from outside.