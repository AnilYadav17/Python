"""
02_stack_and_queue.py
Pure Python implementations of:
1. Node-based Stack (LIFO: push, pop, peek in O(1))
2. Node-based Queue (FIFO: enqueue, dequeue, peek in O(1) using head & tail pointers)
No built-in list methods (pop(0), append) used for queue operations.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# ==================== PURE STACK (LIFO) ====================
class LinkedStack:
    def __init__(self):
        self.top = None
        self._count = 0

    def push(self, item):
        """Adds item to top: O(1) time."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._count += 1

    def pop(self):
        """Removes and returns top item: O(1) time."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_value = self.top.value
        self.top = self.top.next
        self._count -= 1
        return popped_value

    def peek(self):
        """Inspects top item without removing: O(1) time."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    def is_empty(self) -> bool:
        return self.top is None

    def __len__(self) -> int:
        return self._count


# ==================== PURE QUEUE (FIFO) ====================
class LinkedQueue:
    def __init__(self):
        self.head = None  # Front of queue (dequeue from here)
        self.tail = None  # Rear of queue (enqueue to here)
        self._count = 0

    def enqueue(self, item):
        """Adds item to rear: O(1) time."""
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._count += 1

    def dequeue(self):
        """Removes and returns front item: O(1) time."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        popped_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None  # Queue is now empty
        self._count -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.head.value

    def is_empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self._count


def main():
    print("--- 1. Testing LinkedStack (LIFO) ---")
    stack = LinkedStack()
    stack.push("Page 1")
    stack.push("Page 2")
    stack.push("Page 3")
    print(f"Stack size: {len(stack)}, Top item: '{stack.peek()}'")
    print(f"Popped: '{stack.pop()}'")
    print(f"Popped: '{stack.pop()}'")
    print(f"Remaining top: '{stack.peek()}'")

    print("\n--- 2. Testing LinkedQueue (FIFO) ---")
    queue = LinkedQueue()
    queue.enqueue("Customer 1")
    queue.enqueue("Customer 2")
    queue.enqueue("Customer 3")
    print(f"Queue size: {len(queue)}, Front item: '{queue.peek()}'")
    print(f"Dequeued: '{queue.dequeue()}'")
    print(f"Dequeued: '{queue.dequeue()}'")
    print(f"Remaining front: '{queue.peek()}'")

if __name__ == "__main__":
    main()
