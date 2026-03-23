"""
Challenge: Neural Network from Scratch
Difficulty: ⭐⭐⭐ Hard
Topic: ML, Neural Networks, Backpropagation

Implement a simple feedforward neural network with:
- Configurable layers
- ReLU and Sigmoid activations
- Binary cross-entropy loss
- Backpropagation

No PyTorch or TensorFlow — NumPy only!
"""

import numpy as np


class NeuralNetwork:
    def __init__(self, layer_sizes: list[int], learning_rate: float = 0.01):
        """layer_sizes: e.g., [2, 4, 1] means 2 inputs, 4 hidden, 1 output."""
        self.lr = learning_rate
        self.weights = []
        self.biases = []
        self.losses = []

        # Initialize weights (Xavier initialization)
        np.random.seed(42)
        for i in range(len(layer_sizes) - 1):
            w = np.random.randn(layer_sizes[i], layer_sizes[i + 1]) * np.sqrt(2.0 / layer_sizes[i])
            b = np.zeros((1, layer_sizes[i + 1]))
            self.weights.append(w)
            self.biases.append(b)

    def relu(self, z: np.ndarray) -> np.ndarray:
        # YOUR CODE HERE
        pass

    def relu_derivative(self, z: np.ndarray) -> np.ndarray:
        # YOUR CODE HERE
        pass

    def sigmoid(self, z: np.ndarray) -> np.ndarray:
        # YOUR CODE HERE
        pass

    def forward(self, X: np.ndarray) -> tuple[list, list]:
        """Forward pass. Return (activations, pre_activations) for backprop."""
        # YOUR CODE HERE
        pass

    def backward(self, X: np.ndarray, y: np.ndarray, activations: list, pre_activations: list) -> None:
        """Backpropagation: compute gradients and update weights."""
        # YOUR CODE HERE
        pass

    def fit(self, X: np.ndarray, y: np.ndarray, epochs: int = 100) -> "NeuralNetwork":
        """Train the network."""
        # YOUR CODE HERE
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Return binary predictions (0 or 1)."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    np.random.seed(42)

    # XOR problem — not linearly separable
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    nn = NeuralNetwork([2, 8, 1], learning_rate=0.5)
    nn.fit(X, y, epochs=2000)

    preds = nn.predict(X)
    accuracy = (preds == y).mean()
    assert accuracy >= 0.75, f"Can't solve XOR: accuracy = {accuracy}"
    assert nn.losses[-1] < nn.losses[0]
    print(f"✅ All tests passed! XOR accuracy = {accuracy:.2f}")
