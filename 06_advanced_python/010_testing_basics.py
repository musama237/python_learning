"""
Challenge: Writing Testable Code
Difficulty: ⭐⭐ Medium
Topic: Testing, unittest.mock, Dependency Injection

Write code that's easy to test, then write the tests.
This challenge teaches you to think about testability.

1. Refactor tightly-coupled code to use dependency injection.
2. Write a test double (fake) for an external service.
3. Implement a simple test runner.
"""


class WeatherService:
    """Interface for weather data."""
    def get_temperature(self, city: str) -> float:
        raise NotImplementedError


class FakeWeatherService(WeatherService):
    """Test double that returns predetermined temperatures."""

    def __init__(self, data: dict[str, float]):
        # YOUR CODE HERE
        pass

    def get_temperature(self, city: str) -> float:
        """Return temperature for city. Raise KeyError if unknown."""
        # YOUR CODE HERE
        pass


class WeatherAdvisor:
    """Gives clothing advice based on temperature.
    Uses dependency injection for the weather service.
    """

    def __init__(self, weather_service: WeatherService):
        # YOUR CODE HERE
        pass

    def get_advice(self, city: str) -> str:
        """Return advice based on temperature:
        < 0: "Wear a heavy coat"
        0-15: "Wear a jacket"
        16-25: "Comfortable temperature"
        > 25: "Wear light clothes"
        """
        # YOUR CODE HERE
        pass


class SimpleTestRunner:
    """Runs test functions and reports results.
    Test functions raise AssertionError on failure.
    """

    def __init__(self):
        self.tests = []
        self.passed = 0
        self.failed = 0
        self.errors = []

    def add_test(self, test_func) -> None:
        # YOUR CODE HERE
        pass

    def run(self) -> dict:
        """Run all tests. Return {"passed": n, "failed": n, "errors": [...]}"""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test FakeWeatherService
    fake = FakeWeatherService({"NYC": -5, "LA": 30, "London": 12})
    assert fake.get_temperature("NYC") == -5
    assert fake.get_temperature("LA") == 30

    # Test WeatherAdvisor with fake
    advisor = WeatherAdvisor(fake)
    assert advisor.get_advice("NYC") == "Wear a heavy coat"
    assert advisor.get_advice("LA") == "Wear light clothes"
    assert advisor.get_advice("London") == "Wear a jacket"

    # Test SimpleTestRunner
    runner = SimpleTestRunner()

    def test_pass():
        assert 1 + 1 == 2

    def test_fail():
        assert 1 + 1 == 3

    runner.add_test(test_pass)
    runner.add_test(test_fail)
    results = runner.run()
    assert results["passed"] == 1
    assert results["failed"] == 1
    assert len(results["errors"]) == 1
    print("✅ All tests passed!")
