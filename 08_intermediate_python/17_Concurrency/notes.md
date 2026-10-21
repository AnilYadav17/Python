# 17. Concurrency Basics: Complete Reference

---

## 1. Concurrency vs Parallelism vs Asynchrony

### What it is
- **Concurrency**: Dealing with lots of things at once. Structuring a program into independent tasks that can be executed in overlapping time periods (interleaved on a single core or parallel across multiple cores).
- **Parallelism**: Doing lots of things at once. Executing multiple computational tasks simultaneously on separate physical CPU cores.
- **Asynchrony (Asynchronous I/O)**: A single-threaded concurrency model where tasks voluntarily yield control while waiting for external I/O events, allowing the single thread to serve other tasks in the interim.
- **Task Classification**:
  - **I/O-Bound**: Tasks spending most of their time waiting for external responses (network requests, database queries, file reads).
  - **CPU-Bound**: Tasks spending most of their time doing intensive computations (cryptographic hashing, image processing, machine learning training).

### Why it matters
- Applying the wrong concurrency model will fail to improve performance (e.g. using Python threads for CPU-bound math runs slower than single-threaded code due to lock contention).
- Selecting the correct paradigm maximizes system throughput and minimizes hardware costs.

### How it works (internals, if relevant)
- **Amdahl's Law**: The theoretical speedup of a program is limited by the serial (non-parallelizable) portion of the task: $\text{Speedup} = \frac{1}{(1 - P) + \frac{P}{N}}$, where $P$ is the parallel fraction and $N$ is the number of cores.

### Common mistakes / gotchas
- Expecting standard Python multithreading to speed up CPU-bound mathematical loops across multiple CPU cores (prevented by the GIL).

### Connects to
- The Global Interpreter Lock (subtopic 2 below).

---

## 2. The Global Interpreter Lock (GIL)

### What it is
- A mutex (mutual exclusion lock) used by CPython to ensure that only **one thread executes Python bytecode at any given moment**, even on multi-core processors.

### Why it matters
- **The Core Trade-off**:
  - Python threads provide true concurrency for **I/O-bound tasks** (the GIL is released during OS system calls, network I/O, sleep, and C extensions like NumPy).
  - Python threads **CANNOT execute CPU-bound bytecode in parallel**. Running two CPU-heavy Python threads on two cores will run serially, often running *slower* than single-threaded code due to GIL acquisition overhead.

### How it works (internals, if relevant)
- **Why the GIL Exists**: CPython's memory management relies on reference counting (`ob_refcnt`). Without the GIL, every increment/decrement of reference counts would require fine-grained thread locking, causing massive performance degradation for single-threaded code and high deadlock risks.
- **GIL Switching**: Every 5 milliseconds (`sys.getswitchinterval()`), CPython pauses bytecode execution and releases the GIL, allowing waiting threads to contend for it.
- **Python 3.13+ Free-Threaded Build (PEP 703)**: Experimental build option (`--disable-gil`) that replaces the GIL with mimalloc-based thread-safe reference counting and immortal objects.

### Common mistakes / gotchas
- Assuming Python threads are "green threads" or fake: Python threads are genuine OS-level POSIX/Windows threads scheduled by the kernel; the GIL simply prevents them from executing CPython bytecode simultaneously.

### Connects to
- Multithreading (subtopic 3 below) and Multiprocessing (subtopic 4).

---

## 3. Multithreading (`threading` & `ThreadPoolExecutor`)

### What it is
- Spawning multiple threads within the **same process memory space**:
  - `threading.Thread`: Manual thread creation, `thread.start()`, `thread.join()`.
  - `threading.Lock`: Mutual exclusion lock to prevent race conditions on shared memory.
  - `concurrent.futures.ThreadPoolExecutor`: High-level worker pool for managing thread lifecycles.

### Why it matters
- Ideal for **I/O-bound tasks** (fetching multiple HTTP endpoints, database calls, reading files concurrently).
- Shared memory makes sharing data between threads trivial (no serialization overhead).

### How it works (internals, if relevant)
- When a thread enters an I/O operation (e.g. `socket.recv()`, `time.sleep()`), the CPython interpreter explicitly releases the GIL, allowing another thread to execute bytecode.
- **Race Condition**: Occurs when multiple threads read and mutate shared mutable state without synchronization. Even simple statements like `counter += 1` compile to multiple bytecode instructions (`LOAD_GLOBAL`, `BINARY_ADD`, `STORE_GLOBAL`), which can be interrupted mid-execution.

### Common mistakes / gotchas
- Mutating shared dictionaries or lists from multiple threads without a `threading.Lock`.
- Creating hundreds of raw threads manually instead of using a bounded `ThreadPoolExecutor`, exhausting OS thread limits.

