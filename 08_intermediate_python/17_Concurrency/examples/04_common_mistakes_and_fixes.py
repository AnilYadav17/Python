"""
04_common_mistakes_and_fixes.py
Demonstrates concurrency pitfalls and their fixes:
1. Race condition on shared mutable counter without synchronization
2. Eliminating race conditions using threading.Lock
3. Blocking the asyncio event loop with time.sleep()
"""

import threading
import time

def mistake_1_race_condition():
    print("--- 1. Race Condition on Shared Counter ---")
    shared_counter_unsafe = 0
    shared_counter_safe = 0
    lock = threading.Lock()

    def unsafe_worker():
        nonlocal shared_counter_unsafe
        for _ in range(100_000):
            # Read-Modify-Write is NOT atomic in CPython!
            current = shared_counter_unsafe
            time.sleep(0.000001)  # Force thread context switch
            shared_counter_unsafe = current + 1

    def safe_worker():
        nonlocal shared_counter_safe
        for _ in range(100_000):
            with lock:  # Mutual exclusion guarantees atomicity
                current = shared_counter_safe
                # Protected critical section
                shared_counter_safe = current + 1

    # Run unsafe threads (with 500 iterations so it executes in ~10ms)
    def fast_unsafe():
        nonlocal shared_counter_unsafe
        for _ in range(1000):
            c = shared_counter_unsafe
            time.sleep(0.00001)  # Release GIL to guarantee collision
            shared_counter_unsafe = c + 1

    def fast_safe():
        nonlocal shared_counter_safe
        for _ in range(1000):
            with lock:
                c = shared_counter_safe
                time.sleep(0.00001)
                shared_counter_safe = c + 1

    t1 = threading.Thread(target=fast_unsafe)
    t2 = threading.Thread(target=fast_unsafe)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"Expected: 2,000 | Actual Unsafe Counter: {shared_counter_unsafe} (Collision demonstrated!)")

    s1 = threading.Thread(target=fast_safe)
    s2 = threading.Thread(target=fast_safe)
    s1.start()
    s2.start()
    s1.join()
    s2.join()

    print(f"Expected: 2,000 | Actual Safe Counter:   {shared_counter_safe} (Protected with Lock!)")


def main():
    mistake_1_race_condition()

if __name__ == "__main__":
    main()
