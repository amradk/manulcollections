# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, redirect, render_template
from . import db
from mylibrary.models import Book, Author, Translator, Serie, Publisher, Genre, Editor, Composition
from sqlalchemy import and_

bp = Blueprint('book', __name__, template_folder='template', url_prefix='/book')

@bp.route('/', methods=['GET'])
def books_path():
        books = Book.query.all()
        return render_template('books.html',list=books)

@bp.route('/add', methods=['GET', 'POST'])
def add_books_path():
    if request.method == 'POST':

        book = Book(request.form.get('bname'), request.form.get('bisbn'), request.form.get('byear'))
        book.volume = request.form.get('bvol')
        editor_name = request.form.get('beditor').split()
        editor = Editor.query.filter(and_(Editor.surname==editor_name[0], Editor.name==editor_name[1])).first()
        #DK, check if editor in DB
        if editor is None:
            editor = Editor(editor_name[1], editor_name[0])
            db.session.add(editor)
        book.editor.append(editor)
        publisher = Publisher.query.filter(Publisher.name == request.form.get('pname')).first()
        if publisher is None:
            publisher = Publisher(request.form.get('pname'), request.form.get('purl'), request.form.get('pcity'))
            db.session.add(publisher)
        book.publisher.append(publisher)

        #ДК, серии пока не поддерживаются
        #serie_name = request.form.get('pname')
        #serie = Serie.query.get(Serie.name == )

        num_of_cmp = int((len(request.form) - 7)/4)
        for i in range(num_of_cmp):
            author_name = request.form.get('cmp[' + str(i) + '].aname').split()
            author = Author.query.filter(Author.name == author_name[1], Author.surname == author_name[0]).first()
            if author is None:
                author = Author(author_name[1], author_name[0])
                db.session.add(author)

            tr_name = request.form.get('cmp[' + str(i) + '].ctranslator')
            if tr_name != "":
                tr_name = tr_name.split()
                translator = Translator.query.filter(Translator.name == tr_name[1], Translator.surname == tr_name[0]).first()
                if translator is None:
                    translator = Translator(tr_name[1], tr_name[0])
                    db.session.add(translator)
            else:
                translator = None

            genre_name = request.form.get('cmp[' + str(i) + '].cgenre')
            genre = Genre.query.filter(Genre.name == genre_name ).first()
            if genre is None:
                genre = Genre(genre_name)
                db.session.add(genre)

            composition = Composition.query.filter(Composition.name == request.form.get('cmp[' + str(i) + '].cname')).first()
            if composition is None:
                composition = Composition(request.form.get('cmp[' + str(i) + '].cname'))
            composition.author.append(author)
            composition.genre.append(genre)
            if translator != None:
                composition.translator.append(translator)
            db.session.add(composition)

            book.composition.append(composition)

        db.session.add(book)
        db.session.commit()

    return render_template('add_book.html')

@bp.route('/info', methods=['GET', 'POST'])
def book_info_path():
    book_id = request.args.get('book_id')
    book = Book.query.get(book_id)

    return render_template('book_info.html',book=book)

@bp.route('/edit', methods=['GET', 'POST'])
def book_edit_path():
    book_id = request.args.get('book_id')
    book = Book.query.get(book_id)

    if request.method == 'POST':
        editor_name = request.form.get('beditor').split()
        editor = Editor.query.filter(and_(Editor.surname == editor_name[0], Editor.name == editor_name[1])).first()
        # DK, check if editor in DB
        if editor is None:
            editor = Editor(editor_name[1], editor_name[0])
            db.session.add(editor)
        book.editor.append(editor)
        publisher = Publisher.query.filter(Publisher.name == request.form.get('pname')).first()
        if publisher is None:
            publisher = Publisher(request.form.get('pname'), request.form.get('purl'), request.form.get('pcity'))
            db.session.add(publisher)
        book.publisher.append(publisher)
        book.name = request.form.get('bname')
        book.isbn = request.form.get('bisbn')
        book.year = request.form.get('byear')
        book.note = request.form.get('bnote')

        # ДК, серии пока не поддерживаются
        # serie_name = request.form.get('pname')
        # serie = Serie.query.get(Serie.name == )

        num_of_cmp = int((len(request.form) - 7) / 4)
        for i in range(num_of_cmp):
            author_name = request.form.get('cmp[' + str(i) + '].aname').split()
            author = Author.query.filter(Author.name == author_name[1], Author.surname == author_name[0]).first()
            if author is None:
                author = Author(author_name[1], author_name[0])
                db.session.add(author)

            tr_name = request.form.get('cmp[' + str(i) + '].ctranslator').split()
            translator = Translator.query.filter(Translator.name == tr_name[1],
                                                 Translator.surname == tr_name[0]).first()
            if translator is None:
                translator = Translator(tr_name[1], tr_name[0])
                db.session.add(translator)

            genre_name = request.form.get('cmp[' + str(i) + '].cgenre')
            genre = Genre.query.filter(Genre.name == genre_name).first()
            if genre is None:
                genre = Genre(genre_name)
                db.session.add(genre)

            composition = Composition.query.filter(
                Composition.name == request.form.get('cmp[' + str(i) + '].cname')).first()
            if composition is None:
                composition = Composition(request.form.get('cmp[' + str(i) + '].cname'))
            composition.author.append(author)
            composition.genre.append(genre)
            composition.translator.append(translator)
            #composition.annotation = request.form.get('cmp[' + str(i) + '].cannotation')
            db.session.add(composition)

            book.composition.append(composition)

        db.session.add(book)
        db.session.commit()

    return render_template('book_edit.html',book=book)

#ДК, нужно добавить информацию об успешном уделении
@bp.route('/del', methods=['GET','POST'])
def book_del_path():
    book_id = request.args.get('book_id')
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect("/books")

@bp.route('/search', methods=['GET'])
def book_search_path():
    search_type = request.args.get('search_type')
    regx = '^' + request.args.get('search_expr')+'*'
    search_expr = re.compile(regx)
    result = list(coll.find({search_type:search_expr},{"bname":1, "byear":1, "pname":1}))

    return render_template('book_search.html',result=result,type=search_type)