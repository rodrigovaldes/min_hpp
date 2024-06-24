# zero to hero inspiration: https://www.geeksforgeeks.org/flask-creating-first-simple-application/
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from flask_migrate import Migrate
# from db_test import db
import os
from dotenv import load_dotenv
from utils import print_message
load_dotenv()

# Get constants from the environment
uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

# Initialize the app
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = uri
db = SQLAlchemy(app)
migrate = Migrate(app, db)
scheduler = APScheduler()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/other')
def other():
    return render_template('other.html')

# Add the tables
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

if __name__ == '__main__':
   
   # scheduler.add_job(func=print_message, trigger='interval', seconds=2, id='printer')
   scheduler.add_job(func=print_message,
                     trigger='cron',
                     day_of_week='mon-sun',
                     hour=15,
                     minute=27,
                     id='printer')
   scheduler.start()

   # app.run(debug=False, host='0.0.0.0', use_reloader=False) ## USE RELOADER?
   app.run(debug=False, host='0.0.0.0')
   
