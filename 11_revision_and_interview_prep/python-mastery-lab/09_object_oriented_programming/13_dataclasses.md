# Lesson 13: Dataclasses (PEP 557)

## 1. The Pain of Writing Boilerplate Classes
In traditional Python OOP, creating a class to simply hold data required writing endless boilerplate:
```python
# The Tedious Traditional Way:
class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

    def __eq__(self, other):
        return (self.id, self.name, self.email) == (other.id, other.name, other.email)
```
Look at all those lines of repetitive code just to store three fields!

---

## 2. Enter `@dataclass` (Clean, Modern Python)

Introduced in **Python 3.7 (PEP 557)**, the `@dataclass` decorator inspects your type annotations and **automatically generates `__init__`, `__repr__`, and `__eq__` for you in just 4 lines**:

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool = True  # Default value!
```

### Look What You Get for Free:
```python
user1 = User(101, "Anil", "anil@example.com")
user2 = User(101, "Anil", "anil@example.com")

# 1. Beautiful __repr__ out of the box!
print(user1)
# Output: User(id=101, name='Anil', email='anil@example.com', is_active=True)

# 2. Value-based __eq__ comparison works automatically!
print(user1 == user2)  # True!
```

---

## 3. Immutable Dataclasses (`frozen=True`)

Want an immutable object that can be safely used as a dictionary key or placed inside a set? Set `frozen=True`:

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lng: float

point = Coordinate(12.9716, 77.5946)

# Trying to mutate raises FrozenInstanceError!
# point.lat = 0.0  # dataclasses.FrozenInstanceError: cannot assign to field 'lat'

# Can be used as a dictionary key!
city_map = {point: "Bangalore"}
print(city_map[point])  # "Bangalore"
```

---

## 4. The Mutable Default Trap in Dataclasses: Use `field(default_factory=...)`

Just like regular function defaults, you cannot write `tags: list = []` in a dataclass!  
Use `default_factory`:

```python
from dataclasses import dataclass, field

@dataclass
class BlogPost:
    title: str
    tags: list[str] = field(default_factory=list)  # Brand-new list per instance!
```

---

## 5. Quick Self-Test
1. What dunder methods does `@dataclass` generate by default?
   - *Answer: `__init__`, `__repr__`, and `__eq__`.*
2. How do you make a dataclass immutable and hashable?
   - *Answer: By adding `frozen=True` (`@dataclass(frozen=True)`).*
