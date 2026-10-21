"""
05_advanced_idiomatic.py
Demonstrates advanced, idiomatic Python patterns:
1. Structural Pattern Matching (Python 3.10+ match-case) with guards
2. Extended sequence unpacking (*rest operator)
3. Dictionary view set operations (keys() and items() act as set-like views)
4. Assignment expressions (Walrus operator :=)
"""

def demonstrate_structural_pattern_matching(command):
    # Pattern matching unpacks sequences, validates structure, and binds variables
    match command:
        case ["quit" | "exit"]:
            return "Terminating application session."
        case ["get", str(key)]:
            return f"Retrieving value for cache key: '{key}'"
        case ["set", str(key), value] if len(str(value)) <= 100:
            return f"Storing key '{key}' with value '{value}' (length guard passed)"
        case ["set", str(key), _]:
            return f"Rejected: payload for key '{key}' exceeds maximum permitted length"
        case _:
            return f"Unknown command format: {command}"


def demonstrate_extended_unpacking():
    print("--- 1. Extended Sequence Unpacking ---")
    data = [10, 20, 30, 40, 50, 60]
    head, *middle, tail = data
    print(f"Original: {data}")
    print(f"head: {head}, middle: {middle}, tail: {tail}")


def demonstrate_dict_view_set_operations():
    print("\n--- 2. Dictionary Views & Set Operations ---")
    # dict.keys() and dict.items() support mathematical set operations!
    user_roles = {"alice": "admin", "bob": "editor", "charlie": "viewer"}
    superusers = {"alice": "admin", "david": "superadmin"}

    # Common keys across both dictionaries
    common_users = user_roles.keys() & superusers.keys()
    print(f"Common users (keys intersection): {common_users}")

    # Unique users in first dict but not second
    roles_only = user_roles.keys() - superusers.keys()
    print(f"Users only in first dict (difference): {roles_only}")


def demonstrate_walrus_operator():
    print("\n--- 3. Walrus Operator (:=) ---")
    # Walrus operator assigns and returns value in an expression
    raw_inputs = ["   alpha  ", " ", "beta\t", "", "   gamma "]

    # Clean, filter, and capture length in a single readable pass
    processed = [
        f"{cleaned} (len={n})"
        for item in raw_inputs
        if (cleaned := item.strip()) and (n := len(cleaned)) > 3
    ]
    print(f"Processed strings: {processed}")


def main():
    demonstrate_extended_unpacking()
    demonstrate_dict_view_set_operations()
    demonstrate_walrus_operator()

    print("\n--- 4. Structural Pattern Matching ---")
    commands = [
        ["get", "user:101"],
        ["set", "cache:banner", "Welcome back!"],
        ["set", "cache:blob", "X" * 150],
        ["quit"],
        ["unrecognized", 1, 2, 3]
    ]
    for cmd in commands:
        result = demonstrate_structural_pattern_matching(cmd)
        print(f"Command {cmd} -> {result}")

if __name__ == "__main__":
    main()
