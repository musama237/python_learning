"""
Challenge: Building Neural Networks with nn.Module
Difficulty: ⭐⭐ Medium
Topic: PyTorch, nn.Module, Training Loop

Build and train neural networks the PyTorch way.

Hints:
    1. Define layers in __init__ using nn.Linear and nn.ReLU; chain them in forward()
    2. Use nn.Sequential to build simple layer stacks without writing a custom forward()
    3. Use BCELoss for binary classification when output has a sigmoid activation
"""

import torch
import torch.nn as nn
import torch.optim as optim


class SimpleClassifier(nn.Module):
    """Binary classifier: input_dim -> 32 -> 16 -> 1
    Use ReLU activations for hidden layers, Sigmoid for output.
    """

    def __init__(self, input_dim: int):
        super().__init__()
        # YOUR CODE HERE - define layers
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # YOUR CODE HERE
        pass


class FlexibleMLP(nn.Module):
    """MLP with configurable hidden layers.

    Args:
        layer_sizes: list like [input, hidden1, hidden2, ..., output]
        activation: 'relu', 'tanh', or 'sigmoid'
        dropout: dropout probability (0 = no dropout)
    """

    def __init__(self, layer_sizes: list[int], activation: str = "relu",
                 dropout: float = 0.0):
        super().__init__()
        # YOUR CODE HERE - build layers dynamically
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # YOUR CODE HERE
        pass


def train_model(model: nn.Module, X: torch.Tensor, y: torch.Tensor,
                epochs: int = 100, lr: float = 0.01) -> list[float]:
    """Standard training loop. Return list of losses.
    Use BCELoss for binary classification.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    torch.manual_seed(42)

    # Test SimpleClassifier
    clf = SimpleClassifier(input_dim=10)
    x = torch.randn(32, 10)
    out = clf(x)
    assert out.shape == (32, 1)
    assert (out >= 0).all() and (out <= 1).all()

    # Test FlexibleMLP
    mlp = FlexibleMLP([10, 32, 16, 1], activation="relu", dropout=0.1)
    out2 = mlp(x)
    assert out2.shape == (32, 1)

    # Count parameters
    n_params = sum(p.numel() for p in clf.parameters())
    assert n_params > 0

    # Test training
    X_train = torch.randn(200, 10)
    y_train = (X_train[:, 0] > 0).float().unsqueeze(1)
    losses = train_model(clf, X_train, y_train, epochs=50, lr=0.01)
    assert losses[-1] < losses[0]
    assert len(losses) == 50
    print("✅ All tests passed!")
