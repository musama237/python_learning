"""
Challenge: Gradient Descent Variants
Difficulty: ⭐⭐⭐ Hard
Topic: Optimization, SGD, Momentum, Adam

Implement different gradient descent optimizers.
Test them on a simple quadratic function: f(x) = sum(x^2)

Hints:
    1. SGD: simply w -= lr * grad
    2. Momentum: maintain velocity v = momentum*v - lr*grad, then w += v
    3. Adam: track first moment (m) and second moment (v), apply bias correction, then update w -= lr * m_hat / (sqrt(v_hat) + epsilon)

Learn:
    # SGD: params -= lr * grads

    # Momentum:
    self.velocity = self.momentum * self.velocity - self.lr * grads
    params = params + self.velocity

    # Adam:
    self.m = beta1 * self.m + (1 - beta1) * grads      # first moment
    self.v = beta2 * self.v + (1 - beta2) * grads**2    # second moment
    m_hat = self.m / (1 - beta1**self.t)                 # bias correction
    v_hat = self.v / (1 - beta2**self.t)
    params -= self.lr * m_hat / (np.sqrt(v_hat) + eps)
"""

import numpy as np


class SGD:
    """Standard Stochastic Gradient Descent."""
    def __init__(self, learning_rate: float = 0.01):
        self.lr = learning_rate

    def step(self, params: np.ndarray, grads: np.ndarray) -> np.ndarray:
        """Update and return new parameters."""
        # YOUR CODE HERE
        pass


class MomentumSGD:
    """SGD with momentum."""
    def __init__(self, learning_rate: float = 0.01, momentum: float = 0.9):
        self.lr = learning_rate
        self.momentum = momentum
        self.velocity = None

    def step(self, params: np.ndarray, grads: np.ndarray) -> np.ndarray:
        # YOUR CODE HERE
        pass


class Adam:
    """Adam optimizer."""
    def __init__(self, learning_rate: float = 0.001, beta1: float = 0.9,
                 beta2: float = 0.999, epsilon: float = 1e-8):
        self.lr = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = None
        self.v = None
        self.t = 0

    def step(self, params: np.ndarray, grads: np.ndarray) -> np.ndarray:
        # YOUR CODE HERE
        pass


def optimize(optimizer, initial_params: np.ndarray, n_steps: int = 100) -> list[float]:
    """Minimize f(x) = sum(x^2) using the given optimizer.
    Return list of loss values at each step.
    """
    params = initial_params.copy()
    losses = []
    for _ in range(n_steps):
        loss = np.sum(params ** 2)
        losses.append(loss)
        grads = 2 * params  # Gradient of sum(x^2)
        params = optimizer.step(params, grads)
    return losses


# --- Tests (do not modify) ---
if __name__ == "__main__":
    initial = np.array([5.0, -3.0, 2.0])

    # SGD should converge
    sgd_losses = optimize(SGD(lr=0.1), initial, n_steps=100)
    assert sgd_losses[-1] < 0.01

    # Momentum should converge faster
    mom_losses = optimize(MomentumSGD(lr=0.01, momentum=0.9), initial, n_steps=100)
    assert mom_losses[-1] < 0.01

    # Adam should converge
    adam_losses = optimize(Adam(lr=0.1), initial, n_steps=100)
    assert adam_losses[-1] < 0.01

    # All should decrease
    for losses in [sgd_losses, mom_losses, adam_losses]:
        assert losses[-1] < losses[0]
    print("✅ All tests passed!")
