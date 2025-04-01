from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
latest_data = {
    "vehicle_id": "VICU-ESP32-01",
    "engine_speed_rpm": 0,
    "vehicle_speed_kmh": 0,
    "battery_voltage": 0.0,
    "fuel_level": 0,
    "engine_temp": 0,
    "ignition_on": False,
    "gps": {"lat": 0.0, "lon": 0.0},
    "timestamp": "Waiting for data..."
}

@app.route('/')
def dashboard():
    return render_template("index.html", data=latest_data)

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    json_data = request.get_json()

    if not json_data or 'data' not in json_data:
        return "Invalid payload", 400

    vehicle_id = json_data.get("vehicle_id", "Unknown")
    data = json_data["data"]

    latest_data = {
        "vehicle_id": vehicle_id,
        "engine_speed_rpm": data.get("engine_speed_rpm", 0),
        "vehicle_speed_kmh": data.get("vehicle_speed_kmh", 0),
        "battery_voltage": data.get("battery_voltage", 0.0),
        "fuel_level": data.get("fuel_level", 0),
        "engine_temp": data.get("engine_temp", 0),
        "ignition_on": data.get("ignition_on", False),
        "gps": data.get("gps", {"lat": 0.0, "lon": 0.0}),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("Data received:", latest_data)
    return "OK", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
