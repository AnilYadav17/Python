"""
05_advanced_idiomatic.py
Demonstrates advanced idiomatic testing techniques:
1. Data-driven Parameterized Testing with unittest subTest()
2. Complex mock side_effect sequences (transient failures followed by success)
"""

import unittest
from unittest.mock import MagicMock

def validate_credit_card(card_number: str) -> bool:
    """Luhn algorithm validation check."""
    cleaned = card_number.replace(" ", "").replace("-", "")
    if not cleaned.isdigit() or not (13 <= len(cleaned) <= 19):
        return False
    digits = [int(d) for d in cleaned]
    # Reverse digits and double every second digit
    checksum = 0
    reverse_digits = digits[::-1]
    for idx, d in enumerate(reverse_digits):
        if idx % 2 == 1:
            doubled = d * 2
            checksum += doubled - 9 if doubled > 9 else doubled
        else:
            checksum += d
    return checksum % 10 == 0


class TestAdvancedPatterns(unittest.TestCase):
    def test_parameterized_credit_card_validation(self):
        # Table of test cases: (input, expected_boolean, description)
        test_matrix = [
            ("4532-0151-1283-0366", True, "Valid 16-digit Visa Luhn number"),
            ("4532-0151-1283-0367", False, "Invalid checksum digit"),
            ("123", False, "Too short"),
            ("abcd-efgh-ijkl-mnop", False, "Non-numeric input"),
            ("", False, "Empty string"),
        ]

        # subTest generates distinct independent reporting sub-tests
        for card_no, expected, desc in test_matrix:
            with self.subTest(description=desc, card=card_no):
                actual = validate_credit_card(card_no)
                self.assertEqual(actual, expected, f"Failed on: {desc}")
        print("  [subTest] All 5 parameterized matrix cases evaluated independently.")

    def test_mock_transient_failure_then_success(self):
        # Simulating an API that fails twice with ConnectionError then succeeds
        mock_api = MagicMock()
        mock_api.side_effect = [
            ConnectionError("Attempt 1 failed"),
            ConnectionError("Attempt 2 failed"),
            {"status": "SUCCESS", "token": "tok_xyz987"}  # Attempt 3 succeeds
        ]

        def resilient_caller():
            retries = 3
            for _ in range(retries):
                try:
                    return mock_api()
                except ConnectionError:
                    continue
            raise RuntimeError("All retries failed")

        result = resilient_caller()
        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(mock_api.call_count, 3)
        print(f"  [side_effect] Simulated 2 transient failures followed by success (call_count={mock_api.call_count})")


def main():
    print("--- Executing Advanced Testing Patterns ---")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdvancedPatterns)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    assert len(result.failures) == 0 and len(result.errors) == 0

if __name__ == "__main__":
    main()
