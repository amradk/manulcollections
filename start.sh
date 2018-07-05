#!/usr/bin/env bash

export FLASK_APP=./library.py

#flask db migrate -m "Some new migration"
#flask db upgrade

flask run

