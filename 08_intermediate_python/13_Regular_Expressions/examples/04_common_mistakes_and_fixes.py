"""
04_common_mistakes_and_fixes.py
Demonstrates common regex traps and their fixes:
1. Capturing group in re.split retaining delimiters
2. ReDoS / Catastrophic Backtracking prevention
3. Case sensitivity pitfalls and re.IGNORECASE
"""

import re
import time

def mistake_1_split_capturing_group():
    print("--- 1. re.split() Capturing vs Non-Capturing Group Trap ---")
    text = "Item1, Item2; Item3"

    # MISTAKE: using capturing group ([,;]) keeps delimiters in output!
    buggy_split = re.split(r"([,;]\s*)", text)
    print(f"Buggy split with ():  {buggy_split}")

    # FIX: Use non-capturing group (?:[,;])
    clean_split = re.split(r"(?:[,;]\s*)", text)
    print(f"Fixed split with (?:): {clean_split}")


def mistake_2_catastrophic_backtracking_prevention():
    print("\n--- 2. Catastrophic Backtracking (ReDoS) Prevention ---")
    # VULNERABLE PATTERN: (a+)+$ on input "aaaaaaaaaaaaaaaaaaaaa!"
    # Nested quantifiers cause exponential branching on mismatch!

    # SAFE PATTERN: Use atomic or mutually exclusive character sets
    safe_pattern = re.compile(r"^a+!$")
    test_str = "a" * 25 + "!"

    start = time.perf_counter()
    m = safe_pattern.match(test_str)
    dur = (time.perf_counter() - start) * 1000
    print(f"Safe pattern evaluated in {dur:.4f} ms: Match = {bool(m)}")


def mistake_3_case_insensitivity():
    print("\n--- 3. Case Insensitivity: Flags ---")
    email = "USER@EXAMPLE.COM"
    # Using re.IGNORECASE (re.I)
    pattern = re.compile(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$", re.IGNORECASE)
    print(f"'{email}' matches with re.I: {bool(pattern.fullmatch(email))}")


def main():
    mistake_1_split_capturing_group()
    mistake_2_catastrophic_backtracking_prevention()
    mistake_3_case_insensitivity()

if __name__ == "__main__":
    main()
