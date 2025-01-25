import logging


from app.core import bp
from flask import jsonify, Response

from app.core.dice_rolls import DiceRoll

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


@bp.route('/', methods=['GET'])
def home() -> tuple[Response, int]:
    home_response = {"message": "Welcome to Warhammer 40K Army Organizer!"}
    return jsonify(home_response), 200


@bp.route('/dice_roll/<roll>', methods=['GET'])
def dice_rolls(roll: str) -> tuple[Response, int]:
    try:
        return jsonify(DiceRoll(roll).roll()), 200
    except ValueError as ex:
        return jsonify(ex.__str__()), 400
