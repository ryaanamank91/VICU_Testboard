from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
latest_data = {}

@app.route('/')
def dashboard():
    return render_template("index.html", data=latest_data)

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    latest_data = request.get_json()
    latest_data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Data received:", latest_data)
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
