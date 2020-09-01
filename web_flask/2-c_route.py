#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    method for say hello
    Returns:
        [str]: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb/', strict_slashes=False)
def hello_hbnb():
    """
    method for say hello
    Returns:
        [str]: "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    method for say hello
    Returns:
        [str]: "c and the value of text"
    """
    return "C %s" % text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
