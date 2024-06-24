# source: https://www.geeksforgeeks.org/flask-creating-first-simple-application/
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db_test import db
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)


class Second(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    min_transactions = db.Column(db.Integer)