"""
Challenge: PyTorch Autograd
Difficulty: ⭐⭐ Medium
Topic: PyTorch, Automatic Differentiation, Gradients

Understand how autograd works — the engine behind neural network training.

Hints:
    1. Set requires_grad=True on tensors you want to differentiate with respect to
    2. Call .backward() on a scalar loss to compute gradients, then access them via the .grad attribute
    3. Use optimizer.zero_grad() before each backward pass to clear accumulated gradients

Learn:
    x = torch.tensor(2.0, requires_grad=True)
    y = x ** 2
    y.backward()       # compute gradient
    x.grad             # -> tensor(4.0)  (dy/dx = 2x = 4)

    # Gradient descent loop:
    x = torch.tensor(0.0, requires_grad=True)
    for _ in range(100):
        loss = (x - 3) ** 2
        loss.backward()
        with torch.no_grad():
            x -= lr * x.grad
        x.grad.zero_()
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
