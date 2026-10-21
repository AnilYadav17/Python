"""
02_edge_cases.py
Demonstrates tricky regex edge cases:
- Greedy vs Lazy quantifier matching (HTML tag trap)
- Python raw string notation r"..." vs double escaping
- Capturing groups altering re.findall() and re.split() return types
"""

import re

def demonstrate_greedy_vs_lazy():
    print("--- 1. Greedy vs Lazy Quantifier Trap ---")
    html = "<div><b>First Heading</b> and <b>Second Heading</b></div>"

    # GREEDY: <.*> matches from the FIRST '<' to the VERY LAST '>' on the line!
    greedy_matches = re.findall(r"<b>.*</b>", html)
    print(f"Greedy match (matches entire span!): {greedy_matches}")

    # LAZY: <.*?> stops at the earliest possible closing '>'
    lazy_matches = re.findall(r"<b>.*?</b>", html)
    print(f"Lazy match (matches individual tags): {lazy_matches}")


def demonstrate_raw_string_importance():
    print("\n--- 2. Raw String Notation r'...' Importance ---")
    # In a standard string, \b means ASCII Backspace (\x08)
    # In a raw string r"\b", it means regex word boundary
    standard_escape = "\\bcat\\b"  # Requires double escaping without r
    raw_escape = r"\bcat\b"        # Clean and readable

    text = "The category of cat is feline."
    print("Raw string regex matched:", re.findall(raw_escape, text))


def demonstrate_findall_group_tuples():
    print("\n--- 3. re.findall() with Capturing Groups ---")
    text = "John: 30, Alice: 25"

    # When capturing groups are present, findall returns TUPLES of groups!
    grouped = re.findall(r"(\w+):\s*(\d+)", text)
    print(f"findall with groups returns list of tuples: {grouped}")


def main():
    demonstrate_greedy_vs_lazy()
    demonstrate_raw_string_importance()
    demonstrate_findall_group_tuples()

if __name__ == "__main__":
    main()
