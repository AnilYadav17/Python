# Lesson 19.1: Concurrency Triad — Threads, Processes, and AsyncIO

## 1. What Is This in Simple Words?
Computers do multiple things at once, but they do them in different ways:
- **CPU-bound task**: Calculating prime numbers, crunching image pixels, rendering 3D graphics (Heavy math; the CPU is sweating).
- **I/O-bound task**: Downloading 50 web pages, querying a database, waiting for user keyboard input (The CPU is mostly idle, waiting for the network or disk).

To handle these, Python provides three distinct concurrency models:
1. **Multithreading (`threading`)**: Best for simple I/O tasks where threads wait together.
2. **Multiprocessing (`multiprocessing`)**: Best for CPU-bound tasks; spawns separate Python processes, each with its own memory and its own CPU core.
3. **Asynchronous I/O (`asyncio`)**: Single-threaded cooperative multitasking; best for handling tens of thousands of concurrent network connections without thread overhead!

---

## 2. Cheat Sheet: When to Choose What?

| Concurrency Tool | Best For | Memory Overhead | Overcomes GIL? | Difficulty |
| :--- | :--- | :--- | :--- | :--- |
| **`threading`** | Light I/O (File downloads, UI responsiveness) | Low (~8MB per thread) | ❌ No (GIL allows 1 thread on CPU) | Low/Medium |
| **`multiprocessing`** | Heavy CPU computation (Math, ML, Data) | High (Each process copies Python runtime) | ✅ Yes (Full core parallelization) | Medium |
| **`asyncio`** | High-concurrency network servers (Web APIs, WebSockets) | Tiny (~few KB per task) | ❌ No (Single thread event loop) | Medium/High |

---

## 3. Practical Code Examples

### A. ThreadPoolExecutor for I/O:
```python
from concurrent.futures import ThreadPoolExecutor
import time

def simulate_download(url: str) -> str:
    time.sleep(0.5)  # Simulating network latency
    return f"Downloaded {url}"

urls = ["site1.com", "site2.com", "site3.com", "site4.com"]

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(simulate_download, urls))

print(results)
print(f"Total time: {time.perf_counter() - start:.2f}s")  # ~0.5s instead of 2.0s!
```

### B. ProcessPoolExecutor for CPU-Intensive Work:
```python
from concurrent.futures import ProcessPoolExecutor

def heavy_computation(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    numbers = [5_000_000, 5_000_000, 5_000_000, 5_000_000]
    with ProcessPoolExecutor() as executor:
        totals = list(executor.map(heavy_computation, numbers))
    print("Computed totals in parallel across CPU cores:", totals)
```

### C. AsyncIO for Massive Network Concurrency:
```python
import asyncio

async def fetch_api(endpoint: str):
    print(f"Starting fetch for {endpoint}")
    await asyncio.sleep(1)  # Non-blocking pause! Other tasks run while this waits!
    print(f"Finished {endpoint}")
    return {"endpoint": endpoint, "status": 200}

async def main():
    # Run 3 requests concurrently on a single thread:
    results = await asyncio.gather(
        fetch_api("/users"),
        fetch_api("/products"),
        fetch_api("/orders")
    )
    print("All responses gathered:", results)

# To run:
# asyncio.run(main())
```

---

## 4. Mind-Blowing Facts! 💡

> **Fact 1: AsyncIO Can Handle 100,000 Concurrent Connections!**  
> If an operating system tries to spawn 100,000 OS threads, RAM explodes and CPU dies from context-switching overhead. But an `asyncio` task is just a tiny Python generator object in memory (~2 KB). Modern async frameworks (like FastAPI and Uvicorn) easily juggle tens of thousands of active socket connections on a single machine!
>
> **Fact 2: Multiprocessing Must Use the `if __name__ == '__main__':` Guard!**  
> On Windows and macOS, new processes are created by "spawning" a fresh Python interpreter and re-importing your script. If you forget `if __name__ == '__main__':`, the child process will run the process creation code again, triggering an infinite fork bomb that crashes your computer!

---

## 5. Self-Test
1. **Question**: If you have an image-resizing script that needs to resize 10,000 high-res photos, should you use `threading` or `multiprocessing`?
   - *Answer*: `multiprocessing` (or a dedicated C library like Pillow with multi-core pools), because resizing is CPU-bound and standard Python threads are locked by the GIL.
