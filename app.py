from flask import Flask, jsonify, request
from config import Config


app = Flask(__name__)
@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    