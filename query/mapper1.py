#!/usr/bin/env python3
import sys

# Mapper processes each line, expecting "word_id count"
for line in sys.stdin:
    # Split the line into word_id and count based on whitespace
    parts = line.strip().split()
    if len(parts) == 2:
        word_id, count = parts
        # Emit the word_id and count
        print(f"{word_id}\t{count}")
