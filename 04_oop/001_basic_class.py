"""
Challenge: Basic Class - BankAccount
Difficulty: ⭐ Easy
Topic: Classes, Methods, State

Create a BankAccount class with deposit, withdraw, and balance.
- Cannot withdraw more than balance (raise ValueError).
- Cannot deposit/withdraw negative amounts (raise ValueError).

Example:
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    acc.balance -> 150
"""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        # YOUR CODE HERE
        pass

    def deposit(self, amount: float) -> None:
        # YOUR CODE HERE
        pass

    def withdraw(self, amount: float) -> None:
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        """Return 'BankAccount(owner=Alice, balance=100)'"""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    acc = BankAccount("Alice", 100)
    assert acc.owner == "Alice"
    assert acc.balance == 100
    acc.deposit(50)
    assert acc.balance == 150
    acc.withdraw(30)
    assert acc.balance == 120
    try:
        acc.withdraw(200)
        assert False
    except ValueError:
        pass
    try:
        acc.deposit(-10)
        assert False
    except ValueError:
        pass
    assert str(acc) == "BankAccount(owner=Alice, balance=120)"
    print("✅ All tests passed!")
