from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulated dummy vehicle data (you can replace with real JSON input later)
vehicle_data = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "vehicle_id": "VICU-ESP32-01",
    "data": {
        "engine_speed_rpm": 1750,
        "vehicle_speed_kmh": 68,
        "mileage_km": 12457,
        "battery_voltage": 12.7,
        "fuel_level": 48,
        "engine_temp": 87,
        "gps": {"lat": 40.4168, "lon": -3.7038},
        "ignition_on": True
    }
}

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # You can plug in real-time logic here
    return jsonify(vehicle_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
