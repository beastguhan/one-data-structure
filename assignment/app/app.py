from flask import Flask, jsonify
import socket
import random

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Hello from Flask App",
        "host": socket.gethostname()
    })

@app.route('/health')
def health():
    return "OK", 200

@app.route('/metrics')
def metrics():
    # Example metric for Prometheus
    cpu_load = random.uniform(0, 1)
    return f"# TYPE cpu_load gauge\ncpu_load {cpu_load}\n", 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
