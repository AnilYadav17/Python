"""
02_edge_cases.py
Demonstrates tricky OOP edge cases:
- The mutable class attribute trap across instances
- Property setter infinite recursion bug
- Implementing the Singleton pattern via __new__
- Overriding __eq__ nullifying default __hash__
"""

def demonstrate_mutable_class_attribute_trap():
    print("--- 1. Mutable Class Attribute Trap ---")

    # BUGGY: 'items' is shared across every instance of InventoryBuggy
    class InventoryBuggy:
        items = []  # Shared class-level list!

        def add(self, item):
            self.items.append(item)

    inv1 = InventoryBuggy()
    inv2 = InventoryBuggy()
    inv1.add("sword")
    print(f"inv1 items: {inv1.items}")
    print(f"inv2 items (contaminated!): {inv2.items}")  # Contaminated with 'sword'!

    # FIX: Initialize mutable container in __init__
    class InventoryFixed:
        def __init__(self):
            self.items = []  # Unique to each instance

        def add(self, item):
            self.items.append(item)

    f1 = InventoryFixed()
    f2 = InventoryFixed()
    f1.add("shield")
    print(f"Fixed f1 items: {f1.items}, f2 items: {f2.items}")


def demonstrate_property_recursion():
    print("\n--- 2. Property Setter Recursion Guard ---")

    class Temperature:
        def __init__(self, celsius):
            self.celsius = celsius

        @property
        def celsius(self):
            return self._celsius  # Reads from backing field '_celsius'

        @celsius.setter
        def celsius(self, value):
            # If we wrote 'self.celsius = value', it would call THIS setter recursively!
            # Correct: Assign to backing field '_celsius'
            self._celsius = value

    t = Temperature(25)
    print(f"Temperature: {t.celsius}°C")


def demonstrate_singleton_pattern():
    print("\n--- 3. Singleton Pattern via __new__ ---")

    class DatabasePool:
        _instance = None  # Class-level reference to the single instance

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                # Allocate the instance once and cache it
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance

        def __init__(self, dsn="sqlite:///:memory:"):
            if not self._initialized:
                self.dsn = dsn
                self._initialized = True

    p1 = DatabasePool("mysql://host1")
    p2 = DatabasePool("mysql://host2")
    print(f"p1 is p2: {p1 is p2}")  # True: exact same instance
    print(f"p2 DSN retained first initialization: {p2.dsn}")


def demonstrate_hash_nullification():
    print("\n--- 4. __eq__ Nullifying __hash__ ---")

    class User:
        def __init__(self, user_id):
            self.user_id = user_id

        # Defining __eq__ without defining __hash__ causes Python to set __hash__ = None
        def __eq__(self, other):
            return isinstance(other, User) and self.user_id == other.user_id

    u1 = User(1)
    u2 = User(1)
    print(f"u1 == u2: {u1 == u2}")
    try:
        user_set = {u1, u2}
    except TypeError as err:
        print(f"Caught expected TypeError placing u1 in set: {err}")


def main():
    demonstrate_mutable_class_attribute_trap()
    demonstrate_property_recursion()
    demonstrate_singleton_pattern()
    demonstrate_hash_nullification()

if __name__ == "__main__":
    main()
