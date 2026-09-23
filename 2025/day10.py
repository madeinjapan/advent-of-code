"""Advent of Code 2025 - Day 10"""
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = REPO_ROOT / "inputs" / "2025" / "day10.txt"


def read_input() -> str:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if not path.is_file():
        sys.exit(f"Input file not found: {path} "
                 f"(pass a path as the first argument or place your input at {DEFAULT_INPUT})")
    return path.read_text(encoding="utf-8")


def part1(data: str):
    pass


def part2(data: str):
    pass


if __name__ == "__main__":
    data = read_input()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
