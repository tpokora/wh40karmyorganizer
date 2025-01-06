import logging

from app.core import bp
from flask import jsonify, request, Response

from app.crusade.crusade import Crusade, CrusadeService
from app.crusade.model import CrusadeFieldValidationException

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

crusade_service = CrusadeService()


@bp.route('/crusade', methods=['GET'])
def get_all() -> tuple[Response, int]:
    logging.info("Return all crusade forces...")
    all_crusades_dict = []
    for crusade in crusade_service.get_all():
        all_crusades_dict.append(crusade.obj2dict())
    return jsonify(all_crusades_dict), 200


@bp.route('/crusade', methods=['POST'])
def create() -> tuple[Response, int]:
    try:
        crusade = Crusade.from_request(request)
        logging.info(f"Creating crusade force: {crusade}")

        saved_crusade = crusade_service.save(crusade)
        logging.info(f"Created crusade force: {saved_crusade}")

        return jsonify(saved_crusade.obj2dict()), 201
    except CrusadeFieldValidationException as ex:
        return __error_response(ex.message)


@bp.route('/crusade/export', methods=['GET'])
def export_all() -> tuple[Response, int]:
    # logging.info("Export all crusade forces...")
    # all_crusades_dict = []
    # all_crusades_dict.append("Export")
    # for crusade in crusade_service.get_all():
    #     all_crusades_dict.append(crusade.obj2dict())
    # return jsonify(all_crusades_dict), 200
    pass


def __error_response(message: str) -> tuple[Response, int]:
    return jsonify({'error': message}), 400
