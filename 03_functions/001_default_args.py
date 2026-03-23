"""
Challenge: Default & Keyword Arguments
Difficulty: ⭐ Easy
Topic: Functions, Arguments

Write a function that builds a user profile dictionary.
- name is required
- age defaults to None
- occupation defaults to "Unknown"
- Any extra keyword arguments should be added to the dict

Example:
    build_profile("Alice", age=30, city="NYC")
    -> {"name": "Alice", "age": 30, "occupation": "Unknown", "city": "NYC"}
"""


def build_profile(name: str, age: int = None, occupation: str = "Unknown", **kwargs) -> dict:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert build_profile("Alice") == {"name": "Alice", "age": None, "occupation": "Unknown"}
    assert build_profile("Bob", age=25) == {"name": "Bob", "age": 25, "occupation": "Unknown"}
    assert build_profile("Carol", age=30, occupation="Engineer", city="NYC") == {
        "name": "Carol", "age": 30, "occupation": "Engineer", "city": "NYC"
    }
    print("✅ All tests passed!")
