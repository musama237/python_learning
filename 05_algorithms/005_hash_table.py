"""
Challenge: Hash Table from Scratch
Difficulty: ⭐⭐⭐ Hard
Topic: Data Structures, Hashing, Collision Resolution

Implement a hash table with chaining for collision resolution.
Support: put, get, delete, contains, keys, values, len.

Example:
    ht = HashTable()
    ht.put("name", "Alice")
    ht.get("name") -> "Alice"

Hints:
    1. Use hash(key) % capacity to compute the bucket index
    2. Each bucket is a list of (key, value) pairs to handle collisions via chaining
    3. On put, scan the bucket for an existing key to update; otherwise append a new pair

Learn:
    # Hash to bucket index:
    index = hash(key) % self.capacity

    # Chaining: each bucket is a list of pairs:
    self.buckets = [[] for _ in range(capacity)]

    # Put: search bucket, update or append:
    bucket = self.buckets[index]
    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)  # update
            return
    bucket.append((key, value))  # new entry
"""


class HashTable:
    def __init__(self, capacity: int = 16):
        # YOUR CODE HERE
        pass

    def _hash(self, key) -> int:
        """Hash function to map key to bucket index."""
        # YOUR CODE HERE
        pass

    def put(self, key, value) -> None:
        """Insert or update key-value pair."""
        # YOUR CODE HERE
        pass

    def get(self, key, default=None):
        """Get value by key. Return default if not found."""
        # YOUR CODE HERE
        pass

    def delete(self, key) -> None:
        """Delete key. Raise KeyError if not found."""
        # YOUR CODE HERE
        pass

    def contains(self, key) -> bool:
        # YOUR CODE HERE
        pass

    def keys(self) -> list:
        # YOUR CODE HERE
        pass

    def values(self) -> list:
        # YOUR CODE HERE
        pass

    def __len__(self) -> int:
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    ht = HashTable()
    assert len(ht) == 0

    ht.put("name", "Alice")
    ht.put("age", 30)
    assert ht.get("name") == "Alice"
    assert ht.get("age") == 30
    assert len(ht) == 2
    assert ht.contains("name") is True
    assert ht.contains("xyz") is False

    ht.put("name", "Bob")  # Update
    assert ht.get("name") == "Bob"
    assert len(ht) == 2

    ht.delete("age")
    assert ht.get("age") is None
    assert len(ht) == 1

    try:
        ht.delete("nonexistent")
        assert False
    except KeyError:
        pass

    # Test with many keys (collision test)
    for i in range(100):
        ht.put(f"key_{i}", i)
    for i in range(100):
        assert ht.get(f"key_{i}") == i
    print("✅ All tests passed!")
