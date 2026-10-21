# 17. Concurrency — Interview & Viva Questions

---

### Q1: What is the Global Interpreter Lock (GIL) in CPython, and why does it exist?
**Model Answer:**
- The GIL is a mutual exclusion lock in CPython that restricts execution of Python bytecode to **only one thread at any given time**, even on multi-core processors.
- **Why it exists**: CPython's memory management relies heavily on reference counting (`ob_refcnt`). Without a global lock, every reference increment and decrement across all threads would require fine-grained thread-safe synchronization locks, which would severely degrade single-threaded performance and introduce immense deadlock complexity.
- **Consequence**: Python threads cannot achieve true hardware parallelism for CPU-bound tasks. However, threads are fully effective for I/O-bound tasks because CPython releases the GIL during OS system calls (network sockets, disk I/O, sleep, and C extensions like NumPy).

---

### Q2: When should you choose `threading` versus `multiprocessing` versus `asyncio`?
**Model Answer:**
- **`multiprocessing`**: Choose for **CPU-bound tasks** (e.g. video processing, machine learning, heavy numerical simulations). It bypasses the GIL by spawning independent OS processes, each with its own interpreter and memory space, achieving true multi-core hardware parallelism.
- **`threading`**: Choose for **I/O-bound tasks** that rely on traditional synchronous, blocking libraries (e.g. legacy database drivers, file streams, blocking HTTP clients) where tasks spend most of their time waiting for responses.
- **`asyncio`**: Choose for **high-concurrency network I/O** (e.g. web APIs, microservices, chat applications, web scrapers). A single thread can efficiently multiplex 10,000+ non-blocking sockets using an event loop with minimal memory footprint ($\approx 1$ KB per task).

---

### Q3: Why does `counter += 1` create a race condition in Python multithreading?
**Model Answer:**
- In Python, `counter += 1` appears as a single statement, but CPython compiles it into three distinct bytecode instructions:
  1. `LOAD_GLOBAL (counter)`: Read current value onto evaluation stack.
  2. `BINARY_ADD`: Add 1 to the value.
  3. `STORE_GLOBAL (counter)`: Store result back to memory.
- A thread context switch can occur between any of these instructions. If Thread A reads `counter = 5` and is paused, and Thread B runs, increments `counter` to 6, and saves it, Thread A will resume with its old value 5, increment it to 6, and overwrite Thread B's update.
- To prevent this, a `threading.Lock` must be used to make the critical section atomic.

---

### Q4: What happens if you call a blocking synchronous function like `time.sleep()` inside an `asyncio` coroutine?
**Model Answer:**
- `asyncio` runs cooperative multitasking on a **single thread**.
- Calling a blocking function like `time.sleep(5)` or `requests.get()` halts the entire operating system thread for that duration.
- Because the thread is frozen, the **event loop cannot tick**, meaning all other pending asynchronous tasks, timers, and active network connections are completely frozen and cannot make progress.
- **Solution**: Always use non-blocking async equivalents (like `await asyncio.sleep(5)` or `await httpx_client.get()`), or offload the blocking function to a worker thread using `await asyncio.to_thread(func, *args)`.

---

### Q5: What is the Inter-Process Communication (IPC) overhead in `multiprocessing`?
**Model Answer:**
- Unlike threads which share the same virtual memory space, processes have completely isolated memory spaces.
- To pass data (arguments and return values) between processes, Python must **pickle (serialize)** objects into binary byte streams, transmit them across OS pipes/sockets, and **unpickle (deserialize)** them in the receiving process.
- If the dataset is large (e.g. a 2 GB matrix) and the computation is short, the serialization and IPC transmission time will dominate, making multiprocessing significantly slower than single-threaded execution.
- **Optimization**: Use shared memory (`multiprocessing.shared_memory`) to allow zero-copy array sharing across processes.

---

### Q6: What is structured concurrency and how does `asyncio.TaskGroup` (Python 3.11+) improve upon `asyncio.gather()`?
**Model Answer:**
- Structured concurrency ensures that concurrent child tasks have clear lifetimes bounded by their parent scope; tasks cannot outlive the block that created them.
- With `asyncio.gather()`, if one task raises an exception, the other running tasks continue executing in the background ("orphaned background tasks") unless manually cancelled.
- With `asyncio.TaskGroup` (`async with asyncio.TaskGroup() as tg:`):
  - If any task inside the group raises an exception, all other active tasks in the group are **automatically and immediately cancelled**.
  - The group waits for all cancellations to finish cleanly and re-raises all errors together inside an `ExceptionGroup`.

---

### Q7: Why is the `if __name__ == "__main__":` guard mandatory when using `multiprocessing`?
**Model Answer:**
- On Windows and macOS (and Linux with `spawn` start method), child processes do not inherit memory via POSIX `fork()`. Instead, each child process starts a brand-new Python interpreter and **re-imports the main script from the beginning**.
- Without the `if __name__ == "__main__":` guard, the re-imported script will execute the top-level process-spawning code again, which spawns more child processes, causing an infinite recursive "fork bomb" that crashes the operating system.
