# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('api', __name__, template_folder='../template', url_prefix='/api')
from . import publisher