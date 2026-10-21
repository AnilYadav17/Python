# 07. DSA Fundamentals — Interview & Viva Questions

---

### Q1: Compare Merge Sort and Quick Sort in terms of time complexity, space complexity, and stability.
**Model Answer:**
- **Merge Sort**:
  - Time Complexity: Guaranteed $O(n \log n)$ across worst, average, and best cases.
  - Space Complexity: $O(n)$ auxiliary space required for merging subarrays.
  - Stability: **Stable** (preserves the original relative order of equal elements when using `<=`).
- **Quick Sort**:
  - Time Complexity: $O(n \log n)$ average, but degrades to $O(n^2)$ worst case if poor pivots are chosen (e.g. already sorted array with end pivot).
  - Space Complexity: $O(\log n)$ auxiliary space for the recursive call stack (in-place data partitioning).
  - Stability: **Unstable** (in-place partitioning swaps distant elements across the pivot).

---

### Q2: Why is computing `mid = left + (right - left) // 2` preferred over `mid = (left + right) // 2`?
**Model Answer:**
- In statically typed languages like C, C++, and Java, integer variables have fixed-width bit allocations (e.g. 32-bit signed integers capped at $2^{31} - 1 = 2,147,483,647$).
- If `left` and `right` are large numbers, `left + right` will overflow into a negative integer, causing out-of-bounds array access.
- Computing `left + (right - left) // 2` mathematically calculates the identical midpoint while ensuring intermediate values never exceed `right`.
- Note: Although Python integers feature arbitrary precision and will not overflow, using `left + (right - left) // 2` is considered universal algorithmic best practice.

---

### Q3: What is the difference between `bisect.bisect_left` and `bisect.bisect_right` in Python?
**Model Answer:**
- Both functions perform binary search to locate insertion points for maintaining sorted order:
  - `bisect_left(arr, x)`: Returns the leftmost insertion index. If `x` already exists in `arr`, the index points to the **first occurrence** of `x`.
  - `bisect_right(arr, x)`: Returns the rightmost insertion index. If `x` already exists in `arr`, the index points **immediately after the last occurrence** of `x`.
- Difference utility: The total count of duplicate elements `x` in a sorted array is simply `bisect_right(arr, x) - bisect_left(arr, x)`.

---

### Q4: When should you use the Two-Pointer technique versus the Sliding Window technique?
**Model Answer:**
- **Two-Pointer Technique**: Typically used when searching for pairs, triplets, or reconciling two sequences. Pointers often start at opposite ends (`left = 0`, `right = n - 1`) and move toward each other based on monotonic comparisons (e.g. Two Sum on sorted array, container with most water).
- **Sliding Window Technique**: Used when the problem concerns **contiguous subarrays or substrings** (e.g. maximum sum subarray of size $K$, longest substring with unique characters). The window maintains a rolling state over an active contiguous segment bounded by `[start, end]`.

---

### Q5: Why is naive fixed-size sliding window using `sum(arr[i:i+k])` inefficient, and how is it optimized?
**Model Answer:**
- Calling `sum(arr[i:i+k])` slices the array and sums $k$ elements on every single iteration. For an array of size $n$, this requires $O(n \cdot k)$ operations, which degenerates to $O(n^2)$ when $k \approx n / 2$.
- **Optimization (Rolling Sum)**:
  1. Compute the sum of the first window of size $k$ once ($O(k)$).
  2. Slide the window by adding the incoming element (`arr[i]`) and subtracting the outgoing element (`arr[i - k]`).
  3. Updating the sum takes constant $O(1)$ time per step, reducing total runtime to optimal $O(n)$ linear time.

---

### Q6: What is Timsort, and why does Python use it for `list.sort()`?
**Model Answer:**
- Timsort is a hybrid, stable sorting algorithm derived from Merge Sort and Insertion Sort, created by Tim Peters in 2002 for Python.
- Real-world data is rarely completely random; it frequently contains pre-existing sorted subsequences ("runs").
- Timsort identifies natural ascending and strictly descending runs in the input, uses Insertion Sort to extend small runs to a minimum chunk size (`minrun`), and merges runs using an optimized Merge Sort with galloping mode.
- Performance: Guaranteed $O(n \log n)$ worst and average case, but achieves $O(n)$ linear time on already-sorted or partially-sorted data.

---

### Q7: How does Floyd's Tortoise and Hare algorithm detect cycles in $O(1)$ space?
**Model Answer:**
- Floyd's cycle detection uses two pointers moving through a sequence or linked structure at different speeds:
  - Slow pointer ("Tortoise") moves 1 step per tick.
  - Fast pointer ("Hare") moves 2 steps per tick.
- If there is no cycle, the fast pointer reaches the end ($O(n)$ time).
- If a cycle exists, both pointers will eventually enter the cycle. Because the relative distance between them decreases by 1 on every step within the cycle, the fast pointer is guaranteed to lap and meet the slow pointer without requiring a hash set, achieving $O(n)$ time and $O(1)$ auxiliary memory.
