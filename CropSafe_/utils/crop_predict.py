import pickle
import numpy as np
import pandas as pd
import os

def predict_crop(data):
    """
    Predicts the best crop using trained RandomForest and saved StandardScaler.
    """
    model_path = "models/crop_model.pkl"
    scaler_path = "models/crop_scaler.pkl"

    # Check if model and scaler exist
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        raise FileNotFoundError("❌ Model or scaler not found. Please train the crop model first.")

    # Load model and scaler
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)

    # Convert input data to DataFrame
    df = pd.DataFrame([data])

    # Reorder columns to match training
    df = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]

    # Apply scaling
    df_scaled = scaler.transform(df)

    # Predict
    prediction = model.predict(df_scaled)
    return prediction[0]
