import os
import sys
sys.path.insert(0, os.path.abspath('./'))
import settings
import pymongo

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__, template_folder='template') # create the application instance :)
app.config['SECRET_KEY']='HNdou238cxa03bHGAr'

mng_conn = pymongo.MongoClient(host=settings.db['host'], port=settings.db['port'])
db = mng_conn.client[settings.db['database']]

@app.route('/')
def index_path():
        return render_template('home.html')

@app.route('/books')
def books_path():
        return render_template('books.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_books_path():
    if request.method == 'POST':

        book = {}
        book['bname'] = request.form.get('bname')
        book['bisbn'] = request.form.get('bisbn')
        book['byear'] = request.form.get('byear')
        book['beditor'] = request.form.get('beditor')
        book['pname'] = request.form.get('pname')
        book['purl'] = request.form.get('purl')
        book['pcity'] = request.form.get('pcity')
        book['compositions'] = []
        f = request.form
        num_of_cmp = int((len(f) - 7)/4)
        for i in range(num_of_cmp):
            cur_cmp = 'cmp[' + str(i) + ']'
            book['compositions'].append({'aname':f[cur_cmp + '.aname'], \
                'cname':f[cur_cmp + '.cname'], 'ctranslator':f[cur_cmp + '.ctranslator'], \
                 'cgenre':f[cur_cmp + '.cgenre']})
        db.insert_one(book)

    return render_template('add_book.html')
