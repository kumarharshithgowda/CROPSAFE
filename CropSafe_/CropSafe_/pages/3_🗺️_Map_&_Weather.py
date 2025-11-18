import streamlit as st
import folium
from streamlit_folium import st_folium
from utils.weather_map import get_weather

st.set_page_config(page_title="🗺️ Map & Weather", layout="wide")
st.title("🗺️ Real-Time Map & Weather Data")

st.markdown("### 🌍 Click anywhere on the map to get live weather updates!")

# Default map (India)
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Display interactive map
map_data = st_folium(m, width=700, height=500)

# Handle click event
if map_data and map_data.get("last_clicked"):
    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]

    st.info(f"📍 Selected Location: Latitude **{lat:.2f}**, Longitude **{lon:.2f}**")

    weather = get_weather(lat, lon)

    if "error" in weather:
        st.warning(weather["error"])
    else:
        st.success(f"🌡️ Temperature: {weather['temperature']} °C")
        st.write(f"💧 Humidity: {weather['humidity']}%")
        st.write(f"🌧️ Rainfall (1h): {weather['rainfall']} mm")
        st.write(f"📍 Location: {weather['location']}")
        st.write(f"🌤️ Condition: {weather['description']}")
