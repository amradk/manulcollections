# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, redirect, render_template
from . import db
from mylibrary.models import Book, Author, Translator, Serie, Publisher, Genre, Editor, Composition
from sqlalchemy import and_

bp = Blueprint('author', __name__, template_folder='template', url_prefix='/author')

@bp.route('/')
def authors_path():
    authors = Author.query.with_entities(Author.id, Author.surname, Author.name)
    return render_template('authors.html', list=authors)

@bp.route('/info', methods=['GET', 'POST'])
def author_info_path():
    author_id = request.args.get('author_id')
    author = Author.query.get(author_id)
    cmps = Composition.query.filter(Composition.author.any(Author.id == author_id))

    books = []
    for cmp in cmps:
        book = Book.query.filter(Book.composition.any(Composition.id == cmp.id)).first()
        if book not in books:
            books.append(book)

    return render_template('author_info.html',author=author, books=books)

@bp.route('/edit', methods=['GET', 'POST'])
def author_edit_path():

    author_id = request.args.get('author_id')
    author = Author.query.get(author_id)

    if request.method == 'POST':
        author.name = request.args.get('aname')
        author.surname = request.args.get('asurname')
        author.note = request.args.get('anote')
        db.session.add(author)

    return render_template('author_edit.html',author=author)