# 08. Time Complexity & Big-O Analysis: Complete Reference

---

## 1. Asymptotic Analysis & Foundations

### What it is
- **Asymptotic Analysis**: Mathematical framework for describing how execution time or memory requirements scale as input size $n$ tends toward infinity ($n \to \infty$).
- Core Notations:
  - **Big-O ($O$)**: Upper bound / worst-case growth rate ($f(n) \le c \cdot g(n)$ for all $n \ge n_0$).
  - **Big-Omega ($\Omega$)**: Lower bound / best-case growth rate ($f(n) \ge c \cdot g(n)$).
  - **Big-Theta ($\Theta$)**: Tight bound (both upper and lower bound: $c_1 g(n) \le f(n) \le c_2 g(n)$).

### Why it matters
- Evaluates algorithmic efficiency independent of specific hardware, CPU clock speeds, operating systems, or compiler optimizations.
- Guarantees predictable scalability when migrating algorithms from test datasets ($n=100$) to production datasets ($n=10,000,000$).

### How it works (internals, if relevant)
- Rules of Big-O simplification:
  1. **Drop Constants**: $O(2n + 50) \to O(n)$.
  2. **Drop Lower-Order Terms**: $O(n^2 + 100n + 5000) \to O(n^2)$.
  3. **Multi-variable Inputs**: If function takes two independent inputs $A$ and $B$, loops cannot be collapsed to $n^2$: it is $O(A \times B)$ or $O(A + B)$.

### Common mistakes / gotchas
- Equating Big-O strictly with "worst-case": Big-O is an upper bound that can describe best, average, or worst cases (e.g. Quick Sort best case is $O(n \log n)$, worst case is $O(n^2)$).
- Assuming $O(1)$ always means "faster than $O(n)$" for small inputs: an $O(1)$ algorithm with a large constant factor ($C = 1,000,000$) will run slower than an $O(n)$ algorithm when $n < 1,000,000$.

### Connects to
- Common Complexity Classes (subtopic 2 below).

---

## 2. Common Complexity Classes

### What it is
- The fundamental hierarchy of computational efficiency:
  - **$O(1)$ — Constant**: Time remains unchanged regardless of input size (e.g. dict key lookup, list indexing).
  - **$O(\log n)$ — Logarithmic**: Problem space is halved at each step (e.g. Binary Search).
  - **$O(n)$ — Linear**: Work scales directly proportionally with input size (e.g. Linear Search, finding max element).
  - **$O(n \log n)$ — Linearithmic**: Typical optimal comparison sorting (e.g. Merge Sort, Timsort, Heap Sort).
  - **$O(n^2)$ — Quadratic**: Nested iterations over input (e.g. Bubble Sort, nested comparison loops).
  - **$O(2^n)$ — Exponential**: Doubling operations for each additional element (e.g. naive recursive Fibonacci, generating power set).
  - **$O(n!)$ — Factorial**: Permutation generation, Traveling Salesperson brute-force.

### Why it matters
- For $n = 1,000,000$:
  - $\log_2(n) \approx 20$ operations (fractions of a microsecond).
  - $n = 1,000,000$ operations ($\approx 1$ millisecond).
  - $n \log n \approx 20,000,000$ operations ($\approx 20$ milliseconds).
  - $n^2 = 1,000,000,000,000$ operations ($\approx 16$ minutes to hours).
  - $2^n$ exceeds the number of atoms in the known universe.

### How it works (internals, if relevant)
- Divide-and-conquer recurrences are analyzed using the **Master Theorem**:
  $T(n) = a T(n/b) + f(n)$.
  - For Merge Sort: $a=2, b=2, f(n)=O(n) \implies T(n) = O(n \log n)$.

### Common mistakes / gotchas
- Overlooking hidden logarithmic factors when using tree structures.
- Failing to recognize that nested loops with shrinking bounds ($n + (n-1) + (n-2) + \dots + 1 = \frac{n(n+1)}{2}$) are still $O(n^2)$.

### Connects to
- Space Complexity (subtopic 3 below).

---

## 3. Space Complexity & Memory Overhead

### What it is
- The total memory required by an algorithm as a function of input size $n$:
  - **Auxiliary Space**: Extra temporary memory allocated by the algorithm outside the original input.
  - **Total Space**: Input memory + Auxiliary space.

### Why it matters
- Memory constraints in cloud environments, embedded devices, and serverless lambdas can trigger OOM (Out Of Memory) crashes even when time complexity is acceptable.

### How it works (internals, if relevant)
- **Call Stack Space**: In recursive functions, each active stack frame consumes memory for parameters and return pointers. Recursion of depth $n$ consumes $O(n)$ auxiliary space.
- In-place algorithms (e.g. Bubble Sort, Lomuto Quick Sort) use $O(1)$ auxiliary space.
- Out-of-place algorithms (e.g. naive Merge Sort using array slices) allocate $O(n)$ auxiliary memory buffers.

### Common mistakes / gotchas
- Ignoring recursive call stack depth when calculating space complexity.
- Confusing Python variable reference assignment (`b = a`, $O(1)$ memory) with shallow/deep copying (`b = list(a)` or `copy.deepcopy()`, $O(n)$ memory).

### Connects to
- Python Memory Management (Topic 09).

---

## 4. Amortized Complexity Analysis

### What it is
- The average time per operation over a sequence of operations, guaranteeing that even if an occasional single operation is expensive, the average cost remains cheap.
- Primary example in Python: `list.append()`.

### Why it matters
- Explains why appending to a Python list is classified as $O(1)$ amortized, even though individual resizes take $O(n)$ time.

