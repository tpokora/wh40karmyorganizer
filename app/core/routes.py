import logging


from app.core import bp
from flask import jsonify, Response, render_template

from app.core.dice_rolls import DiceRoll

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


@bp.route('/', methods=['GET'])
def home() -> str:
    header = "Welcome to Warhammer 40K Army Organizer!"
    return render_template('core/home.html', header=header)


@bp.route('/dice_roll/<roll>', methods=['GET'])
def dice_rolls(roll: str) -> tuple[Response, int]:
    try:
        return jsonify(DiceRoll(roll).roll()), 200
    except ValueError as ex:
        return jsonify(ex.__str__()), 400
