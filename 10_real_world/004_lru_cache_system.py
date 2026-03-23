"""
Challenge: LRU Cache System
Difficulty: ⭐⭐⭐ Hard
Topic: Data Structures, System Design, Doubly Linked List

Implement a Least Recently Used (LRU) Cache with O(1) get and put.
This is a classic system design interview question.

Requirements:
- get(key): Return value if exists, else -1. Mark as recently used.
- put(key, value): Insert/update. Evict least recently used if at capacity.
- Both operations must be O(1).
"""


class Node:
    """Doubly linked list node."""
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # YOUR CODE HERE
        # Hint: use a dict + doubly linked list
        pass

    def get(self, key: int) -> int:
        """Return value or -1. Move to most recently used."""
        # YOUR CODE HERE
        pass

    def put(self, key: int, value: int) -> None:
        """Insert/update. Evict LRU if over capacity."""
        # YOUR CODE HERE
        pass

    def _remove(self, node: Node) -> None:
        """Remove node from linked list."""
        # YOUR CODE HERE
        pass

    def _add_to_front(self, node: Node) -> None:
        """Add node right after head (most recently used)."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

    cache.put(3, 3)  # Evicts key 2
    assert cache.get(2) == -1

    cache.put(4, 4)  # Evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    # Test update
    cache2 = LRUCache(2)
    cache2.put(1, 1)
    cache2.put(2, 2)
    cache2.put(1, 10)  # Update, not insert
    assert cache2.get(1) == 10
    cache2.put(3, 3)  # Should evict 2, not 1
    assert cache2.get(2) == -1
    assert cache2.get(1) == 10

    # Test capacity 1
    cache3 = LRUCache(1)
    cache3.put(1, 1)
    cache3.put(2, 2)
    assert cache3.get(1) == -1
    assert cache3.get(2) == 2
    print("✅ All tests passed!")
