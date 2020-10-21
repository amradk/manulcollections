#!/bin/sh
set -e

TEMPLATE="/library/mylibrary/settings.tmpl"
CURDIR=$(pwd)

if [ "x${DB_HOST}" == "x" ]
then
  export DB_HOST='localhost'
fi

if [ "x${DB_PORT}" == "x" ]
then
  export DB_PORT='3306'
fi

if [ "x${DB_NAME}" == "x" ]
then
  export DB_NAME='bookshelf'
fi

if [ "x${DB_USER}" == "x" ]
then
  export DB_USER='librarian'
fi

if [ "x${DB_PASS}" == "x" ]
then
  export DB_USER='librarianpass'
fi

cat ${TEMPLATE} | envsubst > "/library/mylibrary/settings.py"
/library/start.sh
