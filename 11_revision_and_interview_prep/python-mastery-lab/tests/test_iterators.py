"""
Automated Tests for Module 07: Iterators, Generators & Protocols
================================================================
Tests iterator protocol (__iter__, __next__), StopIteration,
generator lazy evaluation, and yield from delegation.
"""

import types
import unittest


class TestIteratorsAndGenerators(unittest.TestCase):
    def test_iterator_protocol_methods(self) -> None:
        """Verify custom iterators implement __iter__ and __next__."""
        class CountDown:
            def __init__(self, start: int) -> None:
                self.current = start

            def __iter__(self) -> "CountDown":
                return self

            def __next__(self) -> int:
                if self.current <= 0:
                    raise StopIteration
                val = self.current
                self.current -= 1
                return val

        cd = CountDown(3)
        self.assertEqual(list(cd), [3, 2, 1])
        # Verify it is exhausted
        self.assertEqual(list(cd), [])

    def test_generator_object_type(self) -> None:
        """Verify calling a generator function returns a GeneratorType."""
        def simple_gen():
            yield 1
            yield 2

        g = simple_gen()
        self.assertIsInstance(g, types.GeneratorType)
        self.assertEqual(next(g), 1)
        self.assertEqual(next(g), 2)
        with self.assertRaises(StopIteration):
            next(g)

    def test_yield_from_chaining(self) -> None:
        """Verify yield from flattens nested iterables."""
        def flattener():
            yield from range(3)
            yield from ["x", "y"]

        self.assertEqual(list(flattener()), [0, 1, 2, "x", "y"])


if __name__ == "__main__":
    unittest.main()
