import logging

from app.core import bp
from flask import jsonify, request, Response

from app.crusade.crusade import Crusade, CrusadeService

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

faction_service = CrusadeService()


@bp.route('/crusade/', methods=['GET'])
def get_all() -> Response:
    all_factions = faction_service.load_all()
    return jsonify(all_factions)

@bp.route('/crusade/', methods=['POST'])
def create() -> Response:
    name = request.json['name']
    faction = request.json['faction']

    crusade = Crusade(name=name, faction=faction)

    saved_crusade = faction_service.save(crusade)

    return jsonify(saved_crusade)
