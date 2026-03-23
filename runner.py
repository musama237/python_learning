"""
Python Learning Challenge Runner
================================
Run this script to see your progress across all challenges.

Usage:
    python runner.py              # Show progress dashboard
    python runner.py --level 01   # Show progress for a specific level
    python runner.py --run all    # Run all challenges and update progress
    python runner.py --run 01     # Run all challenges in level 01
    python runner.py --next       # Show your next unsolved challenge
"""

import json
import subprocess
import sys
import io
from pathlib import Path

# Fix Windows console encoding for emoji/unicode
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).parent
PROGRESS_FILE = BASE_DIR / "progress.json"

LEVELS = {
    "01_basics": "Python Basics",
    "02_data_structures": "Data Structures",
    "03_functions": "Functions & Functional Programming",
    "04_oop": "Object-Oriented Programming",
    "05_algorithms": "Algorithms & Problem Solving",
    "06_advanced_python": "Advanced Python",
    "07_data_wrangling": "Data Wrangling (NumPy/Pandas)",
    "08_ml_fundamentals": "ML Fundamentals",
    "09_deep_learning": "Deep Learning (PyTorch)",
    "10_real_world": "Real-World Projects",
}

DIFFICULTY_ICONS = {
    "Easy": "⭐",
    "Medium": "⭐⭐",
    "Hard": "⭐⭐⭐",
    "Extreme": "💀",
}


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {}


def save_progress(progress: dict) -> None:
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2))


def get_challenges(level_filter: str | None = None) -> list[Path]:
    challenges = []
    for level_dir in sorted(BASE_DIR.iterdir()):
        if not level_dir.is_dir() or not level_dir.name[0].isdigit():
            continue
        if level_filter and not level_dir.name.startswith(level_filter):
            continue
        for f in sorted(level_dir.glob("*.py")):
            challenges.append(f)
    return challenges


def extract_difficulty(filepath: Path) -> str:
    text = filepath.read_text(encoding="utf-8")
    for diff in ["Extreme", "Hard", "Medium", "Easy"]:
        if diff in text:
            return diff
    return "Unknown"


def run_challenge(filepath: Path) -> bool:
    try:
        result = subprocess.run(
            [sys.executable, str(filepath)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0 and "All tests passed" in result.stdout
    except (subprocess.TimeoutExpired, Exception):
        return False


def show_progress(level_filter: str | None = None) -> None:
    progress = load_progress()
    challenges = get_challenges(level_filter)

    if not challenges:
        print("No challenges found.")
        return

    current_level = None
    total_passed = 0
    total_count = 0
    level_counts: dict[str, list[int]] = {}

    print("\n" + "=" * 60)
    print("  🐍 PYTHON LEARNING CHALLENGES - PROGRESS DASHBOARD")
    print("=" * 60)

    for ch in challenges:
        level = ch.parent.name
        if level != current_level:
            if current_level is not None:
                print()
            current_level = level
            level_name = LEVELS.get(level, level)
            print(f"\n📂 {level_name}")
            print("-" * 50)
            level_counts[level] = [0, 0]

        name = ch.stem
        difficulty = extract_difficulty(ch)
        icon = DIFFICULTY_ICONS.get(difficulty, "?")
        passed = progress.get(str(ch.relative_to(BASE_DIR)), False)

        status = "✅" if passed else "⬜"
        print(f"  {status} {name:<45} {icon}")

        total_count += 1
        level_counts[level][1] += 1
        if passed:
            total_passed += 1
            level_counts[level][0] += 1

    print("\n" + "=" * 60)
    print("  📊 SUMMARY")
    print("=" * 60)
    for level, (passed, total) in level_counts.items():
        level_name = LEVELS.get(level, level)
        bar_len = 20
        filled = int(bar_len * passed / total) if total > 0 else 0
        bar = "█" * filled + "░" * (bar_len - filled)
        pct = (passed / total * 100) if total > 0 else 0
        print(f"  {level_name:<40} {bar} {passed}/{total} ({pct:.0f}%)")

    print(f"\n  🏆 Total: {total_passed}/{total_count} challenges completed")
    pct = (total_passed / total_count * 100) if total_count > 0 else 0
    print(f"  📈 Overall progress: {pct:.1f}%\n")


def run_all(level_filter: str | None = None) -> None:
    progress = load_progress()
    challenges = get_challenges(level_filter)

    print("\n🔄 Running challenges...\n")
    for ch in challenges:
        key = str(ch.relative_to(BASE_DIR))
        passed = run_challenge(ch)
        progress[key] = passed
        status = "✅" if passed else "❌"
        print(f"  {status} {ch.stem}")

    save_progress(progress)
    print("\n✔ Progress saved!")
    show_progress(level_filter)


def show_next() -> None:
    progress = load_progress()
    challenges = get_challenges()

    for ch in challenges:
        key = str(ch.relative_to(BASE_DIR))
        if not progress.get(key, False):
            difficulty = extract_difficulty(ch)
            icon = DIFFICULTY_ICONS.get(difficulty, "?")
            level_name = LEVELS.get(ch.parent.name, ch.parent.name)
            print(f"\n👉 Next challenge: {ch.stem}")
            print(f"   Level: {level_name}")
            print(f"   Difficulty: {icon} {difficulty}")
            print(f"   File: {ch}")
            print(f"\n   Open it, write your solution, then run:")
            print(f"   python {ch.relative_to(BASE_DIR)}\n")
            return

    print("\n🎉 You've completed ALL challenges! Amazing work!\n")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        show_progress()
    elif "--next" in args:
        show_next()
    elif "--run" in args:
        idx = args.index("--run")
        level = args[idx + 1] if idx + 1 < len(args) else None
        if level == "all":
            level = None
        run_all(level)
    elif "--level" in args:
        idx = args.index("--level")
        level = args[idx + 1] if idx + 1 < len(args) else None
        show_progress(level)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
