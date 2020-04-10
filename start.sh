#!/bin/sh

. ./bin/activate

export FLASK_APP=./library.py

flask db migrate -m "Some new migration"
flask db upgrade

#flask run
gunicorn --bind 127.0.0.1:5060 library:app


