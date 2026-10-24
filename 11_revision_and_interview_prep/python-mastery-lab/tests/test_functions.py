"""
Automated Tests for Module 06: Functions, Scope & Closures
==========================================================
Tests mutable defaults, parameter kinds (/, *), closures,
and decorator wrapping with functools.wraps.
"""

import functools
import unittest


class TestFunctions(unittest.TestCase):
    def test_mutable_default_isolation(self) -> None:
        """Verify the None sentinel pattern isolates default mutable arguments."""
        def safe_append(item: str, storage: list | None = None) -> list:
            if storage is None:
                storage = []
            storage.append(item)
            return storage

        r1 = safe_append("A")
        r2 = safe_append("B")
        self.assertEqual(r1, ["A"])
        self.assertEqual(r2, ["B"])
        self.assertIsNot(r1, r2)

    def test_positional_and_keyword_boundaries(self) -> None:
        """Verify / enforces positional-only and * enforces keyword-only."""
        def sample(a: int, /, b: int, *, c: int) -> tuple[int, int, int]:
            return (a, b, c)

        # Valid calls
        self.assertEqual(sample(1, 2, c=3), (1, 2, 3))
        self.assertEqual(sample(1, b=2, c=3), (1, 2, 3))

        # Invalid keyword on positional-only
        with self.assertRaises(TypeError):
            sample(a=1, b=2, c=3)  # type: ignore

        # Invalid positional on keyword-only
        with self.assertRaises(TypeError):
            sample(1, 2, 3)  # type: ignore

    def test_closure_cell_retention(self) -> None:
        """Verify inner functions capture free variables in closure cells."""
        def make_adder(x: int):
            def adder(y: int) -> int:
                return x + y
            return adder

        add_10 = make_adder(10)
        self.assertEqual(add_10(5), 15)
        self.assertIsNotNone(add_10.__closure__)
        if add_10.__closure__:
            self.assertEqual(add_10.__closure__[0].cell_contents, 10)

    def test_decorator_wraps_metadata(self) -> None:
        """Verify @functools.wraps preserves __name__ and __doc__."""
        def simple_dec(f):
            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                return f(*args, **kwargs)
            return wrapper

        @simple_dec
        def my_calc(x: int) -> int:
            """Multiply x by 2."""
            return x * 2

        self.assertEqual(my_calc.__name__, "my_calc")
        self.assertEqual(my_calc.__doc__, "Multiply x by 2.")
        self.assertEqual(my_calc(5), 10)


if __name__ == "__main__":
    unittest.main()
