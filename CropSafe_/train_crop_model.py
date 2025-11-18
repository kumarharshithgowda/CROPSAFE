import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample
import pickle, os

# Load dataset
df = pd.read_csv("data/crop_dataset.csv")

# 🔍 Display class balance
print("📊 Original crop distribution:")
print(df['label'].value_counts(), "\n")

# ✅ Balance dataset (upsample minority classes)
max_count = df['label'].value_counts().max()
df_balanced = pd.concat([
    resample(group, replace=True, n_samples=max_count, random_state=42)
    for _, group in df.groupby('label')
])

print("✅ Balanced crop distribution:")
print(df_balanced['label'].value_counts(), "\n")

# Select features and target
X = df_balanced[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df_balanced['label']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=400,
    max_depth=20,
    random_state=42,
    class_weight='balanced_subsample'
)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"🌾 Crop Prediction Model Accuracy: {acc*100:.2f}%\n")
print("📈 Classification Report:")
print(classification_report(y_test, y_pred))

# Save model and scaler
os.makedirs("models", exist_ok=True)
with open("models/crop_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("models/crop_scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("\n✅ Model and scaler saved successfully in /models")
