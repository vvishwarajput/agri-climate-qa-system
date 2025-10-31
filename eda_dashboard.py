import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File paths
AGRI_CSV = "datasets/agriculture_data.csv"
RAIN_CSV = "datasets/rainfall_data.csv"

# Load datasets
print("📂 Loading datasets...")
agri_df = pd.read_csv(AGRI_CSV)
rain_df = pd.read_csv(RAIN_CSV)

# Display basic info
print("\n🌾 Agriculture Dataset:")
print(agri_df.head(), "\n")
print(agri_df.info(), "\n")

print("🌧️ Rainfall Dataset:")
print(rain_df.head(), "\n")
print(rain_df.info(), "\n")

# -------------------------------
# 🧹 Basic Data Cleaning
# -------------------------------
print("🧹 Cleaning data...")

# Drop rows with missing values
agri_df = agri_df.dropna()
rain_df = rain_df.dropna()

print(f"✅ Agriculture data after cleaning: {agri_df.shape}")
print(f"✅ Rainfall data after cleaning: {rain_df.shape}\n")

# -------------------------------
# 📊 Summary Statistics
# -------------------------------
print("📈 Agriculture Summary:")
print(agri_df.describe(), "\n")

print("🌦️ Rainfall Summary:")
print(rain_df.describe(), "\n")

# -------------------------------
# 📉 Visualization Section
# -------------------------------
print("📊 Generating charts...")

# 1️⃣ Correlation heatmap for agriculture data
plt.figure(figsize=(10,6))
sns.heatmap(agri_df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title("Agriculture Data Correlation Heatmap")
plt.show()

# 2️⃣ Rainfall over years
plt.figure(figsize=(10,5))
plt.plot(rain_df['Year'], rain_df['Mean'], marker='o')
plt.title("Average Annual Rainfall (or Temperature) Trend")
plt.xlabel("Year")
plt.ylabel("Mean Value")
plt.grid(True)
plt.show()

# 3️⃣ Example comparison — random numeric column
if 'total exports' in agri_df.columns:
    plt.figure(figsize=(8,5))
    plt.scatter(rain_df['Mean'].head(len(agri_df)), agri_df['total exports'].head(len(rain_df)))
    plt.title("Total Exports vs Rainfall Mean (sample)")
    plt.xlabel("Rainfall Mean")
    plt.ylabel("Total Exports")
    plt.grid(True)
    plt.show()
else:
    print("ℹ️ Skipping rainfall vs export plot — column not found.")
