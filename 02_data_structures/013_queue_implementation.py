"""
Challenge: Implement a Queue
Difficulty: ⭐⭐ Medium
Topic: Data Structures, Classes

Implement a Queue class with enqueue, dequeue, peek, is_empty, and size.
FIFO order. Raise IndexError when dequeuing/peeking an empty queue.

Example:
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.peek()     -> 1
    q.dequeue()  -> 1

Hints:
    1. A queue is FIFO — first in, first out. Think about which end to add and which to remove.
    2. A list can work: append() to enqueue at the end, pop(0) to dequeue from the front.
    3. Store items in a list; use append for enqueue, pop(0) for dequeue, [0] for peek, and raise IndexError when empty. For better performance, consider collections.deque.
"""


class Queue:
    def __init__(self):
        # YOUR CODE HERE
        pass

    def enqueue(self, item):
        # YOUR CODE HERE
        pass

    def dequeue(self):
        # YOUR CODE HERE
        pass

    def peek(self):
        # YOUR CODE HERE
        pass

    def is_empty(self) -> bool:
        # YOUR CODE HERE
        pass

    def size(self) -> int:
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    q = Queue()
    assert q.is_empty() is True
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.peek() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.size() == 1
    q.dequeue()
    assert q.is_empty() is True
    try:
        q.dequeue()
        assert False, "Should have raised IndexError"
    except IndexError:
        pass
    print("✅ All tests passed!")
