import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

# Load dataset
df = pd.read_excel("data/processed/cleaned_tickets.xlsx")

# Extract ticket descriptions
texts = df["Ticket Description"].astype(str).tolist()

print("Total tickets loaded:", len(texts))

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")

embeddings = model.encode(texts)

# Convert embeddings to numpy
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("FAISS index created")

# Save FAISS index
faiss.write_index(index, "data/vector_index.faiss")

# Save ticket texts
with open("data/ticket_texts.pkl", "wb") as f:
    pickle.dump(texts, f)

print("Vector index saved successfully")