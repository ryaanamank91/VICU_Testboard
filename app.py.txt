from flask import Flask, render_template, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    simulated_data = {
        "timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "vehicle_id": "TESTVIN123456789",
        "data": {
            "engine_speed_rpm": random.randint(800, 4000),
            "vehicle_speed_kmh": random.randint(0, 120),
            "mileage_km": random.randint(10000, 150000),
            "battery_voltage_v": round(random.uniform(11.5, 14.8), 2),
            "fuel_level_percent": random.randint(0, 100),
            "engine_temp_c": random.randint(70, 110),
            "gps": {
                "lat": round(40.4168 + random.uniform(-0.01, 0.01), 6),
                "lon": round(-3.7038 + random.uniform(-0.01, 0.01), 6)
            },
            "ignition_on": random.choice([True, False])
        }
    }
    return jsonify(simulated_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
