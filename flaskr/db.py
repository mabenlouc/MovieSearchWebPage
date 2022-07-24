import sqlite3
from flask import g

DATABASE = 'movies.db'

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)

    return g.db

def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)