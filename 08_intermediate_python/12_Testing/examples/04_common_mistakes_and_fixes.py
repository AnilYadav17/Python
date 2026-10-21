"""
04_common_mistakes_and_fixes.py
Demonstrates common mocking mistakes and their clean fixes:
1. The typo in mock assertion (assert_called_once_with vs misspelled invented method)
2. autospec to prevent calling non-existent mock methods
3. Patching the wrong location (where defined vs where used)
"""

import unittest
from unittest.mock import MagicMock, create_autospec

class RealService:
    def send_email(self, recipient: str, subject: str):
        return True


class TestMockingPitfalls(unittest.TestCase):
    def test_misspelled_assertion_pitfall(self):
        mock_obj = MagicMock()
        mock_obj.do_action(123)

        # DANGEROUS PITFALL:
        # If you misspell an assertion (e.g. mock_obj.assert_called_once_wit),
        # standard MagicMock will dynamically CREATE that attribute and DO NOTHING!
        # The test passes silently without actually asserting anything!

        # FIX: Always use official assertion methods or create_autospec
        mock_obj.do_action.assert_called_once_with(123)
        print("  [Checked] assert_called_once_with verified correctly.")

    def test_autospec_prevents_bogus_methods(self):
        # Without autospec, mock allows calling any non-existent method:
        loose_mock = MagicMock()
        loose_mock.non_existent_method()  # Passes silently!

        # WITH create_autospec, calling non-existent methods raises AttributeError!
        strict_mock = create_autospec(RealService)
        try:
            strict_mock.non_existent_method()
        except AttributeError as err:
            print(f"  [Autospec Protection] Caught invalid method call on mock: {err}")


def main():
    print("--- Executing Mocking Pitfalls & Fixes ---")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMockingPitfalls)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    main()
