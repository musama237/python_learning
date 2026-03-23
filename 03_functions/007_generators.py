"""
Challenge: Generators
Difficulty: ⭐⭐ Medium
Topic: Generators, Yield, Lazy Evaluation

1. Write a generator that yields Fibonacci numbers infinitely.
2. Write a generator that yields prime numbers up to a limit.
3. Write a generator that chunks an iterable into groups of n.

Example:
    list(islice(fib_generator(), 7)) -> [0, 1, 1, 2, 3, 5, 8]
    list(prime_generator(20)) -> [2, 3, 5, 7, 11, 13, 17, 19]
    list(chunked([1,2,3,4,5], 2)) -> [[1,2], [3,4], [5]]

Hints:
    1. Use yield instead of return -- each yield produces the next value in the sequence.
    2. For fibonacci, keep two variables a, b and yield a, then update a, b = b, a+b. For chunked, slice the list in steps of n.
    3. fib: while True: yield a; a, b = b, a+b (start with a=0, b=1). chunked: for i in range(0, len(lst), n): yield lst[i:i+n]. primes: loop from 2 to limit, check divisibility.
"""

from itertools import islice


def fib_generator():
    """Yield Fibonacci numbers forever: 0, 1, 1, 2, 3, 5, ..."""
    # YOUR CODE HERE
    pass


def prime_generator(limit: int):
    """Yield all prime numbers up to (not including) limit."""
    # YOUR CODE HERE
    pass


def chunked(iterable, n: int):
    """Yield successive n-sized chunks from iterable."""
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert list(islice(fib_generator(), 7)) == [0, 1, 1, 2, 3, 5, 8]
    assert list(islice(fib_generator(), 1)) == [0]

    assert list(prime_generator(20)) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert list(prime_generator(2)) == []
    assert list(prime_generator(3)) == [2]

    assert list(chunked([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(chunked([1, 2, 3], 3)) == [[1, 2, 3]]
    assert list(chunked([], 5)) == []
    print("✅ All tests passed!")
