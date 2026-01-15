from flask import Flask, jsonify, request
import requests
from config import Config



app = Flask(__name__)
@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Config.WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            return jsonify({"error": data.get("message", "Failed to fetch weather data")}), response.status_code
        return jsonify({
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        })
    except requests.RequestException as e:
        return jsonify({"error": "An error occurred while fetching weather data"}), 500
    
   
if __name__ == "__main__":
    app.run(debug=True)
