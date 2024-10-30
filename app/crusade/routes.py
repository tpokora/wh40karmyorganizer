import logging

from app.core import bp
from flask import jsonify, request, Response

from app.crusade.crusade import Crusade, CrusadeService

DEFAULT_SUPPLY_LIMIT = 1000

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

crusade_service = CrusadeService()


@bp.route('/crusade/', methods=['GET'])
def get_all() -> tuple[Response, int]:
    logging.info("Return all crusades...")
    all_crusades_dict = []
    for crusade in crusade_service.get_all():
        all_crusades_dict.append(crusade.obj2dict())
    return jsonify(all_crusades_dict), 200

@bp.route('/crusade/', methods=['POST'])
def create() -> tuple[Response, int]:
    if request.is_json:
        data = request.get_json()
        crusade_force = None
        faction = None
        supply_limit = DEFAULT_SUPPLY_LIMIT
        if 'crusade_force' in data:
            crusade_force = data['crusade_force']
        else:
            return __error_response("Missing 'crusade_force' in request body")
        if 'faction' in data:
            faction = data['faction']
        else:
            return __error_response("Missing 'faction' in request body")
        if 'supply_limit' in data:
            supply_limit = data['supply_limit']

        crusade = Crusade(crusade_force, faction, supply_limit)
        logging.info(f"Creating crusade {crusade}")

        saved_crusade = crusade_service.save(crusade)
        logging.info(f"Created crusade {saved_crusade}")

        return jsonify(saved_crusade.obj2dict()), 200
    else:
        return __error_response('Missing request body')

def __error_response(message: str) -> tuple[Response, int]:
    return jsonify({'error': message}), 400
