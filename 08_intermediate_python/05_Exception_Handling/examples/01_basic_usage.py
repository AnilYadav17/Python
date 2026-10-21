"""
01_basic_usage.py
Demonstrates fundamental exception control flow:
- try, except, else, and finally execution blocks
- Handling multiple distinct exception types in a tuple
- Accessing exception arguments and type metadata
"""

def safe_divide_and_lookup(data_dict, key, divisor):
    """
    Attempts to retrieve a number from data_dict by key and divide it by divisor.
    Demonstrates try / except / else / finally flow.
    """
    result = None
    print(f"\n[Executing] key='{key}', divisor={divisor}")

    try:
        # Code that might raise KeyError, TypeError, or ZeroDivisionError
        value = data_dict[key]
        result = value / divisor

    except KeyError as exc:
        print(f"  [EXCEPT] Missing key error: '{exc.args[0]}'")

    except ZeroDivisionError as exc:
        print(f"  [EXCEPT] Math error: Cannot divide by zero ({exc})")

    except TypeError as exc:
        print(f"  [EXCEPT] Type mismatch error: {exc}")

    else:
        # Runs ONLY if the try block completed with no exceptions
        print(f"  [ELSE] Calculation succeeded cleanly! Result = {result:.2f}")

    finally:
        # Runs UNCONDITIONALLY under all scenarios (cleanup)
        print("  [FINALLY] Cleanup hook executed.")

    return result


def main():
    sample_data = {"score": 100, "name": "Python", "zero": 0}

    # Scenario 1: Clean success -> executes try, else, finally
    safe_divide_and_lookup(sample_data, "score", 4)

    # Scenario 2: ZeroDivisionError -> executes try, except ZeroDivisionError, finally
    safe_divide_and_lookup(sample_data, "score", 0)

    # Scenario 3: KeyError -> executes try, except KeyError, finally
    safe_divide_and_lookup(sample_data, "missing_field", 2)

    # Scenario 4: TypeError -> executes try, except TypeError, finally
    safe_divide_and_lookup(sample_data, "name", 2)

if __name__ == "__main__":
    main()
