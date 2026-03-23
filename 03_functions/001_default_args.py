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

Hints:
    1. Think about how to combine fixed keys with arbitrary extra keys into one dict.
    2. Start by building a dict with the required params (name, age, occupation), then merge in kwargs.
    3. Use dict.update(kwargs) or {**base_dict, **kwargs} to merge the extra keyword arguments into your profile dict.

Learn:
    # Building a dict from known keys:
    profile = {"name": name, "age": age}

    # Merging dicts:
    base = {"a": 1}
    extra = {"b": 2, "c": 3}
    base.update(extra)  # base is now {"a": 1, "b": 2, "c": 3}

    # Or use unpacking:
    merged = {**base, **extra}
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
