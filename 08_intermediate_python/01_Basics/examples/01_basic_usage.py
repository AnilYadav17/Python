"""
01_basic_usage.py
Demonstrates fundamental syntax: variables, primitives, operators,
control structures, collections, and comprehensions in Python.
"""

def main():
    # 1. Variables & Types
    user_name = "Alice"              # str: immutable sequence of characters
    user_age = 28                    # int: arbitrary precision integer
    account_balance = 1250.75        # float: IEEE 754 64-bit float
    is_active = True                 # bool: boolean subclass of int
    metadata = None                  # NoneType: absence of value

    # 2. String Formatting (F-Strings)
    # Using format specifiers: .2f formats float to 2 decimal places
    summary = f"User: {user_name}, Age: {user_age}, Balance: ${account_balance:.2f}, Active: {is_active}"
    print(f"--- 1. String Formatting ---\n{summary}")

    # 3. Operators & Conditionals
    # Arithmetic, membership (in), and ternary expression
    tax_rate = 0.15 if account_balance > 1000.0 else 0.05
    effective_tax = account_balance * tax_rate
    print(f"\n--- 2. Operators & Ternary ---\nTax Rate: {tax_rate * 100}%, Effective Tax: ${effective_tax:.2f}")

    # 4. Collections: List, Tuple, Set, Dictionary
    # List: mutable, ordered sequence
    tags = ["python", "developer", "backend"]
    tags.append("database")          # in-place append O(1) amortized

    # Tuple: immutable, ordered sequence
    coordinates = (37.7749, -122.4194)  # San Francisco (lat, long)

    # Set: unordered collection of unique, hashable items
    unique_roles = {"admin", "editor", "viewer", "editor"}  # 'editor' duplicate eliminated

    # Dict: key-value mapping preserving insertion order
    profile = {
        "id": 101,
        "name": user_name,
        "roles": unique_roles,
        "coords": coordinates
    }
    print(f"\n--- 3. Collections ---\nProfile Dict: {profile}")
    print(f"Unique roles count: {len(unique_roles)}")

    # 5. Loops and Comprehensions
    # List comprehension: square even numbers
    raw_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_squares = [n ** 2 for n in raw_numbers if n % 2 == 0]

    # Dict comprehension: mapping numbers to their cubes
    cube_map = {n: n ** 3 for n in raw_numbers[:5]}

    # Set comprehension: extract word lengths
    word_lengths = {len(tag) for tag in tags}

    print(f"\n--- 4. Comprehensions ---\nEven squares: {even_squares}")
    print(f"Cube map: {cube_map}")
    print(f"Unique tag lengths: {word_lengths}")

    # 6. Loop else construct: executes only if loop did not break
    target = 7
    for num in raw_numbers:
        if num == target:
            print(f"\n--- 5. Loop Else ---\nFound target {target} in list!")
            break
    else:
        print("Target was not found in the list.")

if __name__ == "__main__":
    main()
