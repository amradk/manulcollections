# -*- coding: utf-8 -*-

from . import bp
from flask import request, jsonify, make_response
from mylibrary.models import Genre
from sqlalchemy import and_

@bp.route('/genre/<int:id>', methods=['GET'])
def api_get_genre_by_id(id):
    pass

@bp.route('/genre/<string:name>', methods=['GET'])
def api_get_genre_by_name(name):
    g = Genre.query.filter(Genre.name == name).first()
    response = make_response(
        jsonify({
            'id': g.id,
            'gname': g.name,
        })
    )
    return response

@bp.route('/genres', methods=['GET'])
def api_get_genres():
    term = request.args.get('term')
    if term and term != "":
        genres = Genre.query.filter(Genre.name.like('%' + term + '%'))
    else:
        genres = Genre.query.with_entities(Genre.id, Genre.name)
    g_json = []

    #ДК, строим JSON

    #ДК, для jQueryUI нужно возвражать просто список значений
    #за это отвечает параметр plain
    plain = request.args.get('plain')
    if plain and (plain == 'true' or plain == "1"):
        for p in genres:
            g_json.append(g.name)
    else:
        for g in genres:
            g_json.append(
                {
                    'id':g.id,
                    'gname':g.name,
                }
            )

    response = make_response(jsonify(g_json))
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response
