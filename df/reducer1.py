#!/usr/bin/env python3
import sys
from collections import defaultdict

# Track the current word being processed and a set of articles it has appeared in
current_word_id = None
articles = set()

for line in sys.stdin:
    word_id, article_id = line.strip().split('\t')
    
    # If we're still on the same word, add the article to the set
    if word_id == current_word_id:
        articles.add(article_id)
    else:
        # If this is a new word, but not the first word we've seen
        if current_word_id is not None:
            # Emit the word and the number of unique articles it appeared in
            print(f"{current_word_id}\t{len(articles)}")
        
        # Reset for the new word
        current_word_id = word_id
        articles = {article_id}

# Don't forget to output the last word if there is one
if current_word_id is not None:
    print(f"{current_word_id}\t{len(articles)}")

