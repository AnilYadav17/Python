"""
04_common_mistakes_and_fixes.py
Demonstrates common exception handling pitfalls and their clean fixes:
1. The bare 'except:' antipattern (swallowing KeyboardInterrupt)
2. TOCTOU (Time-of-Check to Time-of-Use) race condition: LBYL vs EAFP
3. Exception handler ordering mistake (catching base before subclass)
"""

import os
import tempfile

def mistake_1_bare_except():
    print("--- 1. The Bare 'except:' Antipattern ---")

    # BAD:
    # try:
    #     some_code()
    # except:   # Intercepts KeyboardInterrupt and SystemExit!
    #     pass

    # FIX: Catch 'Exception' to allow system-exiting signals to propagate
    try:
        num = int("abc")
    except Exception as err:
        print(f"Caught programming exception safely: {type(err).__name__}: {err}")


def mistake_2_lbyl_vs_eafp():
    print("\n--- 2. LBYL vs EAFP (Atomic Operations) ---")

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        temp_path = tmp.name

    # LBYL (Look Before You Leap):
    # if os.path.exists(temp_path):
    #     with open(temp_path) as f: ...
    # Bug: If another process removes the file between exists() and open(), it crashes!

    # EAFP (Easier to Ask for Forgiveness than Permission): Atomic & Pythonic
    try:
        with open(temp_path, "r") as f:
            content = f.read()
            print(f"EAFP successfully opened file (len={len(content)})")
    except FileNotFoundError:
        print(f"File {temp_path} disappeared!")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def mistake_3_handler_ordering():
    print("\n--- 3. Exception Handler Ordering ---")

    # LookupError is the parent class of both IndexError and KeyError
    # BAD ORDERING:
    # except LookupError: ...
    # except KeyError: ... # Never executed!

    # FIX: Put specific child exceptions BEFORE broad parent exceptions
    data = {"name": "Alice"}
    try:
        val = data["age"]
    except KeyError as exc:
        print(f"Caught specific KeyError first: '{exc.args[0]}'")
    except LookupError as exc:
        print(f"Fallback to generic LookupError: {exc}")


def main():
    mistake_1_bare_except()
    mistake_2_lbyl_vs_eafp()
    mistake_3_handler_ordering()

if __name__ == "__main__":
    main()
