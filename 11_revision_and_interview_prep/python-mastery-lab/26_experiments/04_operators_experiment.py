"""
Experiment 04: Operators, Overloading, Bitmasks & Mutation Semantics
===================================================================

Questions Investigated:
-----------------------
1. How does Python map operators (+, ==) to dunder methods (__add__, __eq__)?
2. How does list += compare to list = list + [...] in terms of identity and allocation?
3. How do binary bitmasks track and query permission flags?
4. Are De Morgan's logical transformations mathematically equivalent in Python?

Instructions to Run:
--------------------
$ python3 26_experiments/04_operators_experiment.py
"""

def banner(title: str) -> None:
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


def test_operator_overloading() -> None:
    banner("1. OPERATOR OVERLOADING VIA DUNDER METHODS")

    class Vector:
        def __init__(self, x: float, y: float) -> None:
            self.x = x
            self.y = y

        def __add__(self, other: "Vector") -> "Vector":
            return Vector(self.x + other.x, self.y + other.y)

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, Vector):
                return False
            return self.x == other.x and self.y == other.y

        def __repr__(self) -> str:
            return f"Vector({self.x}, {self.y})"

    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = v1 + v2
    print(f"{v1} + {v2} = {v3}")

    assert v3 == Vector(4, 6), "Vector addition must produce Vector(4, 6)"
    assert (v1 == v2) is False, "v1 and v2 are not equal"
    print("-> Confirmed: Python operators dispatch cleanly to __add__ and __eq__.")


def test_iadd_vs_add_identity() -> None:
    banner("2. IN-PLACE += VS CONCATENATION +")

    # In-place += preserves list identity
    lst1 = [1, 2]
    old_id1 = id(lst1)
    lst1 += [3]
    new_id1 = id(lst1)
    print(f"lst1 += [3] -> Old ID: {old_id1}, New ID: {new_id1} (Equal: {old_id1 == new_id1})")
    assert old_id1 == new_id1, "lst1 += [3] must mutate in-place without changing identity"

    # Concatenation + creates a new object
    lst2 = [1, 2]
    old_id2 = id(lst2)
    lst2 = lst2 + [3]
    new_id2 = id(lst2)
    print(f"lst2 = lst2 + [3] -> Old ID: {old_id2}, New ID: {new_id2} (Equal: {old_id2 == new_id2})")
    assert old_id2 != new_id2, "lst2 + [3] must allocate a new list with a different identity"
    print("-> Confirmed: += modifies in-place; + allocates a fresh object.")


def test_bitwise_permissions() -> None:
    banner("3. BITWISE PERMISSION BITMASKS")
    READ = 0b100     # 4
    WRITE = 0b010    # 2
    EXECUTE = 0b001  # 1

    perms = READ | WRITE  # 0b110 = 6
    print(f"Combined Perms: {bin(perms)} ({perms})")

    has_read = bool(perms & READ)
    has_write = bool(perms & WRITE)
    has_exec = bool(perms & EXECUTE)

    print(f"Has Read: {has_read}, Has Write: {has_write}, Has Execute: {has_exec}")
    assert has_read is True
    assert has_write is True
    assert has_exec is False
    print("-> Confirmed: Bitwise AND cleanly tests flags in a bitmask.")


def test_de_morgans_laws() -> None:
    banner("4. DE MORGAN'S LAWS VERIFICATION")
    test_cases = [
        (True, True),
        (True, False),
        (False, True),
        (False, False),
    ]

    for a, b in test_cases:
        # Law 1: not (a and b) == (not a) or (not b)
        assert (not (a and b)) == ((not a) or (not b))
        # Law 2: not (a or b) == (not a) and (not b)
        assert (not (a or b)) == ((not a) and (not b))

    print("-> Confirmed: De Morgan's laws hold for all boolean combinations.")


def main() -> None:
    test_operator_overloading()
    test_iadd_vs_add_identity()
    test_bitwise_permissions()
    test_de_morgans_laws()
    banner("ALL OPERATOR EXPERIMENTS VERIFIED SUCCESSFULLY")


if __name__ == "__main__":
    main()
