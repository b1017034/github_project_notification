#!/usr/local/bin/python

import os
from flask import Flask, request, jsonify
from slacker import Slacker
import hashlib
import hmac


app = Flask(__name__)
slack = Slacker(os.environ["API_TOKEN"])

@app.route('/')
def index():
    html = '<html><title>welcome</title>'
    html = html + '<body>welcome</body></html>'
    return html

@app.route('/project_card', methods=["GET", "POST"])
def card():
    #get
    if request.method == 'GET':
        return"GET"

     #post
    if request.method == 'POST':
        if not is_valid_key(request.headers.get('X-Hub-Signature'), request.get_data()):
            return jsonify(res='not key')
        data = request.get_json()

        if data['action'] == "created":
            slack.chat.post_message('#test1', create_card(data))
        return jsonify(res='ok')
    return jsonify(res='505')

def is_valid_key(key, payload):
    if key:
        hasher = hmac.new(os.environ['secret'].encode(), payload, hashlib.sha1)
        signature = 'sha1=' + hasher.hexdigest()
        return hmac.compare_digest(signature, key)


def create_card(json):
    name = json['sender']['login']
    card_name = json['project_card']['note']
    return "created: " + card_name + "\n" + "by: " + name


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)