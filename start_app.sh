#!/bin/sh

. ./bin/activate
#export FLASK_APP=backend.py
#flask run
gunicorn --bind :5050 wsgi:app
