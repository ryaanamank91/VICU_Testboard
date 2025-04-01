from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify({
        "timestamp": datetime.utcnow().isoformat(),
        "vehicle_id": "VICU001",
        "data": {
            "engine_speed_rpm": 2733,
            "vehicle_speed_kmh": 42,
            "battery_voltage": 13.8,
            "fuel_level": 57,
            "engine_temp": 82,
            "ignition_on": True,
            "gps": {
                "lat": 48.8566,
                "lon": 2.3522
            }
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
