#!/usr/bin/env bash

export FLASK_APP="app"
export FLASK_ENV="development"

python3 init_db.py
flask run --host=0.0.0.0
