"""
01_basic_usage.py
Demonstrates foundational iterator and generator patterns:
1. Custom Iterator class implementing __iter__ and __next__
2. Generator function using 'yield'
3. Generator expression for lazy on-demand evaluation
"""

# 1. Custom Iterator Class
class FibonacciIterator:
    """Generates first n numbers of Fibonacci sequence."""
    def __init__(self, limit: int):
        self.limit = limit
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # Iterator must return self from __iter__

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration  # Signal iteration termination
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return val


# 2. Generator Function using 'yield'
def range_squares_generator(start: int, stop: int):
    """Yields squares of numbers lazily from start to stop - 1."""
    current = start
    while current < stop:
        yield current ** 2  # Pauses execution and returns value
        current += 1


def main():
    print("--- 1. Custom Iterator Class ---")
    fib = FibonacciIterator(7)
    fib_list = list(fib)
    print(f"First 7 Fibonacci numbers: {fib_list}")

    print("\n--- 2. Generator Function ---")
    sq_gen = range_squares_generator(1, 6)
    print(f"Generator object: {sq_gen}")
    print(f"First manual next(): {next(sq_gen)}")
    print(f"Second manual next(): {next(sq_gen)}")
    print("Remaining items consumed via for loop:")
    for val in sq_gen:
        print(f"  {val}", end=" ")
    print()

    print("\n--- 3. Generator Expression ---")
    # Consumes negligible memory compared to pre-allocating a list
    cubes_gen = (x ** 3 for x in range(1, 6))
    print(f"Generator expression: {cubes_gen}")
    print(f"Sum of cubes calculated lazily: {sum(cubes_gen)}")

if __name__ == "__main__":
    main()
