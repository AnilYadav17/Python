"""
Experiment 08: OOP, MRO C3 Linearization, Descriptors & Exception Hierarchy
===========================================================================

Questions Investigated:
-----------------------
1. How does Python's C3 Linearization resolve diamond multiple inheritance in __mro__?
2. How do descriptors intercept attribute access and mutate instance state?
3. What is the exact inheritance relationship between BaseException, Exception, and KeyboardInterrupt?
4. How do custom context managers (__enter__, __exit__) enforce cleanup on errors?

Instructions to Run:
--------------------
$ python3 26_experiments/08_oop_and_exceptions.py
"""

from dataclasses import FrozenInstanceError, dataclass


def banner(title: str) -> None:
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


def test_mro_diamond_inheritance() -> None:
    banner("1. MRO & C3 LINEARIZATION (DIAMOND PROBLEM)")

    class A:
        def whoami(self) -> str: return "A"

    class B(A):
        def whoami(self) -> str: return "B"

    class C(A):
        def whoami(self) -> str: return "C"

    class D(B, C):
        pass

    mro_names = [cls.__name__ for cls in D.__mro__]
    print(f"MRO Order for D: {mro_names}")
    assert mro_names == ["D", "B", "C", "A", "object"], "C3 Linearization order mismatch"

    d_instance = D()
    print(f"d.whoami() calls: {d_instance.whoami()}")
    assert d_instance.whoami() == "B", "B must precede C in resolution"
    print("-> Confirmed: C3 Linearization resolves diamond inheritance deterministically.")


def test_descriptor_protocol() -> None:
    banner("2. DESCRIPTOR PROTOCOL (__set_name__, __get__, __set__)")

    class PositiveInteger:
        def __set_name__(self, owner, name):
            self.name = name

        def __get__(self, instance, owner):
            if instance is None:
                return self
            return instance.__dict__.get(self.name, 0)

        def __set__(self, instance, value):
            if value < 0:
                raise ValueError(f"{self.name} cannot be negative")
            instance.__dict__[self.name] = value

    class Player:
        score = PositiveInteger()

    p = Player()
    p.score = 50
    print(f"Player score: {p.score}")
    assert p.score == 50

    caught_err = False
    try:
        p.score = -10
    except ValueError as err:
        print(f"Caught expected descriptor error: {err}")
        caught_err = True

    assert caught_err, "Descriptor must reject negative values"
    print("-> Confirmed: Descriptors cleanly intercept and validate attribute access.")


def test_frozen_dataclass_hashability() -> None:
    banner("3. FROZEN DATACLASSES AS DICTIONARY KEYS")

    @dataclass(frozen=True)
    class GeoPoint:
        lat: float
        lng: float

    pt1 = GeoPoint(12.97, 77.59)
    mapping = {pt1: "Bangalore"}
    print(f"Point {pt1} -> {mapping[pt1]}")

    mutated = False
    try:
        pt1.lat = 0.0  # type: ignore
    except FrozenInstanceError:
        mutated = True

    assert mutated, "Frozen dataclass must forbid attribute modification"
    assert mapping[GeoPoint(12.97, 77.59)] == "Bangalore", "Equal points must hash to same key"
    print("-> Confirmed: Frozen dataclasses are immutable and hashable.")


def test_exception_hierarchy() -> None:
    banner("4. EXCEPTION HIERARCHY & KEYBOARD INTERRUPT ISOLATION")

    # KeyboardInterrupt and SystemExit do NOT inherit from Exception!
    assert issubclass(ZeroDivisionError, Exception)
    assert issubclass(ValueError, Exception)
    assert not issubclass(KeyboardInterrupt, Exception), "KeyboardInterrupt must not inherit from Exception"
    assert not issubclass(SystemExit, Exception), "SystemExit must not inherit from Exception"
    assert issubclass(KeyboardInterrupt, BaseException), "KeyboardInterrupt inherits from BaseException"

    print("Confirmed hierarchy: KeyboardInterrupt and SystemExit bypass 'except Exception:'")


def main() -> None:
    test_mro_diamond_inheritance()
    test_descriptor_protocol()
    test_frozen_dataclass_hashability()
    test_exception_hierarchy()
    banner("ALL OOP & EXCEPTION EXPERIMENTS VERIFIED")


if __name__ == "__main__":
    main()
