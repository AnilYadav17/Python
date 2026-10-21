"""
04_common_mistakes_and_fixes.py
Demonstrates common generator and iterator pitfalls:
1. itertools.groupby on unsorted data trap
2. Memory blowout: list comprehension vs generator expression
"""

import sys
import itertools

def mistake_1_groupby_unsorted_trap():
    print("--- 1. itertools.groupby Unsorted Data Trap ---")
    # Data with non-consecutive keys
    records = [
        {"dept": "Engineering", "user": "Alice"},
        {"dept": "Marketing",   "user": "Bob"},
        {"dept": "Engineering", "user": "Charlie"},  # Engineering appears again!
    ]

    # BUGGY: Calling groupby on unsorted data groups only CONSECUTIVE items!
    print("Buggy GroupBy without sorting:")
    for dept, group in itertools.groupby(records, key=lambda r: r["dept"]):
        print(f"  Dept: {dept}, Users: {[u['user'] for u in group]}")

    # FIX: Pre-sort records by the grouping key!
    print("\nFixed GroupBy with pre-sorting:")
    sorted_records = sorted(records, key=lambda r: r["dept"])
    for dept, group in itertools.groupby(sorted_records, key=lambda r: r["dept"]):
        print(f"  Dept: {dept}, Users: {[u['user'] for u in group]}")


def mistake_2_comprehension_memory_blowout():
    print("\n--- 2. Memory Footprint: List Comprehension vs Generator Expression ---")
    n = 100_000

    # List comprehension creates and populates full list in RAM
    eager_list = [x ** 2 for x in range(n)]
    list_mem_bytes = sys.getsizeof(eager_list)

    # Generator expression creates an on-demand generator object
    lazy_gen = (x ** 2 for x in range(n))
    gen_mem_bytes = sys.getsizeof(lazy_gen)

    print(f"Generating {n:,} squared integers:")
    print(f"  List comprehension memory: {list_mem_bytes / 1024:>8.2f} KB")
    print(f"  Generator expression memory: {gen_mem_bytes:>8} bytes")
    print(f"  Memory savings:            {list_mem_bytes / gen_mem_bytes:>8.1f}x smaller!")


def main():
    mistake_1_groupby_unsorted_trap()
    mistake_2_comprehension_memory_blowout()

if __name__ == "__main__":
    main()
