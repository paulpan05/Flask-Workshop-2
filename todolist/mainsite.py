from flask import Blueprint, render_template, jsonify
from .db import get_db

bp = Blueprint('mainsite', __name__, url_prefix='/')

@bp.route('/')
def hello():
    print(get_db)
    return jsonify({'a': 12})