import logging

from app.core import bp
from flask import jsonify

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


@bp.route('/')
def hello_world():  # put application's code here
    return jsonify('Hello World!')

