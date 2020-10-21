#!/bin/sh

#. ./bin/activate

export FLASK_APP=./library.py

flask db migrate -m "Some new migration"
flask db upgrade

#flask run
gunicorn --bind 0.0.0.0:5060 library:app


