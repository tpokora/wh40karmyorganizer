import logging

from app.core import bp
from flask import jsonify, Response

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


@bp.route('/', methods=['GET'])
def home() -> tuple[Response, int]:
    home_response = {"message" : "Welcome to Warhammer 40K Army Organizer!"}
    return jsonify(home_response), 200