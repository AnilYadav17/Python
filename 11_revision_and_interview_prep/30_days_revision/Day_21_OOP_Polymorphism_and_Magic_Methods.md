# Day 21: OOP - Polymorphism & Magic Methods

## Explanation
Polymorphism means "many forms". Different classes can be treated uniformly if they share the same interface. Magic (Dunder) methods allow custom behavior for operators.

## Key Concepts
- **Polymorphism**: E.g., iterating through a list of different object types and calling the same `.draw()` method on all of them.
- **Dunder Methods**: Methods surrounded by double underscores (`__str__`, `__len__`, `__add__`). They overload standard Python operators.

## Code Example
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self): # Overloads print()
        return f"'{self.title}' ({self.pages} pages)"
    
    def __len__(self): # Overloads len()
        return self.pages

b = Book("Python 101", 250)
print(b) # 'Python 101' (250 pages)
```

## Task
Create a `Point` class with x and y coordinates. Implement the `__add__` method so you can use the `+` operator to add two Point objects together.