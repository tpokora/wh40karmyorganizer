import logging

from app.core import bp
from flask import jsonify, request, Response

from app.crusade.crusade import Crusade, CrusadeService

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

crusade_service = CrusadeService()


@bp.route('/crusade/', methods=['GET'])
def get_all() -> Response:
    logging.info("Return all crusades...")
    return jsonify(crusade_service.load_all())

@bp.route('/crusade/', methods=['POST'])
def create() -> Response:
    name = request.json['name']
    faction = request.json['faction']

    crusade = Crusade(name=name, faction=faction)
    logging.info(f"Creating crusade {crusade}")

    saved_crusade = crusade_service.save(crusade)
    logging.info(f"Created crusade {saved_crusade}")

    return jsonify(saved_crusade)
