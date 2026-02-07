from flask import Flask, request, jsonify
from predict import predict_message

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ML service running"}, 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 400

    result = predict_message(data["message"])
    return jsonify(result), 200

if __name__ == "__main__":
    # Important: 0.0.0.0 for Docker
    app.run(host="0.0.0.0", port=5000)
