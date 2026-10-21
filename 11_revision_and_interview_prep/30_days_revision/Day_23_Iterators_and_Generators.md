# Day 23: Iterators and Generators

## Explanation
Iterators process large streams of data lazily (one at a time), saving memory. Generators are an easy way to create iterators using functions.

## Key Concepts
- **Iterable**: Has `__iter__()` (e.g., list, string).
- **Iterator**: Has `__next__()` and maintains state.
- **`yield`**: Keyword used in generators. Unlike `return`, `yield` pauses the function and saves its state for the next call.

## Code Example
```python
def countdown(num):
    while num > 0:
        yield num
        num -= 1

for x in countdown(3):
    print(x) # Prints 3, 2, 1
```

## Task
Write a generator function that yields the Fibonacci sequence indefinitely. Use a loop to print the first 10 numbers from it, then `break`.