#!/usr/bin/python3
""" Nameless Module for Flask """
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/filters", strict_slashes=False)
def filters():
    """ Print out HTML lisitng out all Cities by their States """
    state_cities = []
    amenities = []
    states_list = storage.all(State)
    sorted_states = sorted(states_list.values(), key=lambda s: s.name)

    amenities_list = storage.all(Amenity)
    sorted_amenities = sorted(amenities_list.values(), key=lambda a: a.name)

    for state in sorted_states:
        item = {}
        item['state'] = state

        cities = state.cities
        sorted_cities = sorted(cities, key=lambda c: c.name)

        item['cities'] = sorted_cities

        state_cities.append(item)

    for amenity in sorted_amenities:
        amenities.append(amenity.name)

    return render_template('10-hbnb_filters.html', state_cities=state_cities, amenities=amenities)



@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
