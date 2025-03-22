from flask import Flask, jsonify
import os

app = Flask(__name__)
@app.route('/')
def home():
    return "¡Hola desde mi contenedor personalizado en Cloud Native!"

@app.route('/status')
def status():
    return jsonify(status="ok", container=os.getenv("HOSTNAME"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)