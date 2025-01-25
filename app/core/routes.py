import logging
import random
import re

from app.core import bp
from flask import jsonify, Response

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


@bp.route('/', methods=['GET'])
def home() -> tuple[Response, int]:
    home_response = {"message": "Welcome to Warhammer 40K Army Organizer!"}
    return jsonify(home_response), 200


@bp.route('/dice_roll/<roll>', methods=['GET'])
def dice_rolls(roll: str) -> tuple[Response, int]:
    pattern = r'^\d+d\d+$'
    if not re.match(pattern, roll):
        return jsonify("Incorrect format"), 401
    split = roll.split("d")
    number_of_dice = split[0]
    dice_value = split[1]
    values = []
    for _ in range(0, int(number_of_dice)):
        roll = random.randrange(1, int(dice_value))
        values.append(roll)
    return jsonify(values), 200
