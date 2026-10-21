"""
05_advanced_idiomatic.py
Demonstrates production-grade implementations of core algorithms:
1. Merge Sort: O(n log n) stable divide-and-conquer
2. In-Place Quick Sort: Lomuto partitioning scheme
3. Dynamic Sliding Window: Longest Substring Without Repeating Characters
"""

# 1. Merge Sort: O(n log n) guaranteed time complexity
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    return _merge(left_sorted, right_sorted)

def _merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= guarantees stability
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# 2. In-Place Quick Sort with Lomuto Partitioning
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partition index
        p_idx = _partition(arr, low, high)
        quick_sort_inplace(arr, low, p_idx - 1)
        quick_sort_inplace(arr, p_idx + 1, high)
    return arr

def _partition(arr, low, high):
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1        # Pointer for smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 3. Dynamic Sliding Window: Longest Substring Without Repeating Characters
def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters in O(n) time.
    Uses hash map to store the most recent index of each character.
    """
    char_last_seen = {}
    max_length = 0
    window_start = 0

    for window_end, char in enumerate(s):
        if char in char_last_seen and char_last_seen[char] >= window_start:
            # Shift window_start past the previous occurrence
            window_start = char_last_seen[char] + 1

        char_last_seen[char] = window_end
        current_window_len = window_end - window_start + 1
        if current_window_len > max_length:
            max_length = current_window_len

    return max_length


def main():
    print("--- 1. Merge Sort ---")
    data1 = [38, 27, 43, 3, 9, 82, 10]
    sorted1 = merge_sort(data1)
    print(f"Original: {data1}")
    print(f"Merge Sorted: {sorted1}")

    print("\n--- 2. In-Place Quick Sort ---")
    data2 = [10, 80, 30, 90, 40, 50, 70]
    print(f"Original: {data2}")
    quick_sort_inplace(data2)
    print(f"Quick Sorted: {data2}")

    print("\n--- 3. Longest Substring Without Repeating Characters ---")
    test_strings = ["abcabcbb", "bbbbb", "pwwkew", ""]
    for test in test_strings:
        ans = length_of_longest_substring(test)
        print(f"String: '{test}' -> Longest non-repeating substring length: {ans}")

if __name__ == "__main__":
    main()
