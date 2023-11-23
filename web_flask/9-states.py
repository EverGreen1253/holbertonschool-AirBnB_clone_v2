#!/usr/bin/python3
""" Nameless Module for Flask """
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=""):
    """ Print out HTML lisitng out all Cities by their States """
    data = []
    invalid_id = True
    states_list = storage.all(State)
    sorted_states = sorted(states_list.values(), key=lambda s: s.name)

    for state in sorted_states:
        item = {}
        item['state'] = state

        # print(state.id)
        # print(state.name)

        if state.id == id:
            invalid_id = False

        cities = state.cities
        sorted_cities = sorted(cities, key=lambda c: c.name)

        item['cities'] = sorted_cities

        # for city in sorted_cities:
        #     print(city.id)
        #     print(city.name)
        # print('---')

        data.append(item)

    return render_template('9-states.html', data=data, id=id, invalid_id=invalid_id)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
