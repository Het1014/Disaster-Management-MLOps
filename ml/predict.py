import re
import numpy as np
from model_loader import load_model

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def predict_message(text: str):
    model = load_model()
    cleaned = clean_text(text)

    probs = model.predict_proba([cleaned])[0]
    classes = model.classes_

    idx = np.argmax(probs)
    prediction = classes[idx]
    confidence = float(probs[idx])

    return {
        "prediction": prediction,
        "confidence": round(confidence, 4)
    }

if __name__ == "__main__":
    # quick local test
    sample = "Heavy floods have destroyed houses and roads"
    result = predict_message(sample)
    print(result)
