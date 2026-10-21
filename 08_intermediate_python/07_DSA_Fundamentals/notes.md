# 07. Data Structures & Algorithms Fundamentals: Complete Reference

---

## 1. Array & String Fundamentals

### What it is
- **Array (Python List)**: An ordered sequence of elements stored contiguously in memory as pointers, providing $O(1)$ random access by index.
- **String**: An immutable sequence of Unicode characters. Modifying a string creates a new string object in memory.
- Core operations: In-place reversal, rotation, prefix sum computation, frequency mapping, and palindrome validation.

### Why it matters
- Arrays and strings form the foundation of >70% of coding interview challenges and core algorithmic manipulation.
- Understanding in-place operations avoids redundant $O(n)$ memory allocations.

### How it works (internals, if relevant)
- Python lists store pointers (`PyObject*`) in a contiguous dynamic array.
- Prefix Sum: Precomputing cumulative sums array `prefix[i] = prefix[i-1] + arr[i]` allows answering range sum queries `sum(arr[L...R]) = prefix[R] - prefix[L-1]` in $O(1)$ time instead of $O(n)$.

### Common mistakes / gotchas
- String concatenation in a loop: `s += char` reallocates the entire string repeatedly ($O(n^2)$ total time). Use a list and `''.join(list)` for $O(n)$ linear time.
- Modifying array dimensions during two-pointer or index traversal.

### Connects to
- Two-Pointer Technique (subtopic 6 below) and Time Complexity (Topic 08).

---

## 2. Searching Algorithms: Linear Search vs Binary Search

### What it is
- **Linear Search**: Sequentially inspects every element from index 0 to $n-1$ until target is found or list ends.
  - Complexity: $O(n)$ time, $O(1)$ space. Works on unsorted data.
- **Binary Search**: Efficient search algorithm for **sorted collections** that repeatedly halves the search space.
  - Complexity: $O(\log n)$ time, $O(1)$ space.
  - Standard library module: `bisect` (`bisect.bisect_left`, `bisect.bisect_right`, `bisect.insort`).

### Why it matters
- Binary search turns intractable search problems into sub-millisecond lookups: searching 1,000,000,000 elements takes $\approx 30$ comparisons.
- Serves as the foundation for search-on-answer problems (e.g. finding minimum capacity to ship packages).

### How it works (internals, if relevant)
- Maintain `left = 0`, `right = len(arr) - 1`.
- Compute midpoint: `mid = left + (right - left) // 2` (prevents integer overflow in lower-level languages like C/Java).
- If `arr[mid] == target`, return `mid`.
- If `arr[mid] < target`, discard left half: `left = mid + 1`.
- If `arr[mid] > target`, discard right half: `right = mid - 1`.

### Common mistakes / gotchas
- Applying binary search on an **unsorted** array, yielding wrong results.
- Off-by-one errors in loop condition (`while left < right` vs `while left <= right`). For standard search, `left <= right` ensures the single remaining element at `left == right` is checked.
- Infinite loops caused by updating `left = mid` instead of `left = mid + 1`.

### Connects to
- Time Complexity & Big-O (Topic 08).

---

## 3. Sorting Algorithms: Bubble Sort, Merge Sort, and Quick Sort

### What it is
- Algorithms that arrange elements of a collection into a monotonic order:
  - **Bubble Sort**: Simple comparison sort repeatedly swapping adjacent out-of-order elements.
    - Time: $O(n^2)$ worst/avg, $O(n)$ best (with early exit flag). Space: $O(1)$. Stable.
  - **Merge Sort**: Divide-and-conquer algorithm dividing the array in halves, recursively sorting each, and merging the two sorted halves.
    - Time: $O(n \log n)$ in all cases. Space: $O(n)$. Stable.
  - **Quick Sort**: Divide-and-conquer algorithm selecting a `pivot`, partitioning the array into elements $\le pivot$ and $> pivot$, and recursively sorting partitions.
    - Time: $O(n \log n)$ average, $O(n^2)$ worst (when pivot is poorly chosen, e.g. already sorted array with end pivot). Space: $O(\log n)$ call stack. Unstable.

### Why it matters
- Demonstrates essential algorithm design paradigms: divide-and-conquer, recursion, in-place partitioning, and stability.
- Python's built-in `.sort()` and `sorted()` use **Timsort** (hybrid of Merge Sort and Insertion Sort), running in $O(n \log n)$ worst case and $O(n)$ best case.

