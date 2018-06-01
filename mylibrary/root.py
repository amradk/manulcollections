# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

bp = Blueprint('root', __name__, template_folder='template')

@bp.route('/')
def index_path():
        return render_template('home.html')



