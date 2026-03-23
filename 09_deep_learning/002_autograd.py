"""
Challenge: PyTorch Autograd
Difficulty: ⭐⭐ Medium
Topic: PyTorch, Automatic Differentiation, Gradients

Understand how autograd works — the engine behind neural network training.
"""

import torch


def compute_gradients():
    """Compute gradients for f(x, y) = x^2 * y + y^3 at x=2, y=3.
    Return dict with 'df_dx' and 'df_dy' values (as floats).

    df/dx = 2xy = 12
    df/dy = x^2 + 3y^2 = 4 + 27 = 31
    """
    # YOUR CODE HERE
    pass


def gradient_descent_pytorch(f, x_init: float, lr: float = 0.1, steps: int = 100) -> list[float]:
    """Minimize function f using PyTorch autograd.
    f takes a tensor and returns a scalar tensor.
    Return list of x values at each step.
    """
    # YOUR CODE HERE
    pass


def linear_regression_autograd(X: torch.Tensor, y: torch.Tensor,
                                lr: float = 0.01, epochs: int = 100) -> tuple:
    """Train linear regression using autograd (not manual gradients).
    Return (weights, bias, losses).
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    grads = compute_gradients()
    assert abs(grads["df_dx"] - 12.0) < 0.01
    assert abs(grads["df_dy"] - 31.0) < 0.01

    # Minimize f(x) = (x-3)^2, should converge to x=3
    f = lambda x: (x - 3) ** 2
    x_history = gradient_descent_pytorch(f, x_init=0.0, lr=0.1, steps=50)
    assert abs(x_history[-1] - 3.0) < 0.1

    # Linear regression
    torch.manual_seed(42)
    X = torch.randn(100, 2)
    true_w = torch.tensor([2.0, -1.0])
    y = X @ true_w + 0.5 + torch.randn(100) * 0.1

    weights, bias, losses = linear_regression_autograd(X, y, lr=0.1, epochs=200)
    assert losses[-1] < losses[0]
    assert abs(bias - 0.5) < 0.5
    print("✅ All tests passed!")
