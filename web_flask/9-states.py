#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    """
    Call in this method storage.close()
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """
    return the render of 7-states_list.html
    """
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """
    return the render of 9-states.html
    """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
