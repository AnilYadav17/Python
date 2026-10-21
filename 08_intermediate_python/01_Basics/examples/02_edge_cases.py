"""
02_edge_cases.py
Demonstrates tricky edge cases in Python:
- Small integer caching (-5 to 256) vs larger integers
- Floating point precision limitations
- Modulo behavior with negative numbers
- Mutable objects inside immutable tuples
- Short-circuit boolean evaluation side-effects
"""

import math

def demonstrate_small_int_caching():
    print("--- Edge Case 1: Small Integer Caching ---")
    # CPython pre-allocates singletons for integers in range [-5, 256]
    a = 256
    b = 256
    # 'is' checks pointer identity; '==' checks value equality
    print(f"a = 256, b = 256 -> a is b: {a is b}")  # True: same singleton object

    # Dynamically construct integers at runtime to bypass compile-time constant folding
    x = int("1000")
    y = int("1000")
    print(f"x = 1000, y = 1000 (dynamically constructed) -> x is y: {x is y}")  # False: distinct objects
    print(f"x == y: {x == y}")  # True: values are equal


def demonstrate_float_precision():
    print("\n--- Edge Case 2: Floating Point Precision ---")
    # Binary floating point cannot accurately represent 0.1 or 0.2
    total = 0.1 + 0.2
    expected = 0.3
    print(f"0.1 + 0.2 == 0.3: {total == expected}")  # False!
    print(f"Actual total representation: {total:.17f}")
    # Fix: use math.isclose() for floating-point comparisons
    print(f"math.isclose(0.1 + 0.2, 0.3): {math.isclose(total, expected)}")  # True


def demonstrate_python_modulo():
    print("\n--- Edge Case 3: Python Modulo Sign Rule ---")
    # In Python, the sign of (a % b) always matches the divisor (b)
    # Unlike C/C++ which truncates towards zero, Python rounds floor towards -infinity
    result = -7 % 3
    print(f"-7 % 3 in Python = {result}")  # 2 (since -7 = 3 * (-3) + 2)
    print(f"7 % -3 in Python = {7 % -3}")  # -2 (since 7 = -3 * (-3) + (-2))


def demonstrate_mutable_inside_tuple():
    print("\n--- Edge Case 4: Mutable Objects Inside Tuples ---")
    # A tuple guarantees immutability of its reference bindings, NOT the objects themselves
    inner_list = [1, 2]
    frozen_tuple = (inner_list, "constant")
    print(f"Initial tuple: {frozen_tuple}")

    # Mutating the inner list in-place succeeds!
    frozen_tuple[0].append(99)
    print(f"Tuple after inner list append: {frozen_tuple}")

    # However, attempting += on the list inside the tuple creates a famous quirk:
    try:
        frozen_tuple[0] += [100]
    except TypeError as e:
        # In-place mutation succeeds on list, but reassigning reference to frozen_tuple[0] fails!
        print(f"Caught expected TypeError on += inside tuple: {e}")
    print(f"Tuple state after failed += : {frozen_tuple} (100 was still appended!)")


def demonstrate_short_circuit_side_effects():
    print("\n--- Edge Case 5: Short-Circuit Evaluation Side Effects ---")
    calls = []

    def check_a():
        calls.append("A")
        return False

    def check_b():
        calls.append("B")
        return True

    # In 'and', if first expression is False, second is NEVER evaluated
    res = check_a() and check_b()
    print(f"check_a() and check_b() result: {res}, function calls made: {calls}")


def main():
    demonstrate_small_int_caching()
    demonstrate_float_precision()
    demonstrate_python_modulo()
    demonstrate_mutable_inside_tuple()
    demonstrate_short_circuit_side_effects()

if __name__ == "__main__":
    main()
