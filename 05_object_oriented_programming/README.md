# 🏛️ 05_Object_Oriented_Programming: Classes, Inheritance & Abstraction

## Overview
Object-Oriented Programming (OOP) is a software design paradigm that structures code into entities called **Objects**, which combine state (attributes/data) and behavior (methods/functions).

Python is purely object-oriented: everything in Python is an object, from integers to functions. Mastering OOP enables you to write clean, reusable, maintainable, and large-scale architectures by leveraging the four pillars of OOP: **Encapsulation**, **Abstraction**, **Inheritance**, and **Polymorphism**.

---

## Learning Objectives
By studying this module, you will understand:
1. Class declarations, instantiating objects, and the `self` reference pointer.
2. The `__init__` constructor for instance attribute initialization.
3. Class attributes vs. instance attributes.
4. The 5 types of inheritance in Python:
   * Single inheritance
   * Multilevel inheritance
   * Multiple inheritance
   * Hierarchical inheritance
   * Hybrid inheritance
5. Method Resolution Order (**MRO**) and C3 Linearization (`Class.mro()` or `Class.__mro__`).
6. Utilizing `super()` to invoke parent constructors and methods cooperatively.
7. Abstract Base Classes (**ABCs**) via the `abc` module (`@abstractmethod`) to enforce interface contracts.
8. Encapsulation techniques (public, protected `_`, private `__`) and setter/getter methods.

---

## Prerequisites
* **[04_functions](../04_functions/)** (Function definitions, return types, parameters).

---

## Learning Path

```text
1. Classes & Objects (08July, 09July, constructor_1.py)
   └── Instantiation, Attributes, Methods, __init__ Constructor
       ▼
2. Inheritance Patterns (Inheritance/)
   └── Single, Multilevel, Multiple, Hierarchical, Hybrid
       ▼
3. Cooperative Inheritance & Resolution (Inheritance/)
   └── super(), Method Resolution Order (MRO)
       ▼
4. Abstraction & Interface Design (Abstraction/)
   └── ABC, @abstractmethod, Concrete Subclasses
       ▼
5. Encapsulation & Revision (Revise/)
   └── Data Protection, Getters, Setters, Student Model
```

---

## Repository Contents & Examples

| Folder / File | Focus Area | Key Files & Descriptions |
|:---|:---|:---|
| 📁 **`Class_Work/08July`, `09July`** | Classes & Domain Models | `employee.py`, `book.py`, `product.py`, `constructor_1.py`, `add_two.py` |
| 📁 **`Class_Work/Inheritance`** | Inheritance Types & MRO | `single.py`, `multilevel.py`, `multiple.py`, `hierarchical.py`, `hybrid.py`, `super.py`, `mro.py`, `mro1.py`, `mro2.py` |
| 📁 **`Class_Work/Abstraction`** | Abstract Base Classes | `abstract_class_method1.py`, `abstract_example1.py` - `4.py` (Payment gateway templates), `theory.txt` |
| 📁 **`Class_Work/Closure`** | Closures & Scopes | `1.py`, `2.py` (Inner functions capturing lexical enclosing scope) |
| 📁 **`Revise/`** | Practice Models | `1.py` (Complete Student class with `set_data` and `get_data`) |

---

## How to Run Examples

```bash
# Test single and multiple inheritance:
python3 05_object_oriented_programming/Class_Work/Inheritance/single.py
python3 05_object_oriented_programming/Class_Work/Inheritance/multiple.py

# Inspect Method Resolution Order (MRO):
python3 05_object_oriented_programming/Class_Work/Inheritance/mro.py

# Test abstract payment gateway contracts:
python3 05_object_oriented_programming/Class_Work/Abstraction/abstract_example2.py
```

---

## Practice & Assignments

Solve the OOP assignments in **`09_practice_and_assignments/04_OOPS/`**:
* **[01_Classes_and_Constructors](../09_practice_and_assignments/04_OOPS/01_Classes_and_Constructors/)** — Class design, student/employee records.
* **[02_Inheritance_and_Polymorphism](../09_practice_and_assignments/04_OOPS/02_Inheritance_and_Polymorphism/)** — Vehicle hierarchies, method overriding.
* **[03_Abstraction_and_Encapsulation](../09_practice_and_assignments/04_OOPS/03_Abstraction_and_Encapsulation/)** — Bank accounts, abstract devices, private PIN verification.

---

## Common Beginner Mistakes

1. **Forgetting `self` as the First Parameter of Instance Methods:**
   * Writing `def get_name():` instead of `def get_name(self):` raises `TypeError: get_name() takes 0 positional arguments but 1 was given`.
2. **Attempting to Instantiate an Abstract Class:**
   * Classes inheriting from `ABC` with unimplemented `@abstractmethod` decorators cannot be directly instantiated. You must instantiate concrete subclasses.
3. **Diamond Problem in Multiple Inheritance:**
   * Multiple inheritance can lead to ambiguity about which parent method is called. Python resolves this deterministically using the **C3 Linearization Algorithm** (check via `ClassName.__mro__`).
4. **Confusing Class Variables with Instance Variables:**
   * A mutable class attribute defined on the class body (e.g. `items = []`) is shared across **all** instances of that class! Define instance variables inside `__init__` via `self.items = []`.

---

## Next Step

👉 Advance to **[06_python_modules_and_packages](../06_python_modules_and_packages/)** to organize multi-file applications using Python packages and imports!
