import streamlit as st
import streamlit.components.v1 as components
from utils.weather_map import get_weather as get_weather_data

st.set_page_config(
    page_title="CropSafe — Smart Farming with CroPy 🤖",
    page_icon="🌾",
    layout="wide"
)

# ---------------------------
# THEME SWITCH
# ---------------------------
theme = st.sidebar.radio("🎨 Choose Theme", ["🌤️ Light", "🌙 Dark"])

if theme == "🌤️ Light":
    theme_props = {
        "bg_gradient": "linear-gradient(135deg, #f4fbf0 0%, #e1f7de 40%, #d0ecf2 100%)",
        "text_color": "#1f3d1a",
        "card_bg": "rgba(255, 255, 255, 0.9)",
        "glass_bg": "rgba(255, 255, 255, 0.55)",
        "accent_color": "#4cb648",
        "accent_hover": "#2f8530",
        "badge_bg": "rgba(76, 182, 72, 0.16)",
        "border_color": "rgba(76, 182, 72, 0.28)",
        "tab_background": "rgba(255, 255, 255, 0.4)",
        "tab_active_border": "rgba(76, 182, 72, 0.45)",
        "shadow_color": "rgba(58, 112, 52, 0.18)",
        "sidebar_bg": "rgba(255, 255, 255, 0.72)",
        "sidebar_text": "#21421e",
        "subtle_text": "#4a6f3f"
    }
else:
    theme_props = {
        "bg_gradient": "linear-gradient(135deg, #0f1a0f 0%, #1a3220 40%, #102522 100%)",
        "text_color": "#f5fbed",
        "card_bg": "rgba(18, 28, 22, 0.92)",
        "glass_bg": "rgba(20, 34, 24, 0.75)",
        "accent_color": "#5cd26c",
        "accent_hover": "#36a04b",
        "badge_bg": "rgba(92, 210, 108, 0.18)",
        "border_color": "rgba(118, 231, 148, 0.28)",
        "tab_background": "rgba(22, 36, 26, 0.75)",
        "tab_active_border": "rgba(92, 210, 108, 0.55)",
        "shadow_color": "rgba(9, 34, 18, 0.45)",
        "sidebar_bg": "rgba(16, 28, 20, 0.9)",
        "sidebar_text": "#d6f5dd",
        "subtle_text": "#93c7a1"
    }

# ---------------------------------------
# WEATHER WIDGET
# ---------------------------------------
try:
    w = get_weather_data(12.9716, 77.5946)
    weather_html = f"""
        <div class="weather-chip">
            <div class="chip-label">{w.get("location","India")} • {w.get("description","").title()}</div>
            <div class="chip-values">
                <span>{round(w.get("temperature",0))}°C</span>
                <span>{round(w.get("humidity",0))}% humidity</span>
                <span>{w.get("rainfall",0)} mm rain</span>
            </div>
        </div>
    """
except:
    weather_html = """
        <div class="weather-chip">
            <div class="chip-label">Connect your OpenWeather key</div>
            <div class="chip-values"><span>Activate live agronomic weather pulses</span></div>
        </div>
    """

# ---------------------------------------
# LOAD FULL HTML TEMPLATE
# ---------------------------------------

html_code = f"""
<html>
<head>
<style>
body {{
    background: {theme_props["bg_gradient"]};
    font-family: 'Poppins', sans-serif;
    color: {theme_props["text_color"]};
}}
.weather-chip {{
    padding: 12px;
    background: {theme_props["card_bg"]};
    border: 1px solid {theme_props["border_color"]};
    border-radius: 16px;
    display: inline-block;
    margin-top: 10px;
    box-shadow: 0 12px 30px {theme_props["shadow_color"]};
}}
.chip-label {{
    font-weight: 600;
    margin-bottom: 6px;
}}
.chip-values span {{
    margin-right: 12px;
    color: {theme_props["subtle_text"]};
}}
.hero-box {{
    background: {theme_props["glass_bg"]};
    padding: 40px;
    border-radius: 32px;
    border: 1px solid {theme_props["border_color"]};
    box-shadow: 0 40px 70px {theme_props["shadow_color"]};
    backdrop-filter: blur(20px);
}}
.metric-box {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px,1fr));
    gap: 20px;
    margin-top: 30px;
}}
.metric-card{{
    background: {theme_props["card_bg"]};
    padding: 20px;
    border-radius: 20px;
    border: 1px solid {theme_props["border_color"]};
    box-shadow: 0 24px 48px {theme_props["shadow_color"]};
}}
.metric-value {{
    font-size: 2rem;
    font-weight: bold;
    color: {theme_props["accent_color"]};
}}
.feature-grid {{
    margin-top: 40px;
    display: grid;
    gap: 20px;
    grid-template-columns: repeat(auto-fit, minmax(260px,1fr));
}}
.feature-card {{
    background: {theme_props["card_bg"]};
    border-radius: 22px;
    padding: 20px;
    border: 1px solid {theme_props["border_color"]};
    box-shadow: 0 20px 40px {theme_props["shadow_color"]};
}}
</style>
</head>
<body>

<div class="hero-box">
    <h1>Precision crop intelligence for every acre</h1>
    <p>Blend soil, climate, and CroPy prediction engines for confident crop planning.</p>
    {weather_html}
</div>

<div class="metric-box">
    <div class="metric-card">
        <div class="metric-value">92%</div>
        <div>Prediction accuracy</div>
    </div>

    <div class="metric-card">
        <div class="metric-value">12k+</div>
        <div>Soil profiles analyzed</div>
    </div>

    <div class="metric-card">
        <div class="metric-value">7-day</div>
        <div>Weather horizon</div>
    </div>
</div>

<div class="feature-grid">
    <div class="feature-card">
        <h3>🧪 Soil intelligence engine</h3>
        <p>Instant NPK scoring, pH drift tracking, growth-stage advisors.</p>
    </div>

    <div class="feature-card">
        <h3>🛰 Climate-aware simulations</h3>
        <p>7-day microclimate forecasts with rainfall + heatwave signals.</p>
    </div>

    <div class="feature-card">
        <h3>🤖 CroPy co-pilot</h3>
        <p>Conversational agronomy + fertilizer personalization.</p>
    </div>
</div>

</body>
</html>
"""

# ---------------------------------------
# RENDER FULL PAGE
# ---------------------------------------
components.html(html_code, height=2400, scrolling=True)
