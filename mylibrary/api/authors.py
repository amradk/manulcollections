# -*- coding: utf-8 -*-

from . import bp
from flask import request, jsonify, make_response
from mylibrary import db
from mylibrary.models import Book, Author, Translator, Serie, Publisher, Genre, Editor, Composition
from sqlalchemy import and_

@bp.route('/author/<int:id>', methods=['GET'])
def api_get_author_by_id(id):
    pass

@bp.route('/author/<string:name>', methods=['GET'])
def api_get_author_by_name(name):
    a = Author.query.filter(and_(Author.name == name.split[1], Author.surname == name.split[0])).first()
    response = make_response(
        jsonify({
            'id': a.id,
            'aname': a.name,
            'asurname': a.surname,
        })
    )
    return response

@bp.route('/authors', methods=['GET'])
def api_get_authors():
    term = request.args.get('term')
    if term and term != "":
        authors = Author.query.filter(Author.surname.like('%' + term + '%'))
    else:
        authors = Author.query.with_entities(Author.id, Author.name, Author.surname)
    a_json = []

    #ДК, строим JSON

    #ДК, для jQueryUI нужно возвражать просто список значений
    #за это отвечает параметр plain
    plain = request.args.get('plain')
    if plain and (plain == 'true' or plain == "1"):
        for a in authors:
            a_json.append(a.surname + " " + a.name)
    else:
        for a in authors:
            a_json.append(
                {
                    'id':a.id,
                    'aname':a.name,
                    'asurname':a.surname,
                }
            )

    response = make_response(jsonify(a_json))
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response
