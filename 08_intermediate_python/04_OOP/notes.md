# 04. Object-Oriented Programming (OOP): Complete Reference

---

## 1. Classes, Objects, and Attributes

### What it is
- A **class** is a blueprint/template that defines the state (attributes) and behavior (methods) of a conceptual entity.
- An **object (instance)** is a concrete instantiation of a class residing in heap memory.
- **Instance Attributes**: Variables bound to a specific instance (`self.attr`), stored in `instance.__dict__`.
- **Class Attributes**: Variables defined directly inside the class body, shared across *all* instances of that class, stored in `Class.__dict__`.

### Why it matters
- Models real-world domain logic into coherent entities, binding data and associated behaviors together.
- Class attributes provide shared state, class configuration, default settings, and tracking counters across all instances.

### How it works (internals, if relevant)
- Classes in Python are themselves objects at runtime! Every class is an instance of the metaclass `type`.
- When an attribute is accessed via `instance.attr`, Python first checks `instance.__dict__`.
- If absent, it searches the class namespace `type(instance).__dict__`, followed by the inheritance chain via the Method Resolution Order (MRO).

### Common mistakes / gotchas
- Mutating a mutable class attribute via an instance:
  ```python
  class Dog:
      tricks = [] # Shared class attribute!
  ```
  Calling `d1.tricks.append("roll")` mutates `tricks` for all dogs! Instance-specific data must always be initialized inside `__init__` as `self.tricks = []`.
- Shadowing a class attribute: writing `instance.class_attr = 5` creates a new instance attribute that shadows the class attribute for that instance alone, rather than modifying the shared class attribute.

### Connects to
- Object Instantiation Lifecycle (subtopic 2 below) and Encapsulation (subtopic 4).

---

## 2. Object Instantiation Lifecycle: `__new__` vs `__init__`

### What it is
- Object creation in Python is a two-phase process:
  1. `__new__(cls, *args, **kwargs)`: The static constructor method responsible for **allocating** and returning the raw instance in memory.
  2. `__init__(self, *args, **kwargs)`: The initializer method responsible for **populating** the newly created instance's state.

### Why it matters
- Understanding `__new__` is mandatory for implementing the Singleton pattern, customizing immutable types (subclassing `int`, `str`, `tuple`), and building custom metaclasses.
- `__init__` cannot return anything other than `None`; returning a value raises `TypeError: __init__() should return None`.

### How it works (internals, if relevant)
- When you execute `obj = MyClass(x, y)`:
  1. Python calls `MyClass.__new__(MyClass, x, y)`.
  2. If `__new__` returns an instance of `MyClass`, Python then calls `instance.__init__(x, y)`.
  3. If `__new__` returns an instance of a different class, Python completely skips `__init__`.

### Common mistakes / gotchas
- Returning a value from `__init__`.
- Forgetting to invoke `super().__new__(cls)` when overriding `__new__`, resulting in `None` being returned and `__init__` never running.

### Connects to
- Advanced Object Patterns (subtopic 9) and Metaclasses.

---

## 3. Method Types: Instance, Class, and Static Methods

### What it is
- **Instance Methods**: Standard methods receiving the instance (`self`) as the first argument; can access and modify both instance and class state.
- **Class Methods** (`@classmethod`): Receive the class (`cls`) as the first argument; can access and modify class state, but cannot access instance-specific state.
- **Static Methods** (`@staticmethod`): Receive neither `self` nor `cls`; regular functions placed inside the class namespace for logical grouping.

### Why it matters
- Class methods serve as **alternative constructors** (e.g. `datetime.fromtimestamp()`, `dict.fromkeys()`), parsing different data formats to instantiate objects.
- Static methods clearly communicate to developers that a method has no side effects on instance or class state (pure utility).

### How it works (internals, if relevant)
- Implemented using Python's **Descriptor Protocol**:
  - Functions are non-data descriptors implementing `__get__()`.
  - When accessed through an instance `inst.method()`, `function.__get__(inst, type(inst))` binds `inst` as the first argument `self` (a bound method).
  - `@classmethod` binds the class `cls` as the first argument.
  - `@staticmethod` simply returns the raw underlying function without binding any arguments.

### Common mistakes / gotchas
- Forgetting the `self` parameter in instance method definitions, causing `TypeError: method() takes 0 positional arguments but 1 was given` upon invocation.
- Calling a class method when instance data was needed, or vice-versa.

### Connects to
- Encapsulation (subtopic 4 below) and Python Descriptors.

---

## 4. Encapsulation & Data Hiding

