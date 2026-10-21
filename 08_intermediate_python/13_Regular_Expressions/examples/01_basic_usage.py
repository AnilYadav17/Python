"""
01_basic_usage.py
Demonstrates core regular expression functions in Python:
- re.search(), re.match(), and re.fullmatch()
- re.findall() and re.finditer()
- re.sub() for text replacement and redaction
- re.split() for multi-delimiter splitting
"""

import re

def demonstrate_search_and_match():
    print("--- 1. re.search vs re.match vs re.fullmatch ---")
    text = "Order ID: ORD-98765 placed on 2026-09-05"
    pattern = r"ORD-\d+"

    # re.match checks strictly at index 0 (returns None here!)
    m_match = re.match(pattern, text)
    print(f"re.match(r'ORD-\\d+', text): {m_match}")  # None

    # re.search scans the whole string for the first match
    m_search = re.search(pattern, text)
    print(f"re.search(r'ORD-\\d+', text): {m_search.group(0) if m_search else None}")

    # re.fullmatch checks if the entire string matches
    exact_pattern = r"Order ID: ORD-\d+ placed on \d{4}-\d{2}-\d{2}"
    m_full = re.fullmatch(exact_pattern, text)
    print(f"re.fullmatch(...): {'Match Confirmed' if m_full else 'No Match'}")


def demonstrate_findall_and_finditer():
    print("\n--- 2. re.findall vs re.finditer ---")
    log_line = "Error at 10.0.0.1:8080, retry at 10.0.0.2:8080, fallback 10.0.0.3:9000"
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+\b"

    # findall returns all matches as a flat list
    all_endpoints = re.findall(ip_pattern, log_line)
    print(f"findall endpoints: {all_endpoints}")

    # finditer yields Match objects lazily with span coordinates
    print("finditer matches with character spans:")
    for match_obj in re.finditer(ip_pattern, log_line):
        print(f"  Found '{match_obj.group(0)}' at span {match_obj.span()}")


def demonstrate_sub_and_split():
    print("\n--- 3. re.sub and re.split ---")
    # Redact sensitive credit card numbers (leave last 4 digits)
    card_text = "Card: 4532-8888-9999-1234, Exp: 12/28"
    redacted = re.sub(r"\d{4}-\d{4}-\d{4}-(\d{4})", r"XXXX-XXXX-XXXX-\1", card_text)
    print(f"Original: {card_text}")
    print(f"Redacted: {redacted}")

    # Splitting on multiple delimiters: comma, semicolon, or whitespace
    messy_csv = "apple, banana; cherry   date ,elderberry"
    tokens = [t for t in re.split(r"[,;\s]+", messy_csv) if t]
    print(f"Multi-delimiter split tokens: {tokens}")


def main():
    demonstrate_search_and_match()
    demonstrate_findall_and_finditer()
    demonstrate_sub_and_split()

if __name__ == "__main__":
    main()
