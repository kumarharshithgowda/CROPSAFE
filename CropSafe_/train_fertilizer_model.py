import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('data/fertilizer_dataset.csv')

features = [
    'Temperature', 'Humidity', 'Moisture',
    'Soil_Type', 'Crop_Type',
    'Nitrogen', 'Potassium', 'Phosphorous'
]
target = 'Fertilizer'

# Encode categorical columns
label_encoders = {}
for col in ['Soil_Type', 'Crop_Type']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print(f"✅ Fertilizer Model Accuracy: {acc:.2f}")

with open('models/fertilizer_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("💧 Fertilizer model saved successfully.")
