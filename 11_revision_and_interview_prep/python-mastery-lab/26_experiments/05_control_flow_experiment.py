"""
Experiment 05: Control Flow, Structural Pattern Matching & Loop Traps
=====================================================================

Questions Investigated:
-----------------------
1. How does Python 3.10+ match/case unpack sequences and apply pattern guards?
2. When exactly does a loop's else: clause execute?
3. What is the physical mechanism causing list.remove() to skip items during iteration?
4. How do list, dict, and set comprehensions evaluate?

Instructions to Run:
--------------------
$ python3 26_experiments/05_control_flow_experiment.py
"""

def banner(title: str) -> None:
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


def test_structural_pattern_matching() -> None:
    banner("1. STRUCTURAL PATTERN MATCHING (PEP 634)")

    def parse_event(event: list) -> str:
        match event:
            case ["LOGIN", username]:
                return f"User '{username}' logged in"
            case ["PAYMENT", amount] if amount > 1000:
                return f"High-value payment alert: ${amount}"
            case ["PAYMENT", amount]:
                return f"Standard payment: ${amount}"
            case ["LOGOUT"]:
                return "User logged out"
            case _:
                return "Unknown event"

    res1 = parse_event(["LOGIN", "Anil"])
    res2 = parse_event(["PAYMENT", 5000])
    res3 = parse_event(["PAYMENT", 50])
    res4 = parse_event(["UNKNOWN", 123])

    print(f"Result 1: {res1}")
    print(f"Result 2: {res2}")
    print(f"Result 3: {res3}")
    print(f"Result 4: {res4}")

    assert res1 == "User 'Anil' logged in"
    assert res2 == "High-value payment alert: $5000"
    assert res3 == "Standard payment: $50"
    assert res4 == "Unknown event"
    print("-> Confirmed: Pattern matching unpacks variables and evaluates guards.")


def test_loop_else_mechanics() -> None:
    banner("2. LOOP ELSE CLAUSE EXECUTION")

    def find_divisor(target: int) -> bool:
        for d in range(2, target):
            if target % d == 0:
                return False  # Non-prime, divisor found
        else:
            return True  # Completed without break -> Prime!

    assert find_divisor(13) is True, "13 is prime, loop else should trigger"
    assert find_divisor(14) is False, "14 is composite, loop breaks early"
    print("-> Confirmed: Loop else: executes only when no break occurs.")


def test_mutation_during_iteration_trap() -> None:
    banner("3. MUTATING A LIST DURING ITERATION TRAP")
    buggy_list = [1, 2, 4, 5, 6]

    # Buggy loop
    for item in buggy_list:
        if item % 2 == 0:
            buggy_list.remove(item)

    print(f"Buggy list result after removing evens: {buggy_list}")
    # Item '4' was skipped because '2' was removed and items shifted left!
    assert 4 in buggy_list, "4 was erroneously skipped due to index shift!"

    # Correct loop using snapshot copy [:]
    fixed_list = [1, 2, 4, 5, 6]
    for item in fixed_list[:]:
        if item % 2 == 0:
            fixed_list.remove(item)

    print(f"Fixed list result using snapshot [:]:    {fixed_list}")
    assert fixed_list == [1, 5], "Fixed iteration must remove all evens"
    print("-> Confirmed: In-place removal during iteration skips items; slicing snapshot fixes it.")


def test_comprehensions() -> None:
    banner("4. COMPREHENSIONS (LIST, SET, DICT)")
    nums = [1, 2, 3, 4, 5]

    squares = [x * x for x in nums if x % 2 != 0]
    lengths = {len(w) for w in ["apple", "pear", "apple", "banana"]}
    mapping = {k: k.upper() for k in ["a", "b", "c"]}

    print(f"Odd squares:     {squares}")
    print(f"Unique lengths:  {lengths}")
    print(f"Mapping:         {mapping}")

    assert squares == [1, 9, 25]
    assert lengths == {4, 5, 6}
    assert mapping == {"a": "A", "b": "B", "c": "C"}
    print("-> Confirmed: Comprehensions correctly transform and filter collections.")


def main() -> None:
    test_structural_pattern_matching()
    test_loop_else_mechanics()
    test_mutation_during_iteration_trap()
    test_comprehensions()
    banner("ALL CONTROL FLOW EXPERIMENTS VERIFIED SUCCESSFULLY")


if __name__ == "__main__":
    main()
