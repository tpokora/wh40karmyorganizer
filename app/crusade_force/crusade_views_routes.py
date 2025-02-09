import logging

from flask import render_template

from app.crusade_force import bp

CRUSADES_HTML_TEMPLATE = 'crusade_force/crusade_force.html'

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


@bp.route('/crusades', methods=['GET'])
def crusade_forces_home() -> str:
    return render_template(CRUSADES_HTML_TEMPLATE)
