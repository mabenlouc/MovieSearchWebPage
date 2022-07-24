# MovieSearchWebPage
## To set up:
### 1) clone this repository to your machine

### 2) inside your local repository: create a virtual environment and activate it
```
python3 -m venv venv
source venv/bin/activate
```

### 3) install the dependencies in `requirements.txt`
```
python3 -m pip install -r requirements.txt
```
### 4) download the database
Under the root directory (NOT the flaskr folder)
```
wget https://github.com/COSC381-2021Fall/movies_data/raw/main/movies.db
```

### 5) run the flask app
Under the root directory (NOT the flaskr folder)
```
flask run --host 0.0.0.0
```
