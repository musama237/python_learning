"""
Challenge: CLI Tool Framework
Difficulty: ⭐⭐ Medium
Topic: argparse, CLI, Text Processing

Build a mini command-line tool framework that supports:
- Subcommands
- Arguments and flags
- Colored output helpers
- Progress display

No external dependencies — stdlib only.

Hints:
    1. Use argparse.ArgumentParser with add_subparsers()
    2. Capture stdout with contextlib.redirect_stdout(StringIO())
    3. TextTable: calculate column widths as max of header/data lengths
    4. ProgressBar: filled = int(width * current / total)

Learn:
    import argparse
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    greet_parser = sub.add_parser("greet")
    greet_parser.add_argument("name")
    args = parser.parse_args(["greet", "World"])

    # Capture print output:
    from io import StringIO
    from contextlib import redirect_stdout
    buf = StringIO()
    with redirect_stdout(buf):
        print("hello")
    output = buf.getvalue()  # -> "hello\n"
"""

import argparse
import sys
from io import StringIO


class CLI:
    """Simple CLI framework with subcommand support."""

    def __init__(self, name: str, description: str):
        # YOUR CODE HERE
        pass

    def command(self, name: str, help: str = ""):
        """Decorator to register a subcommand.

        Usage:
            @cli.command("greet", help="Greet someone")
            def greet(args):
                print(f"Hello, {args.name}!")
        """
        # YOUR CODE HERE
        pass

    def add_argument(self, command_name: str, *args, **kwargs):
        """Add argument to a specific subcommand."""
        # YOUR CODE HERE
        pass

    def run(self, argv: list[str] = None) -> str:
        """Parse args and execute the command. Return command output."""
        # YOUR CODE HERE
        pass


class TextTable:
    """Simple ASCII table formatter."""

    def __init__(self, headers: list[str]):
        # YOUR CODE HERE
        pass

    def add_row(self, row: list) -> None:
        # YOUR CODE HERE
        pass

    def render(self) -> str:
        """Render as formatted ASCII table with borders."""
        # YOUR CODE HERE
        pass


class ProgressBar:
    """Simple text progress bar."""

    def __init__(self, total: int, width: int = 40):
        # YOUR CODE HERE
        pass

    def update(self, current: int) -> str:
        """Return progress bar string like: [████████░░░░░░░░] 50% (50/100)"""
        # YOUR CODE HERE
        pass


# --- Tests (do not modify) ---
if __name__ == "__main__":
    # Test CLI
    cli = CLI("test-app", "A test CLI app")

    @cli.command("greet", help="Greet someone")
    def greet(args):
        print(f"Hello, {args.name}!")

    cli.add_argument("greet", "name", help="Name to greet")

    output = cli.run(["greet", "World"])
    assert "Hello, World!" in output

    # Test TextTable
    table = TextTable(["Name", "Age", "City"])
    table.add_row(["Alice", 30, "NYC"])
    table.add_row(["Bob", 25, "LA"])
    rendered = table.render()
    assert "Alice" in rendered
    assert "Bob" in rendered
    assert "Name" in rendered
    lines = rendered.strip().split("\n")
    assert len(lines) >= 4  # Header + separator + 2 data rows

    # Test ProgressBar
    pb = ProgressBar(100, width=20)
    bar_0 = pb.update(0)
    assert "0%" in bar_0
    bar_50 = pb.update(50)
    assert "50%" in bar_50
    bar_100 = pb.update(100)
    assert "100%" in bar_100
    print("✅ All tests passed!")
