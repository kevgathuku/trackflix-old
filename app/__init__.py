from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Load configuration defaults from the config.py file in the root
# This file will be imported and the config extracted from it
# http://flask.pocoo.org/docs/0.11/api/#flask.Config.from_object
app.config.from_object('config')

# Initialize SQLAlchemy db
db = SQLAlchemy(app)

# Import the views handling the routes
from app import views
