#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    """
    Call in this method storage.close()
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def city_list():
    """
    return the render of 10-hbnb_filters.html
    """
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
