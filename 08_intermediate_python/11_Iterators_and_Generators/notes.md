# 11. Iterators & Generators: Complete Reference

---

## 1. The Iterable and Iterator Protocol

### What it is
- **Iterable**: Any object capable of returning its members one at a time. It implements `__iter__()` which returns an iterator object (or implements `__getitem__()` for sequence indexing). Examples: `list`, `tuple`, `str`, `dict`, `set`.
- **Iterator**: A stateful stream object that produces the next value in the sequence on demand. It implements:
  - `__iter__()`: Returns the iterator object itself (`return self`).
  - `__next__()`: Returns the next element, or raises `StopIteration` when the sequence is exhausted.

### Why it matters
- The universal mechanism driving all iteration constructs in Python: `for` loops, comprehensions, sequence unpacking, `in` operators, and built-ins like `map()`, `filter()`, `sum()`, `min()`, `max()`.
- Decouples collection storage from iteration traversal logic.

### How it works (internals, if relevant)
- When executing `for item in collection:`:
  1. Python calls `iter(collection)` which invokes `collection.__iter__()` to obtain an iterator.
  2. The virtual machine repeatedly calls `next(iterator)` which invokes `iterator.__next__()`.
  3. When `iterator` raises `StopIteration`, CPython traps the exception internally and cleanly exits the loop.

### Common mistakes / gotchas
- Confusing iterables with iterators: lists and tuples are *iterables*, but they are NOT *iterators* (calling `next([1, 2, 3])` raises `TypeError: 'list' object is not an iterator`). You must call `iter(my_list)` first.
- Forgetting that an iterator is **exhaustible**: once an iterator has yielded its final element and raised `StopIteration`, it is permanently consumed.

### Connects to
- Building Custom Iterators (subtopic 2 below).

---

## 2. Building Custom Iterator Classes

### What it is
- Writing user-defined classes that implement both `__iter__()` and `__next__()`:
  ```python
  class CountDown:
      def __init__(self, start):
          self.current = start

      def __iter__(self):
          return self

      def __next__(self):
          if self.current <= 0:
              raise StopIteration
          val = self.current
          self.current -= 1
          return val
  ```

### Why it matters
- Allows creating complex, stateful streaming sequences without pre-generating elements in memory.
- Enables implementing custom traversal algorithms (depth-first tree traversal, graph breadth traversal, matrix spirals).

### How it works (internals, if relevant)
- The iterator maintains state in instance attributes (`self.current`).
- Raising `StopIteration` is Python's standard language signal for sequence termination; returning `None` does NOT stop iteration (it merely yields `None` as a valid value).

### Common mistakes / gotchas
- Forgetting to return `self` from `__iter__()`, which violates the iterator protocol and prevents the iterator from being used in `for` loops.
- Failing to raise `StopIteration`, creating an unintended infinite iterator.

### Connects to
- Generator Functions (subtopic 3 below).

---

## 3. Generator Functions & `yield`

### What it is
- A **generator function** is a function that contains one or more `yield` statements instead of `return`.
- Calling a generator function does not execute its body; instead, it immediately returns a **generator object** implementing the iterator protocol.

### Why it matters
- Simplifies iterator creation by replacing entire classes with simple functions.
- Eliminates manual state management and `StopIteration` boilerplate.

### How it works (internals, if relevant)
- When a generator yields a value, CPython suspends its execution frame (`PyFrameObject`):
  - Saves local variable bindings, instruction pointer (`f_lasti`), and evaluation stack.
  - Returns the yielded value to the caller.
- When `next()` is called again, execution resumes immediately after the `yield` statement with all local state intact.
- Generator states: `GEN_CREATED` -> `GEN_RUNNING` -> `GEN_SUSPENDED` -> `GEN_CLOSED`.
- Reaching the end of the generator or executing `return` causes the generator object to raise `StopIteration`.

### Common mistakes / gotchas
- Expecting calling `my_gen_func()` to execute the code immediately: it only creates the generator object; execution begins on the first `next()` call.
- Putting a `return value` in a generator: in Python 3.3+, `return value` attaches `value` to the `StopIteration(value)` exception, but it does not yield that value in a `for` loop!

### Connects to
- Generator Expressions (subtopic 4 below).

---

## 4. Generator Expressions vs List Comprehensions

### What it is
- **List Comprehension**: `[x * 2 for x in data]` (brackets `[]`) — evaluates eagerly, builds full list in memory.
- **Generator Expression**: `(x * 2 for x in data)` (parentheses `()`) — evaluates lazily, generates elements on demand.

