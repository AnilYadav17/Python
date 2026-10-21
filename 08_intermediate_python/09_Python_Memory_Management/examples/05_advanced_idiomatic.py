"""
05_advanced_idiomatic.py
Demonstrates programmatic memory tracking and profiling using the tracemalloc module:
- Tracking memory allocations line-by-line
- Detecting exact source of memory spikes
- Comparing snapshots to identify leaks
"""

import tracemalloc

def allocate_temporary_data():
    # Allocates 100,000 integers
    return [x ** 2 for x in range(100_000)]

def allocate_persistent_data():
    # Allocates 50,000 string objects
    return [f"user_{x:06d}@enterprise.internal" for x in range(50_000)]

def main():
    print("--- Programmatic Memory Profiling with tracemalloc ---")
    # Start tracing memory allocations
    tracemalloc.start()

    snapshot1 = tracemalloc.take_snapshot()

    # Perform allocations
    temp = allocate_temporary_data()
    persistent = allocate_persistent_data()

    snapshot2 = tracemalloc.take_snapshot()

    # Compare snapshot2 vs snapshot1 to find memory growth
    top_stats = snapshot2.compare_to(snapshot1, "lineno")

    print("\nTop 3 Memory Allocation Hotspots (Allocated Differences):")
    for stat in top_stats[:3]:
        print(f"  {stat}")

    # Current and peak memory usage
    current, peak = tracemalloc.get_traced_memory()
    print(f"\nCurrent memory: {current / (1024 * 1024):.2f} MB")
    print(f"Peak memory:    {peak / (1024 * 1024):.2f} MB")

    tracemalloc.stop()

if __name__ == "__main__":
    main()
