"""
03_asyncio_basics.py
Demonstrates asynchronous I/O using standard asyncio:
- Native coroutines (async def) and non-blocking suspension (await)
- Event loop execution via asyncio.run()
- Concurrent task gathering with asyncio.gather()
"""

import asyncio
import time

async def fetch_user_data(user_id: int, delay: float = 0.1) -> dict:
    print(f"  [Async Coroutine] Fetching user {user_id}...")
    # Non-blocking sleep yields control back to event loop!
    await asyncio.sleep(delay)
    print(f"  [Async Coroutine] Received user {user_id}.")
    return {"user_id": user_id, "username": f"user_{user_id}"}


async def main_async():
    print("--- 3. Asynchronous I/O with asyncio ---")
    start = time.perf_counter()

    # Schedule 5 coroutines concurrently on single-threaded event loop
    results = await asyncio.gather(
        fetch_user_data(101),
        fetch_user_data(102),
        fetch_user_data(103),
        fetch_user_data(104),
        fetch_user_data(105),
    )

    elapsed = time.perf_counter() - start
    print(f"\nAll 5 async requests completed in: {elapsed:.3f} seconds!")
    print(f"Results: {results}")

def main():
    # Starts the event loop
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
