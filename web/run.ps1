$env:FLASK_APP="app"
$env:FLASK_ENV="development"
python3 init_db.py
flask run --host=0.0.0.0