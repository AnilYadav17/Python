"""
03_real_world_use_case.py
Real-world scenario: Optimizing duplicate detection across repository code.
Compares three historical implementations:
1. Brute-Force Nested Loops: O(n^2) time, O(1) space
2. Sort and Adjacent Check:   O(n log n) time, O(1) auxiliary space
3. Hash Set Tracking:        O(n) time, O(n) space
"""

import time
import random

# Implementation 1: O(n^2) Brute Force
def find_duplicates_brute_force(arr):
    n = len(arr)
    duplicates = []
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates


# Implementation 2: O(n log n) Sorting
def find_duplicates_sorted(arr):
    sorted_arr = sorted(arr)  # O(n log n)
    duplicates = []
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] == sorted_arr[i + 1]:
            if not duplicates or duplicates[-1] != sorted_arr[i]:
                duplicates.append(sorted_arr[i])
    return duplicates


# Implementation 3: O(n) Hash Set
def find_duplicates_hash_set(arr):
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


def benchmark(func, data):
    start = time.perf_counter()
    res = func(data)
    elapsed = (time.perf_counter() - start) * 1000
    return len(res), elapsed


def main():
    print("--- Benchmark: Duplicate Detection Algorithms ---")
    dataset_size = 6000
    # Generate random list with deliberate duplicates
    data = [random.randint(1, 4000) for _ in range(dataset_size)]

    count1, t1 = benchmark(find_duplicates_brute_force, data)
    count2, t2 = benchmark(find_duplicates_sorted, data)
    count3, t3 = benchmark(find_duplicates_hash_set, data)

    print(f"Input Size N = {dataset_size}")
    print(f"  1. Brute-Force O(n^2):     {t1:>8.2f} ms")
    print(f"  2. Sorted O(n log n):      {t2:>8.2f} ms")
    print(f"  3. Hash Set O(n):          {t3:>8.2f} ms")
    print(f"  Speedup of Hash Set vs Brute-Force: {t1 / t3:>6.1f}x faster!")

if __name__ == "__main__":
    main()
