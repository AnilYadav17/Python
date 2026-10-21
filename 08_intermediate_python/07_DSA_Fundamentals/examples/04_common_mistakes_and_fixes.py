"""
04_common_mistakes_and_fixes.py
Demonstrates common algorithmic pitfalls and their fixes:
1. The O(n * k) sliding window sum trap vs O(n) rolling window
2. Binary search off-by-one boundary mistake
3. Missing base case in recursion causing stack overflow
"""

import time

def mistake_1_sliding_window_sum_trap():
    print("--- 1. Sliding Window Performance: sum() vs Rolling Addition ---")
    size = 20_000
    k = 500
    data = [1] * size

    # BAD: Calling sum(data[i:i+k]) at each step costs O(k) per step -> O(n * k) total!
    start = time.perf_counter()
    max_sum_bad = 0
    for i in range(len(data) - k + 1):
        window_sum = sum(data[i:i+k])
        if window_sum > max_sum_bad:
            max_sum_bad = window_sum
    dur_bad = time.perf_counter() - start

    # FIX: Rolling sum: add incoming element, subtract outgoing element -> O(n) total!
    start = time.perf_counter()
    rolling_sum = sum(data[:k])
    max_sum_good = rolling_sum
    for i in range(k, len(data)):
        rolling_sum += data[i] - data[i - k]  # O(1) arithmetic update!
        if rolling_sum > max_sum_good:
            max_sum_good = rolling_sum
    dur_good = time.perf_counter() - start

    print(f"Window size k={k} across {size} elements:")
    print(f"  Naive sum() loop:  {dur_bad * 1000:>8.2f} ms")
    print(f"  Rolling sum loop:  {dur_good * 1000:>8.2f} ms")
    print(f"  Speedup factor:    {dur_bad / dur_good:>8.1f}x faster!")


def mistake_2_binary_search_bounds():
    print("\n--- 2. Binary Search Bound Pitfall ---")
    arr = [1, 3, 5, 7, 9]
    target = 9

    # Common bug: using while left < right without handling the last element
    # Fix: use while left <= right for standard exact match search
    left, right = 0, len(arr) - 1
    found_idx = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            found_idx = mid
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"Array: {arr}, Searched for {target}, Found at index: {found_idx}")


def main():
    mistake_1_sliding_window_sum_trap()
    mistake_2_binary_search_bounds()

if __name__ == "__main__":
    main()
