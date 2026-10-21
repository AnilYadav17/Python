# Day 28: Concurrency & Multithreading

## Explanation
Python can execute multiple tasks "simultaneously". Threading is good for I/O bound tasks (like downloading files). Multiprocessing is for CPU bound tasks.

## Key Concepts
- **GIL (Global Interpreter Lock)**: Prevents multiple native threads from executing Python bytecodes at once.
- **`threading` module**: Run functions in separate threads.
- **`concurrent.futures`**: High-level interface for asynchronously executing callables.

## Code Example
```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(0.1)

t1 = threading.Thread(target=print_numbers)
t1.start()
t1.join() # Wait for thread to finish
```

## Task
Create two functions: one that prints numbers and one that prints letters. Run them concurrently using the `threading` module.