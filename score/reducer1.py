#!/usr/bin/env python3
import sys
import math

# Placeholder for the total number of documents in the corpus
N = 817111

def load_document_frequencies(df_path):
    """
    Load document frequencies from a local file.
    """
    word_to_df = {}
    with open(df_path, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                word_id, df = parts
                word_to_df[word_id] = int(df)
    return word_to_df

def calculate_tf_idf_and_normalize(article_id, words_tf, word_to_df):
    """
    Calculate TF-IDF scores, normalize them, and emit the results for a single article.
    """
    squared_sum = 0
    tf_idf_scores = {}
    for word_id, tf in words_tf.items():
        df = word_to_df.get(word_id, 0)
        if df > 0:
            tf_idf = tf * math.log(N / float(df))
            squared_sum += tf_idf ** 2
            tf_idf_scores[word_id] = tf_idf

    if squared_sum > 0:
        normalization_factor = math.sqrt(squared_sum)
        normalized_scores = sorted([(word_id, tf_idf / normalization_factor) for word_id, tf_idf in tf_idf_scores.items()], key=lambda x: x[0])
        normalized_scores_str = ",".join([f"('{word_id}',{score:.6f})" for word_id, score in normalized_scores])
        print(f"({article_id}):[{normalized_scores_str}]")

# Load document frequencies from a local file at the start of the reducer.
df_path = "/home/shahbaz/Desktop/A2/df.txt"  # Specify the correct path to your DF file
word_to_df = load_document_frequencies(df_path)

# Process TF data from stdin
current_article_id = None
words_tf = {}

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) == 4 and parts[1] == "TF":
        article_id, word_id, tf = parts[0], parts[2], int(parts[3])
        if current_article_id and article_id != current_article_id:
            calculate_tf_idf_and_normalize(current_article_id, words_tf, word_to_df)
            words_tf = {}
        current_article_id = article_id
        words_tf[word_id] = tf

# Don't forget the last article
if current_article_id:
    calculate_tf_idf_and_normalize(current_article_id, words_tf, word_to_df)

