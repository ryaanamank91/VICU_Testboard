from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
latest_data = {
    "timestamp": "Waiting for data...",
    "vehicle_id": "VICU-ESP32-01",
    "engine_speed_rpm": 0,
    "speed_kmph": 0,
    "mileage_km": 0,
    "battery_voltage": 0,
    "fuel_level_percent": 0,
    "engine_temp_celsius": 0,
    "latitude": 0.0,
    "longitude": 0.0,
    "ignition": "OFF"
}

@app.route('/')
def dashboard():
    return render_template("index.html", data=latest_data)

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    incoming = request.get_json()
    incoming['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_data.update(incoming)
    print("Data received:", latest_data)
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
