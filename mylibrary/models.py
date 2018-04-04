from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Translator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(120), unique=False, nullable=False)

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.Text, unique=False, nullable=False)

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    city = db.Column(db.String(120), unique=False, nullable=False)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.Text, unique=False, nullable=False)

class Editor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(120), unique=False, nullable=False)

class Composition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    annotation = db.Column(db.Text, unique=False, nullable=False)
    translator = db.relationship('Translator', secondary=rel_cmp_translator, lazy='subquery',
        backref="composition")
    author = db.relationship('Author', secondary=rel_cmp_author, lazy='subquery',
                                 backref="composition")
    genre = db.relationship('Genre', secondary=rel_cmp_genre, lazy='subquery',
                                 backref="genre")

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(120), unique=False, nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    isbn = db.Column(db.String(120), unique=False, nullable=False)
    orig_name = db.Column(db.String(80), unique=False, nullable=False)
    year = db.Column(db.String(80), unique=False, nullable=False)
    note = db.Column(db.Text, unique=False, nullable=False)
    editor = db.relationship('Editor', secondary=rel_book_editor, lazy='subquery',
                                 backref="editor")
    publisher = db.relationship('Publisher', secondary=rel_book_publisher, lazy='subquery',
                                 backref="publisher")
    serie = db.relationship('Serie', secondary=rel_book_serie, lazy='subquery',
                                 backref="serie")
    genre = db.relationship('Genre', secondary=rel_book_genre, lazy='subquery',
                                 backref="genre")
    composition = db.relationship('Composition', secondary=rel_book_composition, lazy='subquery',
                            backref="composition")

rel_comp_translator = db.Table('rel_cmp_translator',
    db.Column('composition_id', db.Integer, db.ForeignKey('composition.id'), primaryKey = True),
    db.Column('translator_id', db.Integer, db.ForeignKey('translator.id'), primaryKey = True)
)

rel_comp_author = db.Table('rel_cmp_author',
    db.Column('composition_id', db.Integer, db.ForeignKey('composition.id'), primaryKey = True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primaryKey = True)
)

rel_comp_genre = db.Table('rel_cmp_genre',
    db.Column('composition_id', db.Integer, db.ForeignKey('composition.id'), primaryKey = True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primaryKey = True)
)

rel_book_editor = db.Table('rel_book_editor',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primaryKey = True),
    db.Column('editor_id', db.Integer, db.ForeignKey('editor.id'), primaryKey = True)
)

rel_book_publisher = db.Table('rel_book_publisher',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primaryKey = True),
    db.Column('publisher_id', db.Integer, db.ForeignKey('publisher.id'), primaryKey = True)
)

rel_book_serie = db.Table('rel_book_serie',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primaryKey = True),
    db.Column('serie_id', db.Integer, db.ForeignKey('serie.id'), primaryKey = True)
)

rel_book_genre = db.Table('rel_book_genre',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primaryKey = True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primaryKey = True)
)

rel_book_composition = db.Table('rel_book_composition',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primaryKey = True),
    db.Column('composition_id', db.Integer, db.ForeignKey('composition.id'), primaryKey = True)
)