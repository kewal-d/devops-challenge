from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def time_service():
    ip = request.remote_addr
    current_time = datetime.utcnow().isoformat()
    return jsonify({
        "timestamp": current_time,
        "ip": ip
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
