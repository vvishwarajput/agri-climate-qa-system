# knowledge_base.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# -----------------------------
# STEP 1: Load datasets
# -----------------------------
def load_data():
    agri_df = pd.read_csv("datasets/agriculture_data.csv")
    rain_df = pd.read_csv("datasets/rainfall_data.csv")

    print("✅ Agriculture Data:", agri_df.shape)
    print("✅ Rainfall Data:", rain_df.shape)
    return agri_df, rain_df


# -----------------------------
# STEP 2: Build text knowledge base
# -----------------------------
def build_knowledge_base():
    agri_df, rain_df = load_data()

    # Convert data into text form
    agri_text = agri_df.astype(str).apply(lambda x: " ".join(x), axis=1)
    rain_text = rain_df.astype(str).apply(lambda x: " ".join(x), axis=1)

    all_text = pd.concat([agri_text, rain_text], axis=0).reset_index(drop=True)
    print(f"🧾 Combined knowledge base size: {len(all_text)} rows")

    # Vectorize text
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(all_text)

    # Save both vectorizer and embeddings
    with open("models/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    with open("models/knowledge_base.pkl", "wb") as f:
        pickle.dump(tfidf_matrix, f)

    all_text.to_csv("datasets/knowledge_text.csv", index=False)
    print("✅ Knowledge base built and saved successfully!")


if __name__ == "__main__":
    build_knowledge_base()