### How it works (internals, if relevant)
- **Merge Step**: Uses two pointers to compare the smallest remaining elements of each sorted subarray, appending the smaller into an auxiliary buffer.
- **Partition Step (Lomuto or Hoare)**: Scans array and swaps elements so that elements smaller than the pivot reside on its left, placing the pivot at its exact final sorted index.

### Common mistakes / gotchas
- Forgetting the early termination flag in Bubble Sort, forcing it to run in $O(n^2)$ even on already-sorted input.
- High memory usage in naive recursive Merge Sort by creating unnecessary array slices (`arr[:mid]`, `arr[mid:]`) at each recursive call.
- Picking the first or last element as pivot in Quick Sort without randomization, causing $O(n^2)$ degradation on sorted inputs.

### Connects to
- Time Complexity (Topic 08) and Data Structures from Scratch (Topic 16).

---

## 4. Basic Recursion Patterns

### What it is
- Algorithmic technique where a function calls itself to decompose a problem into identical sub-problems until reaching a trivial base condition.
- Core patterns:
  - Linear recursion: Factorial ($n! = n \times (n-1)!$), Array sum.
  - Tree recursion: Fibonacci ($F(n) = F(n-1) + F(n-2)$).
  - Combinatorial generation: Subsets, Permutations.

### Why it matters
- Natural mechanism for exploring combinatorial state spaces and tree/graph structures.
- Prerequisite for dynamic programming (memoized recursion).

### How it works (internals, if relevant)
- Each recursive call creates a frame on CPython's execution stack containing local variables and return address.
- Returning from the base case unwinds the call stack, passing values back up to preceding frames.

### Common mistakes / gotchas
- Missing or unreachable base cases, resulting in infinite recursion and `RecursionError`.
- Redundant sub-problem recomputation in tree recursion (e.g. naive Fibonacci running in $O(2^n)$) without caching (`@functools.lru_cache`).

### Connects to
- DSA from Scratch (Topic 16) for Binary Search Tree traversal.

---

## 5. Two-Pointer Technique

### What it is
- An algorithmic pattern using two integer indices (pointers) that traverse a sequence either:
  1. **Opposite Ends**: Pointers start at opposite ends (`left = 0`, `right = n - 1`) and move toward each other (e.g., Two Sum on sorted array, Container With Most Water, Valid Palindrome).
  2. **Same Direction (Fast & Slow)**: Pointers move at different speeds or conditions (e.g., Remove Duplicates from Sorted Array, Cycle detection).

### Why it matters
- Reduces brute-force $O(n^2)$ nested-loop algorithms to optimal $O(n)$ linear time with $O(1)$ auxiliary space.

### How it works (internals, if relevant)
- Exploits sorted order or monotonic properties: if the sum of elements at `left` and `right` is smaller than target, incrementing `left` is guaranteed to increase the sum, while decrementing `right` would decrease it.

### Common mistakes / gotchas
- Applying opposite-end two pointers to an unsorted array without sorting first.
- Pointer overlap condition: Using `left < right` vs `left <= right` depending on whether a single element can be paired with itself.
- Infinite loops caused by missing pointer increment/decrement operations inside loop branches.

### Connects to
- Sliding Window Technique (subtopic 6 below).

---

## 6. Sliding Window Technique

### What it is
- An algorithmic pattern where a continuous subsegment (window) of an array or string is maintained, defined by two boundary indices `[window_start, window_end]`.
- Types:
  - **Fixed-size window**: Window length $K$ remains constant; window slides right by 1 element at each step (subtracting the element leaving the window and adding the new element entering it).
  - **Dynamic-size window**: Window expands (`right += 1`) until a condition is broken, then shrinks (`left += 1`) until the condition is restored.

### Why it matters
- Avoids recalculating subarray metrics from scratch ($O(n \times k)$), reducing running time to optimal $O(n)$ linear time.
- Standard pattern for problems involving contiguous subarrays or substrings (e.g., Max Sum Subarray of size K, Longest Substring Without Repeating Characters).

### How it works (internals, if relevant)
- As `right` pointer increments, the new element is incorporated into auxiliary state (e.g. rolling sum, frequency dictionary).
- While the window violates problem constraints, `left` pointer advances, removing elements from the auxiliary state.
- Each element enters the window once and leaves at most once, guaranteeing amortized $O(n)$ operations.

### Common mistakes / gotchas
- Recalculating window sum or frequency using `sum(arr[left:right])` inside the loop, degrading the algorithm back to $O(n^2)$.
- Off-by-one errors when initializing or sizing fixed windows.
- Failing to properly decrement or remove keys from frequency maps when shrinking the left boundary.

### Connects to
- Time Complexity & Big-O (Topic 08).
