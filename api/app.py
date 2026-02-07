from flask import Flask, request, jsonify
import requests
from config import ML_SERVICE_URL
from db import get_connection

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 400

    message = data["message"]

    # Call ML service
    ml_response = requests.post(
        f"{ML_SERVICE_URL}/predict",
        json={"message": message},
        timeout=15
    )
    result = ml_response.json()

    # Store in DB
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO predictions_log (message, prediction, confidence)
        VALUES (%s, %s, %s)
        """,
        (message, result["prediction"], result["confidence"])
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
