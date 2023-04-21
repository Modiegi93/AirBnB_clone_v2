#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)


def cities_by_states():
    """Displays a HTML page with a list of States and Cities"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    """ Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
