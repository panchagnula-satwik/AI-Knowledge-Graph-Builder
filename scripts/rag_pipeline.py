import faiss
import pickle
import numpy as np
import ollama
from sentence_transformers import SentenceTransformer

# Load FAISS index
index = faiss.read_index("data/vector_index.faiss")

# Load ticket texts
with open("data/ticket_texts.pkl", "rb") as f:
    texts = pickle.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_context(query, top_k=5):

    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []

    for idx in indices[0]:
        results.append(texts[idx])

    return results


def rag_answer(query):

    context = retrieve_context(query)

    context_text = "\n".join(context)

    prompt = f"""
You are an IT support assistant.

Use the following support tickets as context to answer the user's question.

Context:
{context_text}

User Question:
{query}

Provide a helpful troubleshooting answer.
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


# Test RAG system
query = input("Enter your question: ")

answer = rag_answer(query)

print("\nRAG Answer:\n")
print(answer)