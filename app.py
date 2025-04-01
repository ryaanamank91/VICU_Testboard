from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
latest_data = {
    "vehicle_id": "N/A",
    "engine_speed_rpm": 0,
    "speed": 0,
    "mileage": 0,
    "battery_voltage": 0.0,
    "fuel_level": 0,
    "engine_temp": 0,
    "latitude": 0.0,
    "longitude": 0.0,
    "ignition": "OFF",
    "timestamp": "N/A"
}

@app.route('/')
def dashboard():
    return render_template("index.html", data=latest_data)

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    new_data = request.get_json()
    new_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_data.update(new_data)
    print("Updated Data:", latest_data)
    return "OK", 200
