"""
Automated Tests for Modules 08, 09, 10: OOP, MRO & Exception Hierarchy
======================================================================
Tests C3 linearization MRO, properties, descriptors, frozen dataclasses,
context managers, and exception inheritance.
"""

from dataclasses import FrozenInstanceError, dataclass
import unittest


class TestOOPAndExceptions(unittest.TestCase):
    def test_mro_c3_linearization(self) -> None:
        """Verify C3 linearization order for multiple inheritance."""
        class Top: pass
        class Left(Top): pass
        class Right(Top): pass
        class Bottom(Left, Right): pass

        expected = [Bottom, Left, Right, Top, object]
        self.assertEqual(list(Bottom.__mro__), expected)

    def test_property_validation(self) -> None:
        """Verify @property getter and setter validation."""
        class Person:
            def __init__(self, age: int) -> None:
                self.age = age

            @property
            def age(self) -> int:
                return self._age

            @age.setter
            def age(self, val: int) -> None:
                if val < 0:
                    raise ValueError("Age cannot be negative")
                self._age = val

        p = Person(20)
        self.assertEqual(p.age, 20)
        p.age = 25
        self.assertEqual(p.age, 25)

        with self.assertRaises(ValueError):
            p.age = -1

    def test_frozen_dataclass_equality(self) -> None:
        """Verify frozen dataclasses support equality and forbid mutation."""
        @dataclass(frozen=True)
        class Token:
            val: str

        t1 = Token("auth")
        t2 = Token("auth")
        self.assertEqual(t1, t2)
        self.assertEqual(hash(t1), hash(t2))

        with self.assertRaises(FrozenInstanceError):
            t1.val = "hacked"  # type: ignore

    def test_context_manager_protocol(self) -> None:
        """Verify custom context managers run __enter__ and __exit__."""
        events = []

        class ManagedResource:
            def __enter__(self) -> "ManagedResource":
                events.append("ENTER")
                return self

            def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
                events.append("EXIT")
                return False

        with ManagedResource():
            events.append("BODY")

        self.assertEqual(events, ["ENTER", "BODY", "EXIT"])

    def test_exception_tree_hierarchy(self) -> None:
        """Verify critical root branches of BaseException."""
        self.assertTrue(issubclass(KeyError, LookupError))
        self.assertTrue(issubclass(IndexError, LookupError))
        self.assertTrue(issubclass(LookupError, Exception))
        self.assertFalse(issubclass(KeyboardInterrupt, Exception))
        self.assertTrue(issubclass(KeyboardInterrupt, BaseException))


if __name__ == "__main__":
    unittest.main()
