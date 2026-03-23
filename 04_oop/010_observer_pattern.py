"""
Challenge: Observer Pattern (Event System)
Difficulty: ⭐⭐⭐ Hard
Topic: Design Patterns, Callbacks, Decoupling

Implement an event system where objects can subscribe to events
and get notified when events are emitted.

Example:
    bus = EventBus()
    results = []
    bus.on("greet", lambda name: results.append(f"Hello {name}"))
    bus.emit("greet", "Alice")
    results -> ["Hello Alice"]

Hints:
    1. Store callbacks in dict of {event: [callbacks]}
    2. emit iterates and calls each
    3. once wraps callback to auto-unsubscribe
"""


class EventBus:
    def __init__(self):
        # YOUR CODE HERE
        pass

    def on(self, event: str, callback) -> None:
        """Subscribe callback to event."""
        # YOUR CODE HERE
        pass

    def off(self, event: str, callback) -> None:
        """Unsubscribe callback from event."""
        # YOUR CODE HERE
        pass

    def emit(self, event: str, *args, **kwargs) -> None:
        """Emit event, calling all subscribers with given args."""
        # YOUR CODE HERE
        pass

    def once(self, event: str, callback) -> None:
        """Subscribe callback that auto-unsubscribes after first call."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    bus = EventBus()
    results = []

    def on_greet(name):
        results.append(f"Hello {name}")

    bus.on("greet", on_greet)
    bus.emit("greet", "Alice")
    bus.emit("greet", "Bob")
    assert results == ["Hello Alice", "Hello Bob"]

    bus.off("greet", on_greet)
    bus.emit("greet", "Carol")
    assert len(results) == 2  # Carol not added

    once_results = []
    bus.once("click", lambda: once_results.append("clicked"))
    bus.emit("click")
    bus.emit("click")
    assert once_results == ["clicked"]  # Only once

    bus.emit("nonexistent")  # Should not error
    print("✅ All tests passed!")
