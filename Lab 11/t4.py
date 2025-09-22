class Node:
    """A node in the Binary Search Tree."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    """Binary Search Tree with insert and in-order traversal methods."""

    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """Recursive helper for insert."""
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
        # If key == node.key, do nothing (no duplicates)

    def in_order_traversal(self):
        """Perform in-order traversal and print keys."""
        self._in_order_recursive(self.root)
        print()  # new line at the end

    def _in_order_recursive(self, node):
        """Recursive helper for in-order traversal."""
        if node:
            self._in_order_recursive(node.left)
            print(node.key, end=" ")
            self._in_order_recursive(node.right)


# Example usage
if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("In-order Traversal of BST:")
    bst.in_order_traversal()
