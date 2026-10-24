# Lesson 04: Stacks, Queues, and `collections.deque`

## 1. Stacks vs. Queues: The Real-World Picture

- **Stack (LIFO - Last-In, First-Out)**: Like a stack of clean plates at a restaurant. You put plates on top, and you take plates off the top.
- **Queue (FIFO - First-In, First-Out)**: Like a line of people waiting at a movie ticket counter. The first person to arrive is the first person served.

```
       STACK (LIFO)                            QUEUE (FIFO)
   Push Top -> [ Plate 3 ]             Enqueue Back -> [ Person 3 ]
               [ Plate 2 ]                             [ Person 2 ]
    Pop Top <- [ Plate 1 ]              Dequeue Front <- [ Person 1 ]
```

---

## 2. Using Python Lists as Stacks: Fast and Safe ($O(1)$)

Python lists make outstanding stacks:
```python
stack = []

# Push items to the top:
stack.append("Page 1")
stack.append("Page 2")
stack.append("Page 3")

# Pop items from the top:
current = stack.pop()
print("Popped:", current)  # "Page 3"
```
Because `append()` and `pop()` operate on the **end of the list**, both run in blazing-fast **$O(1)$ constant time**.

---

## 3. The Performance Crime: Never Use a List as a Queue!

Look at how beginners write a queue using a list:
```python
# WARNING: TERRIBLE PERFORMANCE!
queue = []
queue.append("Customer 1")
queue.append("Customer 2")

# Dequeue from the front:
served = queue.pop(0)  # SLOW O(N)!
```

### Why Is `list.pop(0)` Catastrophically Slow?
Because a Python list is a contiguous memory array:
- When you remove item 0, Python must physically **shift every single remaining item in memory one slot to the left**!
- If your queue has 100,000 requests, `queue.pop(0)` moves 99,999 memory pointers on every single pop!

---

## 4. The Professional Fix: `collections.deque` ($O(1)$)

Python has a dedicated, high-performance double-ended queue in the standard library: **`collections.deque`**:

```python
from collections import deque

queue = deque()

# Add to back (Enqueue):
queue.append("Job 1")
queue.append("Job 2")
queue.append("Job 3")

# Remove from front (Dequeue) in O(1) instant time!
current_job = queue.popleft()
print("Processing:", current_job)  # "Job 1"
```

### Fascinating Fact 💡
> **Did you know?**
> How is `deque` implemented in CPython?  
> It is not a single array or a pure linked list. It is an **unrolled doubly-linked list of 64-element memory blocks**! This provides cache-friendly memory locality while ensuring adding or popping from either end is always guaranteed **$O(1)$ time with zero memory shifting**!

---

## 5. Quick Self-Test
1. What is the time complexity of `list.pop(0)` vs `deque.popleft()`?
   - *Answer: `list.pop(0)` is $O(N)$ linear time; `deque.popleft()` is $O(1)$ constant time.*
2. Where in the Python standard library does `deque` live?
   - *Answer: In `collections` (`from collections import deque`).*
