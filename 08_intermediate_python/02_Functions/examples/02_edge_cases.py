"""
02_edge_cases.py
Demonstrates tricky function edge cases:
- Mutable default argument trap and its persistent identity across calls
- Late-binding closures in loops (variable binding vs value binding)
- UnboundLocalError compile-time scoping determination
- Maximum recursion depth limit
"""

import sys

def demonstrate_mutable_default_trap():
    print("--- 1. Mutable Default Argument Trap ---")

    # BUGGY: default empty list evaluates ONCE at function definition time
    def append_buggy(item, container=[]):
        container.append(item)
        return container

    print("Call 1 (buggy):", append_buggy("apple"))
    print("Call 2 (buggy):", append_buggy("banana"))  # Contains ['apple', 'banana']!
    print("Internal defaults tuple:", append_buggy.__defaults__)

    # IDIOMATIC FIX: Use None sentinel value
    def append_fixed(item, container=None):
        if container is None:
            container = []
        container.append(item)
        return container

    print("Call 1 (fixed):", append_fixed("apple"))
    print("Call 2 (fixed):", append_fixed("banana"))  # Contains only ['banana']


def demonstrate_late_binding_closures():
    print("\n--- 2. Late-Binding Closure Trap ---")

    # BUGGY: Lambdas capture the variable 'i' by reference, not by value
    buggy_callbacks = [lambda: i * 10 for i in range(4)]
    print("Buggy callback results:", [cb() for cb in buggy_callbacks])  # All 30!

    # IDIOMATIC FIX: Bind default argument at creation time
    fixed_callbacks = [lambda i=i: i * 10 for i in range(4)]
    print("Fixed callback results:", [cb() for cb in fixed_callbacks])  # [0, 10, 20, 30]


def demonstrate_unbound_local_error():
    print("\n--- 3. UnboundLocalError Mechanics ---")
    counter = 100

    def attempt_modify():
        try:
            # Although 'counter' exists in module global scope, the assignment below
            # marks 'counter' as local for the ENTIRE function at compile time.
            print("Counter:", counter)
            counter = 200
        except UnboundLocalError as err:
            print(f"Caught expected UnboundLocalError: {err}")

    attempt_modify()


def demonstrate_recursion_limit():
    print("\n--- 4. Recursion Depth Limit ---")
    current_limit = sys.getrecursionlimit()
    print(f"Current recursion limit: {current_limit}")

    def runaway_recursion(depth):
        try:
            return runaway_recursion(depth + 1)
        except RecursionError as err:
            print(f"Recursion exceeded safe frame depth at step {depth}: {err}")
            return depth

    runaway_recursion(1)


def main():
    demonstrate_mutable_default_trap()
    demonstrate_late_binding_closures()
    demonstrate_unbound_local_error()
    demonstrate_recursion_limit()

if __name__ == "__main__":
    main()
