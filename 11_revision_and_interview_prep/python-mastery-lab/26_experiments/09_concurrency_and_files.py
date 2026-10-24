"""
Experiment 09: Pathlib, Deque vs List Benchmarks & GIL Concurrency
==================================================================

Questions Investigated:
-----------------------
1. How does pathlib.Path / operator combine paths cross-platform?
2. What is the real-world execution speed difference between deque.popleft() and list.pop(0)?
3. What is the status of the GIL in the active interpreter?
4. How does ThreadPoolExecutor parallelize concurrent tasks?

Instructions to Run:
--------------------
$ python3 26_experiments/09_concurrency_and_files.py
"""

from collections import deque
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys
import time


def banner(title: str) -> None:
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


def test_pathlib_operations() -> None:
    banner("1. PATHLIB / OPERATOR OVERLOADING & I/O")
    test_file = Path("test_scratch.txt")
    test_file.write_text("Mastery Lab Pathlib Test", encoding="utf-8")

    assert test_file.exists(), "File must exist after write_text"
    read_data = test_file.read_text(encoding="utf-8")
    print(f"Written & Read: {read_data}")
    assert read_data == "Mastery Lab Pathlib Test"

    # Cleanup
    test_file.unlink()
    assert not test_file.exists(), "File must be removed after unlink"
    print("-> Confirmed: pathlib cleanly manages file lifecycles.")


def test_deque_vs_list_pop_benchmark() -> None:
    banner("2. BENCHMARK: DEQUE.POPLEFT() vs LIST.POP(0)")
    count = 25_000

    # Benchmark list.pop(0) (O(N) memory shifting)
    lst = list(range(count))
    t0 = time.perf_counter()
    while lst:
        lst.pop(0)
    list_time = time.perf_counter() - t0

    # Benchmark deque.popleft() (O(1) block chunk pop)
    deq = deque(range(count))
    t1 = time.perf_counter()
    while deq:
        deq.popleft()
    deque_time = time.perf_counter() - t1

    print(f"Time to pop {count:,} items:")
    print(f"  list.pop(0)      (O(N)): {list_time:.5f} seconds")
    print(f"  deque.popleft()  (O(1)): {deque_time:.5f} seconds")
    print(f"  Speedup factor:         {list_time / max(deque_time, 1e-9):.1f}x faster!")

    assert deque_time < list_time, "deque.popleft must outperform list.pop(0)"
    print("-> Confirmed: collections.deque eliminates O(N) memory shifting.")


def test_gil_status_and_threading() -> None:
    banner("3. GIL STATUS & THREADPOOL EXECUTION")
    is_gil_active = getattr(sys, "_is_gil_enabled", lambda: True)()
    print(f"Interpreter:  {sys.implementation.name} {sys.version.split()[0]}")
    print(f"GIL Active:   {is_gil_active}")

    # Run threaded worker pool
    def worker(n: int) -> int:
        return n * n

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(worker, range(10)))

    print(f"Threaded squares: {results}")
    assert results == [x * x for x in range(10)]
    print("-> Confirmed: ThreadPoolExecutor successfully dispatched concurrent tasks.")


def main() -> None:
    test_pathlib_operations()
    test_deque_vs_list_pop_benchmark()
    test_gil_status_and_threading()
    banner("ALL SYSTEMS & CONCURRENCY EXPERIMENTS VERIFIED")


if __name__ == "__main__":
    main()
