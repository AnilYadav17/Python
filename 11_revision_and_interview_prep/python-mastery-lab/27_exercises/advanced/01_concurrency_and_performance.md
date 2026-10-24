# Advanced Exercises: Concurrency, ThreadPools & Performance Optimization

## Exercise 1: Multi-Core Prime Number Finder
**Task**: Build a function `count_primes_parallel(limit: int, num_workers: int = 4) -> int` that splits the range `2` to `limit` into slices and computes primes across multiple processes using `concurrent.futures.ProcessPoolExecutor`. Compare the runtime against a single-process version.
```python
# Observe: ProcessPool scales linearly with CPU cores because it bypasses the GIL!
```

---

## Exercise 2: Slotted Tree Node for 10-Million Node Graph
**Task**: Create a `TreeNode` class representing a node in a massive graph.
1. Implement `__slots__ = ("value", "children")`.
2. Measure the memory consumption of creating 1,000,000 nodes using `tracemalloc`.
3. Compare against a standard class without `__slots__` to observe the ~30% RAM savings.

---

## Exercise 3: Resilient Async Concurrent Downloader
**Task**: Write an async function `download_all(urls: list[str], max_concurrency: int = 3)` that:
- Uses `asyncio.Semaphore` to cap concurrent network operations at 3.
- Uses `asyncio.gather(*tasks, return_exceptions=True)` so that if one URL fails or times out, the other downloads are not aborted.

---

## Exercise 4: Output & Timing Prediction
Consider this code:
```python
import time
from concurrent.futures import ThreadPoolExecutor

def task(n):
    time.sleep(1)
    return n * 2

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(task, [1, 2, 3, 4]))

print(f"Elapsed: {round(time.perf_counter() - start)}s")
```
**Question**: What is the elapsed time printed?  
<details>
<summary>Click to reveal answer</summary>

**Answer**: `1s`. Because `time.sleep()` is an I/O wait that releases the GIL, all 4 threads sleep concurrently across the 4 available workers!
</details>
