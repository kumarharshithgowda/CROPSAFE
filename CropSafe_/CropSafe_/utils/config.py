import os
from dotenv import load_dotenv

# Always tell dotenv exactly where to find the .env file
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
load_dotenv(dotenv_path)
print("DEBUG: .env path used →", dotenv_path)
print("DEBUG: OPENWEATHER_API_KEY =", os.getenv("OPENWEATHER_API_KEY"))


# Load the API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Optional: print a small confirmation for debugging
if not OPENAI_API_KEY or not OPENWEATHER_API_KEY:
    print("⚠️ Missing one or more API keys in .env")
else:
    print("✅ API keys loaded successfully!")
