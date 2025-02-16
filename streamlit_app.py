# streamlit_app.py
import streamlit as st

# Import the necessary functions and objects from your modules
from embeddings_setup import model, index, docs  # Ensure these are defined in embeddings_setup.py
from retrieval import retrieve_documents
from generate_response import generate_response

# Set the title for the app
st.title("Tech Support Chatbot")

# Create a text input for the user's query
query = st.text_input("Enter your IT support question:")

# When the user clicks the button, process the query
if st.button("Ask"):
    if query:
        # Retrieve relevant documents based on the query
        retrieved_docs = retrieve_documents(query, index, model)
        # Generate an answer using the retrieved context
        answer = generate_response(query, retrieved_docs)
        
        # Display the answer and context
        st.markdown("### Answer:")
        st.write(answer)
        
        st.markdown("### Context Used:")
        for doc in retrieved_docs:
            st.write("- " + doc)
    else:
        st.warning("Please enter a question.")
