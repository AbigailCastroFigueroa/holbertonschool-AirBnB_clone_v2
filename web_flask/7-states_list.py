#!/usr/bin/python3
"""Script to select data from the database."""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_search():
    """Retrieve selected data."""
    data = storage.all(State).values()
    return render_template('7-states_list.html', states=data)


@app.teardown_appcontext
def end_session(self):
    """Close session."""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
