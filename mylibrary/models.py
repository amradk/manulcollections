#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

from mylibrary import db

rel_cmp_translator = db.Table('rel_cmp_translator',
    db.Column('composition_id', db.Integer, db.ForeignKey('composition.id'), primary_key = True),
    db.Column('translator_id', db.Integer, db.ForeignKey('translator.id'), primary_key = True)
)

rel_cmp_author = db.Table('rel_cmp_author',
    db.Column('composition_id', db.Integer, db.ForeignKey('composition.id'), primary_key = True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key = True)
)

rel_cmp_genre = db.Table('rel_cmp_genre',
    db.Column('composition_id', db.Integer, db.ForeignKey('composition.id'), primary_key = True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key = True)
)

rel_book_editor = db.Table('rel_book_editor',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key = True),
    db.Column('editor_id', db.Integer, db.ForeignKey('editor.id'), primary_key = True)
)

rel_book_publisher = db.Table('rel_book_publisher',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key = True),
    db.Column('publisher_id', db.Integer, db.ForeignKey('publisher.id'), primary_key = True)
)

rel_book_serie = db.Table('rel_book_serie',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key = True),
    db.Column('serie_id', db.Integer, db.ForeignKey('serie.id'), primary_key = True)
)

rel_book_genre = db.Table('rel_book_genre',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key = True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key = True)
)

rel_book_composition = db.Table('rel_book_composition',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key = True),
    db.Column('composition_id', db.Integer, db.ForeignKey('composition.id'), primary_key = True)
)

class Translator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80, collation='utf8_general_ci'), unique=False, nullable=False)
    surname = db.Column(db.String(120, collation='utf8_general_ci'), unique=False, nullable=False)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80, collation='utf8_general_ci'), unique=True, nullable=False)
    desc = db.Column(db.Text(collation='utf8_general_ci'), unique=False, nullable=True)

    def __init__(self, name):
        self.name = name

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80, collation='utf8_general_ci'), unique=True, nullable=False)
    url = db.Column(db.String(120, collation='utf8_general_ci'), unique=True, nullable=True)
    city = db.Column(db.String(120, collation='utf8_general_ci'), unique=False, nullable=True)

    def __init__(self, name, url, city):
        self.name = name
        self.url = url
        self.city = city

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80, collation='utf8_general_ci'), unique=True, nullable=False)
    desc = db.Column(db.Text(collation='utf8_general_ci'), unique=False, nullable=True)

    def __init__(self, name):
        self.name = name

class Editor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80, collation='utf8_general_ci'), unique=False, nullable=False)
    surname = db.Column(db.String(120, collation='utf8_general_ci'), unique=False, nullable=False)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Composition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80, collation='utf8_general_ci'), unique=False, nullable=False)
    annotation = db.Column(db.Text(collation='utf8_general_ci'), unique=False, nullable=True)
    translator = db.relationship('Translator', secondary=rel_cmp_translator, lazy='subquery',
        backref="composition")
    author = db.relationship('Author', secondary=rel_cmp_author, lazy='subquery',
                                 backref="composition")
    genre = db.relationship('Genre', secondary=rel_cmp_genre, lazy='subquery',
                                 backref="genre")

    def __init__(self, name):
        self.name = name

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80, collation='utf8_general_ci'), unique=False, nullable=False)
    surname = db.Column(db.String(120, collation='utf8_general_ci'), unique=False, nullable=False)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80, collation='utf8_general_ci'), unique=False, nullable=False)
    isbn = db.Column(db.String(120, collation='utf8_general_ci'), unique=False, nullable=True)
    orig_name = db.Column(db.String(80, collation='utf8_general_ci'), unique=False, nullable=True)
    year = db.Column(db.String(80, collation='utf8_general_ci'), unique=False, nullable=False)
    note = db.Column(db.Text(collation='utf8_general_ci'), unique=False, nullable=True)
    volume = db.Comlumn(db.Integer, default=0)
    editor = db.relationship('Editor', secondary=rel_book_editor, lazy='subquery',
                                 backref="editor")
    publisher = db.relationship('Publisher', secondary=rel_book_publisher, lazy='subquery',
                                 backref="publisher")
    serie = db.relationship('Serie', secondary=rel_book_serie, lazy='subquery',
                                 backref="serie")
    genre = db.relationship('Genre', secondary=rel_book_genre, lazy='subquery',
                                 backref="bgenre")
    composition = db.relationship('Composition', secondary=rel_book_composition, lazy='subquery',
                            backref="composition")

    def __init__(self, name, isbn, year):
        self.name = name
        self.isbn = isbn
        self.year = year
