#!/usr/bin/python3
""" Nameless Module for Flask """
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """ Print out HTML lisitng out all States """
    states_list = storage.all(State)

    # for key, value in states_list.items():
    #     print(key)
    #     print(value['name'])
    #     print("---")

    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
