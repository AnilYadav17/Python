"""
02_edge_cases.py
Demonstrates context manager edge cases:
- Exception suppression via returning True in __exit__
- Failure inside __enter__: proving __exit__ is NOT called
- Exception handling inside generator @contextmanager
"""

from contextlib import contextmanager

def demonstrate_exception_suppression():
    print("--- 1. Exception Suppression in __exit__ ---")

    class SuppressSpecificError:
        def __init__(self, *exceptions_to_swallow):
            self.swallow_types = exceptions_to_swallow

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None and issubclass(exc_type, self.swallow_types):
                print(f"  [__exit__] Successfully suppressed expected {exc_type.__name__}: {exc_val}")
                return True  # Returning True silences the exception!
            return False     # Propagate everything else

    # Case A: Swallowed exception
    with SuppressSpecificError(KeyError):
        print("  Inside block: triggering KeyError...")
        _ = {}["non_existent_key"]
    print("  Execution continued smoothly past suppressed KeyError!")

    # Case B: Unhandled exception propagates
    try:
        with SuppressSpecificError(KeyError):
            print("  Inside block: triggering ValueError...")
            raise ValueError("Fatal ValueError")
    except ValueError as err:
        print(f"  Outer try-except caught unsuppressed error: {err}")


def demonstrate_enter_failure_edge_case():
    print("\n--- 2. Failure Inside __enter__ Edge Case ---")

    class FragileAcquisition:
        def __enter__(self):
            print("  [__enter__] Attempting allocation...")
            raise ConnectionRefusedError("Port unavailable")

        def __exit__(self, exc_type, exc_val, exc_tb):
            # This will NEVER be executed if __enter__ fails!
            print("  [__exit__] Cleanup handler")
            return False

    try:
        with FragileAcquisition():
            print("  This line will never be reached.")
    except ConnectionRefusedError:
        print("  Caught ConnectionRefusedError. Notice __exit__ was NOT executed!")


def main():
    demonstrate_exception_suppression()
    demonstrate_enter_failure_edge_case()

if __name__ == "__main__":
    main()