### Why it matters
- **Memory Footprint**: A list comprehension of 10,000,000 integers consumes $\approx 80$ MB of RAM; a generator expression for the same 10,000,000 integers consumes only $\approx 100$ bytes regardless of sequence length.
- Ideal when data is consumed once and discarded (e.g. `sum(x for x in data)`).

### How it works (internals, if relevant)
- A generator expression compiles into an anonymous code object that returns a generator iterator.
- Evaluates only one element at a time during iteration, freeing each element from memory before computing the next.

### Common mistakes / gotchas
- Assuming `(x for x in data)` creates a tuple; to create a tuple, you must explicitly use `tuple(x for x in data)`.
- Re-using a generator expression: since it is an iterator, it can only be consumed once. Attempting to iterate over it a second time yields nothing.

### Connects to
- Advanced Generator Methods (subtopic 5 below).

---

## 5. Advanced Two-Way Generator Methods (`send`, `throw`, `close`)

### What it is
- Generators are two-way coroutines:
  - **`gen.send(value)`**: Resumes generator and passes `value` into the generator as the result of the `yield` expression (`received = yield output`).
  - **`gen.throw(type, val, tb)`**: Injects an exception into the generator at the point of suspension.
  - **`gen.close()`**: Raises `GeneratorExit` inside the generator to terminate it and trigger cleanup blocks.

### Why it matters
- Enables cooperative multitasking, state machines, actor systems, and was the foundational technology that powered early Python coroutines prior to `async`/`await`.

### How it works (internals, if relevant)
- Before calling `send(value)` with a non-None value, the generator must be "primed" by calling `next(gen)` or `gen.send(None)` to advance execution to the first `yield`.
- Attempting to send a non-None value to a newly created generator raises `TypeError: can't send non-None value to a just-started generator`.

### Common mistakes / gotchas
- Forgetting to prime the generator before sending data.
- Catching `GeneratorExit` inside the generator and yielding another value, which raises `RuntimeError: generator ignored GeneratorExit`.

### Connects to
- Delegating Generators with `yield from` (subtopic 6 below).

---

## 6. Delegating Generators with `yield from`

### What it is
- Syntax `yield from subgenerator` (PEP 380, Python 3.3+):
  - Delegates iteration directly to another iterable or generator.
  - Transparently channels `send()`, `throw()`, and `close()` between the caller and the sub-generator.
  - Automatically captures the sub-generator's return value: `result = yield from subgen()`.

### Why it matters
- Eliminates manual delegation loops (`for item in subgen: yield item`).
- Enables flattening nested recursive tree structures cleanly and building complex modular coroutine pipelines.

### How it works (internals, if relevant)
- Establishes a direct bidirectional communication channel between the delegating caller and the inner sub-generator.
- Handles `StopIteration` automatically and unpacks the returned value from `StopIteration.value`.

### Common mistakes / gotchas
- Manually looping `for item in subgen: yield item` when bidirectional communication or return values are needed; `yield from` is faster and handles all coroutine plumbing.

### Connects to
- Advanced `itertools` (subtopic 7 below).

---

## 7. Advanced `itertools` Deep Dive

### What it is
- Advanced iterator combinators:
  - **`groupby(iterable, key=None)`**: Groups consecutive matching keys (requires data to be pre-sorted by key!).
  - **`tee(iterable, n=2)`**: Splits an iterable into $n$ independent iterators.
  - **`takewhile(predicate, iterable)`**: Yields elements as long as predicate is true, then terminates.
  - **`dropwhile(predicate, iterable)`**: Drops elements until predicate becomes false, then yields the remainder.
  - **`zip_longest(*iterables, fillvalue=None)`**: Zips sequences to the length of the longest input, filling gaps.

### Why it matters
- Provides declarative, high-speed C-implemented streaming transformations.

### How it works (internals, if relevant)
- `itertools.groupby()` groups **consecutive** elements only! If the same key appears again later after a different key, a new group is created. Hence, inputs must be pre-sorted by the grouping key.
- `itertools.tee()` uses internal FIFO buffers. If one iterator advances far ahead of the other, the buffered elements remain in memory, defeating lazy memory savings.

### Common mistakes / gotchas
- Using `itertools.groupby()` without sorting the input collection first, resulting in fragmented duplicate groups.
- Modifying the original iterable after splitting it with `itertools.tee()`.

### Connects to
- Concurrency and Asyncio (Topic 17).
