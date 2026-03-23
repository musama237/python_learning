"""
Challenge: Threading & Thread Safety
Difficulty: ⭐⭐⭐ Hard
Topic: Threading, Locks, Thread Safety

1. Implement a thread-safe counter.
2. Implement a thread-safe bounded queue (producer-consumer).
3. Parallel map function using threads.

Example:
    counter = ThreadSafeCounter()
    # 10 threads each incrementing 1000 times
    # counter.value should be exactly 10000
"""

import threading
from concurrent.futures import ThreadPoolExecutor


class ThreadSafeCounter:
    """Counter that's safe to use from multiple threads."""

    def __init__(self):
        # YOUR CODE HERE
        pass

    def increment(self) -> None:
        # YOUR CODE HERE
        pass

    def decrement(self) -> None:
        # YOUR CODE HERE
        pass

    @property
    def value(self) -> int:
        # YOUR CODE HERE
        pass


def parallel_map(func, data: list, max_workers: int = 4) -> list:
    """Apply func to each element in parallel using ThreadPoolExecutor.
    Return results in the same order as input.
    """
    # YOUR CODE HERE
    pass


class BoundedQueue:
    """Thread-safe bounded queue using conditions."""

    def __init__(self, maxsize: int):
        # YOUR CODE HERE
        pass

    def put(self, item) -> None:
        """Block until space is available, then add item."""
        # YOUR CODE HERE
        pass

    def get(self):
        """Block until item is available, then remove and return it."""
        # YOUR CODE HERE
        pass

    def size(self) -> int:
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test ThreadSafeCounter
    counter = ThreadSafeCounter()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=lambda: [counter.increment() for _ in range(1000)])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    assert counter.value == 10000

    # Test parallel_map
    results = parallel_map(lambda x: x ** 2, list(range(100)))
    assert results == [x ** 2 for x in range(100)]

    # Test BoundedQueue
    bq = BoundedQueue(5)
    produced = []
    consumed = []

    def producer():
        for i in range(20):
            bq.put(i)
            produced.append(i)

    def consumer():
        for _ in range(20):
            item = bq.get()
            consumed.append(item)

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    assert sorted(consumed) == list(range(20))
    print("✅ All tests passed!")
