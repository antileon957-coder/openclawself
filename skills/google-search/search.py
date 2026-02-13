import os
import sys
import google.generativeai as genai

def search(query):
    api_key = os.environ.get("search_key_google_ai_studio")
    if not api_key:
        print("Error: API key for Google AI Studio not found.")
        sys.exit(1)

    try:
        genai.configure(api_key=api_key)
        
        # Using a model confirmed to exist in the list
        model = genai.GenerativeModel("models/gemini-flash-latest")
        
        # Attempt grounding if possible, otherwise plain generation
        try:
            response = model.generate_content(
                query,
                tools=[{"google_search_retrieval": {}}]
            )
        except:
            response = model.generate_content(query)
            
        if response.text:
            print(response.text)
        else:
            print("No content returned from Gemini.")

    except Exception as e:
        print(f"Error executing search: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 search.py <query>")
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    search(query)
