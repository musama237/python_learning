"""
Challenge: Logistic Regression from Scratch
Difficulty: ⭐⭐ Medium
Topic: ML, Classification, Sigmoid, Cross-Entropy

Implement binary logistic regression with gradient descent.

Hints:
    1. Sigmoid is 1/(1+exp(-z)); clip z to avoid overflow (e.g., np.clip(z, -500, 500))
    2. Loss is -mean(y*log(p) + (1-y)*log(1-p)); clip p away from 0 and 1 for stability
    3. Gradients have the same shape as linear regression but use sigmoid output: dw = X.T @ (p - y) / n

Learn:
    # Stable sigmoid:
    def sigmoid(z):
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    # Binary cross-entropy:
    p = np.clip(predictions, 1e-15, 1 - 1e-15)
    loss = -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))

    # Gradient (same form as linear regression):
    dw = (1/n) * X.T @ (p - y)
"""

import numpy as np


class LogisticRegression:
    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.losses = []

    def sigmoid(self, z: np.ndarray) -> np.ndarray:
        """Numerically stable sigmoid."""
        # YOUR CODE HERE
        pass

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LogisticRegression":
        """Train using gradient descent with binary cross-entropy loss."""
        # YOUR CODE HERE
        pass

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Return probability of class 1."""
        # YOUR CODE HERE
        pass

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """Return binary predictions."""
        # YOUR CODE HERE
        pass

    def accuracy(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Compute accuracy."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.randn(200, 2)
    y = (X[:, 0] + X[:, 1] > 0).astype(float)

    model = LogisticRegression(learning_rate=0.1, n_iterations=1000)
    model.fit(X, y)

    preds = model.predict(X)
    acc = model.accuracy(y, preds)
    assert acc > 0.90, f"Accuracy too low: {acc}"
    assert model.losses[-1] < model.losses[0]

    proba = model.predict_proba(X)
    assert np.all(proba >= 0) and np.all(proba <= 1)
    print(f"✅ All tests passed! Accuracy = {acc:.4f}")
