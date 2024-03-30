#!/usr/bin/env python3
import sys
import math
from queue import PriorityQueue

def parse_vector(vector_str):
    vector = {}
    items = vector_str.split(',')
    for item in items:
        try:
            term_id, score = item.split(':')
            vector[int(term_id.strip())] = float(score.strip())
        except ValueError as e:
            sys.stderr.write(f"Error parsing item '{item}': {e}\n")
    return vector

try:
    query_vector = {}
    with open("/home/shahbaz/Desktop/ass2/query.txt", "r") as f:
        for line in f:
            term_id, score = line.strip().split('\t')
            query_vector[int(term_id)] = float(score)
except Exception as e:
    sys.stderr.write(f"Error loading query vector: {e}\n")
    sys.exit(1)

def cosine_similarity(vec1, vec2):
    try:
        intersection = set(vec1.keys()) & set(vec2.keys())
        dot_product = sum(vec1[k] * vec2[k] for k in intersection)
        norm_a = math.sqrt(sum([val**2 for val in vec1.values()]))
        norm_b = math.sqrt(sum([val**2 for val in vec2.values()]))
        if norm_a * norm_b == 0:
            return 0
        return dot_product / (norm_a * norm_b)
    except Exception as e:
        sys.stderr.write(f"Error calculating similarity: {e}\n")
        return 0

top_documents = PriorityQueue(maxsize=10)

for line in sys.stdin:
    try:
        doc_id, vector_str = line.strip().split('\t', 1)
        doc_vector = parse_vector(vector_str)
        similarity = cosine_similarity(doc_vector, query_vector)
        if top_documents.qsize() < 10 or similarity > top_documents.queue[0][0]:
            if top_documents.qsize() == 10:
                top_documents.get()
            top_documents.put((similarity, doc_id))
    except Exception as e:
        sys.stderr.write(f"Error processing line '{line}': {e}\n")

while not top_documents.empty():
    similarity, doc_id = top_documents.get()
    print(f"Document ID: {doc_id}, Similarity: {similarity}")

