"""
Challenge: Singly Linked List
Difficulty: ⭐⭐⭐ Hard
Topic: Data Structures, Pointers

Implement a singly linked list with: append, prepend, delete, find, to_list.

Example:
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(0)
    ll.to_list() -> [0, 1, 2]
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add to end."""
        # YOUR CODE HERE
        pass

    def prepend(self, data):
        """Add to beginning."""
        # YOUR CODE HERE
        pass

    def delete(self, data):
        """Delete first occurrence. Raise ValueError if not found."""
        # YOUR CODE HERE
        pass

    def find(self, data) -> bool:
        """Return True if data exists in list."""
        # YOUR CODE HERE
        pass

    def to_list(self) -> list:
        """Convert to Python list."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    ll = LinkedList()
    assert ll.to_list() == []
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]
    ll.prepend(0)
    assert ll.to_list() == [0, 1, 2, 3]
    assert ll.find(2) is True
    assert ll.find(99) is False
    ll.delete(2)
    assert ll.to_list() == [0, 1, 3]
    ll.delete(0)
    assert ll.to_list() == [1, 3]
    try:
        ll.delete(99)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("✅ All tests passed!")
