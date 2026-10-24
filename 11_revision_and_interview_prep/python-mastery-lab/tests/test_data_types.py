"""
Automated Tests for Module 03: Data Types, Hashability & Truthiness
===================================================================
Tests IEEE 754 precision, Decimal, range memory, dict merging,
and truth-value testing.
"""

from decimal import Decimal
import math
import sys
import unittest


class TestDataTypes(unittest.TestCase):
    def test_float_precision_and_isclose(self) -> None:
        """Verify float rounding artifact and math.isclose resolution."""
        self.assertNotEqual(0.1 + 0.2, 0.3)
        self.assertTrue(math.isclose(0.1 + 0.2, 0.3))
        self.assertEqual(Decimal("0.1") + Decimal("0.2"), Decimal("0.3"))

    def test_hashability_and_dict_keys(self) -> None:
        """Verify immutable types are hashable and mutable containers raise TypeError."""
        hashable_keys = [42, 3.14, "hello", (1, 2, 3), frozenset([1, 2])]
        for k in hashable_keys:
            d = {k: "valid"}
            self.assertEqual(d[k], "valid")

        with self.assertRaises(TypeError):
            _ = {[1, 2]: "invalid"}

        with self.assertRaises(TypeError):
            _ = {(1, [2]): "invalid"}

    def test_range_lazy_properties(self) -> None:
        """Verify range memory is O(1) and arithmetic membership lookup works."""
        r1 = range(10)
        r2 = range(10_000_000_000)
        self.assertEqual(sys.getsizeof(r1), sys.getsizeof(r2))
        self.assertIn(5_000_000_000, r2)
        self.assertNotIn(5_000_000_001, range(0, 10_000_000_000, 2))

    def test_dict_merge_operator(self) -> None:
        """Verify dict union operator (|) merges dictionaries with right-hand precedence."""
        d1 = {"a": 1, "b": 2}
        d2 = {"b": 99, "c": 3}
        merged = d1 | d2
        self.assertEqual(merged, {"a": 1, "b": 99, "c": 3})

    def test_truthiness_rules(self) -> None:
        """Verify truth-value testing of containers and zero values."""
        # Falsy
        self.assertFalse(bool(None))
        self.assertFalse(bool(0))
        self.assertFalse(bool(0.0))
        self.assertFalse(bool(""))
        self.assertFalse(bool([]))
        self.assertFalse(bool(()))
        self.assertFalse(bool({}))
        self.assertFalse(bool(set()))

        # Truthy
        self.assertTrue(bool([0]))
        self.assertTrue(bool("0"))
        self.assertTrue(bool("False"))
        self.assertTrue(bool(-1))


if __name__ == "__main__":
    unittest.main()
