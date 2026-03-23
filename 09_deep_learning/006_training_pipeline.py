"""
Challenge: Complete Training Pipeline
Difficulty: ⭐⭐⭐ Hard
Topic: PyTorch, Training, Validation, Checkpointing

Build a complete training pipeline with best practices.

Hints:
    1. Call model.train() before training and model.eval() before validation to set the correct mode
    2. Wrap validation in torch.no_grad() to disable gradient computation and save memory
    3. Save checkpoints with torch.save({'model': model.state_dict(), 'epoch': epoch}, path)

Learn:
    # Training epoch:
    model.train()
    for batch_X, batch_y in train_loader:
        pred = model(batch_X)
        loss = criterion(pred, batch_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Validation (no gradients):
    model.eval()
    with torch.no_grad():
        for batch_X, batch_y in val_loader:
            pred = model(batch_X)

    # Save/load checkpoint:
    torch.save({"model": model.state_dict(), "epoch": epoch}, path)
    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint["model"])
"""

import torch
import torch.nn as nn
import torch.optim as optim
from pathlib import Path
import tempfile


class Trainer:
    """Complete training pipeline with:
    - Training loop with batching
    - Validation after each epoch
    - Early stopping
    - Model checkpointing (save best model)
    - Learning rate scheduling
    """

    def __init__(self, model: nn.Module, optimizer: optim.Optimizer,
                 criterion: nn.Module, device: str = "cpu"):
        self.model = model.to(device)
        self.optimizer = optimizer
        self.criterion = criterion
        self.device = device
        self.train_losses = []
        self.val_losses = []
        self.best_val_loss = float("inf")

    def train_epoch(self, dataloader) -> float:
        """Run one training epoch. Return average loss."""
        # YOUR CODE HERE
        pass

    def validate(self, dataloader) -> float:
        """Run validation. Return average loss."""
        # YOUR CODE HERE
        pass

    def fit(self, train_loader, val_loader, epochs: int = 10,
            patience: int = 5, save_path: Path = None) -> dict:
        """Full training loop with early stopping.
        Return dict with train_losses, val_losses, best_epoch.
        """
        # YOUR CODE HERE
        pass

    def save_checkpoint(self, path: Path, epoch: int) -> None:
        """Save model checkpoint."""
        # YOUR CODE HERE
        pass

    def load_checkpoint(self, path: Path) -> int:
        """Load model checkpoint. Return the epoch number."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    torch.manual_seed(42)

    # Create simple dataset
    X = torch.randn(200, 10)
    y = (X[:, 0] + X[:, 1] > 0).float().unsqueeze(1)

    train_dataset = torch.utils.data.TensorDataset(X[:160], y[:160])
    val_dataset = torch.utils.data.TensorDataset(X[160:], y[160:])
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=32)

    # Create model and trainer
    model = nn.Sequential(nn.Linear(10, 32), nn.ReLU(), nn.Linear(32, 1), nn.Sigmoid())
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.BCELoss()
    trainer = Trainer(model, optimizer, criterion)

    with tempfile.TemporaryDirectory() as tmpdir:
        save_path = Path(tmpdir) / "best_model.pt"
        results = trainer.fit(train_loader, val_loader, epochs=20,
                              patience=10, save_path=save_path)

        assert "train_losses" in results
        assert "val_losses" in results
        assert len(results["train_losses"]) > 0
        assert results["train_losses"][-1] < results["train_losses"][0]

        # Test checkpoint
        if save_path.exists():
            epoch = trainer.load_checkpoint(save_path)
            assert epoch >= 0
    print("✅ All tests passed!")
