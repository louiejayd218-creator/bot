import os
from google import genai
from google.genai import types

def run_my_search_bot():
    print("🤖 Your AI Search Agent is booting up...")
    
    # Secure setup: Python will automatically find your hidden GEMINI_API_KEY environment variable!
    client = genai.Client()
    
    print("🤖 Online! Ask me anything (or type 'exit' to quit).\n")
    
    while True:
        user_query = input("You: ")
        if user_query.lower() == 'exit':
            print("🤖 Bot: Catch you later, Boss!")
            break
            
        print("🤖 Bot: Let me check the web for you real quick...")
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_query,
                config=types.GenerateContentConfig(
                    tools=[types.Tool(google_search=types.GoogleSearch())]
                )
            )
            print(f"\n🤖 Bot: {response.text}\n")
            
        except Exception as e:
            print(f"\n❌ Error: Something went wrong ({e})\n")

if __name__ == "__main__":
    run_my_search_bot()