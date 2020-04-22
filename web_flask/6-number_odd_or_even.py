#!/usr/bin/python3
"""
This module inits a Flask application server
"""


from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def number_route(n):
    """
    Routing the main path
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    Routing the main path
    """
    template = render_template("5-number.html", number=n)
    return template


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Routing the main path
    """
    state = "odd" if n % 2 != 0 else "even"
    template = render_template("6-number_odd_or_even.html", number=n, st=state)
    return template


@app.route('/python', methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python_route(text="is_cool"):
    """
    Routing the main path
    """
    return "Python " + text.replace("_", " ")


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c_route(text):
    """
    Routing the main path
    """
    return "C " + text.replace("_", " ")


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """
    Routing the main path
    """
    return "HBNB"


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Routing the main path
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
