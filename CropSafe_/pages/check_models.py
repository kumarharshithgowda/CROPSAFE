import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load your .env file
load_dotenv()

# Get your Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Gemini API key not found. Make sure your .env file has GEMINI_API_KEY=your_key_here")
    exit()

# Configure the Gemini client
genai.configure(api_key=api_key)

print("🔍 Checking available Gemini models...\n")

try:
    models = list(genai.list_models())
    for m in models:
        print("✅", m.name)
    print("\nDone! These are the models your API key can use.")
except Exception as e:
    print("❌ Error while listing models:", e)
