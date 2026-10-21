"""
04_common_mistakes_and_fixes.py
Demonstrates common typing mistakes and their fixes:
1. Mutable default argument trap inside typed functions
2. Conflating Optional[T] with argument defaults
3. Legacy typing.List vs modern list[]
"""

from typing import Optional

def mistake_1_mutable_default_with_types():
    print("--- 1. Mutable Default Trap with Type Hints ---")

    # BAD: Even with type hints, mutable defaults are shared across calls!
    # def bad_append(item: str, container: list[str] = []) -> list[str]: ...

    # FIX: Annotate container as list[str] | None = None
    def clean_append(item: str, container: list[str] | None = None) -> list[str]:
        if container is None:
            container = []
        container.append(item)
        return container

    res1 = clean_append("first")
    res2 = clean_append("second")
    print(f"Call 1: {res1}, Call 2: {res2} (Properly isolated!)")


def mistake_2_optional_vs_default():
    print("\n--- 2. Optional[T] vs Default Value ---")
    # 'name: str = "guest"' is NOT Optional[str]; it is a str with a default fallback.
    # 'name: str | None = None' is an Optional string that explicitly accepts None.

    def format_greeting(name: str | None = None) -> str:
        if name is None:
            return "Welcome, Anonymous Guest"
        return f"Welcome, {name}"

    print(format_greeting("Alice"))
    print(format_greeting(None))
    print(format_greeting())


def main():
    mistake_1_mutable_default_with_types()
    mistake_2_optional_vs_default()

if __name__ == "__main__":
    main()
