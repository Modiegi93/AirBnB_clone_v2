#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """ index """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ hbnb route """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ /c route """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ python route """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
