# Imports
from flask import Flask
app = Flask(__name__)




# Config
import os
import Flask-SQLAlchemy
from Flask-SQLAlchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'server.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# Database
app.config.from_object('config')
db = SQLAlchemy
from migrate.versioning import api


import os.path
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))


# User Information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Strings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    String = db.Column(db.String(20), index=True, unique=True)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/tuesday')
def tuesday():
    return

@app.route('/hello')
def hello():
    return 'Hello, World!'

app.run()