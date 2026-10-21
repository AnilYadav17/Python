"""
04_common_mistakes_and_fixes.py
Demonstrates hidden O(n) operations in Python loops and their fixes:
1. 'item in list' inside loop (O(n^2)) vs 'item in set' (O(n))
2. 'list.count()' inside comprehension (O(n^2)) vs 'collections.Counter' (O(n))
3. String concatenation '+=' in loop (O(n^2)) vs ''.join() (O(n))
"""

import time
from collections import Counter

def mistake_1_membership_lookup():
    print("--- 1. Membership Testing in Loops: List vs Set ---")
    size = 15_000
    items_to_check = list(range(0, size, 2))

    search_pool_list = list(range(size))
    search_pool_set = set(search_pool_list)

    # BAD: Checking membership in list is O(n) per check -> O(k * n) total!
    start = time.perf_counter()
    hits_list = [x for x in items_to_check if x in search_pool_list]
    dur_list = time.perf_counter() - start

    # FIX: Checking membership in set is O(1) per check -> O(k) total!
    start = time.perf_counter()
    hits_set = [x for x in items_to_check if x in search_pool_set]
    dur_set = time.perf_counter() - start

    print(f"Checking {len(items_to_check)} items against collection of {size}:")
    print(f"  List lookup O(n^2 total):  {dur_list * 1000:>8.2f} ms")
    print(f"  Set lookup  O(n total):    {dur_set * 1000:>8.2f} ms")
    print(f"  Speedup factor:            {dur_list / dur_set:>8.1f}x faster!")


def mistake_2_string_concat_in_loop():
    print("\n--- 2. String Concatenation: '+=' vs ''.join() ---")
    n = 20_000
    words = ["token"] * n

    # BAD: str += creates a new string object each time -> O(n^2) total!
    start = time.perf_counter()
    bad_str = ""
    for w in words:
        bad_str += w
    dur_bad = time.perf_counter() - start

    # FIX: ''.join(list) precomputes required memory and joins in O(n) linear time!
    start = time.perf_counter()
    good_str = "".join(words)
    dur_good = time.perf_counter() - start

    print(f"Concatenating {n} strings:")
    print(f"  '+=' loop:    {dur_bad * 1000:>8.2f} ms")
    print(f"  ''.join():    {dur_good * 1000:>8.2f} ms")
    print(f"  Speedup:      {dur_bad / dur_good:>8.1f}x faster!")


def main():
    mistake_1_membership_lookup()
    mistake_2_string_concat_in_loop()

if __name__ == "__main__":
    main()
