# 💻 10_Coding_Challenges: Algorithmic Problem Solving & LeetCode

## Overview
Problem-solving is the bridge between syntax familiarity and engineering proficiency. This directory is dedicated to **data structures and algorithms (DSA)** practice, featuring real LeetCode and competitive programming problem solutions implemented in Python.

The solutions focus on space/time complexity optimization, boundary edge-case handling, and algorithmic patterns such as:
* **Two Pointers:** Converging from ends (`125. Valid Palindrome`, `15. 3Sum`) or fast/slow pointers.
* **Sliding Window:** Subarray sum and substring frequency tracking.
* **Prefix Sums:** Fast range sum queries (`560. Subarray Sum Equals K`).
* **Hash Map Lookups:** $O(1)$ complement lookups (`217. Contains Duplicate`, `49. Group Anagrams`).
* **Sorting & Intervals:** In-place color sorting (`75. Sort Colors`) and interval merging (`56. Merge Intervals`).

---

## Learning Objectives
By studying this module, you will understand:
1. Translating English problem descriptions into programmatic constraints and algorithmic logic.
2. Identifying optimal time complexity ($O(n \log n)$ vs $O(n)$) before writing code.
3. Managing edge cases: empty inputs, single-element arrays, duplicates, negative numbers, integer overflows.
4. Writing clean, idiomatic Python solutions using standard library tools (`collections.defaultdict`, `collections.Counter`).

---

## Prerequisites
* **[02_python_fundamentals](../02_python_fundamentals/)** (Loops, slicing, conditionals)
* **[03_python_collections](../03_python_collections/)** (Lists, dictionaries, sets)

---

## Repository Contents & Problem Index

### 📁 [leetcode/Array](./leetcode/Array) (30 Problems)

| Problem # | LeetCode Title / Topic | File | Time Complexity |
|:---:|:---|:---|:---:|
| 15 | **3Sum** | `15.py` | $O(n^2)$ |
| 16 | **3Sum Closest** | `16.py` | $O(n^2)$ |
| 33 | **Search in Rotated Sorted Array** | `33.py` | $O(\log n)$ |
| 34 | **Find First and Last Position of Element** | `34.py` | $O(\log n)$ |
| 53 | **Maximum Subarray (Kadane's Algorithm)** | `53.py` | $O(n)$ |
| 56 | **Merge Intervals** | `56.py` | $O(n \log n)$ |
| 75 | **Sort Colors (Dutch National Flag Algorithm)** | `75.py` | $O(n)$ |
| 88 | **Merge Sorted Array** | `88.py` | $O(m + n)$ |
| 128 | **Longest Consecutive Sequence** | `128.py` | $O(n)$ |
| 209 | **Minimum Size Subarray Sum** | `209.py` | $O(n)$ |
| 215 | **Kth Largest Element in an Array** | `215.py` | $O(n \log k)$ |
| 217 | **Contains Duplicate** | `217.py` | $O(n)$ |
| 219 | **Contains Duplicate II (Sliding Window)** | `219.py` | $O(n)$ |
| 238 | **Product of Array Except Self** | `238.py` | $O(n)$ |
| 268 | **Missing Number** | `268.py` | $O(n)$ |
| 283 | **Move Zeroes** | `283.py` | $O(n)$ |
| 300 | **Longest Increasing Subsequence** | `300.py` | $O(n \log n)$ |
| 448 | **Find All Numbers Disappeared in an Array** | `448.py` | $O(n)$ |
| 560 | **Subarray Sum Equals K (Prefix Sum)** | `560.py` | $O(n)$ |
| 581 | **Shortest Unsorted Continuous Subarray** | `581.py` | $O(n)$ |
| 977 | **Squares of a Sorted Array** | `977.py` | $O(n)$ |
| 1588 | **Sum of All Odd Length Subarrays** | `1588.py` | $O(n)$ |
| 2144 | **Minimum Cost of Buying Candies With Discount** | `2144.py` | $O(n \log n)$ |
| Misc | **Third Maximum Number** | `third_maximum_number.py` | $O(n)$ |
| Misc | **Last Repeating Character** | `last_repeating_char.py` | $O(n)$ |

### 📁 [leetcode/Strings](./leetcode/Strings) (11 Problems)

| Problem # | LeetCode Title / Topic | File | Time Complexity |
|:---:|:---|:---|:---:|
| 28 | **Find the Index of the First Occurrence in a String** | `28.py` | $O(n)$ |
| 49 | **Group Anagrams** | `49.py` | $O(n \cdot k \log k)$ |
| 58 | **Length of Last Word** | `58.py` | $O(n)$ |
| 125 | **Valid Palindrome** | `125.py` | $O(n)$ |
| 242 | **Valid Anagram** | `242.py` | $O(n)$ |
| 344 | **Reverse String (In-Place)** | `344.py` | $O(n)$ |
| 520 | **Detect Capital** | `520.py` | $O(n)$ |
| 557 | **Reverse Words in a String III** | `557.py` | $O(n)$ |
| 590 | **N-ary Tree Postorder Traversal** | `590.py` | $O(n)$ |
| Misc | **Longest Common Substring** | `longest_common_substring.py` | $O(n \cdot m)$ |

---

## How to Run & Test Solutions

```bash
# Test LeetCode 125 (Valid Palindrome):
python3 10_coding_challenges/leetcode/Strings/125.py

# Test LeetCode 53 (Maximum Subarray):
python3 10_coding_challenges/leetcode/Array/53.py

# Test LeetCode 49 (Group Anagrams):
python3 10_coding_challenges/leetcode/Strings/49.py
```

---

## Common Algorithmic Mistakes

1. **Brute Force Quadratic Time ($O(n^2)$) on Large Constraints:**
   * Using nested loops for search operations on $n = 10^5$ leads to `Time Limit Exceeded` (TLE). Use Hash Sets or Binary Search ($O(n)$ or $O(n \log n)$).
2. **Unnecessary Space Allocations:**
   * In-place problems (like `283. Move Zeroes` or `344. Reverse String`) require $O(1)$ auxiliary memory. Creating a brand new list fails in-place requirements.
3. **Ignoring Index Bounds When Comparing Neighbors:**
   * Checking `nums[i] == nums[i+1]` without verifying `i + 1 < len(nums)` raises `IndexError`.
4. **Modifying Lists During Iteration:**
   * Calling `.pop()` or `.remove()` inside a standard index loop skips subsequent elements.

---

## Next Step

👉 Revise all core concepts before interviews with **[11_revision_and_interview_prep](../11_revision_and_interview_prep/)**!
