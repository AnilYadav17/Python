# 04. Object-Oriented Programming (OOP) — Interview & Viva Questions

---

### Q1: What is the fundamental difference between `__new__` and `__init__`?
**Model Answer:**
- `__new__(cls, *args, **kwargs)` is a static method responsible for **allocating and creating** the raw object instance in heap memory. It receives the class `cls` as its first argument and must return a newly created instance (typically via `super().__new__(cls)`).
- `__init__(self, *args, **kwargs)` is an instance method responsible for **initializing** the allocated instance's attributes once it already exists. It receives the instance `self` as its first argument and must return `None`.
- `__new__` is used when subclassing immutable types (like `int` or `tuple`) or when implementing creational design patterns like the Singleton pattern.

---

### Q2: What is the difference between `@classmethod`, `@staticmethod`, and regular instance methods?
**Model Answer:**
- **Instance Method**: Receives the implicit instance pointer `self` as the first argument. Can inspect and mutate both instance attributes (`self.x`) and class attributes (`self.__class__.x`).
- **Class Method (`@classmethod`)**: Receives the implicit class pointer `cls` as the first argument. Can inspect and mutate class-level state, but has no access to individual instance state. Commonly used as alternative constructors (e.g. `from_dict`, `from_csv`).
- **Static Method (`@staticmethod`)**: Receives neither `self` nor `cls`. Behaves like a standard independent function that resides inside the class namespace for organizational cohesion.

---

### Q3: How does Python's Method Resolution Order (MRO) work, and how does it resolve the Diamond Problem?
**Model Answer:**
- Python calculates MRO using the **C3 Linearization Algorithm**, which guarantees that:
  1. Subclasses appear before their parent classes.
  2. If a class inherits from multiple parents `(B, C)`, the ordering of parents listed in the class definition is strictly preserved.
  3. Monotonicity is upheld (no class is visited twice or in contradictory order).
- In the Diamond Problem (Class `D` inherits from `B` and `C`, both inheriting from `A`), naive inheritance would call `A` twice.
- In Python, `super()` does not call the direct parent; it delegates to the *next class in the instance's MRO*. In the Diamond problem, `D.mro()` is `[D, B, C, A, object]`, ensuring `A`'s method executes exactly once.

---

### Q4: Explain Duck Typing and how it relates to Python protocols.
**Model Answer:**
- Duck typing is dynamic polymorphism summarized by: *"If it walks like a duck and quacks like a duck, it is a duck."*
- Python code does not check whether an object explicitly inherits from a specific base class (nominal typing); instead, it checks whether the object implements the required interface methods (structural behavior).
- For instance, if an object implements `__len__()` and `__getitem__()`, Python treats it as a Sequence (allowing indexing and iteration) regardless of its inheritance lineage.

---

### Q5: Why does defining `__eq__` make an object unhashable by default, and how do you restore hashability?
**Model Answer:**
- Python mandates that if two objects compare equal (`a == b`), they must produce the identical hash value (`hash(a) == hash(b)`).
- By default, Python classes inherit `__hash__` from `object` based on memory address (`id()`).
- If you override `__eq__` to compare values (e.g. comparing IDs), using the default address-based hash would violate the hash invariant. To prevent bugs, Python automatically sets `__hash__ = None` whenever `__eq__` is overridden.
- To restore hashability for immutable objects, you must explicitly implement `__hash__()` by hashing a tuple of the immutable fields used in `__eq__`: `return hash((self.id, self.name))`.

---

### Q6: Why is Composition generally favored over Inheritance?
**Model Answer:**
- Inheritance models a rigid "Is-A" relationship and binds child classes tightly to the internal implementation of parent classes. Changes to the parent class can inadvertently break subclasses (the Fragile Base Class problem).
- Composition models a flexible "Has-A" relationship by assembling components as internal instance attributes and delegating tasks to them.
- Benefits of composition:
  - Loose coupling: internal components can be modified or refactored without altering the public API.
  - Runtime flexibility: components can be dynamically swapped (Dependency Injection) for testing or feature switching.
  - Prevents interface pollution: subclassing an existing class (like `list`) exposes unwanted methods (e.g. `sort`, `reverse` on a `Stack`), whereas composition exposes only the intended methods.

---

### Q7: What is Name Mangling in Python, and how is it triggered?
**Model Answer:**
- Name mangling is Python's mechanism for preventing attribute name collisions in class inheritance hierarchies.
- It is triggered when an attribute name is prefixed with at least two leading underscores and at most one trailing underscore (e.g. `__secret`).
- The Python compiler textually transforms the identifier to `_ClassName__secret`.
- While often mistaken for true "private" encapsulation, it is not a security feature; the attribute can still be accessed or modified from the outside using its mangled name (`instance._ClassName__secret`).
