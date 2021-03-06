#!/usr/bin/python3
"""
This module inits a Flask application server
"""


from flask import Flask


app = Flask(__name__, root_path='')


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def number_route(n):
    return "{} is a number".format(n)


@app.route('/python', methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python_route(text="is_cool"):
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
