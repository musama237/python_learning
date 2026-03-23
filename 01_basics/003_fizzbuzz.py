"""
Challenge: FizzBuzz
Difficulty: ⭐ Easy
Topic: Conditionals, Loops, Modulo

Write a function that returns a list of strings from 1 to n:
- "Fizz" for multiples of 3
- "Buzz" for multiples of 5
- "FizzBuzz" for multiples of both 3 and 5
- The number as a string otherwise

Example:
    fizzbuzz(5) -> ["1", "2", "Fizz", "4", "Buzz"]

Hints:
    1. The order in which you check divisibility matters — what happens with numbers divisible by both 3 and 5?
    2. Check divisibility by 15 (or both 3 and 5) first, then by 3, then by 5, then default to the number as a string.
    3. Loop from 1 to n, build a result list, and append the appropriate string for each number based on the divisibility checks.

Learn:
    # Check divisibility with modulo:
    if n % 3 == 0:   # n is divisible by 3
    if n % 15 == 0:  # n is divisible by both 3 and 5

    # Building a list in a loop:
    result = []
    for i in range(1, 6):
        result.append(str(i))

    # Convert int to string:
    str(42)  # -> "42"
"""


def fizzbuzz(n: int) -> list[str]:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(1) == ["1"]
    assert fizzbuzz(3) == ["1", "2", "Fizz"]
    assert len(fizzbuzz(100)) == 100
    print("✅ All tests passed!")
