# CROPSAFE

🌾 CropSafe — AI-Powered Smart Farming Dashboard  
Precision agriculture with crop prediction, fertilizer recommendation & live weather insights

CropSafe is an advanced Streamlit-based agronomy intelligence system combining machine learning models, real-time weather analytics, and soil chemistry inputs to help farmers make data-driven decisions.

It includes ML-trained prediction engines, interactive dashboards, conversational AI, and a fully modular backend architecture.

---------------------------------------------------------------------

🚀 KEY FEATURES

🔮 1. Crop Prediction Engine
- Predicts the most suitable crop using NPK, temperature, humidity, rainfall, pH
- Built on trained ML models (crop_model.pkl)
- Outputs best crop recommendations + confidence scores

🧪 2. Fertilizer Recommendation System
- Suggests ideal fertilizer combinations
- Identifies nutrient deficiencies
- Powered by fertilizer_model.pkl
- Inference via utils/fertilizer_predict.py

🌦️ 3. Weather Intelligence Console
- Live weather from OpenWeather API
- Includes rainfall, humidity, description, temperature
- Map-based lookup
- Logic inside utils/weather_map.py

🤖 4. CroPy – Conversational Agronomy Chatbot
- Chat-based agronomy assistant
- Soil health, fertilizer ratios, crop selection
- Always-on farming guidance
- Implemented in pages/4_🤖_Cropy(Help).py

---------------------------------------------------------------------

📁 PROJECT STRUCTURE

CropSafe_
│
├── data/
│   ├── crop_dataset.csv
│   └── fertilizer_dataset.csv
│
├── models/
│   ├── crop_model.pkl
│   ├── crop_scaler.pkl
│   └── fertilizer_model.pkl
│
├── pages/
│   ├── 1_🌾_Crop_Prediction.py
│   ├── 2_🌿_Fertilizer_Prediction.py
│   ├── 3_📖_Map_&_Weather.py
│   └── 4_🤖_Cropy(Help).py
│
├── utils/
│   ├── config.py
│   ├── crop_predict.py
│   ├── fertilizer_predict.py
│   └── weather_map.py
│
├── .env
├── streamlit_app.py
├── train_crop_model.py
├── train_fertilizer_model.py
└── README.md

---------------------------------------------------------------------

🛠️ INSTALLATION

1️⃣ Clone the repo:
git clone https://github.com/your-username/CropSafe.git
cd CropSafe_

2️⃣ Install dependencies:
pip install -r requirements.txt

3️⃣ Add weather API key inside .env:
OPENWEATHER_API_KEY=YOUR_KEY

4️⃣ Run the app:
streamlit run streamlit_app.py

---------------------------------------------------------------------

🧠 MACHINE LEARNING MODELS

Crop Prediction Model: models/crop_model.pkl  
Scaler: models/crop_scaler.pkl  
Fertilizer Model: models/fertilizer_model.pkl  

Training scripts:
- train_crop_model.py
- train_fertilizer_model.py

---------------------------------------------------------------------

🎨 UI & THEME ENGINE

- Light/Dark mode  
- Glassmorphism cards  
- Custom HTML injected via components.html()  
- Modern gradients and layout  

Since Streamlit 1.50 restricts raw HTML rendering, the app uses:
components.html(html_code, height=2400)

---------------------------------------------------------------------

📊 DATASETS

crop_dataset.csv  
fertilizer_dataset.csv  

Used for ML training and inference.

---------------------------------------------------------------------

🧪 RETRAIN MODELS

python train_crop_model.py  
python train_fertilizer_model.py  

---------------------------------------------------------------------

🤝 CONTRIBUTING

PRs and suggestions are welcome.  
Create a separate branch for major features.

---------------------------------------------------------------------

📜 LICENSE

MIT License (free for personal & commercial use)

---------------------------------------------------------------------

⭐ SUPPORT THE PROJECT

If you like this project,  
DON'T FORGET TO GIVE A ⭐ ON GITHUB!  
It motivates development and helps others discover the project.

---------------------------------------------------------------------
