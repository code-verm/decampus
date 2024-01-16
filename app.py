
from flask import Flask
from models import User, Book
from flask_pymongo import PyMongo
app = Flask(__name__)

# Import other modules here

if __name__ == "__app__":
    app.run(host='0.0.0.0', port=81, debug=True)
app.config["MONGO_URI"] = "mongodb+srv://adrishbora:fIrFnJafGOLS3gte@decampus-test-db-0.zybncgz.mongodb.net/?retryWrites=true&w=majority"

mongo = PyMongo(app)

from routes import *  # Import all routes from the routes file

