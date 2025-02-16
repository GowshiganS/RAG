# embeddings_setup.py
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Loading of the pretrained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example of documents 
docs = [
    "To reset your password, click on 'Forgot Password' on the login page and follow the instructions.",
    "If you can't connect to Wi-Fi, try restarting your router and checking your network settings.",
    "To install software, download the installer from the official website and follow the prompts.",
    "For printer issues, ensure the printer is connected to the network and turned on.",
    "If your computer is running slow, try closing unnecessary programs and restarting your machine."
]

# Generate embeddings for each document
doc_embeddings = np.array([model.encode(doc) for doc in docs])

# Creating FAISS index (using L2 distance for simplicity)
embedding_dim = doc_embeddings.shape[1]  # For MiniLM, usually 384 dimensions.
index = faiss.IndexFlatL2(embedding_dim)
index.add(doc_embeddings)

print("FAISS index built with", index.ntotal, "documents.")