### Connects to
- Multiprocessing (subtopic 4 below).

---

## 4. Multiprocessing (`multiprocessing` & `ProcessPoolExecutor`)

### What it is
- Spawning multiple independent **OS processes**, each with its own separate Python interpreter, memory space, and GIL:
  - `multiprocessing.Process`: Manual process creation.
  - `concurrent.futures.ProcessPoolExecutor`: High-level pool managing worker processes across CPU cores.
  - Inter-Process Communication (IPC): `multiprocessing.Queue`, `multiprocessing.Pipe`.

### Why it matters
- **The solution for CPU-bound tasks**: Achieves true parallel execution across multiple physical CPU cores (number of workers typically equals `os.cpu_count()`).

### How it works (internals, if relevant)
- On POSIX, processes are spawned using `fork()` or `spawn()`; on Windows/macOS, `spawn()` is default.
- **IPC Serialization Overhead**: Because processes do not share memory, all data passed into worker processes (arguments) and returned from worker processes (results) must be **pickled (serialized)** to bytes, transmitted over OS IPC pipes/sockets, and unpickled by the parent.
- If data transmission overhead exceeds the computation time, multiprocessing will run slower than single-threaded code.

### Common mistakes / gotchas
- Omitting `if __name__ == "__main__":` guard: on Windows and macOS (`spawn` start method), worker processes re-import the main script from scratch. Without this guard, it triggers a fork bomb of infinite process spawning!
- Passing unpicklable objects (like open file handles, database connections, or lambdas) to worker processes, raising `PicklingError`.

### Connects to
- Asynchronous Programming with `asyncio` (subtopic 5 below).

---

## 5. Asynchronous Programming with `asyncio`

### What it is
- Single-threaded, single-process, cooperative multitasking based on an **Event Loop**:
  - `async def`: Declares a native coroutine function.
  - `await`: Suspends execution of current coroutine until the awaited awaitable (Task, Future) completes, yielding control back to the event loop.
  - `asyncio.run(main())`: Initializes and runs the event loop until completion.
  - `asyncio.gather(*coros)` / `asyncio.TaskGroup`: Schedules and awaits multiple coroutines concurrently.

### Why it matters
- Extreme scalability for massive I/O concurrency (handling 10,000 to 100,000 simultaneous network connections / web sockets on a single thread).
- Memory-efficient: A Python thread consumes $\approx 8-16$ KB stack memory; an asyncio task consumes only $\approx 1$ KB.

### How it works (internals, if relevant)
- The **Event Loop** maintains a queue of ready tasks.
- It uses OS-level I/O multiplexers (`epoll` on Linux, `kqueue` on macOS, `IOCP` on Windows) to monitor thousands of file descriptors without blocking.
- When a coroutine hits `await asyncio.sleep(1)` or an async socket read, it yields control back to the loop, which executes other ready tasks.

### Common mistakes / gotchas
- Calling blocking synchronous functions (like `time.sleep()` or `requests.get()`) inside an `async def` coroutine! This blocks the entire single-threaded event loop, freezing all other concurrent tasks. Use non-blocking async equivalents (`asyncio.sleep()`, `httpx.AsyncClient()`) or offload to `asyncio.to_thread()`.
- Forgetting to `await` a coroutine: calling `my_async_func()` without `await` does not execute it; it merely returns an unawaited coroutine object.

### Connects to
- Architectural Decision Matrix (subtopic 6 below).

---

## 6. Architectural Decision Matrix

### What it is
- A definitive reference guide for choosing concurrency models in Python:

| Dimension | `threading` | `multiprocessing` | `asyncio` |
| :--- | :--- | :--- | :--- |
| **Best For** | I/O-bound (blocking libraries) | CPU-bound (math, hashing) | High-concurrency I/O (APIs, websockets) |
| **Execution** | Preemptive multitasking | True hardware parallelism | Cooperative multitasking |
| **Memory Model** | Shared memory | Isolated memory spaces | Shared memory (single thread) |
| **GIL Impact** | Constrained by GIL | Bypasses GIL (one per process) | Constrained by GIL (single thread) |
| **Overhead** | Medium ($\approx 16$ KB / thread) | High (Separate process, IPC) | Extremely low ($\approx 1$ KB / task) |
| **Communication** | Direct variables + Locks | Pickled IPC (Queues/Pipes) | Direct variables (no locks needed) |
| **Max Scale** | $\approx 1,000$ threads | $\approx \text{CPU cores}$ ($4 - 64$) | $10,000 - 100,000+$ tasks |

### Why it matters
- Guides senior engineering decisions: prevents picking multiprocessing for lightweight web scraping or threading for video encoding.
