"""
05_advanced_idiomatic.py
Demonstrates advanced typing patterns:
1. Generic Repository with TypeVar and Generic[T]
2. Structural Typing with @runtime_checkable Protocol (Static Duck Typing)
"""

from typing import TypeVar, Generic, Protocol, runtime_checkable

# 1. Structural Subtyping with Protocol
@runtime_checkable
class Serializable(Protocol):
    """Protocol declaring an object must have a to_dict() method."""
    def to_dict(self) -> dict:
        ...

class Product:
    def __init__(self, sku: str, price: float):
        self.sku = sku
        self.price = price

    # Product does NOT inherit from Serializable, but satisfies its interface!
    def to_dict(self) -> dict:
        return {"sku": self.sku, "price": self.price}


# 2. Generic Repository Pattern
T = TypeVar("T")

class MemoryRepository(Generic[T]):
    def __init__(self):
        self._storage: list[T] = []

    def add(self, entity: T) -> None:
        self._storage.append(entity)

    def get_all(self) -> list[T]:
        return list(self._storage)

    def find_first(self) -> T | None:
        return self._storage[0] if self._storage else None


def serialize_any_model(obj: Serializable) -> str:
    """Accepts any object conforming to Serializable Protocol."""
    import json
    return json.dumps(obj.to_dict())


def main():
    print("--- 1. Structural Subtyping with Protocol ---")
    prod = Product("TECH-100", 299.99)
    # Check runtime adherence
    print(f"isinstance(prod, Serializable): {isinstance(prod, Serializable)}")
    print(f"Serialized output: {serialize_any_model(prod)}")

    print("\n--- 2. Generic Repository ---")
    product_repo = MemoryRepository[Product]()
    product_repo.add(Product("LAPTOP-01", 1200.00))
    product_repo.add(Product("MOUSE-02", 25.50))

    first_item = product_repo.find_first()
    if first_item:
        print(f"First product in generic repo: {first_item.sku} (${first_item.price})")

if __name__ == "__main__":
    main()
