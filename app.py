# source: https://www.geeksforgeeks.org/flask-creating-first-simple-application/
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db_test import db
# from card_test import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://one_user:one123400@localhost:5432/flask_one'


db = SQLAlchemy(app)
migrate = Migrate(app, db)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     age = db.Column(db.Integer)


class Second(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    min_transactions = db.Column(db.Integer)