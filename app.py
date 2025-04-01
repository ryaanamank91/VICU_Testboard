from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
latest_data = {
    "timestamp": "Waiting for data...",
    "vehicle_id": "VICU-ESP32-01",
    "engine_speed_rpm": 0,
    "vehicle_speed_kmh": 0,
    "battery_voltage": 0.0,
    "fuel_level": 0,
    "engine_temp": 0,
    "ignition_on": False,
    "gps": {"lat": 0.0, "lon": 0.0}
}

@app.route('/')
def dashboard():
    return render_template("index.html", data=latest_data)

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    json_data = request.get_json()

    # Merge new data into the latest_data structure
    if "data" in json_data:
        latest_data.update(json_data["data"])
        latest_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        latest_data["vehicle_id"] = json_data.get("vehicle_id", "VICU-ESP32-01")
        print("Received data:", latest_data)

    return "OK", 200

# Don't run app.run() here. Render auto-handles this. Just push this file.
