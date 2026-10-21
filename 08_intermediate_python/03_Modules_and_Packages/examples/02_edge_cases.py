"""
02_edge_cases.py
Demonstrates tricky module and library edge cases:
- Circular import explanation and safe resolution
- random (PRNG) vs secrets (CSPRNG) security differences
- Aware vs Naive datetime arithmetic TypeError
- Infinite iterator consumption trap and safe bounded slicing
"""

import sys
import random
import secrets
import datetime
import itertools

def demonstrate_secrets_vs_random():
    print("--- 1. random vs secrets Security Edge Case ---")
    # random.random() is deterministic (Mersenne Twister) - NOT safe for security tokens!
    random.seed(42)
    insecure_token_1 = random.randint(100000, 999999)
    random.seed(42)
    insecure_token_2 = random.randint(100000, 999999)
    print(f"Seeded random produces reproducible output: {insecure_token_1} == {insecure_token_2}")

    # secrets uses OS entropy (/dev/urandom) - cryptographically secure!
    secure_token = secrets.token_hex(16)
    secure_url_token = secrets.token_urlsafe(16)
    print(f"Cryptographically secure token: {secure_token}")
    print(f"Secure URL token: {secure_url_token}")


def demonstrate_datetime_timezone_traps():
    print("\n--- 2. Naive vs Aware Datetime Subtraction Trap ---")
    naive_dt = datetime.datetime.now()  # No tzinfo
    aware_dt = datetime.datetime.now(datetime.timezone.utc)  # Has tzinfo

    try:
        # Subtracting naive from aware raises TypeError
        diff = aware_dt - naive_dt
        print(diff)
    except TypeError as exc:
        print(f"Caught expected TypeError: {exc}")

    # FIX: Ensure both datetimes are timezone-aware in the same base (UTC)
    now_utc_1 = datetime.datetime.now(datetime.timezone.utc)
    now_utc_2 = datetime.datetime.now(datetime.timezone.utc)
    print(f"Aware difference works cleanly: {now_utc_2 - now_utc_1}")


def demonstrate_infinite_iterator_safety():
    print("\n--- 3. Infinite Iterator Trap & Safety Guard ---")
    # BAD: list(itertools.cycle([1, 2, 3])) would crash with OutOfMemoryError!

    # GOOD: Guard infinite generators using itertools.islice() or take while condition
    cycler = itertools.cycle(["RED", "YELLOW", "GREEN"])
    traffic_sequence = list(itertools.islice(cycler, 7))
    print(f"Safely bounded cycle sample (7 ticks): {traffic_sequence}")


def demonstrate_circular_import_theory():
    print("\n--- 4. Circular Import Mechanics ---")
    # Circular imports occur when module A imports B while B imports A at file top-level.
    # At load time, module A enters sys.modules before finishing execution.
    # When B attempts 'from A import symbol', 'symbol' does not yet exist in A's namespace.
    # Resolution:
    # 1. Refactor shared dependencies into a third neutral module C.
    # 2. Defer the import inside the specific function that uses it (local import).
    print("Circular import prevention strategy: keep shared symbols in separate leaf modules.")


def main():
    demonstrate_secrets_vs_random()
    demonstrate_datetime_timezone_traps()
    demonstrate_infinite_iterator_safety()
    demonstrate_circular_import_theory()

if __name__ == "__main__":
    main()
