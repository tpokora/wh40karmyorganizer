import logging

from flask import render_template

from app.crusade_force import bp

ROLLS_DICE_ROLL_HTML_TEMPLATE = 'crusade_force/crusade_force.html'

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


@bp.route('/crusades', methods=['GET'])
def crusade_forces_home() -> str:
    return render_template(ROLLS_DICE_ROLL_HTML_TEMPLATE)
