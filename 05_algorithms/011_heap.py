"""
Challenge: Min-Heap Implementation
Difficulty: ⭐⭐⭐ Hard
Topic: Heaps, Priority Queues

Implement a min-heap from scratch (no heapq).
Support: push, pop (min), peek, heapify a list.

Example:
    h = MinHeap()
    h.push(5); h.push(3); h.push(7)
    h.pop() -> 3
    h.peek() -> 5

Hints:
    1. Store the heap as an array: parent at i//2, children at 2*i+1 and 2*i+2
    2. Push: append to end and bubble up by swapping with parent while smaller
    3. Pop: swap root with last element, remove last, then bubble down the new root
"""


class MinHeap:
    def __init__(self):
        # YOUR CODE HERE
        pass

    def push(self, val) -> None:
        """Add value and maintain heap property."""
        # YOUR CODE HERE
        pass

    def pop(self) -> int:
        """Remove and return minimum. Raise IndexError if empty."""
        # YOUR CODE HERE
        pass

    def peek(self) -> int:
        """Return minimum without removing. Raise IndexError if empty."""
        # YOUR CODE HERE
        pass

    def __len__(self) -> int:
        # YOUR CODE HERE
        pass

    @staticmethod
    def heapify(arr: list) -> "MinHeap":
        """Build a heap from a list in O(n)."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    h = MinHeap()
    h.push(5)
    h.push(3)
    h.push(7)
    h.push(1)
    assert h.peek() == 1
    assert h.pop() == 1
    assert h.pop() == 3
    assert len(h) == 2

    h2 = MinHeap.heapify([9, 4, 7, 1, 3])
    results = []
    while len(h2):
        results.append(h2.pop())
    assert results == [1, 3, 4, 7, 9]
    print("✅ All tests passed!")
