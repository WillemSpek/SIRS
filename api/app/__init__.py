import os

from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# app.config['MONGO_URI'] = os.environ.get('MOGNO_URI')

# mongodb_client = PyMongo(app)
# db = mongodb_client.db

from app import routes