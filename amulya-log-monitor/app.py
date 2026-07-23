from flask import Flask, jsonify
from log_monitor import events

app = Flask(__name__)

@app.route("/")
def home():
    with open("index.html", "r") as file:
        return file.read()

@app.route("/api/events")
def api_events():
    return jsonify(events)

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        use_reloader=False
    )