### How it works (internals, if relevant)
- When a Python dynamic array (`PyListObject`) runs out of allocated space:
  1. CPython allocates a new contiguous block of memory with a growth factor of approximately $\approx 1.125 \times$ (over-allocation).
  2. Copies existing element pointers into the new buffer ($O(n)$ work).
  3. Frees the old buffer.
- Because resizes happen with geometrically decreasing frequency ($1, 4, 8, 16, 25, 35, 46, \dots$), $n$ append operations cost a total of $O(n)$ work.
- Amortized cost per append: $\frac{O(n)}{n} = O(1)$.

### Common mistakes / gotchas
- Assuming `list.insert(0, val)` is $O(1)$ amortized: inserting at the beginning requires shifting all $n$ pointers every single time, making it strictly $O(n)$.
- Mistaking worst-case latency for amortized latency in real-time embedded systems where a sudden resize spike can violate latency SLAs.

### Connects to
- Built-in Operation Complexities (subtopic 5 below).

---

## 5. Time Complexity of Built-in Python Operations

### What it is
- The standard asymptotic running times of CPython operations:
  - **List**:
    - Indexing `lst[i]`: $O(1)$
    - Append `lst.append(x)`: $O(1)$ amortized
    - Pop from end `lst.pop()`: $O(1)$
    - Pop from front `lst.pop(0)`: $O(n)$
    - Insert `lst.insert(i, x)`: $O(n)$
    - Delete `del lst[i]`: $O(n)$
    - Slice `lst[a:b]`: $O(b - a)$
    - Membership `x in lst`: $O(n)$
    - Sort `lst.sort()`: $O(n \log n)$
  - **Dict & Set**:
    - Lookup `key in d` / `item in s`: $O(1)$ average, $O(n)$ worst (pathological hash collisions)
    - Insert / Delete: $O(1)$ average, $O(n)$ worst
  - **String**:
    - Concatenation `s1 + s2`: $O(\text{len}(s1) + \text{len}(s2))$
    - Join `''.join(seq)`: $O(n)$ where $n$ is total combined character count.

### Why it matters
- Writing optimal Python code requires selecting the data structure whose intrinsic operations match the algorithmic requirements.

### How it works (internals, if relevant)
- Dictionaries and sets use open-address hash tables with perturbation sequences, delivering true $O(1)$ lookups.
- Lists are contiguous pointer arrays, delivering $O(1)$ indexed reads via direct memory offset calculation: `address = base_address + index * sizeof(pointer)`.

### Common mistakes / gotchas
- Using `x in my_list` inside a loop iterating over $n$ items: creates a hidden $O(n^2)$ bottleneck. Converting `my_list` to a `set` drops the overall time to $O(n)$.
- String concatenation with `+=` in large loops.

### Connects to
- Analyzing Real Functions (subtopic 6 below).

---

## 6. Analyzing Real Functions from Repository Code

### What it is
- Deconstructing real-world Python routines into algorithmic complexity expressions:
  - **Pattern 1: Nested Loops on Same Data**:
    ```python
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)): ...
    ```
    Comparisons: $\frac{n(n-1)}{2} \implies O(n^2)$ time.
  - **Pattern 2: Linear Scan inside Comprehension**:
    ```python
    duplicates = [x for x in data if data.count(x) > 1]
    ```
    `.count(x)` is $O(n)$, executed $n$ times $\implies O(n^2)$ time!
    Fix: `counts = Counter(data)` ($O(n)$) then filter ($O(n)$) $\implies O(n)$ total.
  - **Pattern 3: Hash Set Deduplication**:
    ```python
    seen = set()
    for x in data:
        if x not in seen: seen.add(x)
    ```
    $n$ iterations $\times O(1)$ lookup $\implies O(n)$ time and $O(n)$ space.

### Why it matters
- Uncovers silent algorithmic slowdowns hidden behind clean, compact Python syntax.

### How it works (internals, if relevant)
- High-level Python methods like `list.count()`, `list.index()`, and `x in list` hide full linear scans under C-level loops.
- Just because code is written on a single line does not mean it runs in $O(1)$!

### Common mistakes / gotchas
- Assuming list comprehensions automatically optimize asymptotic complexity (they optimize constant-factor bytecode dispatch, not algorithmic Big-O).

### Connects to
- Benchmarking & Profiling (subtopic 7 below).

---

## 7. Benchmarking and Profiling in Python

### What it is
- Measuring empirical performance to validate theoretical asymptotic analysis:
  - `timeit`: Standard library module for measuring micro-benchmarks with high precision.
  - `cProfile`: Deterministic C-level profiler that tracks call counts and execution duration per function.
  - `pstats`: Formatter and analyzer for `cProfile` output files.

### Why it matters
- Identifies the exact 10% of code causing 90% of execution runtime (Pareto Principle / 90-10 rule).
- Prevents premature optimization of non-bottleneck routines.

### How it works (internals, if relevant)
- `cProfile` hooks into CPython's interpreter execution loop (`sys.setprofile`), recording timestamps at function entry and exit.
- Reports metrics: `ncalls` (number of invocations), `tottime` (time spent in function excluding sub-calls), `cumtime` (cumulative time including sub-calls).

### Common mistakes / gotchas
- Profiling code that includes heavy network I/O or disk I/O when attempting to measure CPU algorithmic complexity.
- Running micro-benchmarks with `time.time()` instead of `time.perf_counter()` or `timeit`.

### Connects to
- Python Memory Management (Topic 09).
