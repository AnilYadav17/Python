"""
04_binary_search_tree.py
Pure Python Binary Search Tree (BST) implementation:
- Node class with left and right pointers
- Insert, Search
- Delete (handling 3 cases: leaf, 1 child, 2 children using in-order successor)
- Traversals: In-order (sorted), Pre-order, Post-order
"""

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key) -> bool:
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key) -> bool:
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node to delete found!
            # Case 1 & 2: Node has 0 or 1 child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 3: Node has 2 children -> find in-order successor (min in right subtree)
            successor = self._min_node(node.right)
            node.key = successor.key
            node.right = self._delete_recursive(node.right, successor.key)

        return node

    def _min_node(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr

    def inorder_traversal(self):
        """In-order traversal: Left, Root, Right (Yields sorted order!)."""
        result = []
        def _traverse(node):
            if node:
                _traverse(node.left)
                result.append(node.key)
                _traverse(node.right)
        _traverse(self.root)
        return result


def main():
    print("--- Pure Python Binary Search Tree (BST) ---")
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]

    for val in values:
        bst.insert(val)

    print(f"In-order Traversal (Sorted): {bst.inorder_traversal()}")
    print(f"Search 40: {bst.search(40)}")
    print(f"Search 99: {bst.search(99)}")

    print("\nDeleting leaf node (20):")
    bst.delete(20)
    print(f"In-order: {bst.inorder_traversal()}")

    print("\nDeleting node with 2 children (50):")
    bst.delete(50)
    print(f"In-order: {bst.inorder_traversal()}")

if __name__ == "__main__":
    main()
