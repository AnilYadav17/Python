# Day 29: Asynchronous Programming (Asyncio)

## Explanation
`asyncio` is a library to write concurrent code using the `async`/`await` syntax. It's the modern way to handle heavily I/O-bound code (like web scrapers or servers).

## Key Concepts
- **`async def`**: Defines an asynchronous function (coroutine).
- **`await`**: Pauses execution until the awaited task is complete.
- **`asyncio.run()`**: Entry point to execute the async code.

## Code Example
```python
import asyncio

async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(1) # Simulating I/O
    print("Data fetched!")

asyncio.run(fetch_data())
```

## Task
Write two async functions that simulate downloading files (using `asyncio.sleep`). Run them concurrently using `asyncio.gather()`.