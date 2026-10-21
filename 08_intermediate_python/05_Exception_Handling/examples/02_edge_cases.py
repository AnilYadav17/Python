"""
02_edge_cases.py
Demonstrates subtle exception edge cases:
- Return statement in finally block swallowing active exceptions
- Explicit exception chaining with 'raise ... from ...' (__cause__)
- Implicit exception chaining (__context__)
- Suppressing exception context using 'raise ... from None'
"""

def demonstrate_finally_swallow():
    print("--- 1. Finally Block Swallowing Exception Trap ---")

    def risky_func():
        try:
            raise ValueError("Critical validation failure!")
        finally:
            # ANTIPATTERN: return in finally silences the ValueError entirely!
            return "Returned from finally!"

    result = risky_func()
    print(f"Function result: '{result}' (Notice: ValueError was swallowed!)")


def demonstrate_explicit_chaining():
    print("\n--- 2. Explicit Exception Chaining (__cause__) ---")

    def parse_config(raw_text):
        try:
            return int(raw_text)
        except ValueError as original_exc:
            # Explicit chaining: sets __cause__
            raise RuntimeError("Failed to load application configuration") from original_exc

    try:
        parse_config("not-a-number")
    except RuntimeError as err:
        print(f"Caught high-level error: {err}")
        print(f"Direct root cause (__cause__): {err.__cause__}")


def demonstrate_suppressing_context():
    print("\n--- 3. Suppressing Exception Context (raise ... from None) ---")

    def lookup_user(user_id):
        raw_db = {"101": "Alice"}
        try:
            return raw_db[str(user_id)]
        except KeyError:
            # from None explicitly suppresses KeyError from user-facing traceback
            raise LookupError(f"User ID {user_id} not found") from None

    try:
        lookup_user(999)
    except LookupError as err:
        print(f"Caught clean error: {err}")
        print(f"Suppressed context (__suppress_context__): {err.__suppress_context__}")


def main():
    demonstrate_finally_swallow()
    demonstrate_explicit_chaining()
    demonstrate_suppressing_context()

if __name__ == "__main__":
    main()
