# 16. Data Structures from Scratch — Interview & Viva Questions

---

### Q1: How do you reverse a Singly Linked List in-place with $O(n)$ time and $O(1)$ auxiliary space?
**Model Answer:**
- Maintain three pointers: `prev = None`, `curr = head`, and `next_node = None`.
- While `curr` is not `None`:
  1. Save the next node: `next_node = curr.next`.
  2. Reverse the link: `curr.next = prev`.
  3. Advance `prev`: `prev = curr`.
  4. Advance `curr`: `curr = next_node`.
- Set `self.head = prev`.
- This reverses all pointer directions in a single pass without allocating any new nodes or lists.

---

### Q2: Why is implementing a Queue using a linked list with `head` and `tail` pointers superior to using a Python `list`?
**Model Answer:**
- A standard Python `list` is a contiguous dynamic array. While appending (`enqueue`) is $O(1)$ amortized, removing from the front (`list.pop(0)`) requires shifting all remaining $n-1$ element pointers in memory, costing $O(n)$ time.
- A node-based queue with `head` and `tail` pointers maintains references to both ends:
  - `enqueue`: Appends a node to `tail.next` and advances `tail` in $O(1)$ constant time.
  - `dequeue`: Removes the node at `head` and advances `head = head.next` in $O(1)$ constant time.
- Neither operation requires shifting memory or reallocating buffers.

---

### Q3: How does a Hash Map handle collisions using Separate Chaining, and why is dynamic rehashing necessary?
**Model Answer:**
- **Separate Chaining**: Each bucket in the hash table's internal array stores the head of a linked list (or dynamic bucket). When two different keys hash to the same bucket index (`hash(k) % capacity`), the new key-value pair is simply appended to that bucket's linked list.
- **Why Rehashing is Necessary**:
  - As more items are added, the **load factor** ($\alpha = \frac{\text{items}}{\text{capacity}}$) increases.
  - If capacity remains fixed, linked lists grow longer, causing lookups, updates, and deletes to degrade from average $O(1)$ to worst-case $O(n)$ linear time.
  - When $\alpha > 0.75$, the table doubles its capacity and **rehashes** all existing keys into the new bucket array, keeping bucket chains short and restoring $O(1)$ performance.

---

### Q4: How do you delete a node with two children from a Binary Search Tree (BST)?
**Model Answer:**
- When deleting a node with two children, you cannot simply remove it without violating the tree structure.
- **Algorithm**:
  1. Find the node's **in-order successor** (the smallest value in its right subtree, found by going right once, then following `left` pointers to the end).
  2. Copy the successor's key/value into the target node being deleted.
  3. Recursively delete the successor from the right subtree (the successor is guaranteed to have at most one child, reducing the problem to the simple 0-child or 1-child case).

---

### Q5: What is the difference between Breadth-First Search (BFS) and Depth-First Search (DFS) on a graph?
**Model Answer:**
- **Breadth-First Search (BFS)**:
  - Traverses the graph level-by-level, exploring all immediate neighbors before moving to deeper levels.
  - Uses a **Queue (FIFO)** data structure.
  - **Guarantee**: Guaranteed to find the **shortest path** (fewest edges) between two nodes in an unweighted graph.
- **Depth-First Search (DFS)**:
  - Traverses as deep as possible along each branch before backtracking.
  - Uses a **Stack (LIFO)** or function recursion call stack.
  - Preferred for topological sorting, cycle detection, and maze solving.
- Both run in $O(V + E)$ time when using an adjacency list.

---

### Q6: Why does an in-order traversal of a Binary Search Tree (BST) yield elements in sorted order?
**Model Answer:**
- By definition, a BST upholds the invariant that for any node:
  - Every key in its left subtree is smaller than `node.key`.
  - Every key in its right subtree is larger than `node.key`.
- In-order traversal visits nodes recursively in the order: **Left -> Root -> Right**.
- Therefore, all elements smaller than `node.key` are visited first, followed by `node.key` itself, followed by all elements larger than `node.key`. Applying this recursively across the entire tree produces a strictly sorted ascending sequence.

---

### Q7: Compare Adjacency Matrix versus Adjacency List for graph representation.
**Model Answer:**
- **Adjacency Matrix ($V \times V$ 2D array)**:
  - Space Complexity: $O(V^2)$ regardless of the number of edges.
  - Edge Lookup (`has_edge(u, v)`): Instant $O(1)$ matrix indexing.
  - Best for dense graphs where $E \approx V^2$. Wasteful for sparse graphs.
- **Adjacency List (Dictionary of Lists)**:
  - Space Complexity: $O(V + E)$.
  - Edge Lookup: $O(\text{degree}(u))$ scanning the neighbor list.
  - Best for sparse graphs where $E \ll V^2$ (most real-world networks, road maps, web links). Iterating over all neighbors of a vertex takes optimal $O(\text{degree}(u))$ time rather than $O(V)$.
