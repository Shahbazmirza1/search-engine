#!/usr/bin/env python3
import sys
import re
import ast

for line in sys.stdin:
    # The line format is: (article_id:,[('word_id', count), ...])
    # First, isolate the article_id and the list part
    article_id, word_list_str = re.match(r"\((\d+):,\[(.*)\]\)", line.strip()).groups()
    
    # Convert the list part from string to an actual list of tuples
    # Using `ast.literal_eval` for safely evaluating a string containing a Python literal or container display
    word_list = ast.literal_eval(f"[{word_list_str}]")
    
    # Now, process each word_id in the word_list
    for word_id, _ in word_list:
        # Emit the word_id and article_id, no need to emit count for DF calculation
        print(f"{word_id}\t{article_id}")

