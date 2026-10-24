"""
Automated Tests for Module 04: Operators & Overloading
======================================================
Tests arithmetic modulo, negative division, in-place += mutation,
bitwise masks, and dunder operator dispatch.
"""

import unittest


class TestOperators(unittest.TestCase):
    def test_arithmetic_modulo_and_floor(self) -> None:
        """Verify true division, floor division, and negative modulo."""
        self.assertEqual(10 / 4, 2.5)
        self.assertEqual(10 // 4, 2)
        self.assertEqual(-10 // 3, -4)
        self.assertEqual(14 % 5, 4)

    def test_iadd_vs_add_on_lists(self) -> None:
        """Verify += preserves list identity while + produces a new list."""
        lst_a = [1, 2]
        id_before = id(lst_a)
        lst_a += [3]
        self.assertEqual(id(lst_a), id_before)

        lst_b = [1, 2]
        id_before_b = id(lst_b)
        lst_b = lst_b + [3]
        self.assertNotEqual(id(lst_b), id_before_b)

    def test_bitwise_operations(self) -> None:
        """Verify bitwise operations, shifts, and inverts."""
        self.assertEqual(5 << 1, 10)
        self.assertEqual(20 >> 2, 5)
        self.assertEqual(0b1100 & 0b1010, 0b1000)
        self.assertEqual(0b1100 | 0b1010, 0b1110)
        self.assertEqual(0b1100 ^ 0b1010, 0b0110)
        self.assertEqual(~0, -1)

    def test_operator_dunder_dispatch(self) -> None:
        """Verify custom objects dispatch operators to dunder methods."""
        class Currency:
            def __init__(self, amount: int) -> None:
                self.amount = amount

            def __add__(self, other: "Currency") -> "Currency":
                return Currency(self.amount + other.amount)

            def __eq__(self, other: object) -> bool:
                if not isinstance(other, Currency):
                    return False
                return self.amount == other.amount

        c1 = Currency(50)
        c2 = Currency(75)
        c3 = c1 + c2

        self.assertEqual(c3, Currency(125))
        self.assertEqual(c3.amount, 125)


if __name__ == "__main__":
    unittest.main()
