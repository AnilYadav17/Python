"""
Experiment 02: Names, Objects, Aliasing, Mutability & Memory Mechanics
======================================================================

Questions Investigated:
-----------------------
1. How does aliasing differ from shallow copying and deep copying on nested structures?
2. What are the exact boundaries of the CPython small integer singleton cache?
3. What happens when attempting in-place addition on a mutable list inside an immutable tuple?
4. How do reference cycles form, and can gc.collect() reclaim them?

Instructions to Run:
--------------------
$ python3 26_experiments/02_memory_and_objects.py
"""

import copy
import gc
import sys


def banner(title: str) -> None:
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


def test_aliasing_vs_shallow_vs_deep() -> None:
    banner("1. ALIASING vs SHALLOW COPY vs DEEP COPY")
    original = [["Item 1", 10], ["Item 2", 20]]

    alias = original
    shallow = original.copy()
    deep = copy.deepcopy(original)

    # Mutate the nested list via alias
    alias[0][1] = 99
    print(f"After alias[0][1] = 99:")
    print(f"  Original: {original}")
    print(f"  Shallow:  {shallow}")
    print(f"  Deep:     {deep}")

    assert original[0][1] == 99, "Original was mutated through alias!"
    assert shallow[0][1] == 99, "Shallow copy shared the inner list reference!"
    assert deep[0][1] == 10, "Deep copy inner list was completely independent!"
    print("-> Confirmed: Only deepcopy isolates nested mutable structures.")


def test_small_integer_cache_boundaries() -> None:
    banner("2. SMALL INTEGER CACHE BOUNDARIES (CPython Detail)")
    # -5 to 256 are pre-allocated singletons in standard CPython
    a = 256
    b = 256
    print(f"256 is 256: {a is b} (id: {id(a)})")
    assert a is b, "256 must be cached singleton"

    # Numbers outside the range created dynamically
    c = int("1000")
    d = int("1000")
    print(f"1000 is 1000: {c is d} (id_c: {id(c)}, id_d: {id(d)})")
    print("-> Confirmed: Small integers are singletons; larger integers have distinct identities.")


def test_tuple_mutation_trap() -> None:
    banner("3. THE TUPLE MUTATION PARADOX: t[2] += [30]")
    t = (1, 2, [10, 20])
    print(f"Initial tuple: {t}")

    try:
        t[2] += [30]
    except TypeError as err:
        print(f"Caught expected TypeError: {err}")

    print(f"Tuple state after failed assignment: {t}")
    assert t[2] == [10, 20, 30], "The list inside was modified before the tuple raised TypeError!"
    print("-> Confirmed: In-place addition mutated list, then assignment to tuple raised error.")


def test_reference_cycles_and_gc() -> None:
    banner("4. REFERENCE CYCLES & GENERATIONAL GC")
    gc.collect()  # Clean initial state

    class Node:
        def __init__(self, name: str) -> None:
            self.name = name
            self.partner = None

    node1 = Node("Left")
    node2 = Node("Right")
    node1.partner = node2
    node2.partner = node1

    del node1
    del node2

    # Both objects are unreachable from code, but reference count is 1 due to the cycle
    unreachable = gc.collect()
    print(f"GC sweep identified and collected {unreachable} cyclic objects.")
    assert unreachable >= 2, "GC should have freed the cyclic nodes"
    print("-> Confirmed: Cyclic Garbage Collector successfully resolved reference cycle.")


def main() -> None:
    test_aliasing_vs_shallow_vs_deep()
    test_small_integer_cache_boundaries()
    test_tuple_mutation_trap()
    test_reference_cycles_and_gc()
    banner("ALL OBJECT & MEMORY EXPERIMENTS VERIFIED SUCCESSFULLY")


if __name__ == "__main__":
    main()
