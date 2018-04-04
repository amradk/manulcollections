import os
import sys
sys.path.insert(0, os.path.abspath('./'))
import settings
import pymongo
import re
from bson.objectid import ObjectId

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__, template_folder='template') # create the application instance :)
app.config['SECRET_KEY']='HNdou238cxa03bHGAr'

mng_conn = pymongo.MongoClient(host=settings.db['host'], port=settings.db['port'])
db = mng_conn[settings.db['database']]
coll = db['books']

@app.route('/')
def index_path():
        return render_template('home.html')

@app.route('/books')
def books_path():
        books = list(coll.find({},{"bname":1, "byear":1, "pname":1}))
        #for book in books:
            #print(book)
        return render_template('books.html',list=books)

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
        coll.insert_one(book)

    return render_template('add_book.html')

@app.route('/book_info', methods=['GET', 'POST'])
def book_info_path():
    book_id = request.args.get('book_id')
    book = coll.find_one({'_id':ObjectId(book_id)})

    return render_template('book_info.html',book=book)

@app.route('/book_edit', methods=['GET', 'POST'])
def book_edit_path():
    book_id = request.args.get('book_id')
    book = coll.find_one({'_id':ObjectId(book_id)})

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
        coll.update_one({'_id':ObjectId(book_id)},{'$set':book})

    return render_template('book_edit.html',book=book)

#ДК, нужно добавить информацию об успешном уделении
@app.route('/book_del', methods=['GET','POST'])
def book_del_path():
    book_id = request.args.get('book_id')
    coll.delete_one({'_id':ObjectId(book_id)})

    return redirect("/books")

@app.route('/book_search', methods=['GET'])
def book_search_path():
    search_type = request.args.get('search_type')
    regx = '^' + request.args.get('search_expr')+'*'
    search_expr = re.compile(regx)
    result = list(coll.find({search_type:search_expr},{"bname":1, "byear":1, "pname":1}))

    return render_template('book_search.html',result=result,type=search_type)
