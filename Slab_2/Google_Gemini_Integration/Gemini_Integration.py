import google.generativeai as genai
import google.auth
from googleapiclient.discovery import build
import os
import datetime

# Configure your API keys and model
GOOGLE_API_KEY = os.environ.get("AIzaSyCuoyjvoO7HxgB76S2kVDtHkYNphyyhfz0")  # Set your Gemini API key as an environment variable
GOOGLE_SEARCH_API_KEY = os.environ.get("AIzaSyBt6sT4x4Ath1P3GTqSrgwCzrJa_yx6ETk") # Set your Google Search API Key as an environment variable
GOOGLE_SEARCH_ENGINE_ID = os.environ.get("040afcbafb5204b87") # Set your Google Search Engine ID as an environment variable

# Debug statements to check if environment variables are set
print(f"GOOGLE_API_KEY: {GOOGLE_API_KEY}")
print(f"GOOGLE_SEARCH_API_KEY: {GOOGLE_SEARCH_API_KEY}")
print(f"GOOGLE_SEARCH_ENGINE_ID: {GOOGLE_SEARCH_ENGINE_ID}")


genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def search_google(query):
    """Performs a Google Search and returns the top result."""
    service = build("customsearch", "v1", developerKey=GOOGLE_SEARCH_API_KEY)
    res = service.cse().list(q=query, cx=GOOGLE_SEARCH_ENGINE_ID).execute()
    if 'items' in res and len(res['items']) > 0:
        return res['items'][0]['snippet']
    else:
        return "No results found."

def get_realtime_data(query):
    """Retrieves real-time data using Google Search."""
    try:
        if "weather in" in query.lower():
            return search_google(query)
        elif "price of bitcoin" in query.lower():
            return search_google(query)
        elif "current time in" in query.lower():
            return search_google(query)
        else:
          return None
    except Exception as e:
        print(f"Error retrieving real-time data: {e}")
        return None

def chat_with_gemini(user_input, chat_history=None):
    """Interacts with the Gemini model, remembering conversation history and retrieving real-time data."""

    if chat_history is None:
        chat_history = []

    realtime_data = get_realtime_data(user_input)

    if realtime_data:
        user_input = f"{user_input}. Here is some relevant information: {realtime_data}"

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