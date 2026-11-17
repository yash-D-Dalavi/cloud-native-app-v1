import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = "2.0.0"

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Cloud-Native Containerized Application!",
        "status": "Success",
        "version": APP_VERSION,
        "environment": os.getenv("APP_ENV", "development"),
        "served_by": socket.gethostname()
    })

@app.route('/health')
def health():
    return jsonify({"status": "Healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)