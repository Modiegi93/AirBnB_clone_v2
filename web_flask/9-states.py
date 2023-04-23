#!/usr/bin/python3
""" Flask web application that displays States and Cities """

from flask import Flask, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """ closes the storage on teardown """
    storage.close()


@app.route('/states', strict_slashes=False, defaults={'id': None})
@app.route('/states/<id>', strict_slashes=False)
def show_states(id):
    """Display the states and cities listed in alphabetical order"""
    state = states = None
    if not id:
        states = list(storage.all(State).values())
    else:
        states = storage.all(State)
        key = "State." + id
        if key in states:
            state = states[key]
        else:
            state = None
        states = []
    return render_template('9-states.html', states=states, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
