"""
Automated Tests for Module 02: Names, Objects, Aliasing & Memory
================================================================
Validates identity vs equality, mutability, aliasing, copying semantics,
and tuple mutation edge cases.
"""

import copy
import gc
import unittest


class TestNamesObjectsAndMemory(unittest.TestCase):
    def test_identity_vs_equality(self) -> None:
        """Verify identity ('is') checks memory address while '==' checks value."""
        list_a = [1, 2, 3]
        list_b = [1, 2, 3]
        list_c = list_a

        self.assertEqual(list_a, list_b)
        self.assertIsNot(list_a, list_b)

        self.assertEqual(list_a, list_c)
        self.assertIs(list_a, list_c)

    def test_small_integer_cache(self) -> None:
        """Verify CPython small integer singletons between -5 and 256."""
        a = 256
        b = 256
        self.assertIs(a, b)

        # Dynamic construction outside the cache
        c = int("1000")
        d = int("1000")
        self.assertEqual(c, d)
        self.assertIsNot(c, d)

    def test_shallow_vs_deepcopy(self) -> None:
        """Verify shallow copy shares nested objects while deepcopy isolates them."""
        nested = [["a", "b"], [1, 2]]
        shallow = nested.copy()
        deep = copy.deepcopy(nested)

        # Outer list is distinct for both
        self.assertIsNot(nested, shallow)
        self.assertIsNot(nested, deep)

        # Inner list is shared in shallow copy, isolated in deep copy
        self.assertIs(nested[0], shallow[0])
        self.assertIsNot(nested[0], deep[0])

        # Mutate inner list
        shallow[0].append("c")
        self.assertIn("c", nested[0])
        self.assertNotIn("c", deep[0])

    def test_tuple_mutation_edge_case(self) -> None:
        """Verify modifying a mutable list inside a tuple raises TypeError but modifies list."""
        t = (1, 2, [10, 20])
        with self.assertRaises(TypeError):
            t[2] += [30]

        # The list inside was modified in-place before the assignment failed
        self.assertEqual(t[2], [10, 20, 30])

    def test_cyclic_garbage_collection(self) -> None:
        """Verify that cyclic references are freed by the generational GC."""
        class Node:
            def __init__(self) -> None:
                self.cycle = None

        node1 = Node()
        node2 = Node()
        node1.cycle = node2
        node2.cycle = node1

        del node1
        del node2

        collected = gc.collect()
        self.assertGreaterEqual(collected, 2)


if __name__ == "__main__":
    unittest.main()
