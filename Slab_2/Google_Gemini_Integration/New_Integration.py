import google.generativeai as genai
import os

# Configure your API key
GOOGLE_API_KEY = "AIzaSyCuoyjvoO7HxgB76S2kVDtHkYNphyyhfz0"

if not GOOGLE_API_KEY:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

def chat_with_gemini(user_input, chat_history=None):
    """Interacts with the Gemini model, remembering conversation history."""

    if chat_history is None:
        chat_history = []

    chat_history.append({"role": "user", "parts": [user_input]})

    try:
        response = model.generate_content(chat_history)
        response_text = response.text
        chat_history.append({"role": "model", "parts": [response_text]})
        return response_text, chat_history

    except Exception as e:
        return f"An error occurred: {e}", chat_history

# Example usage
conversation_history = []
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response, conversation_history = chat_with_gemini(user_input, conversation_history)
    print("Gemini:", response)