from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

from utils.recommend import get_recommendation

app = Flask(__name__)
CORS(app)

# Endpoint proxy ke ML API di Railway, contoh respons ("type": "oily")
@app.route("/analyze", methods=["POST"])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400

    file = request.files['file']
    files = {'file': (file.filename, file.stream, file.mimetype)}

    try:
        ml_url = "https://ml-skinsync-api-production.up.railway.app/predict"
        response = requests.post(ml_url, files=files)
        return response.json(), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    skin_type = data.get("type")  # misalnya "oily"

    if not skin_type:
        return jsonify({'error': 'Skin type is required'}), 400

    rec = get_recommendation(skin_type)
    if not rec:
        return jsonify({'error': 'Invalid skin type'}), 400

    return jsonify(rec)

@app.route("/")
def home():
    return jsonify({"message": "SkinSync Backend is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)