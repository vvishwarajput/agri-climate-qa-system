import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib
import os

print("🌾 Loading datasets...")

# Load agriculture dataset
agri_path = "datasets/agriculture_data.csv"
if not os.path.exists(agri_path):
    raise FileNotFoundError("❌ Agriculture dataset not found! Please run data_loader.py first.")

agri_df = pd.read_csv(agri_path)

# Preview columns
print(f"✅ Columns: {list(agri_df.columns)}")

# ---------------- DATA CLEANING ----------------
print("🧹 Cleaning data...")

# Keep only numeric columns (production/exports)
numeric_cols = ['beef', 'pork', 'poultry', 'dairy', 'fruits fresh',
                'fruits proc', 'total fruits', 'veggies fresh',
                'veggies proc', 'total veggies', 'corn', 'wheat', 'cotton']

target_col = 'total exports'

# Drop missing or invalid values
agri_df = agri_df.dropna(subset=[target_col])
agri_df = agri_df.fillna(0)

X = agri_df[numeric_cols]
y = agri_df[target_col]

# ---------------- TRAIN-TEST SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------- MODEL TRAINING ----------------
print("🤖 Training RandomForest model...")
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# ---------------- EVALUATION ----------------
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"📊 R² Score: {r2:.3f}")
print(f"📉 MAE: {mae:.3f}")

# ---------------- SAVE MODEL ----------------
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/agri_export_model.pkl")
print("✅ Model saved successfully: models/agri_export_model.pkl")
