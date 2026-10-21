"""
02_edge_cases.py
Demonstrates subtle iterator and generator edge cases:
- Iterator exhaustion (iterators cannot be rewound)
- The return statement inside generator and StopIteration.value
- itertools.tee() independent stream duplication and memory caveats
"""

import itertools

def demonstrate_iterator_exhaustion():
    print("--- 1. Iterator Exhaustion Trap ---")
    numbers = [1, 2, 3]

    # A list is an iterable (reusable)
    print("List iteration pass 1:", [x for x in numbers])
    print("List iteration pass 2:", [x for x in numbers])

    # A generator/iterator is single-use only!
    gen = (x for x in numbers)
    print("Generator iteration pass 1:", list(gen))
    print("Generator iteration pass 2 (EMPTY!):", list(gen))  # Empty! Exhausted


def demonstrate_generator_return_value():
    print("\n--- 2. Generator 'return' and StopIteration Value ---")

    def generator_with_return():
        yield "Step 1: Init"
        yield "Step 2: Process"
        return "Final Return Status: SUCCESS"

    g = generator_with_return()
    print(next(g))
    print(next(g))
    try:
        next(g)
    except StopIteration as stop_err:
        # In Python 3.3+, the return value is attached to the StopIteration exception!
        print(f"StopIteration caught! Return value attached: '{stop_err.value}'")


def demonstrate_itertools_tee():
    print("\n--- 3. itertools.tee() Stream Duplication ---")
    stream = (x * 10 for x in range(1, 4))

    # Split one iterator into two independent iterators
    stream_a, stream_b = itertools.tee(stream, 2)

    print("Stream A first item:", next(stream_a))
    print("Stream B all items:", list(stream_b))
    print("Stream A remaining items:", list(stream_a))
    print("Caution: If one tee branch runs far ahead, it buffers items in RAM!")


def main():
    demonstrate_iterator_exhaustion()
    demonstrate_generator_return_value()
    demonstrate_itertools_tee()

if __name__ == "__main__":
    main()
