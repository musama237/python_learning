"""
Challenge: Linear Regression from Scratch
Difficulty: ⭐⭐ Medium
Topic: ML, Gradient Descent, Regression

Implement linear regression using gradient descent.
No sklearn allowed — use only NumPy.

Steps:
1. Initialize weights and bias
2. Forward pass: y_pred = X @ w + b
3. Compute MSE loss
4. Compute gradients
5. Update parameters
"""

import numpy as np


class LinearRegression:
    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.losses = []

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LinearRegression":
        """Train the model using gradient descent."""
        # YOUR CODE HERE
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict target values."""
        # YOUR CODE HERE
        pass

    def mse(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Compute mean squared error."""
        # YOUR CODE HERE
        pass

    def r2_score(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Compute R-squared score."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.randn(100, 3)
    true_weights = np.array([2.0, -1.0, 0.5])
    y = X @ true_weights + 3.0 + np.random.randn(100) * 0.1

    model = LinearRegression(learning_rate=0.1, n_iterations=1000)
    model.fit(X, y)

    y_pred = model.predict(X)
    r2 = model.r2_score(y, y_pred)
    assert r2 > 0.95, f"R2 too low: {r2}"
    assert len(model.losses) > 0
    assert model.losses[-1] < model.losses[0]  # Loss decreased
    assert np.allclose(model.weights, true_weights, atol=0.3)
    print(f"✅ All tests passed! R² = {r2:.4f}")
