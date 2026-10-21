# 16. Data Structures from Scratch: Complete Reference

---

## 1. Linked Lists from Scratch

### What it is
- A linear data structure where elements (nodes) are stored non-contiguously in memory, linked together via pointer references:
  - **Singly Linked List**: Each node contains a data payload and a single pointer `next` to the succeeding node.
  - **Doubly Linked List**: Each node contains a data payload, a pointer `next` to the succeeding node, and a pointer `prev` to the preceding node.
- Core operations: `prepend(val)` ($O(1)$), `append(val)` ($O(1)$ with tail pointer), `delete(val)` ($O(n)$), `search(val)` ($O(n)$), `reverse()` ($O(n)$).

### Why it matters
- Unlike arrays/lists, inserting or deleting an element at the beginning takes guaranteed constant $O(1)$ time without memory reallocation or element shifting.
- Foundational building block for queues, adjacency lists, separate chaining hash maps, and LRU caches.

### How it works (internals, if relevant)
- **In-Place Reversal Algorithm**:
  Maintain three pointers: `prev = None`, `curr = head`, `next_node = None`.
  Iterate through the list:
  ```python
  next_node = curr.next # Save next
  curr.next = prev      # Reverse pointer
  prev = curr           # Advance prev
  curr = next_node      # Advance curr
  ```
  Returns `prev` as the new head. Space: $O(1)$, Time: $O(n)$.

### Common mistakes / gotchas
- Losing the reference to the rest of the list by updating `curr.next` before caching `curr.next` in a temporary variable.
- Forgetting to update the `tail` pointer when deleting the last node or appending to an empty list.

### Connects to
- Stacks and Queues (subtopics 2 and 3 below).

---

## 2. Stacks from Scratch

### What it is
- A Last-In, First-Out (LIFO) linear data structure where elements are added and removed exclusively from the top.
- Fundamental operations:
  - `push(item)`: Inserts element at the top ($O(1)$).
  - `pop()`: Removes and returns the top element ($O(1)$). Raises error if empty.
  - `peek()`: Returns top element without removing it ($O(1)$).
  - `is_empty()`: Returns boolean status ($O(1)$).

### Why it matters
- Models call stacks, syntax parsing (matching parentheses, HTML tag balancing), undo/redo history, and iterative Depth-First Search (DFS).

### How it works (internals, if relevant)
- Can be implemented via a dynamic array or a singly linked list with head pointer as the top.
- Node-based stack: `push` prepends a node to `head`; `pop` advances `head = head.next`. Both are strictly guaranteed $O(1)$ operations.

### Common mistakes / gotchas
- Calling `pop()` on an empty stack without checking `is_empty()`, causing unhandled exceptions.
- Confusing LIFO (Stack) with FIFO (Queue).

### Connects to
- Queues (subtopic 3 below) and Graph DFS (subtopic 6).

---

## 3. Queues from Scratch

### What it is
- A First-In, First-Out (FIFO) linear data structure where elements are inserted at the rear (tail) and removed from the front (head).
- Fundamental operations:
  - `enqueue(item)`: Appends element to rear ($O(1)$).
  - `dequeue()`: Removes and returns front element ($O(1)$).
  - `peek()`: Inspects front element ($O(1)$).
  - `is_empty()`: Returns boolean status ($O(1)$).

### Why it matters
- Essential for task scheduling, printer spoolers, network packet buffers, and Breadth-First Search (BFS) graph traversals.

### How it works (internals, if relevant)
- **Why Naive Python Lists Fail for Queues**:
  Using `list.pop(0)` takes $O(n)$ time because all remaining element pointers must shift in memory.
- **Node-based Queue Solution**:
  Maintains two pointers: `head` (front) and `tail` (rear).
  - `enqueue`: Links `tail.next = new_node; tail = new_node` ($O(1)$).
  - `dequeue`: Advances `head = head.next` ($O(1)$).

### Common mistakes / gotchas
- Forgetting to set `tail = None` when the last remaining element is dequeued (`head` becomes `None`).

### Connects to
- Hash Maps (subtopic 4 below) and Graph BFS (subtopic 6).

---

## 4. Hash Maps from Scratch

