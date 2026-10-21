"""
05_advanced_idiomatic.py
Demonstrates advanced dunder (magic) methods by implementing an immutable
2D Vector class supporting:
- __repr__ and __str__
- Operator overloading: __add__, __sub__, __mul__, __rmul__, __abs__
- Comparison & Hashing: __eq__, __hash__
- Container-like access: __len__, __getitem__
- Truthiness: __bool__
"""

import math

class Vector2D:
    # __slots__ optimizes memory allocation by preventing dynamic __dict__ creation
    __slots__ = ("_x", "_y", "_hash")

    def __init__(self, x: float, y: float):
        # Store as private immutable attributes
        object.__setattr__(self, "_x", float(x))
        object.__setattr__(self, "_y", float(y))
        object.__setattr__(self, "_hash", None)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # Developer string representation
    def __repr__(self):
        return f"Vector2D(x={self._x}, y={self._y})"

    # User-friendly string representation
    def __str__(self):
        return f"({self._x}, {self._y})"

    # Absolute value: magnitude of vector
    def __abs__(self):
        return math.hypot(self._x, self._y)

    # Boolean truthiness: non-zero magnitude is True
    def __bool__(self):
        return bool(self._x or self._y)

    # Addition: Vector + Vector
    def __add__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self._x + other._x, self._y + other._y)

    # Subtraction: Vector - Vector
    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self._x - other._x, self._y - other._y)

    # Multiplication: Vector * scalar (or dot product if Vector)
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector2D(self._x * scalar, self._y * scalar)
        if isinstance(scalar, Vector2D):
            # Dot product
            return self._x * scalar._x + self._y * scalar._y
        return NotImplemented

    # Reflected multiplication: scalar * Vector
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # Equality: check both components
    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self._x, other._x) and math.isclose(self._y, other._y)

    # Hashing: makes Vector2D usable in sets and as dictionary keys
    def __hash__(self):
        if self._hash is None:
            computed = hash((self._x, self._y))
            object.__setattr__(self, "_hash", computed)
        return self._hash

    # Sequence protocol: len(v) returns dimension (2)
    def __len__(self):
        return 2

    # Indexing: v[0] -> x, v[1] -> y
    def __getitem__(self, index):
        if index == 0:
            return self._x
        elif index == 1:
            return self._y
        raise IndexError("Vector2D index out of range (must be 0 or 1).")


def main():
    print("--- 1. Vector Instantiation & Representation ---")
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    print(f"v1 repr: {repr(v1)}")
    print(f"v1 str:  {v1}")
    print(f"v1 magnitude: {abs(v1)}")

    print("\n--- 2. Operator Overloading ---")
    v_sum = v1 + v2
    v_diff = v1 - v2
    v_scaled = v1 * 3
    v_rscaled = 2.5 * v2
    dot_product = v1 * v2

    print(f"v1 + v2 = {v_sum}")
    print(f"v1 - v2 = {v_diff}")
    print(f"v1 * 3  = {v_scaled}")
    print(f"2.5 * v2 = {v_rscaled}")
    print(f"v1 . v2 = {dot_product}")

    print("\n--- 3. Container Indexing & Sequence Protocol ---")
    print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")
    x_coord, y_coord = v1  # Sequence unpacking works automatically via __getitem__ and __len__!
    print(f"Unpacked coords: x={x_coord}, y={y_coord}")

    print("\n--- 4. Hashing and Set Membership ---")
    v3 = Vector2D(3.0, 4.0)
    print(f"v1 == v3: {v1 == v3}")
    vectors_set = {v1, v2, v3}
    print(f"Set length (v1 and v3 deduplicated): {len(vectors_set)}")

if __name__ == "__main__":
    main()
