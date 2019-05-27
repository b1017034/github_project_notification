#!/usr/local/bin/python

import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = '<html><title>welcome</title>'
    html = html + '<body>welcome</body></html>'
    return html

@app.route('/project_card', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return"GET"
    else:
        print(request)
        return request


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)