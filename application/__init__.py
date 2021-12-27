from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import uuid

app = Flask(__name__)

# Set the db connection string using environment variable
# export DATABASE_URI=<DB server connection string>
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = str(uuid.uuid4())

db = SQLAlchemy(app)

from application import routes