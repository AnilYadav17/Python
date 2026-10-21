"""
05_advanced_idiomatic.py
Demonstrates programmatic profiling using Python's standard cProfile & pstats modules:
- Profiling a pipeline to find precise hotspots
- Extracting metrics: ncalls, tottime, percall, cumtime programmatically
"""

import cProfile
import pstats
import io

def slow_quadratic_task(data):
    """Simulated bottleneck: O(n^2) comparison loop."""
    matches = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] == data[j]:
                matches += 1
    return matches

def fast_linear_task(data):
    """Simulated optimized task: O(n) dictionary pass."""
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return freq

def simulated_data_pipeline():
    sample = list(range(1500))
    # Call both functions
    res1 = slow_quadratic_task(sample)
    res2 = fast_linear_task(sample)
    return res1, len(res2)

def profile_pipeline():
    # Instantiate profiler
    profiler = cProfile.Profile()
    profiler.enable()

    # Execute pipeline under profiling
    simulated_data_pipeline()

    profiler.disable()

    # Capture and format profiling statistics
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats(pstats.SortKey.CUMULATIVE)
    ps.print_stats(10)  # Print top 10 most time-consuming calls

    print("--- Programmatic Profiler Report (Top Bottlenecks) ---")
    for line in s.getvalue().splitlines()[:15]:
        print(line)

def main():
    profile_pipeline()

if __name__ == "__main__":
    main()
