"""
04_common_mistakes_and_fixes.py
Demonstrates common beginner-to-intermediate Python traps and their idiomatic fixes:
1. Modifying a collection while iterating over it
2. The nested list multiplier bug (shared reference row trap)
3. Modifying a dictionary during iteration
4. Using == (value equality) vs is (reference identity)
"""

def mistake_1_mutating_list_in_loop():
    print("--- Mistake 1: Mutating a List While Iterating Over It ---")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    # BAD: Removing elements shifts subsequent indices, causing elements to be skipped
    buggy_list = list(numbers)
    for item in buggy_list:
        if item % 2 == 0:
            buggy_list.remove(item)
    print(f"Buggy result (skipped 4 and 8!): {buggy_list}")

    # FIX: Use a list comprehension to filter without in-place index shifting
    fixed_list = [item for item in numbers if item % 2 != 0]
    print(f"Fixed result via comprehension: {fixed_list}")


def mistake_2_grid_multiplication():
    print("\n--- Mistake 2: The Nested List Multiplier Bug ---")
    # BAD: [ [0] * 3 ] * 3 replicates the outer list's inner list REFERENCE 3 times!
    buggy_grid = [[0] * 3] * 3
    buggy_grid[0][0] = 99  # Intended to modify only top-left cell
    print(f"Buggy grid (all rows modified!): {buggy_grid}")

    # FIX: Use a comprehension to create a fresh independent list for each row
    fixed_grid = [[0] * 3 for _ in range(3)]
    fixed_grid[0][0] = 99
    print(f"Fixed grid (only row 0 modified): {fixed_grid}")


def mistake_3_mutating_dict_in_loop():
    print("\n--- Mistake 3: Modifying a Dictionary During Iteration ---")
    scores = {"alice": 85, "bob": 42, "charlie": 90, "david": 55}

    # BAD: for k in scores: if scores[k] < 60: del scores[k]
    # Raises: RuntimeError: dictionary changed size during iteration

    # FIX 1: Iterate over a snapshot list of keys
    scores_copy = dict(scores)
    for student in list(scores_copy.keys()):
        if scores_copy[student] < 60:
            del scores_copy[student]
    print(f"Fixed via list(dict.keys()): {scores_copy}")

    # FIX 2: Create a new dictionary using dict comprehension
    filtered_scores = {k: v for k, v in scores.items() if v >= 60}
    print(f"Fixed via dict comprehension: {filtered_scores}")


def mistake_4_equality_vs_identity():
    print("\n--- Mistake 4: '==' (Value) vs 'is' (Identity) ---")
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]

    print(f"list_a == list_b: {list_a == list_b}")  # True: content values match
    print(f"list_a is list_b: {list_a is list_b}")  # False: separate memory allocations!

    # Correct use of 'is': comparing singletons like None
    val = None
    if val is None:  # Idiomatic Python (PEP 8)
        print("Idiomatic: 'val is None' used correctly for singleton check.")


def main():
    mistake_1_mutating_list_in_loop()
    mistake_2_grid_multiplication()
    mistake_3_mutating_dict_in_loop()
    mistake_4_equality_vs_identity()

if __name__ == "__main__":
    main()
