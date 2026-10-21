# Day 20: OOP - Inheritance

## Explanation
Inheritance allows a new class to inherit attributes and methods from an existing class, promoting code reuse.

## Key Concepts
- **Parent/Base Class**: The class being inherited from.
- **Child/Derived Class**: The class that inherits.
- **`super()`**: Used to call methods from the parent class (especially `__init__`).
- **Overriding**: Redefining a parent's method in the child class.

## Code Example
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        return "Meow"
```

## Task
Create a `Vehicle` class with a `move()` method. Create a `Bicycle` child class that overrides `move()` to print "Pedaling along!". 