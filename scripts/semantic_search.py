import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load FAISS index
index = faiss.read_index("data/vector_index.faiss")

# Load ticket texts
with open("data/ticket_texts.pkl", "rb") as f:
    texts = pickle.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_search(query, top_k=5):

    # Convert query to embedding
    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    # Search in FAISS index
    distances, indices = index.search(query_vector, top_k)

    results = []

    for idx in indices[0]:
        results.append(texts[idx])

    return results


# Test query
query = "laptop not turning on"

results = semantic_search(query)

print("\nSemantic Search Results:\n")

for r in results:
    print("-", r)