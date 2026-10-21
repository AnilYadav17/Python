"""
04_common_mistakes_and_fixes.py
Demonstrates common module and package design mistakes:
1. Performance disaster: list.pop(0) vs collections.deque.popleft()
2. Module shadowing pitfalls
3. defaultdict factory instantiation mistake
"""

import time
from collections import deque, defaultdict

def mistake_1_queue_performance():
    print("--- 1. Performance Trap: list.pop(0) vs deque.popleft() ---")
    size = 20_000

    # Test list.pop(0): O(n) per pop -> O(n^2) total
    items_list = list(range(size))
    start = time.perf_counter()
    while items_list:
        items_list.pop(0)  # Shifting all elements in memory on each pop
    list_time = time.perf_counter() - start

    # Test deque.popleft(): O(1) per pop -> O(n) total
    items_deque = deque(range(size))
    start = time.perf_counter()
    while items_deque:
        items_deque.popleft()  # Unlinking node in doubly-linked structure
    deque_time = time.perf_counter() - start

    print(f"Popping {size} items from front:")
    print(f"  list.pop(0):         {list_time * 1000:>8.2f} ms")
    print(f"  deque.popleft():     {deque_time * 1000:>8.2f} ms")
    print(f"  Speedup factor:      {list_time / deque_time:>8.1f}x faster!")


def mistake_2_defaultdict_factory():
    print("\n--- 2. defaultdict Factory Pitfall ---")
    # BUGGY: passing an instantiated object instead of a callable factory function:
    # d = defaultdict([]) -> raises TypeError: first argument must be callable or None

    # FIX: pass the class/callable itself (list, int, dict, set, or custom lambda)
    valid_dict = defaultdict(list)
    valid_dict["primes"].append(2)
    valid_dict["primes"].append(3)
    print(f"Valid defaultdict with list factory: {dict(valid_dict)}")


def mistake_3_module_shadowing():
    print("\n--- 3. Module Name Shadowing Explanation ---")
    # If you name your script 'random.py' or 'email.py', any line executing
    # 'import random' will load your local file instead of Python's standard library module!
    # Always name test scripts descriptively (e.g. test_random_features.py).
    print("Tip: Never name your local scripts the same as standard library or PyPI modules.")


def main():
    mistake_1_queue_performance()
    mistake_2_defaultdict_factory()
    mistake_3_module_shadowing()

if __name__ == "__main__":
    main()
