"""
01_threading_basics.py
Demonstrates multithreading for I/O-bound tasks:
- concurrent.futures.ThreadPoolExecutor
- Measuring real-world speedup when waiting on I/O
- Releasing the GIL during I/O wait
"""

import time
from concurrent.futures import ThreadPoolExecutor

def simulated_io_download(endpoint_id: int, latency_seconds: float = 0.1) -> dict:
    """Simulates an external I/O bound network request."""
    # time.sleep releases the GIL in CPython!
    time.sleep(latency_seconds)
    return {"id": endpoint_id, "status": 200, "bytes": 1024}


def main():
    print("--- 1. Sequential vs ThreadPoolExecutor for I/O-Bound Tasks ---")
    tasks = list(range(10))

    # Sequential Run
    start = time.perf_counter()
    seq_results = [simulated_io_download(task_id) for task_id in tasks]
    seq_time = time.perf_counter() - start
    print(f"Sequential Execution (10 tasks): {seq_time:.3f} seconds")

    # Concurrent Run with ThreadPoolExecutor
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=5) as executor:
        # executor.map preserves input order of results
        thread_results = list(executor.map(simulated_io_download, tasks))
    thread_time = time.perf_counter() - start
    print(f"Threaded Execution (5 workers):    {thread_time:.3f} seconds")
    print(f"Speedup Factor:                    {seq_time / thread_time:.1f}x faster!")

if __name__ == "__main__":
    main()
