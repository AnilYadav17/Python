"""
02_edge_cases.py
Demonstrates algorithmic edge cases:
- Binary Search on duplicates: bisect_left vs bisect_right
- Empty array, single-element, and two-element edge cases
- Quicksort recursion depth on already-sorted arrays
"""

import bisect

def demonstrate_bisect_duplicates():
    print("--- 1. Binary Search on Duplicates (bisect_left vs bisect_right) ---")
    # Array with multiple duplicate targets
    arr = [1, 2, 4, 4, 4, 4, 7, 9]
    target = 4

    # bisect_left: returns leftmost insertion index (first occurrence)
    left_idx = bisect.bisect_left(arr, target)

    # bisect_right: returns rightmost insertion index (index immediately after last occurrence)
    right_idx = bisect.bisect_right(arr, target)

    print(f"Array: {arr}, Target: {target}")
    print(f"bisect_left  (first occurrence): index {left_idx}")
    print(f"bisect_right (after last occurrence): index {right_idx}")
    print(f"Total occurrences of {target}: {right_idx - left_idx}")


def demonstrate_empty_and_single_element():
    print("\n--- 2. Empty & Single-Element Edge Cases ---")

    def safe_find_max(nums):
        if not nums:
            return None  # Edge case: empty list
        if len(nums) == 1:
            return nums[0]  # Edge case: single element
        current_max = nums[0]
        for n in nums[1:]:
            if n > current_max:
                current_max = n
        return current_max

    print(f"Empty list max: {safe_find_max([])}")
    print(f"Single item max: {safe_find_max([42])}")
    print(f"Multiple items max: {safe_find_max([3, 7, 2, 9, 5])}")


def demonstrate_two_sum_sorted_edge_case():
    print("\n--- 3. Two-Sum on Sorted Array (Exact Bounds) ---")
    # Edge case: two elements summing to target
    numbers = [2, 7]
    target = 9

    def two_sum_sorted(nums, tgt):
        l, r = 0, len(nums) - 1
        while l < r:
            curr = nums[l] + nums[r]
            if curr == tgt:
                return (l, r)
            elif curr < tgt:
                l += 1
            else:
                r -= 1
        return None

    print(f"Two-sum of [2, 7] for target 9: {two_sum_sorted(numbers, target)}")
    print(f"Two-sum of [2, 7] for target 10: {two_sum_sorted(numbers, 10)}")


def main():
    demonstrate_bisect_duplicates()
    demonstrate_empty_and_single_element()
    demonstrate_two_sum_sorted_edge_case()

if __name__ == "__main__":
    main()
