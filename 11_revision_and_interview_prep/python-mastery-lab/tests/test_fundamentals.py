"""
Automated Tests for Module 01: Language Fundamentals
====================================================
Tests operator precedence, associativity, short-circuit evaluation,
and docstring presence.
"""

import keyword
import unittest


class TestLanguageFundamentals(unittest.TestCase):
    def test_keywords_and_case(self) -> None:
        """Verify keyword properties and casing."""
        self.assertIn("True", keyword.kwlist)
        self.assertIn("False", keyword.kwlist)
        self.assertIn("None", keyword.kwlist)
        self.assertIn("def", keyword.kwlist)
        self.assertIn("class", keyword.kwlist)
        # Verify lowercase versions of boolean literals are not keywords
        self.assertNotIn("true", keyword.kwlist)
        self.assertNotIn("false", keyword.kwlist)
        self.assertNotIn("none", keyword.kwlist)

    def test_exponentiation_associativity(self) -> None:
        """Verify right-to-left associativity of exponentiation (**)."""
        self.assertEqual(2 ** 3 ** 2, 512)
        self.assertNotEqual(2 ** 3 ** 2, 64)

    def test_evaluation_order_left_to_right(self) -> None:
        """Verify operands evaluate strictly left-to-right."""
        calls = []

        def get_val(name: str, val: int) -> int:
            calls.append(name)
            return val

        result = get_val("first", 5) + get_val("second", 10) * get_val("third", 2)
        self.assertEqual(result, 25)
        self.assertEqual(calls, ["first", "second", "third"])

    def test_short_circuit_returns_objects(self) -> None:
        """Verify 'and' and 'or' return operand objects, not coerced booleans."""
        # or returns first truthy
        self.assertEqual("" or "fallback", "fallback")
        self.assertEqual("first" or "fallback", "first")
        self.assertEqual(0 or False or [] or 100, 100)

        # and returns first falsy or last truthy
        self.assertEqual(0 and "hello", 0)
        self.assertEqual("apple" and "banana", "banana")
        self.assertIs(True and 50 and None and "end", None)

    def test_chained_comparisons(self) -> None:
        """Verify chained comparisons behave like mathematical inequalities."""
        x = 5
        self.assertTrue(1 < x < 10)
        self.assertFalse(1 < x < 4)

        # Verify middle term is evaluated only once
        eval_count = 0

        def get_x() -> int:
            nonlocal eval_count
            eval_count += 1
            return 5

        result = 1 < get_x() < 10
        self.assertTrue(result)
        self.assertEqual(eval_count, 1)

    def test_docstring_runtime_accessibility(self) -> None:
        """Verify docstrings are preserved on functions at runtime."""
        def sample_function() -> None:
            """This is official documentation."""
            # This is a comment

        self.assertEqual(sample_function.__doc__, "This is official documentation.")


if __name__ == "__main__":
    unittest.main()
