#!/usr/bin/python3
"""
This module inits a Flask application server
"""


from flask import Flask


app = Flask(__name__, root_path='')


@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python_route(text):
    return "Python " + text.replace("_", " ")


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c_route(text):
    return "C " + text.replace("_", " ")


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Routing the main path
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
