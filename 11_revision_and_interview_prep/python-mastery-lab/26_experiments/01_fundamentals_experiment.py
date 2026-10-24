"""
Experiment 01: Language Fundamentals, Evaluation Order & Precedence
===================================================================

Questions Investigated:
-----------------------
1. Does evaluation order (execution in time) follow operator precedence, or does it strictly evaluate left-to-right?
2. Does exponentiation (**) associate right-to-left as specified?
3. Do logical 'and' and 'or' return boolean values or the actual operand objects?

Instructions to Run:
--------------------
$ python3 26_experiments/01_fundamentals_experiment.py
"""

def banner(title: str) -> None:
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


def test_evaluation_order_vs_precedence() -> None:
    banner("1. EVALUATION ORDER VS OPERATOR PRECEDENCE")
    execution_trace = []

    def track(name: str, value: int) -> int:
        execution_trace.append(name)
        print(f"  [Evaluating Operand] {name} -> {value}")
        return value

    print("Evaluating expression: track('A', 10) + track('B', 20) * track('C', 5)\n")
    result = track("A", 10) + track("B", 20) * track("C", 5)

    print(f"\nFinal Result: {result}")
    print(f"Order operands were evaluated in time: {execution_trace}")
    assert execution_trace == ["A", "B", "C"], "Operands must evaluate left-to-right!"
    print("-> Confirmed: Operands evaluate strictly left-to-right in time.")


def test_exponentiation_associativity() -> None:
    banner("2. EXPONENTIATION ASSOCIATIVITY (RIGHT-TO-LEFT)")
    # If left-to-right: (2 ** 3) ** 2 = 8 ** 2 = 64
    # If right-to-left: 2 ** (3 ** 2) = 2 ** 9 = 512
    result = 2 ** 3 ** 2
    print(f"Calculation: 2 ** 3 ** 2 = {result}")
    assert result == 512, "2 ** 3 ** 2 must equal 512"
    print("-> Confirmed: Exponentiation associates from right to left.")


def test_short_circuit_object_returns() -> None:
    banner("3. SHORT-CIRCUIT EVALUATION RETURNS ACTUAL OBJECTS")
    
    # 'or' returns first truthy value
    obj1 = "" or "Default User"
    print(f"'' or 'Default User' => {obj1!r} (type: {type(obj1).__name__})")
    assert obj1 == "Default User"

    # 'and' returns first falsy value
    obj2 = 0 and [1, 2, 3]
    print(f"0 and [1, 2, 3]      => {obj2!r} (type: {type(obj2).__name__})")
    assert obj2 == 0

    # Chained guard preventing crash
    class User:
        def get_role(self) -> str:
            return "Admin"

    logged_in_user = None
    # If short-circuit works, logged_in_user.get_role() is NEVER called
    is_admin = (logged_in_user is not None) and (logged_in_user.get_role() == "Admin")
    print(f"Guard result with None user: {is_admin}")
    assert is_admin is False
    print("-> Confirmed: Short-circuiting protects against AttributeError.")


def main() -> None:
    test_evaluation_order_vs_precedence()
    test_exponentiation_associativity()
    test_short_circuit_object_returns()
    banner("ALL FUNDAMENTAL EXPERIMENTS VERIFIED SUCCESSFULLY")


if __name__ == "__main__":
    main()
