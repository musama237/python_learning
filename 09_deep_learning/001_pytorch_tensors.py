"""
Challenge: PyTorch Tensor Operations
Difficulty: ⭐ Easy
Topic: PyTorch, Tensors, GPU

Master PyTorch tensor operations — the building blocks of deep learning.

Hints:
    1. Use torch.zeros(), torch.ones(), torch.randn(), torch.arange(), and torch.eye() to create different tensor types
    2. Reshape tensors with .view() or .reshape(); use .unsqueeze() to add dimensions
    3. Boolean indexing works like NumPy: x[x > 0] returns all positive elements as a 1D tensor

Learn:
    import torch
    torch.zeros(3, 4)          # 3x4 zeros
    torch.randn(5, 5)          # random normal
    torch.arange(10)           # [0, 1, ..., 9]
    x.reshape(3, 4)            # reshape
    x.unsqueeze(0)             # add dimension: (12,) -> (1, 12)
    x[x > 0]                   # boolean indexing
    torch.softmax(x, dim=1)    # softmax along columns
    x.T                        # transpose
"""

import torch


def create_tensors() -> dict[str, torch.Tensor]:
    """Create and return various tensors:
    - 'zeros': 3x4 zero tensor
    - 'ones': 2x3 ones tensor
    - 'random': 5x5 random normal tensor
    - 'range': tensor [0, 1, 2, ..., 9]
    - 'eye': 4x4 identity matrix
    """
    # YOUR CODE HERE
    pass


def tensor_operations(a: torch.Tensor, b: torch.Tensor) -> dict[str, torch.Tensor]:
    """Perform operations and return dict with:
    - 'add': element-wise addition
    - 'matmul': matrix multiplication
    - 'transpose': transpose of a
    - 'mean': mean of a per column (dim=0)
    - 'softmax': softmax of a along dim=1
    """
    # YOUR CODE HERE
    pass


def reshape_operations(x: torch.Tensor) -> dict[str, torch.Tensor]:
    """Given a 1D tensor of size 12, return:
    - 'matrix': reshaped to 3x4
    - 'cube': reshaped to 2x2x3
    - 'flat': flattened back to 1D
    - 'unsqueezed': add batch dimension -> 1x12
    """
    # YOUR CODE HERE
    pass


def indexing_operations(x: torch.Tensor) -> dict:
    """Given a 5x5 tensor, return:
    - 'row_0': first row
    - 'col_2': third column
    - 'diagonal': diagonal elements
    - 'masked': elements > 0 (1D tensor of positive values)
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    tensors = create_tensors()
    assert tensors["zeros"].shape == (3, 4)
    assert tensors["ones"].sum() == 6
    assert tensors["range"].shape == (10,)
    assert tensors["eye"].sum() == 4

    a = torch.randn(3, 4)
    b = torch.randn(4, 5)
    ops = tensor_operations(a, b)
    assert ops["matmul"].shape == (3, 5)
    assert ops["transpose"].shape == (4, 3)
    assert ops["mean"].shape == (4,)
    assert torch.allclose(ops["softmax"].sum(dim=1), torch.ones(3), atol=1e-5)

    x = torch.arange(12, dtype=torch.float)
    reshaped = reshape_operations(x)
    assert reshaped["matrix"].shape == (3, 4)
    assert reshaped["cube"].shape == (2, 2, 3)
    assert reshaped["flat"].shape == (12,)
    assert reshaped["unsqueezed"].shape == (1, 12)

    y = torch.randn(5, 5)
    idx = indexing_operations(y)
    assert idx["row_0"].shape == (5,)
    assert idx["col_2"].shape == (5,)
    assert idx["diagonal"].shape == (5,)
    print("✅ All tests passed!")
