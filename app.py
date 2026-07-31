from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to call the API

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Flask Backend!",
        "status": "running",
        "port": 5000
    })

@app.route('/api/hello')
def hello():
    return jsonify({
        "message": "This is the Flask API endpoint",
        "data": ["item1", "item2", "item3"]
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)