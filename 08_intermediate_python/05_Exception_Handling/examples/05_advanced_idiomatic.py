"""
05_advanced_idiomatic.py
Demonstrates modern exception architecture:
- Python 3.11+ ExceptionGroup and except* syntax
- Re-raising while enriching exceptions with add_note() (PEP 678)
"""

def demonstrate_pep_678_add_note():
    print("--- 1. Exception Notes (PEP 678: add_note) ---")
    try:
        try:
            raise ConnectionRefusedError("Failed to connect to 10.0.0.1:5432")
        except ConnectionRefusedError as err:
            # Attach contextual debug info to the exception without changing its type
            err.add_note("Context: Occurred while connecting to Primary Read Replica.")
            err.add_note("Timestamp: 2026-09-05T09:45:00 UTC")
            raise
    except ConnectionRefusedError as re_raised:
        print(f"Caught: {re_raised}")
        print("Attached Notes:")
        for note in re_raised.__notes__:
            print(f"  * {note}")


def demonstrate_exception_groups():
    print("\n--- 2. Exception Groups & except* (Python 3.11+) ---")
    # In concurrent tasks, multiple exceptions can occur simultaneously
    errors = [
        ValueError("Invalid port number: -1"),
        TypeError("Expected string, got int"),
        KeyError("Missing 'database_name' setting"),
        ValueError("Max connections must be > 0")
    ]
    eg = ExceptionGroup("Multiple configuration errors encountered", errors)

    # except* matches and handles subsets of exceptions from the group
    try:
        raise eg
    except* ValueError as eg_val:
        print(f"Handled {len(eg_val.exceptions)} ValueError(s):")
        for e in eg_val.exceptions:
            print(f"  - {e}")
    except* TypeError as eg_type:
        print(f"Handled {len(eg_type.exceptions)} TypeError(s):")
        for e in eg_type.exceptions:
            print(f"  - {e}")
    except* KeyError as eg_key:
        print(f"Handled {len(eg_key.exceptions)} KeyError(s):")
        for e in eg_key.exceptions:
            print(f"  - {e}")


def main():
    demonstrate_pep_678_add_note()
    demonstrate_exception_groups()

if __name__ == "__main__":
    main()
