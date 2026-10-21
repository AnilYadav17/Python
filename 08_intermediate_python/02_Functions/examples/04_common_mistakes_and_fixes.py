"""
04_common_mistakes_and_fixes.py
Demonstrates common function mistakes and their clean fixes:
1. Missing nonlocal when creating stateful closures
2. Exponential naive recursion vs memoized recursion
3. Unintended global state mutations
"""

import functools
import time

def mistake_1_closure_state():
    print("--- 1. Enclosing Scope Mutation (nonlocal) ---")

    # BUGGY:
    # def make_counter_buggy():
    #     count = 0
    #     def increment():
    #         count += 1  # UnboundLocalError! (count flagged as local due to +=)
    #         return count
    #     return increment

    # FIXED: Declare 'nonlocal' to bind to nearest enclosing non-global scope
    def make_counter_fixed():
        count = 0
        def increment():
            nonlocal count  # Tells Python 'count' belongs to outer enclosing function
            count += 1
            return count
        return increment

    counter = make_counter_fixed()
    print("Counter call 1:", counter())
    print("Counter call 2:", counter())
    print("Counter call 3:", counter())


def mistake_2_naive_recursion_vs_memoization():
    print("\n--- 2. Naive Recursion vs Memoization ---")

    # Naive recursive Fibonacci: O(2^n) time complexity
    call_count_naive = 0
    def fib_naive(n):
        nonlocal call_count_naive
        call_count_naive += 1
        if n <= 1:
            return n
        return fib_naive(n - 1) + fib_naive(n - 2)

    # Memoized Fibonacci using functools.lru_cache: O(n) time complexity
    @functools.lru_cache(maxsize=128)
    def fib_memoized(n):
        if n <= 1:
            return n
        return fib_memoized(n - 1) + fib_memoized(n - 2)

    target_n = 20

    # Test Naive
    start = time.perf_counter()
    ans_naive = fib_naive(target_n)
    dur_naive = time.perf_counter() - start

    # Test Memoized
    start = time.perf_counter()
    ans_memo = fib_memoized(target_n)
    dur_memo = time.perf_counter() - start

    print(f"Naive Fib({target_n}) = {ans_naive}, Function calls: {call_count_naive}, Time: {dur_naive * 1000:.3f}ms")
    print(f"Memoized Fib({target_n}) = {ans_memo}, Time: {dur_memo * 1000:.3f}ms")
    print(f"Cache Stats: {fib_memoized.cache_info()}")


def mistake_3_global_leakage():
    print("\n--- 3. Eliminating Global State Mutations ---")
    # Instead of relying on global configuration variables that can be modified concurrently,
    # pass configuration explicitly or use closure encapsulation.
    def build_tax_calculator(rate):
        def calculate(amount):
            return round(amount * rate, 2)
        return calculate

    calc_standard = build_tax_calculator(0.08)
    calc_reduced = build_tax_calculator(0.05)

    print("Standard tax on $100:", calc_standard(100))
    print("Reduced tax on $100:", calc_reduced(100))


def main():
    mistake_1_closure_state()
    mistake_2_naive_recursion_vs_memoization()
    mistake_3_global_leakage()

if __name__ == "__main__":
    main()
