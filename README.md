# min_hpp
Minimum Heroku Python Postgress, with full python (sqlalchemy) implementation

## Objectives of this repo
+ Document how to create a database and connect it to a Flask App
+ Understand flask db migrate
+ Comprehend alembic
+ Long term reference on how to use databases in Flask

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

1. Setup db and create username and password to access the db
```
psql postgres
CREATE DATABASE <database_name>;
CREATE USER <username> WITH PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <username>;
```
### DELTE THIS postgres=# CREATE USER rhpp  WITH PASSWORD 'hpp1234!@#$'; ###

2. replace the value in .env file for DATABASE_URL to your db 
```
DATABASE_URL=postgresql://{username}:{password}@localhost:5432/{dbname}
```


