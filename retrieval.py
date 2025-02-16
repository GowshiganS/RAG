# retrieval.py
import numpy as np

from embeddings_setup import docs, model, index  # Ensure this file is in the same directory

def retrieve_documents(query, index, model, top_k=2):
    # Encoding the query
    query_embedding = model.encode(query)

    # Reshaping and searching in the FAISS index for top_k nearest neighbors
    query_embedding = np.array([query_embedding])
    distances, indices = index.search(query_embedding, k=top_k)

    # Retrieving corresponding documents
    retrieved = [docs[i] for i in indices[0]]
    return retrieved

# Example of usage:
if __name__ == "__main__":
    query = "How do I reset my password?"
    retrieved_docs = retrieve_documents(query, index, model)
    print("Retrieved documents:", retrieved_docs)

