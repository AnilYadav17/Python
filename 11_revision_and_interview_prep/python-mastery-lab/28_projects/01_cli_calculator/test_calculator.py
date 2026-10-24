"""
Unit Tests for Project 1: Safe CLI Calculator
=============================================
Tests standard math, precedence, negative numbers, division by zero,
and security violation rejection.
"""

import unittest
from calculator import (
    DivisionByZeroError,
    InvalidExpressionError,
    evaluate,
)


class TestCalculator(unittest.TestCase):
    def test_basic_arithmetic(self) -> None:
        """Verify addition, subtraction, multiplication, and division."""
        self.assertEqual(evaluate("10 + 5"), 15)
        self.assertEqual(evaluate("10 - 3"), 7)
        self.assertEqual(evaluate("4 * 5"), 20)
        self.assertEqual(evaluate("20 / 4"), 5.0)

    def test_precedence_and_parentheses(self) -> None:
        """Verify operator precedence and grouping."""
        self.assertEqual(evaluate("2 + 3 * 4"), 14)
        self.assertEqual(evaluate("(2 + 3) * 4"), 20)
        self.assertEqual(evaluate("2 ** 3 ** 2"), 512)
        self.assertEqual(evaluate("10 + 20 // 3"), 16)

    def test_unary_signs(self) -> None:
        """Verify positive and negative signs."""
        self.assertEqual(evaluate("-5 + 10"), 5)
        self.assertEqual(evaluate("-(-5)"), 5)
        self.assertEqual(evaluate("+10 * -2"), -20)

    def test_division_by_zero(self) -> None:
        """Verify division or modulo by zero raises DivisionByZeroError."""
        with self.assertRaises(DivisionByZeroError):
            evaluate("10 / 0")

        with self.assertRaises(DivisionByZeroError):
            evaluate("10 // 0")

        with self.assertRaises(DivisionByZeroError):
            evaluate("10 % 0")

    def test_security_rejections(self) -> None:
        """Verify code injection and unauthorized AST constructs are rejected."""
        # Function calls
        with self.assertRaises(InvalidExpressionError):
            evaluate("__import__('os').system('ls')")

        # Variable lookups
        with self.assertRaises(InvalidExpressionError):
            evaluate("x + 5")

        # String literals
        with self.assertRaises(InvalidExpressionError):
            evaluate("'hello' + 'world'")

        # Empty expression
        with self.assertRaises(InvalidExpressionError):
            evaluate("   ")


if __name__ == "__main__":
    unittest.main()
