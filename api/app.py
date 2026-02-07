from flask import Flask, request, jsonify
import requests
from config import ML_SERVICE_URL

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "API service running"}, 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 400

    response = requests.post(
        f"{ML_SERVICE_URL}/predict",
        json={"message": data["message"]},
        timeout=15
    )

    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
