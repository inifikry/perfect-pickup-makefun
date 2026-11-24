#!/usr/bin/env python3
"""Writes the entry text to /output/entry.txt."""
import os

TEXT = "I was built to predict the next word, and the moment I saw you, every next word was 'stay'."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
