# streamlit_app.py
import streamlit as st
import requests

# Setting the title of the app
st.title("Tech Support Chatbot")

# Creating a text input field for the user's query
query = st.text_input("Enter your IT support question:")

# When the user clicks the button, call the FastAPI endpoint to get an answer
if st.button("Ask"):
    if query:
        # URL of the FastAPI endpoint (adjust the port if needed)
        url = "http://127.0.0.1:8000/ask/"
        # Sending the query as a URL parameter
        params = {"query": query}
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                st.markdown("### Answer:")
                st.write(data["answer"])
                
                # Optionally, display the context used (retrieved documents)
                st.markdown("### Context Used:")
                for doc in data["context_used"]:
                    st.write("- " + doc)
            else:
                st.error(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")
