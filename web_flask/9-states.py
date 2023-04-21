#!/usr/bin/python3
""" Flask web application that displays States and Cities """

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states', strict_slashes=False
@app.route('/states/<state_id>', strict_slashes=False)
def show_states(state_id=None):
    """Display the states and cities listed in alphabetical order"""
    states = storage.all("State").values()
    if state_id:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def close_session(exception):
    """ closes the storage on teardown """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
