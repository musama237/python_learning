"""
Challenge: Trie (Prefix Tree)
Difficulty: ⭐⭐⭐ Hard
Topic: Trees, Strings, Autocomplete

Implement a Trie that supports insert, search, startsWith, and autocomplete.

Example:
    trie = Trie()
    trie.insert("apple")
    trie.search("apple") -> True
    trie.starts_with("app") -> True
    trie.autocomplete("app") -> ["apple"]
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        # YOUR CODE HERE
        pass

    def insert(self, word: str) -> None:
        # YOUR CODE HERE
        pass

    def search(self, word: str) -> bool:
        """Return True if exact word exists."""
        # YOUR CODE HERE
        pass

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word starts with prefix."""
        # YOUR CODE HERE
        pass

    def autocomplete(self, prefix: str) -> list[str]:
        """Return all words that start with prefix, sorted."""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("application")
    trie.insert("banana")

    assert trie.search("apple") is True
    assert trie.search("app") is True
    assert trie.search("ap") is False
    assert trie.starts_with("app") is True
    assert trie.starts_with("ban") is True
    assert trie.starts_with("xyz") is False

    auto = trie.autocomplete("app")
    assert sorted(auto) == ["app", "apple", "application"]
    assert trie.autocomplete("ban") == ["banana"]
    assert trie.autocomplete("xyz") == []
    print("✅ All tests passed!")
