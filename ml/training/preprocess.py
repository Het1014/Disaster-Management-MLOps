import pandas as pd
import re

CATEGORIES = ["earthquake", "floods", "storm", "fire"]
PRIORITY = ["earthquake", "floods", "storm", "fire"]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def get_dominant_label(row):
    for cat in PRIORITY:
        if row[cat] == 1:
            return cat
    return None

def preprocess_file(input_path, output_path):
    df = pd.read_csv(input_path)

    df = df[["message"] + CATEGORIES]
    df["label"] = df.apply(get_dominant_label, axis=1)
    df = df.dropna(subset=["label"])

    df["clean_message"] = df["message"].apply(clean_text)
    df = df[["clean_message", "label"]]

    df.to_csv(output_path, index=False)
    print(f"[OK] Saved: {output_path}")

if __name__ == "__main__":
    preprocess_file(
        "../../data/raw/disaster_response_messages_training.csv",
        "../../data/processed/train_clean.csv"
    )

    preprocess_file(
        "../../data/raw/disaster_response_messages_validation.csv",
        "../../data/processed/validation_clean.csv"
    )

    preprocess_file(
        "../../data/raw/disaster_response_messages_test.csv",
        "../../data/processed/test_clean.csv"
    )