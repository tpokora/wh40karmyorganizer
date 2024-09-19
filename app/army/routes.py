from app.army import bp
from flask import request, jsonify

from app.army.army import ArmyService, Army

army_service = ArmyService()


@bp.route('/army', methods=['GET'])
def get_all():
    all_armies = army_service.get_all()
    return jsonify(all_armies)


@bp.route('/army', methods=['POST'])
def create():
    name = request.json['name']
    faction = request.json['faction']

    army = Army(name, faction)

    saved_army = army_service.save(army)

    return jsonify(saved_army.__dict__)
