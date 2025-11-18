import streamlit as st
from utils.crop_predict import predict_crop
import folium
from streamlit_folium import st_folium
from utils.weather_map import get_weather  # ✅ Corrected import name

st.title("🌾 Crop Prediction")

st.subheader("🗺️ Select a Location to Get Real-Time Weather Data")

# ---- Map Section ----
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
map_data = st_folium(m, width=700, height=400)

# Default placeholders for weather values
temperature = None
humidity = None
rainfall = None

# When user clicks a location on map
if map_data and map_data.get("last_clicked"):
    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]
    st.success(f"📍 Selected Location: Latitude {lat:.2f}, Longitude {lon:.2f}")

    try:
        weather = get_weather(lat, lon)
        st.write(f"🌡️ Temperature: {weather['temperature']} °C")
        st.write(f"💧 Humidity: {weather['humidity']}%")
        st.write(f"🌧️ Rainfall: {weather['rainfall']} mm")
        st.write(f"🏙️ Location: {weather['location']}")

        # Auto-fill from weather API
        temperature = weather["temperature"]
        humidity = weather["humidity"]
        rainfall = weather["rainfall"]

    except Exception as e:
        st.error(f"⚠️ {str(e)}")

st.subheader("🧮 Enter Soil & Nutrient Details")

# ---- Input Fields ----
N = st.number_input("Nitrogen (N)", 0, 200)
P = st.number_input("Phosphorus (P)", 0, 200)
K = st.number_input("Potassium (K)", 0, 200)

temperature = st.number_input("Temperature (°C)", 0.0, 50.0, value=float(temperature or 0.0))
humidity = st.number_input("Humidity (%)", 0.0, 100.0, value=float(humidity or 0.0))
ph = st.number_input("pH", 0.0, 14.0)
rainfall = st.number_input("Rainfall (mm)", 0.0, 500.0, value=float(rainfall or 0.0))



# ---- Prediction Button ----
if st.button("Predict Crop 🌱"):
    data = {
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }
    result = predict_crop(data)
    st.success(f"🌿 Recommended Crop: **{result}**")