### What it is
- An associative array mapping unique keys to values with average constant time $O(1)$ lookups, insertions, and deletions.
- Components:
  1. **Fixed-Size Bucket Array**: Internal list of fixed capacity $M$.
  2. **Hash Function**: Converts an arbitrary key into an integer index: `index = hash(key) % capacity`.
  3. **Collision Resolution Strategy**: Separate Chaining (each bucket holds a linked list of key-value nodes).
  4. **Dynamic Resizing & Rehashing**: Doubling capacity and re-inserting all items when Load Factor ($\alpha = \frac{N}{M}$) exceeds 0.75.

### Why it matters
- Understanding the internal collision resolution and rehashing mechanics demystifies Python's built-in `dict` and `set`.

### How it works (internals, if relevant)
- When two distinct keys produce the identical bucket index (`hash(k1) % M == hash(k2) % M`), a **hash collision** occurs.
- Under **Separate Chaining**, the bucket stores a linked list. Python traverses the bucket list, checks `if node.key == search_key:`, updates/retrieves the value if found, or appends a new node.
- If the table becomes crowded ($\alpha > 0.75$), linked lists lengthen, degrading lookups to $O(n)$. Doubling capacity ($2M$) and rehashing restores short chain lengths and $O(1)$ performance.

### Common mistakes / gotchas
- Forgetting to re-calculate hash indices during resizing: you cannot simply copy buckets over, because modulo divisor $M$ changed to $2M$!

### Connects to
- Binary Search Trees (subtopic 5 below).

---

## 5. Binary Search Trees (BST) from Scratch

### What it is
- A hierarchical tree data structure where each node has at most two children (`left` and `right`), adhering to the **Binary Search Invariant**:
  - All keys in `node.left` are strictly smaller than `node.key`.
  - All keys in `node.right` are strictly greater than `node.key`.
- Operations:
  - `insert(val)`: $O(\log n)$ average, $O(n)$ worst.
  - `search(val)`: $O(\log n)$ average, $O(n)$ worst.
  - `delete(val)`: $O(\log n)$ average, $O(n)$ worst.
- Traversals:
  - **In-order (Left, Root, Right)**: Yields values in strictly sorted ascending order!
  - **Pre-order (Root, Left, Right)**: Useful for copying or serializing trees.
  - **Post-order (Left, Right, Root)**: Useful for bottom-up deletion and directory sizing.

### Why it matters
- Maintains sorted order dynamically with fast logarithmic searches and insertions, serving as the basis for AVL trees, Red-Black trees, and database B-Trees.

### How it works (internals, if relevant)
- **Node Deletion Cases**:
  1. Node is a leaf (no children): Remove node directly.
  2. Node has one child: Replace node with its child.
  3. Node has two children: Find node's **in-order successor** (the smallest node in its right subtree), copy its value into the node, and recursively delete the successor from the right subtree.

### Common mistakes / gotchas
- Degenerating into a linked list ($O(n)$ time) when elements are inserted in already-sorted order without self-balancing mechanisms.

### Connects to
- Graph Representation & Traversals (subtopic 6 below).

---

## 6. Graph Representation & Traversals

### What it is
- A non-linear data structure consisting of a set of vertices (nodes) and edges connecting pairs of vertices:
  - **Adjacency Matrix**: 2D grid where `matrix[u][v] = 1` indicates an edge. Space: $O(V^2)$.
  - **Adjacency List**: Dictionary mapping each vertex to a list of its neighboring vertices. Space: $O(V + E)$ (preferred for sparse graphs).
- Core Traversals:
  - **Breadth-First Search (BFS)**: Explores level-by-level using a **Queue**. Guaranteed to find the **shortest path** in unweighted graphs.
  - **Depth-First Search (DFS)**: Explores branch-by-branch going as deep as possible using a **Stack** or recursion. Used for cycle detection and topological sorting.

### Why it matters
- Models networks: social connections, computer routing topologies, dependency graphs, and route mapping.

### How it works (internals, if relevant)
- Must maintain a `visited = set()` to prevent infinite loops in cyclic graphs.
- Time complexity of both BFS and DFS on adjacency lists is $O(V + E)$, where $V$ is number of vertices and $E$ is number of edges.

### Common mistakes / gotchas
- Forgetting the `visited` set in cyclic graphs, causing infinite loops and stack overflow.
- Using DFS to find the shortest path in an unweighted graph (DFS does NOT guarantee shortest path; only BFS does).
