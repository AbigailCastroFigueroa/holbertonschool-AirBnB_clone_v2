#!/usr/bin/python3
"""Script that start a flask application."""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return a given message."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def message1():
    """Return a given message."""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
