"""
Challenge: Convolutional Neural Networks
Difficulty: ⭐⭐⭐ Hard
Topic: PyTorch, CNN, Image Classification

Build CNN architectures for image data.
"""

import torch
import torch.nn as nn


class SimpleCNN(nn.Module):
    """CNN for 1-channel 28x28 images (like MNIST).
    Architecture:
    - Conv(1, 16, 3, padding=1) -> ReLU -> MaxPool(2)
    - Conv(16, 32, 3, padding=1) -> ReLU -> MaxPool(2)
    - Flatten -> Linear(32*7*7, 128) -> ReLU -> Linear(128, num_classes)
    """

    def __init__(self, num_classes: int = 10):
        super().__init__()
        # YOUR CODE HERE
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # YOUR CODE HERE
        pass


class ResidualBlock(nn.Module):
    """A residual block: output = relu(x + conv(relu(conv(x))))
    Both convolutions preserve spatial dimensions (padding=1, kernel=3).
    """

    def __init__(self, channels: int):
        super().__init__()
        # YOUR CODE HERE
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # YOUR CODE HERE
        pass


class MiniResNet(nn.Module):
    """Mini ResNet: Conv -> 2 ResidualBlocks -> Global AvgPool -> Linear
    Input: 3-channel 32x32 images (like CIFAR).
    """

    def __init__(self, num_classes: int = 10):
        super().__init__()
        # YOUR CODE HERE
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test SimpleCNN
    cnn = SimpleCNN(num_classes=10)
    x_mnist = torch.randn(4, 1, 28, 28)
    out = cnn(x_mnist)
    assert out.shape == (4, 10), f"Expected (4, 10), got {out.shape}"

    # Test ResidualBlock
    res_block = ResidualBlock(32)
    x_res = torch.randn(2, 32, 16, 16)
    out_res = res_block(x_res)
    assert out_res.shape == (2, 32, 16, 16)

    # Test MiniResNet
    resnet = MiniResNet(num_classes=10)
    x_cifar = torch.randn(4, 3, 32, 32)
    out_resnet = resnet(x_cifar)
    assert out_resnet.shape == (4, 10), f"Expected (4, 10), got {out_resnet.shape}"

    # Count parameters
    n_params = sum(p.numel() for p in resnet.parameters())
    assert n_params > 100, "Model seems too small"
    print(f"✅ All tests passed! MiniResNet params: {n_params:,}")
