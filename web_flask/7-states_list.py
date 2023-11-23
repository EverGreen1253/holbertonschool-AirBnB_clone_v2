#!/usr/bin/python3
""" Nameless Module for Flask """
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """ Print out HTML lisitng out all States """
    unsorted_states = {}
    states_list = storage.all(State)
    for key, value in states_list.items():
        unsorted_states[value['name']] = {
            'id': value['id'],
            'name': value['name']
        }
    sorted_states = dict(sorted(unsorted_states.items()))
    # for key in sorted_states:
    #     print(key)
    #     print(sorted_states[key]['id'])

    return render_template('7-states_list.html', states_list=sorted_states)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
