import os
import pandas as pd

# Ensure datasets directory exists
os.makedirs("datasets", exist_ok=True)

# ✅ Working public dataset URLs
AGRI_URL = "https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv"
RAIN_URL = "https://raw.githubusercontent.com/datasets/global-temp/master/data/annual.csv"

# Local file paths
AGRI_CSV = "datasets/agriculture_data.csv"
RAIN_CSV = "datasets/rainfall_data.csv"


def safe_download(url, save_path):
    print(f"🔗 Downloading from: {url}")
    df = pd.read_csv(url)
    df.to_csv(save_path, index=False)
    print(f"✅ Saved: {save_path} ({len(df)} rows)")
    return df


def load_datasets():
    print("🌾 Loading Agriculture Production Data...")
    agri_df = safe_download(AGRI_URL, AGRI_CSV)
    print(agri_df.head(), "\n")

    print("🌧️ Loading Rainfall Data...")
    rain_df = safe_download(RAIN_URL, RAIN_CSV)
    print(rain_df.head(), "\n")

    return agri_df, rain_df


if __name__ == "__main__":
    agri_df, rain_df = load_datasets()
