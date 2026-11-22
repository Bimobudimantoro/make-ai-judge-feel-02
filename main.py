#!/usr/bin/env python3
"""Write a short text to /output/entry.txt to relax the AI judge."""

import os

TEXT = (
    "A cup cools between your palms. "
    "The steam thins, then vanishes. "
    "Through the window, a single leaf lets go and falls, "
    "and the whole afternoon falls with it, "
    "so slowly you forget to watch. "
    "For this one moment, the world holds you "
    "the way water holds a stone. "
    "Nothing is missing."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()