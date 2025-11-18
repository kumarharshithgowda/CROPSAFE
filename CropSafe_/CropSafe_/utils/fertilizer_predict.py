import pandas as pd
import pickle
import os

# Load the trained fertilizer model
model_path = os.path.join("models", "fertilizer_model.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Mapping for categorical fields
soil_type_mapping = {
    "Sandy": 0,
    "Loamy": 1,
    "Clayey": 2,
    "Black": 3,
    "Red": 4
}

crop_type_mapping = {
    "Rice": 0,
    "Wheat": 1,
    "Maize": 2,
    "Cotton": 3,
    "Sugarcane": 4
}

# Expected columns (MUST match training time order)
EXPECTED_COLUMNS = [
    "Temperature", "Humidity", "Moisture",
    "Soil_Type", "Crop_Type",
    "Nitrogen", "Potassium", "Phosphorous"
]

def predict_fertilizer(data):
    """
    Predict the best fertilizer based on environmental and soil data.
    Input: dict with Temperature, Humidity, Moisture, Soil_Type, Crop_Type, Nitrogen, Potassium, Phosphorous
    """

    # Encode soil & crop type
    soil_type = soil_type_mapping.get(data["Soil_Type"], 0)
    crop_type = crop_type_mapping.get(data["Crop_Type"], 0)

    # Create dataframe using exact column names used in training
    input_df = pd.DataFrame([{
        "Temperature": float(data["Temperature"]),
        "Humidity": float(data["Humidity"]),
        "Moisture": float(data["Moisture"]),
        "Soil_Type": soil_type,
        "Crop_Type": crop_type,
        "Nitrogen": float(data["Nitrogen"]),
        "Potassium": float(data["Potassium"]),
        "Phosphorous": float(data["Phosphorous"])
    }], columns=EXPECTED_COLUMNS)  # 👈 ensures feature names match

    # Predict fertilizer type
    prediction = model.predict(input_df)[0]

    return prediction
