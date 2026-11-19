
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Read our knowledge document
file_path = Path("documents/solar_system.txt")

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Divide document into smaller chunks
def split_text(text, chunk_size=100):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

document_chunks = split_text(text)

# Convert chunks into numerical vectors
chunk_embeddings = embedding_model.encode(document_chunks)

# Search for relevant information

def retrieve_context(question, top_k=2, threshold=0.30):
    question_embedding = embedding_model.encode([question])

    similarities = cosine_similarity(
        question_embedding,
        chunk_embeddings
    )[0]

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []

    for index in top_indices:
        score = similarities[index]

        if score >= threshold:
            results.append(document_chunks[index])

    return results
