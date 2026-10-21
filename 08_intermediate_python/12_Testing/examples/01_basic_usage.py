"""
01_basic_usage.py
Demonstrates foundational unit testing using Python's standard library unittest:
- TestCase definition
- setUp() and tearDown() lifecycle hooks
- Standard assertions (assertEqual, assertTrue, assertFalse, assertIn, assertRaises)
"""

import unittest

# Production code to be tested
def format_user_display(first_name, last_name, title=None):
    if not first_name or not last_name:
        raise ValueError("Both first_name and last_name are required.")
    full_name = f"{first_name.strip()} {last_name.strip()}"
    return f"{title.strip()} {full_name}" if title else full_name


class TestUserDisplayFormatting(unittest.TestCase):
    def setUp(self):
        # Runs BEFORE every test method
        self.default_title = "Dr."

    def tearDown(self):
        # Runs AFTER every test method (cleanup)
        pass

    def test_standard_full_name(self):
        result = format_user_display("Alice", "Smith")
        self.assertEqual(result, "Alice Smith")

    def test_name_with_title(self):
        result = format_user_display("Bruce", "Banner", title=self.default_title)
        self.assertEqual(result, "Dr. Bruce Banner")

    def test_whitespace_trimming(self):
        result = format_user_display("  Clark  ", "  Kent  ")
        self.assertEqual(result, "Clark Kent")

    def test_missing_first_name_raises_value_error(self):
        # Verifying exception is raised
        with self.assertRaises(ValueError) as ctx:
            format_user_display("", "Wayne")
        self.assertIn("required", str(ctx.exception))


def main():
    print("--- Executing unittest Test Suite ---")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUserDisplayFormatting)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print(f"\nTests run: {result.testsRun}, Errors: {len(result.errors)}, Failures: {len(result.failures)}")

if __name__ == "__main__":
    main()
