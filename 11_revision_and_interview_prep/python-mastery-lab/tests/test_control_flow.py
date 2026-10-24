"""
Automated Tests for Module 05: Control Flow & Pattern Matching
==============================================================
Tests match/case, loop else clauses, enumerate, zip,
and comprehension semantics.
"""

import unittest


class TestControlFlow(unittest.TestCase):
    def test_pattern_matching_guards(self) -> None:
        """Verify structural pattern matching with sequence unpacking and guards."""
        def evaluate_action(action: list) -> str:
            match action:
                case ["MOVE", x, y] if x < 0 or y < 0:
                    return "NEGATIVE_BOUNDS"
                case ["MOVE", x, y]:
                    return f"POS_{x}_{y}"
                case ["STOP"]:
                    return "HALT"
                case _:
                    return "UNKNOWN"

        self.assertEqual(evaluate_action(["MOVE", 10, 20]), "POS_10_20")
        self.assertEqual(evaluate_action(["MOVE", -1, 5]), "NEGATIVE_BOUNDS")
        self.assertEqual(evaluate_action(["STOP"]), "HALT")
        self.assertEqual(evaluate_action(["JUMP"]), "UNKNOWN")

    def test_loop_else_execution(self) -> None:
        """Verify loop else triggers only when break is not reached."""
        no_break_ran = False
        for i in range(3):
            if i == 99:
                break
        else:
            no_break_ran = True
        self.assertTrue(no_break_ran)

        break_ran_else = False
        for i in range(3):
            if i == 1:
                break
        else:
            break_ran_else = True
        self.assertFalse(break_ran_else)

    def test_enumerate_and_zip(self) -> None:
        """Verify enumerate indexing and zip pairs."""
        items = ["a", "b"]
        enum_list = list(enumerate(items, start=1))
        self.assertEqual(enum_list, [(1, "a"), (2, "b")])

        nums = [10, 20]
        zipped = list(zip(items, nums))
        self.assertEqual(zipped, [("a", 10), ("b", 20)])

    def test_comprehension_filtering(self) -> None:
        """Verify list, dict, and set comprehensions."""
        evens = [x for x in range(10) if x % 2 == 0]
        self.assertEqual(evens, [0, 2, 4, 6, 8])

        cube_map = {x: x**3 for x in range(1, 4)}
        self.assertEqual(cube_map, {1: 1, 2: 8, 3: 27})


if __name__ == "__main__":
    unittest.main()
