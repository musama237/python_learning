"""
Challenge: Custom Dataset & DataLoader
Difficulty: ⭐⭐ Medium
Topic: PyTorch, Dataset, DataLoader, Transforms

Create custom datasets and understand the data loading pipeline.

Hints:
    1. __getitem__ should return a (tensor_x, tensor_y) tuple; convert numpy arrays to tensors there
    2. Convert numpy to torch tensors inside __getitem__ using torch.from_numpy() or torch.tensor()
    3. Use torch.utils.data.random_split to divide a dataset into train/val splits
"""

import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np


class NumpyDataset(Dataset):
    """Custom dataset from NumPy arrays.
    Supports optional transform function.
    """

    def __init__(self, X: np.ndarray, y: np.ndarray, transform=None):
        # YOUR CODE HERE
        pass

    def __len__(self) -> int:
        # YOUR CODE HERE
        pass

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        # YOUR CODE HERE - apply transform if provided
        pass


class SyntheticClassificationDataset(Dataset):
    """Generate synthetic classification data on-the-fly.
    Creates n_samples points in n_features dimensions with n_classes classes.
    """

    def __init__(self, n_samples: int = 1000, n_features: int = 10,
                 n_classes: int = 2, seed: int = 42):
        # YOUR CODE HERE - generate data using torch
        pass

    def __len__(self) -> int:
        # YOUR CODE HERE
        pass

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        # YOUR CODE HERE
        pass


def create_dataloaders(dataset: Dataset, batch_size: int = 32,
                       train_ratio: float = 0.8) -> tuple[DataLoader, DataLoader]:
    """Split dataset into train/val and create DataLoaders.
    Train loader should shuffle, val loader should not.
    Return (train_loader, val_loader).
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test NumpyDataset
    X = np.random.randn(100, 5).astype(np.float32)
    y = np.random.randint(0, 2, 100).astype(np.int64)

    dataset = NumpyDataset(X, y)
    assert len(dataset) == 100
    x_sample, y_sample = dataset[0]
    assert isinstance(x_sample, torch.Tensor)
    assert x_sample.shape == (5,)

    # With transform
    normalize = lambda x: (x - x.mean()) / (x.std() + 1e-8)
    dataset_t = NumpyDataset(X, y, transform=normalize)
    x_t, _ = dataset_t[0]
    assert isinstance(x_t, torch.Tensor)

    # Test SyntheticClassificationDataset
    syn = SyntheticClassificationDataset(n_samples=500, n_features=10, n_classes=3)
    assert len(syn) == 500
    x_syn, y_syn = syn[0]
    assert x_syn.shape == (10,)

    # Test DataLoader creation
    train_loader, val_loader = create_dataloaders(dataset, batch_size=16)
    train_batch = next(iter(train_loader))
    assert train_batch[0].shape[0] == 16
    assert len(train_loader.dataset) + len(val_loader.dataset) == 100
    print("✅ All tests passed!")
