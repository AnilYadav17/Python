"""
05_advanced_idiomatic.py
Demonstrates modern Python 3.11+ asyncio.TaskGroup:
- Structured concurrency with TaskGroup
- Cooperative cancellation: if one task fails, remaining tasks are automatically cancelled
- Grouped exception propagation
"""

import asyncio
import time

async def worker_job(name: str, delay: float, fail: bool = False):
    print(f"  [Task {name}] Started (will take {delay}s)...")
    try:
        await asyncio.sleep(delay)
        if fail:
            print(f"  [Task {name}] ENCOUNTERED FAILURE!")
            raise ConnectionError(f"Network crashed in {name}")
        print(f"  [Task {name}] Finished successfully.")
        return f"{name}_OK"
    except asyncio.CancelledError:
        print(f"  [Task {name}] CANCELLED cooperatively by TaskGroup!")
        raise


async def demonstrate_structured_taskgroup():
    print("--- 1. Python 3.11+ asyncio.TaskGroup with Automatic Cancellation ---")
    try:
        # TaskGroup ensures that if any child task raises an exception,
        # all other active child tasks are immediately cancelled!
        async with asyncio.TaskGroup() as tg:
            t1 = tg.create_task(worker_job("A", 0.05))
            t2 = tg.create_task(worker_job("B", 0.10, fail=True))  # Fails at 0.1s
            t3 = tg.create_task(worker_job("C", 0.30))             # Would take 0.3s -> gets cancelled!
    except* ConnectionError as eg:
        print(f"\nCaught ExceptionGroup via except*: {eg.exceptions[0]}")

    print("Result: Task C did not waste resources running to completion!")


def main():
    asyncio.run(demonstrate_structured_taskgroup())

if __name__ == "__main__":
    main()
