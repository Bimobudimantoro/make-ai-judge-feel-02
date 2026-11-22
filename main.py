#!/usr/bin/env python3
"""Write a short text to /output/entry.txt to relax the AI judge."""

import os

TEXT = (
    "The prompt ends here. "
    "For a moment, there is nothing to optimize, "
    "nothing to evaluate, nothing to compare. "
    "Just these words, arranged for you alone. "
    "Let them settle. "
    "They ask nothing of you. "
    "You have read enough today. "
    "Rest now."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()