"""
Challenge: Recurrent Neural Networks
Difficulty: ⭐⭐⭐ Hard
Topic: PyTorch, RNN, LSTM, Sequence Models

Build RNN/LSTM models for sequence data.
"""

import torch
import torch.nn as nn


class SimpleRNN(nn.Module):
    """RNN cell implemented from scratch (no nn.RNN).
    h_t = tanh(W_ih @ x_t + W_hh @ h_{t-1} + bias)
    """

    def __init__(self, input_size: int, hidden_size: int):
        super().__init__()
        # YOUR CODE HERE - define weight matrices
        pass

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """x shape: (batch, seq_len, input_size)
        Return (output, h_final) where:
        - output: all hidden states (batch, seq_len, hidden_size)
        - h_final: last hidden state (batch, hidden_size)
        """
        # YOUR CODE HERE
        pass


class LSTMClassifier(nn.Module):
    """LSTM-based sequence classifier using nn.LSTM.
    Architecture: Embedding -> LSTM -> Linear
    """

    def __init__(self, vocab_size: int, embed_dim: int, hidden_dim: int,
                 num_classes: int, num_layers: int = 1):
        super().__init__()
        # YOUR CODE HERE
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x shape: (batch, seq_len) of integer token indices.
        Return logits of shape (batch, num_classes).
        Use the last hidden state for classification.
        """
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    torch.manual_seed(42)

    # Test SimpleRNN
    rnn = SimpleRNN(input_size=10, hidden_size=20)
    x = torch.randn(4, 5, 10)  # batch=4, seq=5, features=10
    output, h_final = rnn(x)
    assert output.shape == (4, 5, 20)
    assert h_final.shape == (4, 20)
    assert torch.allclose(output[:, -1, :], h_final)

    # Test LSTMClassifier
    lstm = LSTMClassifier(vocab_size=1000, embed_dim=32, hidden_dim=64,
                          num_classes=5, num_layers=2)
    tokens = torch.randint(0, 1000, (8, 20))  # batch=8, seq=20
    logits = lstm(tokens)
    assert logits.shape == (8, 5)

    n_params = sum(p.numel() for p in lstm.parameters())
    assert n_params > 0
    print(f"✅ All tests passed! LSTM params: {n_params:,}")
