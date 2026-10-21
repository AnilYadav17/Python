"""
02_multiprocessing_basics.py
Demonstrates multiprocessing for CPU-bound tasks:
- concurrent.futures.ProcessPoolExecutor
- Bypassing the Global Interpreter Lock (GIL)
- True parallel computation across multiple physical CPU cores
"""

import time
import hashlib
from concurrent.futures import ProcessPoolExecutor

def cpu_heavy_hash_task(seed_number: int) -> str:
    """CPU-intensive task: 100,000 iterations of SHA-256 hashing."""
    data = str(seed_number).encode("utf-8")
    for _ in range(100_000):
        data = hashlib.sha256(data).digest()
    return data.hex()


def main():
    print("--- 2. Multiprocessing for CPU-Bound Tasks (Bypassing GIL) ---")
    numbers = [1000, 2000, 3000, 4000]

    # Sequential Execution (Single Core)
    start = time.perf_counter()
    seq_results = [cpu_heavy_hash_task(n) for n in numbers]
    seq_dur = time.perf_counter() - start
    print(f"Single-Core Sequential: {seq_dur:.3f} seconds")

    # Multi-Core Parallel Execution (ProcessPoolExecutor)
    start = time.perf_counter()
    # MANDATORY: if __name__ == '__main__' guard must wrap ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=4) as executor:
        parallel_results = list(executor.map(cpu_heavy_hash_task, numbers))
    parallel_dur = time.perf_counter() - start
    print(f"Multi-Core Parallel (4 cores): {parallel_dur:.3f} seconds")
    print(f"Parallel Speedup:             {seq_dur / parallel_dur:.1f}x faster!")

if __name__ == "__main__":
    main()
