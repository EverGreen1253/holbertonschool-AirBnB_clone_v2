#!/usr/bin/python3
""" Nameless Module for Flask """
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Prints hello hbnb string """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Prints hbnb string """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Prints text passed in """
    return "C {0}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is_cool"):
    """ Prints text passed in """
    return "Python {0}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
