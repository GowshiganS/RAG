# generate_response.py
from transformers import pipeline

# Initializing a text-generation pipeline with a free model.
# we can use other models "gpt2" or "EleutherAI/gpt-neo-125M", 
generator = pipeline("text-generation", model="distilgpt2")

def generate_response(query, retrieved_docs, max_length=150, temperature=0.7):
    """
    Generate a response using a Hugging Face model.

    Args:
        query (str): The user's query.
        retrieved_docs (list): List of context documents retrieved.
        max_length (int): Maximum number of tokens to generate.
        temperature (float): Controls randomness in generation.

    Returns:
        str: The generated answer.
    """
    # Combining the retrieved documents into a single context string.
    context = "\n".join(retrieved_docs)

    # Building the prompt that includes context and the query.
    prompt = (
        f"Using the following information, answer the question as helpfully as possible:\n\n"
        f"{context}\n\n"
        f"Question: {query}\n\n"
        f"Answer:"
    )

    # Generating text using the model.
    outputs = generator(
        prompt,
        max_length=len(prompt.split()) + max_length,
        do_sample=True,
        temperature=temperature
    )

    # Extracting the generated text.
    generated_text = outputs[0]['generated_text']

    # Removing the prompt portion to isolate the answer.
    answer = generated_text[len(prompt):].strip()

    return answer

# Testing the function locally:
if __name__ == "__main__":
    test_docs = [
        "To reset your password, click on 'Forgot Password' on the login page and follow the instructions.",
        "If you cannot connect to Wi-Fi, try restarting your router and checking your network settings."
    ]
    test_query = "How do I reset my password?"
    print("Generated answer:", generate_response(test_query, test_docs))

