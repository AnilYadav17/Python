"""
05_advanced_idiomatic.py
Demonstrates advanced zero-width assertions:
1. Positive and Negative Lookaround for Password Strength Verification
2. Positive Lookbehind for Currency Extraction without consuming currency symbol
"""

import re

# 1. Complex Password Policy via Zero-Width Lookaheads
# Requirements:
# - At least 8 characters
# - At least one digit (?=.*\d)
# - At least one lowercase letter (?=.*[a-z])
# - At least one uppercase letter (?=.*[A-Z])
# - At least one special symbol (?=.*[!@#$%^&*])
PASSWORD_POLICY = re.compile(
    r"""
    ^
    (?=.*[a-z])       # Must contain at least one lowercase letter
    (?=.*[A-Z])       # Must contain at least one uppercase letter
    (?=.*\d)          # Must contain at least one digit
    (?=.*[!@#$%^&*])  # Must contain at least one special symbol
    [A-Za-z\d!@#$%^&*]{8,} # Total length at least 8 characters
    $
    """,
    re.VERBOSE
)

def validate_password_strength(password: str) -> bool:
    return bool(PASSWORD_POLICY.fullmatch(password))


# 2. Extracting Currency Amounts using Positive Lookbehind & Lookahead
def extract_us_dollar_amounts(text: str):
    # (?<=\$): Lookbehind asserts string is preceded by '$' without capturing '$'
    # \d+(?:\.\d{2})?: Captures the numerical amount
    # (?=\s|[.,]|$): Lookahead asserts boundary
    pattern = r"(?<=\$)\d+(?:\.\d{2})?"
    return [float(amount) for amount in re.findall(pattern, text)]


def main():
    print("--- 1. Password Strength Validation (Lookahead Assertions) ---")
    passwords = [
        "weak",                 # Too short, no upper/digit/symbol
        "Password123",          # No special symbol
        "P@ssword",             # No digit
        "Str0ng!P@ssw0rd",      # Valid!
    ]
    for pwd in passwords:
        status = "STRONG" if validate_password_strength(pwd) else "WEAK/INVALID"
        print(f"Password '{pwd:<16}' -> {status}")

    print("\n--- 2. Currency Amount Extraction (Lookbehind Assertions) ---")
    receipt_text = "Items purchased: Laptop: $1299.99, Mouse: $45.50, Cable: $12. Total discount: $100."
    amounts = extract_us_dollar_amounts(receipt_text)
    print(f"Extracted Dollar Amounts (float values without '$'): {amounts}")
    print(f"Total Sum: ${sum(amounts):.2f}")

if __name__ == "__main__":
    main()
