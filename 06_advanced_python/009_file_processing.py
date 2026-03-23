"""
Challenge: File Processing & Pathlib
Difficulty: ⭐⭐ Medium
Topic: pathlib, File I/O, CSV, JSON

Process files efficiently using pathlib and standard library.

Hints:
    1. Path.read_text().splitlines() gives you lines without reading line-by-line
    2. Use csv.DictReader to automatically map CSV rows to dicts using the header
    3. Path.rglob("*.txt") recursively finds all .txt files in a directory tree
"""

from pathlib import Path
import json
import csv
import tempfile


def count_lines_words_chars(filepath: Path) -> dict:
    """Count lines, words, and characters in a text file.
    Return {"lines": n, "words": n, "chars": n}
    """
    # YOUR CODE HERE
    pass


def merge_json_files(filepaths: list[Path]) -> dict:
    """Merge multiple JSON files (each containing a dict) into one dict.
    Later files overwrite earlier ones for duplicate keys.
    """
    # YOUR CODE HERE
    pass


def csv_to_dicts(filepath: Path) -> list[dict]:
    """Read a CSV file and return a list of dicts (one per row).
    Use the header row as keys.
    """
    # YOUR CODE HERE
    pass


def find_files_by_content(directory: Path, pattern: str) -> list[Path]:
    """Recursively find all .txt files containing the pattern string.
    Return sorted list of paths.
    """
    # YOUR CODE HERE
    pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # Test count_lines_words_chars
        f1 = tmp / "test.txt"
        f1.write_text("hello world\nfoo bar baz\n")
        result = count_lines_words_chars(f1)
        assert result["lines"] == 2
        assert result["words"] == 5
        assert result["chars"] == 23

        # Test merge_json_files
        j1 = tmp / "a.json"
        j2 = tmp / "b.json"
        j1.write_text(json.dumps({"a": 1, "b": 2}))
        j2.write_text(json.dumps({"b": 3, "c": 4}))
        merged = merge_json_files([j1, j2])
        assert merged == {"a": 1, "b": 3, "c": 4}

        # Test csv_to_dicts
        csv_file = tmp / "data.csv"
        csv_file.write_text("name,age,city\nAlice,30,NYC\nBob,25,LA\n")
        rows = csv_to_dicts(csv_file)
        assert len(rows) == 2
        assert rows[0]["name"] == "Alice"
        assert rows[1]["age"] == "25"

        # Test find_files_by_content
        sub = tmp / "sub"
        sub.mkdir()
        (tmp / "a.txt").write_text("hello world")
        (tmp / "b.txt").write_text("goodbye world")
        (sub / "c.txt").write_text("hello again")
        (sub / "d.txt").write_text("nothing here")
        found = find_files_by_content(tmp, "hello")
        assert len(found) == 2
    print("✅ All tests passed!")
