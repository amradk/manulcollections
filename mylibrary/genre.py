# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, redirect, render_template
from . import db
from mylibrary.models import Book, Author, Translator, Serie, Publisher, Genre, Editor, Composition
from sqlalchemy import and_

bp = Blueprint('genre', __name__, template_folder='template', url_prefix='/genre')

@bp.route('/')
def genres_path():
    genres = Genre.query.with_entities(Genre.id, Genre.name)
    return render_template('genres.html', list=genres)

@bp.route('/info', methods=['GET', 'POST'])
def genres_info_path():
    genre_id = request.args.get('genre_id')
    genre = Genre.query.get(genre_id)

    cmps = Composition.query.filter(Composition.genre.any(Genre.id == genre_id))

    books = []
    for cmp in cmps:
        book = Book.query.filter(Book.composition.any(Composition.id == cmp.id)).first()
        if book not in books:
            books.append(book)

    return render_template('genre_info.html',genre=genre, books=books)

@bp.route('/edit', methods=['GET', 'POST'])
def genre_edit_path():

    genre_id = request.args.get('genre_id')
    genre = Genre.query.get(genre_id)

    if request.method == 'POST':
        genre.name = request.args.get('gname')
        genre.desc = request.args.get('gdesc')

        db.session.add(genre)

    return render_template('genre_edit.html', genre=genre)