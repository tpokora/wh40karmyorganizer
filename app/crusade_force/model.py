import logging

from flask import Request

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


class CrusadeFieldValidationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Crusade:
    DEFAULT_SUPPLY_LIMIT = 1000

    def __init__(self, crusade_id: int | None, crusade_force: str, faction: str, supply_limit: int, supply_used: int = 0):
        self.crusade_id = crusade_id
        self.crusade_force = crusade_force
        self.faction = faction
        self.supply_limit = supply_limit if supply_limit is not None else self.DEFAULT_SUPPLY_LIMIT
        self.supply_used = supply_used

    def __str__(self):
        return f"Crusade(id={self.crusade_id}, crusade_force={self.crusade_force}, faction={self.faction}, supply_limit={self.supply_limit}, supply_used={self.supply_used})"

    def obj2dict(self):
        return {
            'crusade_id': self.crusade_id,
            'crusade_force': self.crusade_force,
            'faction': self.faction,
            'supply_limit': self.supply_limit,
            'supply_used': self.supply_used
        }

    @staticmethod
    def from_request(request: Request):
        if request.is_json:
            data = request.get_json()
            return Crusade.from_dict(data)
        else:
            raise CrusadeFieldValidationException("Request is not proper JSON format")

    @staticmethod
    def from_dict(crusade_dict: dict):
        crusade_force = crusade_dict.get('crusade_force')
        if crusade_force is None:
            raise CrusadeFieldValidationException("Missing 'crusade_force' in request body")
        faction = crusade_dict.get('faction')
        if faction is None:
            raise CrusadeFieldValidationException("Missing 'faction' in request body")
        supply_limit = crusade_dict.get('supply_limit')
        crusade_id = crusade_dict.get('crusade_id')

        return Crusade(crusade_id, crusade_force, faction, supply_limit)
