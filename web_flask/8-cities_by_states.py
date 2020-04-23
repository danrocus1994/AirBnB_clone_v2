#!/usr/bin/python3
"""
This module inits a Flask application server
"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template


def get_name(name):
        """Get element by name"""
        return name[1]


def get_cities(city):
        """Get element by name"""
        return city.name


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(uknown):
    """
    apply a close to the storage engine to reload
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    List all state in db
    """
    states = storage.all(State)
    resp = {}
    for state_id, state in states.items():
        resp[state_id.split('.')[1]] = state.name
    states = []
    for key in sorted(resp, key=resp.get, reverse=False):
        states.append((key, resp[key]))
    return render_template("7-states_list.html", states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states_list():
    """
    List all Cities in db
    """
    states = storage.all(State)
    resp = []
    for state_id, state in states.items():
        resp.append([state_id.split('.')[1], state.name, state.cities])
    states = []
    for el in sorted(resp, key=get_name, reverse=False):
        cities = sorted(el[2], key=get_cities, reverse=False)
        cities = [{'name': citi.name, 'id': citi.id} for citi in cities]
        states.append((el[0], el[1], cities))
    return render_template("8-cities_by_states.html", states=states)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Routing the main path
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
