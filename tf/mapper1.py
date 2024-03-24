#!/usr/bin/env python3
import sys
import re

# Load the vocabulary into a dictionary
vocab = {}
with open("/home/shahbaz/Desktop/A2/vocab.txt", "r") as f:
    for line in f:
        word_id, word = line.strip().split("\t")
        vocab[word] = word_id

for line in sys.stdin:
    article_id, section_text = line.strip().split(',', 1)
    words = re.findall(r'\b[a-zA-Z]+\b', section_text.lower())
    for word in words:
        if word in vocab:  # Check if the word is in the vocabulary
            print(f"{article_id}\t{vocab[word]}\t1")
