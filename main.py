from flask import Flask

from models import User, Book  # Import your models once they're defined

from routes import *  # Import all routes from the routes file


app = Flask(__name__)


@app.route('/')
def index():
    return 'decampus'


app.run(host='0.0.0.0', port=81)
