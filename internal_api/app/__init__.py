import os

from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MONGO_URI'] = os.environ.get('MOGNO_URI')

mongodb_client = MongoClient(app, tls=True, tlsCAFile='../certs/db_cert.pem')
db = mongodb_client.db

from app import routes
