"""
01_basic_usage.py
Demonstrates foundational context manager patterns:
1. Class-based context manager with __enter__ and __exit__
2. Generator-based context manager with @contextmanager
3. Precision code execution block timer
"""

import time
from contextlib import contextmanager

# 1. Class-Based Context Manager
class ManagedResource:
    def __init__(self, resource_name):
        self.name = resource_name

    def __enter__(self):
        print(f"[Class Context] Acquiring resource: '{self.name}'")
        return f"ACTIVE_CONNECTION({self.name})"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[Class Context] Releasing resource: '{self.name}'")
        return False  # Propagate any exception


# 2. Generator-Based Context Manager via @contextmanager
@contextmanager
def managed_log_channel(channel_name):
    print(f"[Generator Context] Channel '{channel_name}' opened.")
    try:
        yield f"CHANNEL_HANDLE({channel_name})"
    finally:
        print(f"[Generator Context] Channel '{channel_name}' closed.")


# 3. Precision Execution Timer Context Manager
class ExecutionTimer:
    def __init__(self, label="Operation"):
        self.label = label
        self.duration_ms = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self  # Return self so caller can inspect metrics

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.duration_ms = (time.perf_counter() - self.start) * 1000
        print(f"[{self.label}] Elapsed time: {self.duration_ms:.3f} ms")
        return False


def main():
    print("--- 1. Class-Based Context Manager ---")
    with ManagedResource("PostgreSQL_Pool") as handle:
        print(f"  Working inside with block: {handle}")

    print("\n--- 2. Generator-Based Context Manager ---")
    with managed_log_channel("syslog") as ch:
        print(f"  Emitting audit event through: {ch}")

    print("\n--- 3. Execution Timer Block ---")
    with ExecutionTimer("Fibonacci Computation") as timer:
        total = sum(x ** 2 for x in range(500_000))
    print(f"Recorded timer result outside block: {timer.duration_ms:.2f} ms")

if __name__ == "__main__":
    main()
