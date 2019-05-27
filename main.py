#!/usr/local/bin/python

import os
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    html = '<html><title>welcome</title>'
    html = html + '<body>welcome</body></html>'
    return html

@app.route('/project_card', methods=["GET", "POST"])
def card():
    if request.method == 'GET':
        return"GET"
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        print(data)
        return jsonify(res='ok')
    return jsonify(res='505')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)