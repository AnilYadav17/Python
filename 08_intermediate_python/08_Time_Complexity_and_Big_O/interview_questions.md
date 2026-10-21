# 08. Time Complexity & Big-O — Interview & Viva Questions

---

### Q1: What is the formal definition of Big-O ($O$), Big-Omega ($\Omega$), and Big-Theta ($\Theta$)?
**Model Answer:**
- **Big-O ($O$)**: Represents an **asymptotic upper bound**. Function $f(n) = O(g(n))$ means there exist positive constants $c$ and $n_0$ such that $0 \le f(n) \le c \cdot g(n)$ for all $n \ge n_0$. It describes the growth rate that an algorithm will never exceed.
- **Big-Omega ($\Omega$)**: Represents an **asymptotic lower bound**. $f(n) = \Omega(g(n))$ means $f(n) \ge c \cdot g(n)$ for all $n \ge n_0$. It describes the best possible performance or minimum effort required.
- **Big-Theta ($\Theta$)**: Represents an **asymptotically tight bound**. $f(n) = \Theta(g(n))$ means $f(n)$ is bounded both above and below: $c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n)$.

---

### Q2: Why is `list.append()` considered $O(1)$ amortized time complexity in Python?
**Model Answer:**
- A Python list is backed by a contiguous dynamic array of pointers.
- When the allocated buffer is full, CPython reallocates a new, larger memory block (over-allocation with a growth factor $\approx 1.125 \times$), copies all existing element pointers over, and frees the old buffer. This single resize operation costs $O(n)$ time.
- However, as the array grows larger, these resize operations occur with exponentially decreasing frequency.
- Over a sequence of $N$ appends, the total number of element copies across all resizes is proportional to $2N$. Dividing total work by $N$ appends gives an **amortized cost of $O(1)$** per operation.

---

### Q3: What is the time complexity of `item in container` for a list versus a set or dict, and why?
**Model Answer:**
- **List (`item in list`)**: $O(n)$ linear time. Lists are ordered sequences without index-to-value indexing. Python must perform a linear scan comparing `item` against each element one by one until a match is found or the end is reached.
- **Set / Dict (`item in set` / `key in dict`)**: $O(1)$ average time. Sets and dictionaries are implemented as hash tables using open addressing. Python computes `hash(item)` to locate the exact bucket index directly in constant time. (Worst case is $O(n)$ in the pathological event of severe hash collisions).

---

### Q4: Why is string concatenation using `+=` inside a loop an $O(n^2)$ operation, and what is the optimal solution?
**Model Answer:**
- Python strings are immutable. When you execute `s += next_str`, Python cannot append to the existing string buffer in place; it must allocate a brand new string in memory large enough to hold `len(s) + len(next_str)` and copy all characters from both strings into it.
- In a loop concatenating $n$ small strings, the first iteration copies 1 character, the second copies 2, the third copies 3, and so on: $1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2} \approx O(n^2)$ total character copies.
- **Optimal Solution**: Collect chunks into a list (`chunks.append(...)`, $O(1)$ amortized) and call `''.join(chunks)`. Python pre-calculates the exact total combined string length upfront, allocates memory once, and copies the data in a single $O(n)$ linear pass.

---

### Q5: What is the difference between Space Complexity and Auxiliary Space?
**Model Answer:**
- **Total Space Complexity**: Measures all memory consumed by the algorithm during execution, including the memory required to store the original input data.
- **Auxiliary Space**: Measures only the **extra or temporary memory** allocated by the algorithm outside the original input data (e.g. temporary variables, helper arrays, recursive call stack frames).
- Example: An in-place sorting algorithm like Quick Sort has an auxiliary space complexity of $O(\log n)$ (due to recursion call stack), whereas Merge Sort has an auxiliary space complexity of $O(n)$ (due to temporary merge buffers).

---

### Q6: How does `list.pop(0)` compare to `list.pop()` in Big-O time complexity?
**Model Answer:**
- `list.pop()` removes the last element of the list in $O(1)$ constant time because the tail pointer is simply decremented without shifting any other elements.
- `list.pop(0)` removes the element at index 0 in $O(n)$ linear time. Because Python lists are contiguous arrays, removing the first pointer requires shifting every remaining $n-1$ element pointer one position to the left in memory. For FIFO queue operations, `collections.deque` must be used instead to achieve $O(1)$ `popleft()`.

---

### Q7: How does Python's `cProfile` module help identify algorithmic bottlenecks in production code?
**Model Answer:**
- `cProfile` is a built-in deterministic C-extension profiler that hooks into CPython's interpreter execution loop.
- It intercepts every function entry and exit, recording:
  - `ncalls`: Number of times the function was invoked.
  - `tottime`: Total duration spent inside the function itself, excluding sub-function calls.
  - `cumtime`: Cumulative duration spent inside the function and all nested functions it called.
- Sorting by `cumtime` or `tottime` immediately reveals the exact function or loop that dominates application runtime, enabling targeted algorithmic optimization without guesswork.
