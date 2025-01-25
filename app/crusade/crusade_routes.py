import logging

from flask import jsonify, request, Response, make_response

from app.core import bp
from app.crusade.crusade import Crusade, CrusadeService
from app.crusade.model import CrusadeFieldValidationException

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

crusade_service = CrusadeService()


@bp.route('/crusade', methods=['GET'])
def get_all() -> tuple[Response, int]:
    logging.info("Return all crusade forces...")
    all_crusade_forces_dict = []
    for crusade in crusade_service.get_all():
        all_crusade_forces_dict.append(crusade.obj2dict())
    return jsonify(all_crusade_forces_dict), 200


@bp.route('/crusade/<crusade_id>', methods=['GET'])
def get_crusade_by_id(crusade_id: str) -> tuple[Response, int]:
    logging.info("Return crusade force...")
    try:
        crusade = crusade_service.get_by_id(crusade_id)
        return jsonify(crusade.obj2dict()), 200
    except ValueError as ex:
        return __error_response(ex.__str__(), 400)


@bp.route('/crusade/find/<name>', methods=['GET'])
def find_all_by_name(name) -> tuple[Response, int]:
    logging.info(f"Return crusade forces with name: {name} ...")
    all_crusade_forces_dict = []
    for crusade in crusade_service.find_all_by_name(name):
        all_crusade_forces_dict.append(crusade.obj2dict())
    return jsonify(all_crusade_forces_dict), 200


@bp.route('/crusade', methods=['POST'])
def create() -> tuple[Response, int]:
    try:
        crusade = Crusade.from_request(request)
        logging.info(f"Creating crusade force: {crusade}")

        saved_crusade = crusade_service.save(crusade)
        logging.info(f"Created crusade force: {saved_crusade}")

        return jsonify(saved_crusade.obj2dict()), 201
    except CrusadeFieldValidationException as ex:
        return __error_response(ex.message, 400)


@bp.route('/crusade/import', methods=['POST'])
def import_all() -> tuple[Response, int]:
    logging.info("Importing crusade forces...")

    if request.is_json:
        crusade_forces = request.get_json()
        try:
            for crusade in crusade_forces:
                logging.info(f"Crusade: {crusade}")
                crusade_service.save(Crusade.from_dict(crusade))
            all_crusade_forces_dict = []
            for crusade in crusade_service.get_all():
                all_crusade_forces_dict.append(crusade.obj2dict())
            return jsonify(all_crusade_forces_dict), 201
        except CrusadeFieldValidationException as ex:
            return __error_response(ex.message, 400)
    else:
        return __error_response("Could not load crusade forces from input JSON", 400)


@bp.route('/crusade/export', methods=['GET'])
def export_all() -> tuple[Response, int]:
    logging.info("Export all crusade forces...")
    all_crusade_forces_dict = []
    for crusade in crusade_service.get_all():
        all_crusade_forces_dict.append(crusade.obj2dict())

    json_response = make_response(jsonify(all_crusade_forces_dict))
    json_response.headers['Content-Disposition'] = 'attachment; filename=crusade_forces.json'
    json_response.headers['Content-Type'] = 'application/json'
    return json_response, 200


def __error_response(message: str, status_code: int) -> tuple[Response, int]:
    return jsonify({'error': message}), status_code
