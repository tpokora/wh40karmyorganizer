import logging

from flask import render_template

from app.crusade_force import bp
from app.crusade_force.crusade import CrusadeService

CRUSADES_HTML_TEMPLATE = 'crusade_force/crusade_force.html'

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

crusade_service = CrusadeService()


@bp.route('/crusades', methods=['GET'])
def crusade_forces_home() -> str:
    logging.info("Displaying all crusade forces...")
    crusade_forces = crusade_service.get_all()
    return render_template(CRUSADES_HTML_TEMPLATE, crusade_forces=crusade_forces)
