# min_hpp
Minimum Heroku Python Postgress, with full python (sqlalchemy) implementation

## Objectives of this repo
+ Document how to create a database and connect it to a Flask App
+ Understand flask db migrate
+ Comprehend alembic
+ Long term reference on how to use databases in Flask
+ Use a basic scheduler

## Virtual environment
Change directory to local repo root. NOTE: venv is the standard name of a
virtual environment. You can change it, but it may just generate confusion
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to create a postgress database?
Database creation is not made in the APP. It's necessary to create the database
before the app deployment. Create a database on the CLI

1. Setup db and create username and password to access the db.
```
psql postgres
CREATE DATABASE <database_name>;
CREATE USER <username> WITH PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <username>;
```
2. replace the value in .env file for DATABASE_URL to your db 
```
DATABASE_URL=postgresql://{username}:{password}@localhost:5432/{dbname}
```

## Install the SQLAlchemy
`pip3 install Flask-SQLAlchemy`

## Remember that all apps going to heroku need gnicorn
`pip3 install gunicorn`

## Add the Procfile (only used for Heroku)
`touch Procfile`
+ Inside the Procfile add
`web: gunicorn app:app`
NOTE: the first app is the name of your master file, like main, app, or so

## How to avoid the scheduler to run twice?
Theorethically, either `app.run(use_reloader=False)` or `app.run(debug=False)`

However, it does not always work. As an alternative, in the main app.py file
```
if app.debug == False:
    # configure the scheduler
```

The solution may be to add preload to the Procfile, like this:
`web: gunicorn app:app --preload`

More information here [https://github.com/viniciuschiele/flask-apscheduler/issues/139]