### What it is
- The principle of restricting direct external access to an object's internal representation, exposing state only through controlled interfaces:
  - **Public**: `self.name` (accessible anywhere).
  - **Protected**: `self._name` (convention signaling internal use; subclasses and internal methods).
  - **Private**: `self.__name` (triggers name mangling: transformed to `_ClassName__name`).
  - **Properties**: Managed attributes using `@property`, `@<attr>.setter`, and `@<attr>.deleter`.

### Why it matters
- Enables validation, lazy evaluation, and invariants enforcement without breaking client code (maintains uniform attribute access syntax `obj.attr`).
- Protects internal object state from corrupted, invalid values.

### How it works (internals, if relevant)
- Python has no true compiler-enforced access restrictions (like C++ or Java `private`).
- **Name Mangling**: Any identifier with at least two leading underscores and at most one trailing underscore (`__attr`) is textually replaced by the compiler with `_ClassName__attr`.
- This is designed to prevent unintentional name clashes in subclasses, not for impenetrable security.
- `@property` converts a method into a descriptor whose getter and setter are called whenever the attribute is read or assigned.

### Common mistakes / gotchas
- Creating recursive loops inside property setters: writing `self.x = value` inside `def x(self, value): self.x = value` calls the setter infinitely until `RecursionError`. It must write to a backing variable: `self._x = value`.
- Believing double-underscore private variables are completely unhackable: they are still accessible via `obj._ClassName__attr`.

### Connects to
- Inheritance (subtopic 5 below).

---

## 5. Inheritance, MRO, and `super()`

### What it is
- The mechanism by which a child class acquires attributes and behaviors from one or more parent classes:
  - **Single Inheritance**: Child inherits from one parent (`class Child(Parent): ...`).
  - **Multilevel Inheritance**: Child inherits from parent, which inherits from grandparent.
  - **Multiple Inheritance**: Child inherits from multiple parents (`class Child(ParentA, ParentB): ...`).
- **Method Resolution Order (MRO)**: The deterministic order in which Python searches base classes for an attribute or method.
- `super()`: Returns a proxy object delegating method calls to the next class in the MRO chain.

### Why it matters
- Enables polymorphic reuse and specialization of code across hierarchies.
- Multiple inheritance allows mixins and modular feature composition, but requires strict MRO understanding to avoid the infamous **Diamond Problem**.

### How it works (internals, if relevant)
- Python calculates MRO using the **C3 Linearization Algorithm**:
  1. Children precede their parents.
  2. The relative order of parent classes listed in the class definition is preserved.
  3. No class appears twice in the resolution chain.
- You can inspect a class's MRO at any time via `Class.__mro__` or `Class.mro()`.
- `super().method()` does *not* simply call the immediate parent; it calls the *next class in the caller instance's MRO*, which is essential for cooperative multiple inheritance.

### Common mistakes / gotchas
- Calling `ParentClass.__init__(self)` directly instead of `super().__init__()`, breaking cooperative multiple inheritance chains.
- Creating inconsistent class hierarchies that violate local precedence order, raising `TypeError: Cannot create a consistent method resolution order (MRO)`.

### Connects to
- Polymorphism (subtopic 6 below) and Abstraction (subtopic 7).

---

## 6. Polymorphism & Duck Typing

### What it is
- **Polymorphism**: The ability of different types to respond to the same method interface in their own distinct manner.
- **Duck Typing**: Python's dynamic typing philosophy: *"If it walks like a duck and quacks like a duck, it is a duck."* Code does not verify object types; it verifies whether objects implement the required methods or behaviors.
- **Operator Overloading**: Customizing how built-in operators (`+`, `-`, `*`, `==`) behave on custom classes by overriding dunder methods.

### Why it matters
- Promotes extreme decoupling: algorithms and functions depend on behavior/interfaces rather than concrete class inheritance hierarchies.
- Overloading operators makes custom domain models (vectors, money, matrices) intuitive and idiomatic.

### How it works (internals, if relevant)
- When executing `len(x)`, Python invokes `x.__len__()`.
- When iterating `for item in x:`, Python calls `x.__iter__()` (or falls back to `__getitem__`).
- Binary operators check for reverse operations: if `a + b` fails because `type(a)` does not know how to add `b`, Python evaluates `b.__radd__(a)`.

### Common mistakes / gotchas
- Writing explicit type checks (`if type(obj) == list: ...`), which breaks duck typing and prevents custom list-like objects or subclasses from working. Use `isinstance()` if type checking is strictly necessary, or prefer EAFP (`try: ... except AttributeError: ...`).
- Forgetting to return `NotImplemented` from comparison dunder methods (`__eq__`, `__lt__`) when encountering an incompatible operand, which prevents Python from attempting the reflected operator on the right-hand operand.

### Connects to
- Abstraction (subtopic 7 below) and Magic Methods (subtopic 8).

