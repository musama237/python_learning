"""
Challenge: Binary Search Tree
Difficulty: ⭐⭐⭐ Hard
Topic: Trees, BST, Recursion

Implement a BST with: insert, search, in-order traversal,
min, max, height, and delete.

Example:
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.inorder() -> [3, 5, 7]
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val) -> None:
        # YOUR CODE HERE
        pass

    def search(self, val) -> bool:
        # YOUR CODE HERE
        pass

    def inorder(self) -> list:
        """Return in-order traversal as a list."""
        # YOUR CODE HERE
        pass

    def find_min(self) -> int:
        """Return minimum value. Raise ValueError if empty."""
        # YOUR CODE HERE
        pass

    def find_max(self) -> int:
        """Return maximum value. Raise ValueError if empty."""
        # YOUR CODE HERE
        pass

    def height(self) -> int:
        """Return height of tree. Empty tree has height 0."""
        # YOUR CODE HERE
        pass

    def delete(self, val) -> None:
        """Delete a value from the BST."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    bst = BST()
    for v in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(v)

    assert bst.inorder() == [1, 3, 4, 5, 6, 7, 8]
    assert bst.search(4) is True
    assert bst.search(10) is False
    assert bst.find_min() == 1
    assert bst.find_max() == 8
    assert bst.height() == 3

    bst.delete(3)
    assert bst.inorder() == [1, 4, 5, 6, 7, 8]
    bst.delete(5)  # Delete root
    assert 5 not in bst.inorder()
    assert sorted(bst.inorder()) == bst.inorder()
    print("✅ All tests passed!")
