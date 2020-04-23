#!/usr/bin/python3
"""
This module inits a Flask application server
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
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
    storage.close()
    amenities = storage.all(Amenity)
    amens = []
    try:
        for ameni in amenities.items():
            #print(ameni[1].name)
            amens.append(ameni[1].name)
        for st in states:
            print(st[1])
            for cit in st[2]:
                print('\t', cit['name'])
        for am in amens:
            print(am)
    except Exception as e:
        print(e)
    #print('\n\n\t\tStates:\n', states, '\n\n\t\tAmenities', amenities)
    return render_template("10-hbnb_filters.html", **{'states': states, 'amenities': amens})

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Routing the main path
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
