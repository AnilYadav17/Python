"""
01_basic_usage.py
Demonstrates fundamental searching and sorting algorithms:
- Linear Search
- Iterative & Recursive Binary Search
- Bubble Sort with early-termination optimization
- Palindrome validation using two-pointer
"""

# 1. Linear Search: O(n) time, O(1) space
def linear_search(arr, target):
    """Returns index of target if present, else -1."""
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1


# 2. Binary Search (Iterative): O(log n) time, O(1) space
def binary_search_iterative(sorted_arr, target):
    left, right = 0, len(sorted_arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Overflow-safe midpoint
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# 3. Binary Search (Recursive): O(log n) time, O(log n) call stack space
def binary_search_recursive(sorted_arr, target, left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if sorted_arr[mid] == target:
        return mid
    elif sorted_arr[mid] < target:
        return binary_search_recursive(sorted_arr, target, mid + 1, right)
    else:
        return binary_search_recursive(sorted_arr, target, left, mid - 1)


# 4. Bubble Sort: O(n^2) worst/avg, O(n) best time, O(1) space
def bubble_sort(arr):
    """Sorts array in-place with early exit if already sorted."""
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Tuple swap
                swapped = True
        # If no swaps occurred, the array is already sorted
        if not swapped:
            break
    return arr


# 5. Two-Pointer: Valid Palindrome (ignoring non-alphanumeric & case)
def is_valid_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        # Advance pointers past non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def main():
    print("--- 1. Linear Search ---")
    data = [14, 5, 29, 3, 19, 8]
    print(f"Linear search for 19: index = {linear_search(data, 19)}")
    print(f"Linear search for 99: index = {linear_search(data, 99)}")

    print("\n--- 2. Binary Search (Iterative & Recursive) ---")
    sorted_data = [3, 5, 8, 14, 19, 29]
    print(f"Iterative Binary Search for 14: index = {binary_search_iterative(sorted_data, 14)}")
    print(f"Recursive Binary Search for 14: index = {binary_search_recursive(sorted_data, 14, 0, len(sorted_data)-1)}")

    print("\n--- 3. Bubble Sort ---")
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {unsorted}")
    bubble_sort(unsorted)
    print(f"Sorted:   {unsorted}")

    print("\n--- 4. Two-Pointer Palindrome Check ---")
    phrases = ["A man, a plan, a canal: Panama", "race a car", "Was it a car or a cat I saw?"]
    for phrase in phrases:
        print(f"'{phrase}' -> Is palindrome: {is_valid_palindrome(phrase)}")

if __name__ == "__main__":
    main()
