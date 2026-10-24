"""
Experiment 06: Functions, Scope, Closures, Decorators & Default Traps
=====================================================================

Questions Investigated:
-----------------------
1. How does a mutable default argument persist state inside func.__defaults__?
2. How do positional-only (/) and keyword-only (*) parameters enforce caller syntax?
3. How does a closure store captured variables in __closure__ cell objects?
4. How does @functools.wraps protect function identity and docstrings?

Instructions to Run:
--------------------
$ python3 26_experiments/06_functions_experiment.py
"""

import functools


def banner(title: str) -> None:
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


def test_mutable_default_trap() -> None:
    banner("1. MUTABLE DEFAULT ARGUMENT TRAP & __defaults__")

    def buggy_append(item: str, storage: list = []) -> list:
        storage.append(item)
        return storage

    r1 = buggy_append("First")
    r2 = buggy_append("Second")

    print(f"Call 1: {r1}")
    print(f"Call 2: {r2}")
    print(f"Stored in buggy_append.__defaults__: {buggy_append.__defaults__}")

    assert r1 is r2, "Calls without argument share the exact same default list!"
    assert buggy_append.__defaults__[0] == ["First", "Second"], "Persistent state in __defaults__"
    print("-> Confirmed: Default parameters are instantiated once at def time.")


def test_positional_and_keyword_only() -> None:
    banner("2. POSITIONAL-ONLY (/) AND KEYWORD-ONLY (*) ENFORCEMENT")

    def strict_api(pos_val: int, /, standard_val: int, *, kw_val: int) -> int:
        return pos_val + standard_val + kw_val

    # Valid call
    result = strict_api(10, 20, kw_val=30)
    print(f"strict_api(10, 20, kw_val=30) = {result}")
    assert result == 60

    # Test positional-only violation
    pos_error = False
    try:
        strict_api(pos_val=10, standard_val=20, kw_val=30)
    except TypeError:
        pos_error = True
    assert pos_error, "Passing positional-only arg as keyword must raise TypeError"

    # Test keyword-only violation
    kw_error = False
    try:
        strict_api(10, 20, 30)  # kw_val passed positionally
    except TypeError:
        kw_error = True
    assert kw_error, "Passing keyword-only arg positionally must raise TypeError"
    print("-> Confirmed: / and * strictly enforce calling conventions.")


def test_closure_cell_inspection() -> None:
    banner("3. CLOSURE INSPECTION VIA __closure__")

    def make_counter(start: int = 0):
        count = start

        def increment() -> int:
            nonlocal count
            count += 1
            return count

        return increment

    counter = make_counter(100)
    print(f"Step 1: {counter()}")
    print(f"Step 2: {counter()}")

    assert counter.__closure__ is not None, "Closure must have __closure__ tuple"
    captured_value = counter.__closure__[0].cell_contents
    print(f"Captured value in cell: {captured_value}")
    assert captured_value == 102
    print("-> Confirmed: Closures preserve state in Cell objects.")


def test_decorator_wraps() -> None:
    banner("4. DECORATOR WITH @functools.wraps")

    def logger(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    @logger
    def original_function(a: int, b: int) -> int:
        """Official documentation for original function."""
        return a + b

    assert original_function.__name__ == "original_function", "Name must be preserved"
    assert original_function.__doc__ == "Official documentation for original function.", "Docstring preserved"
    assert original_function(3, 4) == 7
    print(f"Decorated name: {original_function.__name__}")
    print(f"Decorated doc:  {original_function.__doc__}")
    print("-> Confirmed: functools.wraps preserves function introspection attributes.")


def main() -> None:
    test_mutable_default_trap()
    test_positional_and_keyword_only()
    test_closure_cell_inspection()
    test_decorator_wraps()
    banner("ALL FUNCTION EXPERIMENTS VERIFIED SUCCESSFULLY")


if __name__ == "__main__":
    main()
