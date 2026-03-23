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
