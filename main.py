#!/usr/local/bin/python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    html = '<html><title>welcome</title>'
    html = html + '<body>welcome</body></html>'
    return html

if __name__ == '__main__':
    app.run()
