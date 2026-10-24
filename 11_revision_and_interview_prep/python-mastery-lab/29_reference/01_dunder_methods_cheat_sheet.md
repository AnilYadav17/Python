# Python Dunder (Magic) Methods Quick Reference

Special methods (double underscore "dunder" methods) let your custom classes hook into Python's built-in operators, protocols, and language semantics.

---

## 1. Object Lifecycle
| Method | Trigger / Purpose |
| :--- | :--- |
| `__new__(cls, ...)` | Allocates memory for the instance; returns the new object. |
| `__init__(self, ...)` | Initializes attributes of the newly created instance. |
| `__del__(self)` | Called when the instance's reference count reaches zero. |

---

## 2. String Representations
| Method | Trigger / Purpose |
| :--- | :--- |
| `__repr__(self)` | Unambiguous developer representation; ideally valid Python code (`eval(repr(obj)) == obj`). |
| `__str__(self)` | User-friendly readable representation (`print(obj)`, `str(obj)`). |
| `__format__(self, format_spec)` | Formatted string operations (`f"{obj:format_spec}"`). |

---

## 3. Comparison Operators
| Method | Trigger |
| :--- | :--- |
| `__eq__(self, other)` | `self == other` |
| `__ne__(self, other)` | `self != other` |
| `__lt__(self, other)` | `self < other` |
| `__le__(self, other)` | `self <= other` |
| `__gt__(self, other)` | `self > other` |
| `__ge__(self, other)` | `self >= other` |

---

## 4. Arithmetic & Bitwise
| Method | Trigger |
| :--- | :--- |
| `__add__(self, other)` | `self + other` |
| `__sub__(self, other)` | `self - other` |
| `__mul__(self, other)` | `self * other` |
| `__truediv__(self, other)` | `self / other` |
| `__floordiv__(self, other)`| `self // other` |
| `__mod__(self, other)` | `self % other` |
| `__pow__(self, other)` | `self ** other` |
| `__iadd__(self, other)` | In-place addition `self += other` (mutates in-place). |
| `__radd__(self, other)` | Reflected addition when left operand does not support operation. |

---

## 5. Protocols: Container & Sequences
| Method | Trigger / Purpose |
| :--- | :--- |
| `__len__(self)` | `len(obj)` (must return integer $\ge 0$). |
| `__getitem__(self, key)` | `obj[key]` item or slice lookup. |
| `__setitem__(self, key, val)` | `obj[key] = val` item assignment. |
| `__delitem__(self, key)` | `del obj[key]` item deletion. |
| `__contains__(self, item)` | `item in obj` membership testing ($O(1)$ in sets/dicts). |
| `__iter__(self)` | `iter(obj)`, returns an iterator. |
| `__next__(self)` | `next(obj)`, returns next item or raises `StopIteration`. |

---

## 6. Context Managers
| Method | Trigger / Purpose |
| :--- | :--- |
| `__enter__(self)` | Called on entering `with` block; return value bound to `as target`. |
| `__exit__(self, exc_type, exc_val, tb)` | Called on exiting `with` block. Return `True` to swallow exception. |
| `__aenter__(self)`, `__aexit__(...)` | Asynchronous context managers (`async with`). |

---

## 7. Descriptors & Callable
| Method | Trigger / Purpose |
| :--- | :--- |
| `__call__(self, ...)` | Allows instance to be invoked as a function: `obj(*args)`. |
| `__get__(self, instance, owner)` | Descriptor getter. |
| `__set__(self, instance, value)` | Descriptor setter. |
| `__delete__(self, instance)` | Descriptor deleter. |
