"""
Experiment 07: Iterators, Generators, yield from & Memory Savings
=================================================================

Questions Investigated:
-----------------------
1. How does the iterator protocol (__iter__, __next__, StopIteration) operate manually?
2. What is the RAM footprint comparison between eager lists vs lazy generator expressions?
3. How does yield from delegate to nested iterators?
4. How does .send() pass data bidirectionally into a generator coroutine?

Instructions to Run:
--------------------
$ python3 26_experiments/07_iterators_and_generators.py
"""

import sys


def banner(title: str) -> None:
    print(f"\n{'=' * 65}\n{title}\n{'=' * 65}")


def test_manual_iteration_protocol() -> None:
    banner("1. MANUAL ITERATOR PROTOCOL")
    data = [10, 20]
    it = iter(data)

    print(f"Type of iterator: {type(it).__name__}")
    val1 = next(it)
    val2 = next(it)
    print(f"Pulled: {val1}, {val2}")

    exhausted = False
    try:
        next(it)
    except StopIteration:
        exhausted = True

    assert exhausted, "Iterator must raise StopIteration when exhausted"
    print("-> Confirmed: Iterator raises StopIteration upon completion.")


def test_generator_memory_footprint() -> None:
    banner("2. MEMORY FOOTPRINT: EAGER LIST VS LAZY GENERATOR")
    count = 100_000

    eager_list = [x * 2 for x in range(count)]
    lazy_gen = (x * 2 for x in range(count))

    list_size = sys.getsizeof(eager_list)
    gen_size = sys.getsizeof(lazy_gen)

    print(f"Memory for {count:,} items:")
    print(f"  Eager List:          {list_size:,} bytes")
    print(f"  Generator Object:    {gen_size:,} bytes")
    print(f"  Memory Savings:      {((list_size - gen_size) / list_size) * 100:.2f}%")

    assert gen_size < 300, "Generator object must be tiny constant size"
    assert list_size > 800_000, "List must allocate full array of pointers"
    print("-> Confirmed: Generators offer massive memory efficiency for sequence pipelines.")


def test_yield_from_delegation() -> None:
    banner("3. DELEGATION VIA YIELD FROM")

    def nested_gen():
        yield from [1, 2, 3]
        yield from ("A", "B")

    result = list(nested_gen())
    print(f"Delegated output: {result}")
    assert result == [1, 2, 3, "A", "B"]
    print("-> Confirmed: yield from transparently streams from multiple iterables.")


def test_bidirectional_send() -> None:
    banner("4. BIDIRECTIONAL COMMUNICATION WITH .send()")

    def cumulative_sum():
        total = 0
        while True:
            val = yield total
            if val is None:
                break
            total += val

    calc = cumulative_sum()
    next(calc)  # Prime
    assert calc.send(10) == 10
    assert calc.send(25) == 35
    assert calc.send(5) == 40
    print(f"Final cumulative sum via .send(): 40")
    print("-> Confirmed: Generators receive input via .send().")


def main() -> None:
    test_manual_iteration_protocol()
    test_generator_memory_footprint()
    test_yield_from_delegation()
    test_bidirectional_send()
    banner("ALL ITERATOR & GENERATOR EXPERIMENTS VERIFIED")


if __name__ == "__main__":
    main()
