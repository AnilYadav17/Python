"""
05_advanced_idiomatic.py
Demonstrates advanced generator paradigms:
1. Two-way coroutine communication with yield as an expression and send()
2. Flattening nested recursive tree structures using 'yield from'
"""

# 1. Two-Way Coroutine: Running Average Accumulator
def running_average_coroutine():
    """
    Coroutine that receives numbers via send() and yields current running average.
    """
    total = 0.0
    count = 0
    average = None

    while True:
        # yield returns current average to caller AND receives next value from send()
        received_val = yield average
        if received_val is None:
            break
        total += received_val
        count += 1
        average = total / count


# 2. Flattening Nested Structures with 'yield from'
def flatten_nested(iterable):
    """Recursively flattens deeply nested lists/tuples using yield from."""
    for item in iterable:
        if isinstance(item, (list, tuple)):
            # yield from delegates iteration to the recursive subgenerator!
            yield from flatten_nested(item)
        else:
            yield item


def main():
    print("--- 1. Two-Way Coroutine with send() ---")
    avg_coro = running_average_coroutine()

    # Prime the coroutine by advancing to first yield
    next(avg_coro)

    # Send values into the coroutine
    for val in [10, 20, 30, 40]:
        current_avg = avg_coro.send(val)
        print(f"Sent: {val:2d} -> Running Average: {current_avg:.2f}")

    # Close the coroutine cleanly
    avg_coro.close()

    print("\n--- 2. Recursive Flattening with 'yield from' ---")
    nested_data = [1, [2, [3, 4], 5], [6, [7, [8, 9]]], 10]
    print(f"Original Nested: {nested_data}")
    flat_list = list(flatten_nested(nested_data))
    print(f"Flattened:       {flat_list}")

if __name__ == "__main__":
    main()
