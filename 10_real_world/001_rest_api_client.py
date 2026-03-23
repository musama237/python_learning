"""
Challenge: REST API Client
Difficulty: ⭐⭐ Medium
Topic: HTTP, APIs, JSON, Error Handling

Build a robust API client with retries, rate limiting, and caching.
Uses only stdlib (no requests library needed — use urllib).

Hints:
    1. RateLimiter: store timestamps of calls, remove old ones, check count
    2. ResponseCache: store (value, expiry_time) tuples, check time.time() < expiry
    3. APIClient: loop with try/except and exponential backoff sleep(2**attempt * base_delay)
"""

import json
import time
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from functools import lru_cache


class APIClient:
    """A simple REST API client with built-in retry and caching."""

    def __init__(self, base_url: str, max_retries: int = 3, timeout: int = 10):
        # YOUR CODE HERE
        pass

    def _request(self, method: str, endpoint: str, data: dict = None,
                 headers: dict = None) -> dict:
        """Make an HTTP request. Return parsed JSON response.
        Implement retry logic with exponential backoff.
        """
        # YOUR CODE HERE
        pass

    def get(self, endpoint: str, headers: dict = None) -> dict:
        # YOUR CODE HERE
        pass

    def post(self, endpoint: str, data: dict, headers: dict = None) -> dict:
        # YOUR CODE HERE
        pass


class RateLimiter:
    """Token bucket rate limiter."""

    def __init__(self, max_calls: int, period: float):
        """Allow max_calls within period seconds."""
        # YOUR CODE HERE
        pass

    def acquire(self) -> bool:
        """Try to acquire a token. Return True if allowed, False if rate limited."""
        # YOUR CODE HERE
        pass

    def wait_and_acquire(self) -> None:
        """Block until a token is available."""
        # YOUR CODE HERE
        pass


class ResponseCache:
    """Simple TTL cache for API responses."""

    def __init__(self, ttl: float = 60):
        """ttl: time-to-live in seconds."""
        # YOUR CODE HERE
        pass

    def get(self, key: str) -> dict | None:
        """Return cached value or None if expired/missing."""
        # YOUR CODE HERE
        pass

    def set(self, key: str, value: dict) -> None:
        # YOUR CODE HERE
        pass

    def clear(self) -> None:
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test RateLimiter
    limiter = RateLimiter(max_calls=3, period=1.0)
    assert limiter.acquire() is True
    assert limiter.acquire() is True
    assert limiter.acquire() is True
    assert limiter.acquire() is False  # Rate limited

    # Test ResponseCache
    cache = ResponseCache(ttl=0.5)
    cache.set("key1", {"data": "hello"})
    assert cache.get("key1") == {"data": "hello"}
    time.sleep(0.6)
    assert cache.get("key1") is None  # Expired

    cache.set("key2", {"data": "world"})
    cache.clear()
    assert cache.get("key2") is None

    # Test APIClient construction (no actual HTTP calls)
    client = APIClient("https://api.example.com", max_retries=3)
    assert client.base_url == "https://api.example.com"
    print("✅ All tests passed!")
