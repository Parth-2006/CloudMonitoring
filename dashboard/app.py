from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def home():

    with open("../monitor/data.json") as f:
        data = json.load(f)

    return f"""
    <h1>Cloud Monitoring Dashboard</h1>

    CPU Usage: {data['cpu']}%<br>
    RAM Usage: {data['ram']}%<br>
    Disk Usage: {data['disk']}%
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
