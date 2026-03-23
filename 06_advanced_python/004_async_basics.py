"""
Challenge: Async/Await Basics
Difficulty: ⭐⭐⭐ Hard
Topic: asyncio, Coroutines, Concurrency

1. Write async functions that simulate concurrent operations.
2. Use asyncio.gather for parallel execution.
3. Implement an async rate limiter.

Run with: python 06_advanced_python/004_async_basics.py

Hints:
    1. Use await asyncio.sleep(delay) to simulate an async operation
    2. asyncio.gather(*coroutines) runs multiple coroutines concurrently and returns results in order
    3. For retry: loop with try/except, await asyncio.sleep between attempts, re-raise on final failure

Learn:
    import asyncio
    async def fetch(url, delay):
        await asyncio.sleep(delay)  # non-blocking sleep
        return {"url": url, "status": 200}

    # Run multiple coroutines in parallel:
    results = await asyncio.gather(fetch("a", 0.1), fetch("b", 0.1))

    # Main entry point:
    asyncio.run(main())
"""

import asyncio
import time


async def fetch_data(url: str, delay: float) -> dict:
    """Simulate fetching data with a delay.
    Return {"url": url, "status": 200}
    """
    # YOUR CODE HERE
    pass


async def fetch_all(urls: list[str], delay: float = 0.1) -> list[dict]:
    """Fetch all URLs concurrently using asyncio.gather.
    Return results in the same order as input URLs.
    """
    # YOUR CODE HERE
    pass


async def async_retry(coro_func, max_attempts: int = 3, delay: float = 0.1):
    """Retry an async function up to max_attempts times.
    Wait 'delay' seconds between attempts.
    Raise the last exception if all fail.
    coro_func is a callable that returns a coroutine.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
async def run_tests():
    # Test fetch_data
    result = await fetch_data("http://example.com", 0.05)
    assert result == {"url": "http://example.com", "status": 200}

    # Test concurrent fetch (should be faster than sequential)
    urls = [f"http://example.com/{i}" for i in range(5)]
    start = time.time()
    results = await fetch_all(urls, delay=0.1)
    elapsed = time.time() - start
    assert len(results) == 5
    assert elapsed < 0.4  # Concurrent, not 0.5+ sequential
    assert all(r["status"] == 200 for r in results)

    # Test async_retry
    attempt = 0

    async def flaky():
        nonlocal attempt
        attempt += 1
        if attempt < 3:
            raise ValueError("not yet")
        return "ok"

    result = await async_retry(flaky, max_attempts=3, delay=0.01)
    assert result == "ok"
    print("✅ All tests passed!")


if __name__ == "__main__":
    asyncio.run(run_tests())
