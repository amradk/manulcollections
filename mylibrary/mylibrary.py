import os
import settings
import pymongo

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__, template_folder='template') # create the application instance :)

mng_conn = pymongo.MongoClient(host=settings.db['host'], port=settings.db['port'])
db = mng_conn.client[settings.db['database']]

@app.route('/')
def index_path():
        return render_template('home.html')

@app.route('/books')
def books_path():
        return render_template('books.html')
