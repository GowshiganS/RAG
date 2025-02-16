# app.py
from fastapi import FastAPI, Query
from retrieval import retrieve_documents, model, index  # Import our retrieval function and model/index
from generate_response import generate_response

app = FastAPI()

@app.get("/ask/")
def ask(query: str = Query(..., description="The IT support question to ask the chatbot")):
    # Retrieve relevant documents based on the query
    retrieved_docs = retrieve_documents(query, index, model)
    # Generate an answer using GPT and the retrieved documents
    answer = generate_response(query, retrieved_docs)
    return {"query": query, "answer": answer, "context_used": retrieved_docs}

# To run the app locally, use the command:
# uvicorn app:app --reload
