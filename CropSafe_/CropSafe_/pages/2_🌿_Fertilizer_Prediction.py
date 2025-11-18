import streamlit as st
from utils.fertilizer_predict import predict_fertilizer
import folium
from streamlit_folium import st_folium
from utils.weather_map import get_weather

st.title("🌿 Fertilizer Recommendation")

st.subheader("🗺️ Select a Location to Get Real-Time Weather Data")

# ---- Map Section ----
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
map_data = st_folium(m, width=700, height=400)

# Default placeholders
Temperature = None
Humidity = None

# When user clicks a location
if map_data and map_data.get("last_clicked"):
    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]
    st.success(f"📍 Selected Location: Latitude {lat:.2f}, Longitude {lon:.2f}")

    try:
        weather = get_weather(lat, lon)

        if "error" in weather:
            st.error(weather["error"])
        else:
            st.write(f"🌡️ Temperature: {weather['temperature']} °C")
            st.write(f"💧 Humidity: {weather['humidity']}%")
            st.write(f"🏙️ Location: {weather['location']}")

            # Auto-fill fields
            Temperature = weather["temperature"]
            Humidity = weather["humidity"]

    except Exception as e:
        st.error(f"⚠️ {str(e)}")

# ---- Input Section ----
st.subheader("🧮 Enter Soil, Crop, and Nutrient Details")

Temperature = st.number_input("Temperature (°C)", 0.0, 50.0, value=float(Temperature) if Temperature else 0.0)
Humidity = st.number_input("Humidity (%)", 0.0, 100.0, value=float(Humidity) if Humidity else 0.0)
Moisture = st.number_input("Moisture (%)", 0.0, 100.0)
Soil_Type = st.selectbox("Soil Type", ["Sandy", "Loamy", "Clayey", "Black", "Red"])
Crop_Type = st.selectbox("Crop Type", ["Rice", "Wheat", "Maize", "Cotton", "Sugarcane"])
Nitrogen = st.number_input("Nitrogen (N)", 0, 200)
Potassium = st.number_input("Potassium (K)", 0, 200)
Phosphorous = st.number_input("Phosphorous (P)", 0, 200)

# ---- Prediction ----
if st.button("Recommend Fertilizer 💧"):
    data = {
        "Temperature": Temperature,
        "Humidity": Humidity,
        "Moisture": Moisture,
        "Soil_Type": Soil_Type,
        "Crop_Type": Crop_Type,
        "Nitrogen": Nitrogen,
        "Potassium": Potassium,
        "Phosphorous": Phosphorous
    }
    result = predict_fertilizer(data)
    st.success(f"💧 Recommended Fertilizer: **{result}**")
