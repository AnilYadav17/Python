# Day 18: OOP - Classes and Objects

## Explanation
Object-Oriented Programming (OOP) groups data and behavior into single entities called objects. A Class is the blueprint for creating objects.

## Key Concepts
- **`class`**: Keyword to define a blueprint.
- **`__init__`**: Constructor method used to initialize attributes.
- **`self`**: Represents the specific instance of the class being operated on.
- **Instance Attributes**: Variables that belong to a specific object.

## Code Example
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.bark())
```

## Task
Create a `Car` class with attributes `make`, `model`, and `year`. Add a method `start_engine()` that prints a message. Create two different car objects and call the method.