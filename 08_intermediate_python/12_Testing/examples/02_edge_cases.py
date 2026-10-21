"""
02_edge_cases.py
Demonstrates testing edge cases:
- Floating-point assertions using assertAlmostEqual with precision/delta
- Context-manager based exception assertions capturing message metadata
- Testing boundary collections
"""

import unittest
import math

class TestNumericalEdgeCases(unittest.TestCase):
    def test_floating_point_imprecision(self):
        # Standard equality (self.assertEqual) on floats often fails: 0.1 + 0.2 != 0.3
        val = 0.1 + 0.2
        expected = 0.3

        # BAD: self.assertEqual(val, expected) -> AssertionError!

        # FIX: Use assertAlmostEqual with places or delta
        self.assertAlmostEqual(val, expected, places=7)
        self.assertAlmostEqual(val, expected, delta=1e-9)

    def test_exception_detail_inspection(self):
        def parse_port(port_str):
            port = int(port_str)
            if not (1 <= port <= 65535):
                raise ValueError(f"Port {port} out of range [1, 65535]")
            return port

        # Verify not only that ValueError is raised, but that the exact error message matches
        with self.assertRaises(ValueError) as err_ctx:
            parse_port("99999")

        self.assertIn("out of range", str(err_ctx.exception))
        self.assertIn("99999", str(err_ctx.exception))


def main():
    print("--- Executing Edge Case Assertions ---")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumericalEdgeCases)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    main()
