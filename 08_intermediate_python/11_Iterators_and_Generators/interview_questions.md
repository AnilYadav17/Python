# 11. Iterators & Generators — Interview & Viva Questions

---

### Q1: What is the technical difference between an iterable and an iterator in Python?
**Model Answer:**
- **Iterable**: Any object that implements `__iter__()` (returning an iterator) or `__getitem__()` for sequence indexing. Iterables can be iterated over repeatedly (e.g. `list`, `str`, `dict`, `range`).
- **Iterator**: A stateful object representing a stream of data that produces values one at a time via `__next__()`. It must implement both `__iter__()` (returning itself) and `__next__()` (raising `StopIteration` when finished).
- An iterable produces new iterators every time `iter(iterable)` is called, whereas an iterator is stateful and permanently exhausted once consumed.

---

### Q2: How does `yield` work under the hood inside the CPython virtual machine?
**Model Answer:**
- When a function containing `yield` is compiled, Python sets the `CO_GENERATOR` flag on its code object. Calling the function instantiates a `generator` object without executing the body.
- When `next(gen)` is called:
  - CPython executes the generator's stack frame until it hits the `YIELD_VALUE` bytecode instruction.
  - The VM pushes the yielded value to the caller and suspends the generator frame, freezing its instruction pointer (`f_lasti`), local variables, and execution state in heap memory.
- When `next(gen)` is called again, CPython restores the frozen frame and resumes execution immediately after the `yield` instruction.

---

### Q3: Why does `itertools.groupby` produce unexpected fragmented groups on unsorted data?
**Model Answer:**
- Unlike SQL `GROUP BY` (which groups all matching rows across the entire table), `itertools.groupby` operates strictly as a **streaming consecutive grouper**.
- It steps through the iterable and creates a new group whenever the evaluated key changes.
- If identical keys are separated by a different key (e.g. `['A', 'B', 'A']`), `groupby` will produce two separate groups for `'A'`.
- To group all identical keys together, the input sequence **must always be pre-sorted by the grouping key** beforehand (`sorted(data, key=...)`).

---

### Q4: What is the purpose of `yield from` introduced in Python 3.3 (PEP 380)?
**Model Answer:**
- `yield from <iterable>` delegates iteration directly to a sub-generator or iterable.
- Key capabilities:
  1. Simplifies syntax: replaces `for x in subgen: yield x` with `yield from subgen`.
  2. Bidirectional communication: transparently passes values sent via `.send()`, exceptions thrown via `.throw()`, and terminations via `.close()` directly to the inner sub-generator.
  3. Return value capture: if the sub-generator executes a `return result` statement, `yield from` unpacks `StopIteration.value` and assigns it: `result = yield from subgen()`.

---

### Q5: How do generator expressions achieve massive memory savings over list comprehensions?
**Model Answer:**
- A **list comprehension** (`[expr for x in data]`) evaluates **eagerly**: it computes every element immediately and allocates a contiguous dynamic array of pointers in RAM to hold the entire collection.
- A **generator expression** (`(expr for x in data)`) evaluates **lazily**: it creates a lightweight generator iterator ($\approx 100-200$ bytes). Elements are computed on-demand one at a time only when requested by the consumer (`next()` or loop).
- Once an element is consumed, it is discarded from memory before the next element is generated, keeping auxiliary memory constant ($O(1)$) even when processing billions of records.

---

### Q6: What happens when you call `.send(value)` on a generator?
**Model Answer:**
- `.send(value)` resumes a suspended generator and injects `value` as the result of the `yield` expression inside the generator: `received = yield output`.
- It allows two-way communication between caller and generator, transforming the generator into a cooperative coroutine.
- **Requirement**: A generator must be "primed" before sending a non-None value (by calling `next(gen)` or `gen.send(None)`) to advance execution to the first `yield` statement. Calling `.send(non_none)` on an unstarted generator raises `TypeError`.

---

### Q7: What are the risks of using `itertools.tee()` on large streams?
**Model Answer:**
- `itertools.tee(iterable, n)` creates $n$ independent iterators from a single source iterable.
- Under the hood, `tee` maintains a shared FIFO buffer of yielded values. If one split iterator advances further than another, all intermediate values must remain buffered in memory until the slowest iterator catches up and consumes them.
- If one iterator consumes the entire stream before the second iterator starts, the entire stream is buffered in RAM, completely defeating the memory advantages of lazy generator iteration.
