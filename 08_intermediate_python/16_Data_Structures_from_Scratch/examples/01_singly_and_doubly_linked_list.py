"""
01_singly_and_doubly_linked_list.py
Pure Python implementations of:
1. Singly Linked List (with prepend, append, search, delete, and in-place reversal)
2. Doubly Linked List (with bidirectional node pointers)
"""

# ==================== SINGLY LINKED LIST ====================
class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def prepend(self, data):
        """Inserts at beginning: O(1) time."""
        new_node = SNode(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def append(self, data):
        """Inserts at end: O(n) without tail pointer."""
        new_node = SNode(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def delete_value(self, data) -> bool:
        """Deletes first occurrence of data: O(n) time."""
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True

        curr = self.head
        while curr.next and curr.next.data != data:
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next
            self._size -= 1
            return True
        return False

    def reverse_inplace(self):
        """Reverses the linked list in-place: O(n) time, O(1) auxiliary space."""
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next  # Save next
            curr.next = prev       # Reverse pointer
            prev = curr            # Advance prev
            curr = next_node       # Advance curr
        self.head = prev

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result


# ==================== DOUBLY LINKED LIST ====================
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def to_forward_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def to_backward_list(self):
        result = []
        curr = self.tail
        while curr:
            result.append(curr.data)
            curr = curr.prev
        return result


def main():
    print("--- 1. Singly Linked List Operations ---")
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.prepend(5)
    print(f"Initial list: {sll.to_list()}")

    sll.delete_value(20)
    print(f"After deleting 20: {sll.to_list()}")

    sll.reverse_inplace()
    print(f"After in-place reversal: {sll.to_list()}")

    print("\n--- 2. Doubly Linked List Operations ---")
    dll = DoublyLinkedList()
    dll.append("A")
    dll.append("B")
    dll.append("C")
    print(f"Forward traversal:  {dll.to_forward_list()}")
    print(f"Backward traversal: {dll.to_backward_list()}")

if __name__ == "__main__":
    main()
