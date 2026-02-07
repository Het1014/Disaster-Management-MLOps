import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "model_v1.joblib")

_model = None

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
        print("[INFO] Baseline model loaded")
    return _model
