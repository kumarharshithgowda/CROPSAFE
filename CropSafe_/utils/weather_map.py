import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get your OpenWeather API key
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(lat, lon):
    """
    Fetch weather data for a given latitude and longitude using the OpenWeather API.
    Returns temperature, humidity, rainfall, and location name.
    """
    if not OPENWEATHER_API_KEY:
        return {"error": "⚠️ Missing OPENWEATHER_API_KEY in .env"}

    # Construct API URL
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={lat}&lon={lon}&units=metric&appid={OPENWEATHER_API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return {"error": data.get("message", "Error fetching weather data")}

        return {
            "location": data.get("name", "Unknown"),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "rainfall": data.get("rain", {}).get("1h", 0),
            "description": data["weather"][0]["description"].capitalize(),
        }

    except Exception as e:
        return {"error": f"Exception: {str(e)}"}
