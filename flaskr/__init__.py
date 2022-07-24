from flask import Flask, render_template
from . import db
import json

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_pyfile('app_config.py', silent=True)
    columns = ['adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id', 'imdb_id', 'original_language', 'original_title', 
        'overview', 'popularity', 'poster_path', 'production_companies', 'production_countries', 'release_date', 'revenue',
        'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count']

    @app.route("/")
    def index():
        return "Hello COSC381!"

    @app.route("/api/v1/movies")
    def get_movies():
        cur = db.get_db().cursor()
        cur.execute('''SELECT * from movies LIMIT 10''')
        results = cur.fetchall()
        formatted_results = []
        for record in results:
            new_record = {}
            for idx, column in enumerate(columns):
                new_record[column] = record[idx]
            
            formatted_results.append(new_record)

        return json.dumps(formatted_results)

    @app.route("/movies")
    def view_movies():
        cur = db.get_db().cursor()
        cur.execute('''SELECT * from movies LIMIT 10''')
        results = cur.fetchall()
        formatted_results = []
        for record in results:
            new_record = {}
            for idx, column in enumerate(columns):
                new_record[column] = record[idx]

            formatted_results.append(new_record)
        
        return render_template("movies.html", movies=formatted_results)

    return app