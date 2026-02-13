import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

TRAIN_PATH = "../../data/processed/train_clean.csv"
VAL_PATH = "../../data/processed/validation_clean.csv"
MODEL_PATH = "../models/model_v1.joblib"

def train():
    train_df = pd.read_csv(TRAIN_PATH)
    val_df = pd.read_csv(VAL_PATH)

    X_train = train_df["clean_message"]
    y_train = train_df["label"]

    X_val = val_df["clean_message"]
    y_val = val_df["label"]

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=3000)),
        ("clf", LogisticRegression(max_iter=200))
    ])

    pipeline.fit(X_train, y_train)

    val_score = pipeline.score(X_val, y_val)
    print(f"[INFO] Validation accuracy (v1): {val_score:.4f}")

    joblib.dump(pipeline, MODEL_PATH)
    print("[OK] model_v1.joblib saved")

    
    mlflow.set_tracking_uri("file:./mlruns")
    mlflow.set_experiment("First")

    with mlflow.start_run():
        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("max_features", 3000)
        mlflow.log_metric("val_accuracy", val_score)
        mlflow.sklearn.log_model(pipeline, "model")
if __name__ == "__main__":
    train()
