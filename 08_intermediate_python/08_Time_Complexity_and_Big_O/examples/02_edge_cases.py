"""
02_edge_cases.py
Demonstrates subtle complexity edge cases:
- Dynamic list over-allocation and amortized O(1) append vs resize jumps
- Space complexity comparison: recursive call stack vs iterative loop
"""

import sys

def demonstrate_list_amortized_growth():
    print("--- 1. List Memory Allocation & Amortized Growth Pattern ---")
    dynamic_list = []
    prev_size = sys.getsizeof(dynamic_list)
    print(f"Initial empty list size: {prev_size} bytes")

    # Track how CPython over-allocates internal pointer buffers
    resizes = []
    for i in range(50):
        dynamic_list.append(i)
        current_size = sys.getsizeof(dynamic_list)
        if current_size != prev_size:
            resizes.append((i, current_size))
            prev_size = current_size

    print("List capacity reallocation points (item index, new buffer bytes):")
    for idx, bytes_size in resizes[:8]:
        print(f"  Item #{idx:2d} triggered buffer resize -> {bytes_size} bytes")
    print("Conclusion: Most appends take O(1) time; rare buffer resizes amortize to O(1) overall.")


def demonstrate_space_complexity_recursion():
    print("\n--- 2. Space Complexity: Iteration O(1) vs Recursion O(n) ---")

    # Iterative Sum: O(n) time, O(1) auxiliary memory
    def sum_iterative(n):
        total = 0
        for i in range(1, n + 1):
            total += i
        return total

    # Recursive Sum: O(n) time, O(n) auxiliary call stack memory
    def sum_recursive(n):
        if n <= 1:
            return n
        return n + sum_recursive(n - 1)

    print(f"Iterative sum(100): {sum_iterative(100)} (Auxiliary Space: O(1))")
    print(f"Recursive sum(100): {sum_recursive(100)} (Auxiliary Space: O(100) stack frames)")


def main():
    demonstrate_list_amortized_growth()
    demonstrate_space_complexity_recursion()

if __name__ == "__main__":
    main()
