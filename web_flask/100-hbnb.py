#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
from models import State, Amenity, Place
from models import storage
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """display a HTML page like 6-index.html from static"""
    state = storage.all(State)
    amenities = storage.all(Amenity)
    place = storage.all(Place)
    return render_template('100-hbnb.html', states=states, amenities=amenities,
                           place=place)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
