"""
Challenge: Attention & Transformer Basics
Difficulty: 💀 Extreme
Topic: PyTorch, Attention, Transformer

Implement attention mechanisms from scratch.

Hints:
    1. Attention scores = QK^T / sqrt(d_k); apply mask by setting masked positions to -inf before softmax, then multiply by V
    2. Multi-head: split d_model into n_heads, apply attention to each head independently, then concatenate
    3. Transformer block: self-attention + residual + LayerNorm, then FFN + residual + LayerNorm
"""

import torch
import torch.nn as nn
import math


class ScaledDotProductAttention(nn.Module):
    """Implement scaled dot-product attention from scratch.
    Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
    """

    def forward(self, Q: torch.Tensor, K: torch.Tensor,
                V: torch.Tensor, mask: torch.Tensor = None) -> torch.Tensor:
        """
        Q, K, V shape: (batch, seq_len, d_model)
        mask: optional (batch, 1, seq_len) or (batch, seq_len, seq_len)
        Return: (batch, seq_len, d_model)
        """
        # YOUR CODE HERE
        pass


class MultiHeadAttention(nn.Module):
    """Multi-head attention: split d_model into n_heads, apply attention, concat."""

    def __init__(self, d_model: int, n_heads: int):
        super().__init__()
        assert d_model % n_heads == 0
        # YOUR CODE HERE
        pass

    def forward(self, Q: torch.Tensor, K: torch.Tensor,
                V: torch.Tensor, mask: torch.Tensor = None) -> torch.Tensor:
        # YOUR CODE HERE
        pass


class TransformerBlock(nn.Module):
    """Single transformer encoder block:
    1. Multi-head self-attention + residual + LayerNorm
    2. Feed-forward network + residual + LayerNorm
    """

    def __init__(self, d_model: int, n_heads: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        # YOUR CODE HERE
        pass

    def forward(self, x: torch.Tensor, mask: torch.Tensor = None) -> torch.Tensor:
        # YOUR CODE HERE
        pass


class PositionalEncoding(nn.Module):
    """Add positional encoding to embeddings.
    PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
    PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
    """

    def __init__(self, d_model: int, max_len: int = 5000):
        super().__init__()
        # YOUR CODE HERE - precompute PE matrix
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x shape: (batch, seq_len, d_model)"""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    torch.manual_seed(42)
    batch, seq_len, d_model = 2, 10, 64

    # Test Scaled Dot-Product Attention
    attn = ScaledDotProductAttention()
    Q = K = V = torch.randn(batch, seq_len, d_model)
    out = attn(Q, K, V)
    assert out.shape == (batch, seq_len, d_model)

    # Test with mask
    mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
    mask = mask.unsqueeze(0)  # (1, seq_len, seq_len)
    out_masked = attn(Q, K, V, mask=mask)
    assert out_masked.shape == (batch, seq_len, d_model)

    # Test Multi-Head Attention
    mha = MultiHeadAttention(d_model=64, n_heads=8)
    out_mha = mha(Q, K, V)
    assert out_mha.shape == (batch, seq_len, d_model)

    # Test Transformer Block
    block = TransformerBlock(d_model=64, n_heads=8, d_ff=256)
    out_block = block(Q)
    assert out_block.shape == (batch, seq_len, d_model)

    # Test Positional Encoding
    pe = PositionalEncoding(d_model=64)
    x = torch.randn(batch, seq_len, d_model)
    out_pe = pe(x)
    assert out_pe.shape == (batch, seq_len, d_model)
    assert not torch.allclose(x, out_pe)  # PE should change values
    print("✅ All tests passed!")
