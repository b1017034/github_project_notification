#!/usr/local/bin/python

import os
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    html = '<html><title>welcome</title>'
    html = html + '<body>welcome</body></html>'
    return html

@app.route('/project_card', methods=["GET", "POST"])
def card():
    if request.method == "GET":
        return"GET"
    else:
        print(request.data)

        data = request.data
        data = json.loads(data)

        print(data['zen'])

        return app.jsonify(res='ok')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)