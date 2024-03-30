query = "anarchism anarchy philosophy aa"
tokens = query.lower().split()  # Simple tokenization, adjust as needed.

# Load the vocab to map terms to IDs
vocab = {}
with open("/home/shahbaz/Desktop/ass2/vocab.txt", "r") as f:
    for line in f:
        term_id, term = line.strip().split("\t")
        vocab[term] = term_id

# Count occurrences of each token to get term frequencies
token_counts = {}
for token in tokens:
    if token in vocab:  # Only consider tokens that are in the vocab
        term_id = vocab[token]
        if term_id not in token_counts:
            token_counts[term_id] = 0
        token_counts[term_id] += 1

# Prepare the token_counts for MapReduce processing, e.g., by writing to a file
with open("query.txt", "w") as f:
    for term_id, count in token_counts.items():
        f.write(f"{term_id}\t{count}\n")  # Write each term_id with its count