---

## 7. Abstraction & Abstract Base Classes (ABCs)

### What it is
- **Abstraction**: Hiding complex implementation details and exposing only essential interface contracts to consumers.
- **Abstract Base Class (ABC)**: A class created by inheriting from `abc.ABC` that cannot be instantiated directly if it contains any `@abc.abstractmethod` declarations.
- Subclasses *must* implement all abstract methods and properties before Python allows instantiation.

### Why it matters
- Enforces architectural contracts and API compliance at instantiation time across large teams and codebases.
- Provides a formal alternative to pure duck typing when explicit structural guarantees are needed.

### How it works (internals, if relevant)
- `abc.ABC` uses the metaclass `abc.ABCMeta`.
- During class creation, `ABCMeta` scans the class attributes for callables with `__isabstractmethod__ = True`.
- If any abstract methods remain unimplemented in a subclass, attempting instantiation immediately raises `TypeError: Can't instantiate abstract class ... with abstract methods ...`.
- Supports virtual subclasses via `ABC.register(Subclass)`, allowing classes to pass `isinstance(obj, ABC)` without explicitly inheriting from `ABC`.

### Common mistakes / gotchas
- Forgetting to inherit from `abc.ABC` (or set `metaclass=ABCMeta`), rendering `@abstractmethod` completely ineffective (the class will instantiate normally without errors).
- Attempting to instantiate an abstract base class directly.

### Connects to
- Type Hints & Protocols (Topic 14) and Testing (Topic 12).

---

## 8. Magic / Dunder Methods

### What it is
- Special methods surrounded by double underscores (`__name__`) that allow user-defined classes to hook into Python's core language mechanics:
  - **Representation**: `__str__` (user-friendly string), `__repr__` (unambiguous developer representation).
  - **Comparison**: `__eq__` (`==`), `__ne__` (`!=`), `__lt__` (`<`), `__le__` (`<=`), `__gt__` (`>`), `__ge__` (`>=`).
  - **Container Protocol**: `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`.
  - **Callable Object**: `__call__` allows an instance to be invoked like a function (`obj()`).
  - **Hashing**: `__hash__` enables an object to be stored in sets and used as dictionary keys.

### Why it matters
- Makes custom classes first-class citizens in Python, integrating seamlessly with built-ins like `print()`, `sorted()`, `len()`, and dictionary indexing.

### How it works (internals, if relevant)
- Dunder methods are looked up directly on the **class** of the object, completely bypassing the instance dictionary (`instance.__dict__`).
- If you define `__eq__`, Python automatically sets `__hash__ = None` to preserve hash consistency (mutable objects must not be hashed). If you need an immutable class to remain hashable, you must explicitly implement both `__eq__` and `__hash__`.

### Common mistakes / gotchas
- Overriding `__eq__` without implementing `__hash__`, making instances unhashable and unable to be placed in sets or dicts.
- `__repr__` vs `__str__`: If `__repr__` is implemented and `__str__` is not, Python falls back to `__repr__`. But if only `__str__` is implemented, inspecting the object in a container or REPL will show the default generic memory address representation. Always implement `__repr__` first!

### Connects to
- Context Managers (Topic 10, `__enter__`/`__exit__`) and Iterators (Topic 11, `__iter__`/`__next__`).

---

## 9. Composition vs Inheritance

### What it is
- **Inheritance ("Is-A" relationship)**: A class derives from a base class to acquire its interface and implementation (e.g., `Manager` is an `Employee`).
- **Composition ("Has-A" relationship)**: A class achieves functionality by referencing one or more separate objects as components and delegating tasks to them (e.g., `Car` has an `Engine`).

### Why it matters
- The Gang of Four design principle: *"Favor object composition over class inheritance."*
- Deep inheritance hierarchies produce fragile, tightly-coupled architectures where changing a base class unpredictably breaks distant child classes (the Fragile Base Class problem).
- Composition provides flexibility, loose coupling, and easy runtime swappability of behaviors (Dependency Injection).

### How it works (internals, if relevant)
- In composition, the composite class holds instance references to component classes in its `__init__`.
- Calls to component methods are either executed explicitly (`self.engine.start()`) or forwarded automatically using `__getattr__` delegation.

### Common mistakes / gotchas
- Using inheritance simply for code sharing when there is no genuine semantic "Is-A" relationship (e.g. subclassing `list` to create a `Stack`, exposing dozens of inappropriate list methods like `insert()` or `sort()`). Use composition instead!
- Overly deep inheritance trees (> 3 levels) that make tracing method definitions difficult.

### Connects to
- Context Managers (Topic 10) and Architecture Patterns in Flask (Topic 20).
