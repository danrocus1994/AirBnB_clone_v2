#!/usr/bin/python3
"""
This module inits a Flask application server
"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(uknown):
    """
    apply a close to the storage engine to reload
    """
    print(uknown, type(uknown))
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    List all state in db
    """
    states = storage.all(State)
    resp = {}

    for state_id, state in states.items():
        print(state.name)
        resp[state_id.split('.')[1]] = state.name
    states = []
    for key in sorted(resp, key=resp.get, reverse=False):
        states.append((key, resp[key]))
    return render_template("7-states_list.html", states=states)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Routing the main path
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
