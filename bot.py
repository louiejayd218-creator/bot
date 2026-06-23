import os
from google import genai
from google.genai import types

def run_my_search_bot():
    client = genai.Client()
    
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())]
        )
    )
    
    print("Session initialized. Type 'exit' to quit.\n")
    
    while True:
        try:
            user_query = input("User: ")
            if user_query.strip().lower() == 'exit':
                break
                
            if not user_query.strip():
                continue
                
            response = chat.send_message(message=user_query)
            print(f"\nBot: {response.text}\n")
            
        except Exception as e:
            print(f"\n[Error: {e}]\n")

if __name__ == "__main__":
    run_my_search_bot()