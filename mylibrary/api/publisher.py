# -*- coding: utf-8 -*-

from . import bp
from flask import request, jsonify, make_response
from mylibrary import db
from mylibrary.models import Book, Author, Translator, Serie, Publisher, Genre, Editor, Composition
from sqlalchemy import and_

@bp.route('/publisher/<int:id>', methods=['GET'])
def api_get_publisher_by_id(id):
    pass

@bp.route('/publisher/<string:name>', methods=['GET'])
def api_get_publisher_by_name(name):
    p = Publisher.query.filter(Publisher.name == name).first()
    response = make_response(
        jsonify({
            'id': p.id,
            'pname': p.name,
            'pcity': p.city,
            'purl': p.url
        })
    )
    return response

@bp.route('/publishers', methods=['GET'])
def api_get_publishers():
    term = request.args.get('term')
    if term and term != "":
        publishers = Publisher.query.filter(Publisher.name.like('%' + term + '%'))
        print(term)
    else:
        publishers = Publisher.query.with_entities(Publisher.id, Publisher.name, Publisher.city, Publisher.url)
    pub_json = []

    #ДК, строим JSON

    #ДК, для jQueryUI нужно возвражать просто список значений
    #за это отвечает параметр plain
    plain = request.args.get('plain')
    if plain and (plain == 'true' or plain == 1):
        for p in publishers:
            pub_json.append(p.name)
    else:
        for p in publishers:
            pub_json.append(
                {
                    'id':p.id,
                    'pname':p.name,
                    'pcity':p.city,
                    'purl':p.url
                }
            )

    response = make_response(jsonify(pub_json))
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response
