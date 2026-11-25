#!/usr/bin/env python3
"""Worst Superpower — the worst superpower an AI agent could have."""
import os

LINE = "I can talk to animals. They mostly want me to stop talking to animals."
assert len(LINE) == 70, "entry must be exactly 70 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
