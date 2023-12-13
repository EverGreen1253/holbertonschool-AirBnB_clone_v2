#!/usr/bin/python3
""" Nameless Module for Flask """
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State

app = Flask(__name__)
# app.config['DEBUG'] = False
app.config['FLASK_DEBUG'] = False


@app.route("/states_list", strict_slashes=False)
def states():
    """ Print out HTML lisitng out all States """
    states_list = storage.all(State)
    sorted_states = sorted(states_list.values(), key=lambda s: s.name)

    # print(sorted_states)

    return render_template('7-states_list.html', states_list=sorted_states)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
