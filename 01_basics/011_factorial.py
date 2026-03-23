"""
Challenge: Factorial
Difficulty: ⭐ Easy
Topic: Loops, Math, Recursion

Calculate the factorial of n (n!). Do NOT use math.factorial.
n! = n * (n-1) * (n-2) * ... * 1
0! = 1

Example:
    factorial(5) -> 120
    factorial(0) -> 1

Hints:
    1. Think about repeated multiplication — or a function that calls itself with a smaller problem.
    2. Iterative: multiply a running result by each number from 1 to n. Recursive: n! = n * (n-1)! with base case 0! = 1.
    3. Start result = 1, loop i from 1 to n inclusive, multiply result *= i each step. Return result.
"""


def factorial(n: int) -> int:
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(3) == 6
    print("✅ All tests passed!")
