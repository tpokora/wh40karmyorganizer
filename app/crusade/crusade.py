import logging

from app.core.file_handler import FileHandler
from app.core.in_memory_storage import Storage

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

class Crusade:
    def __init__(self, crusade_force, faction, supply_limit, supply_used=0):
        self.crusade_force = crusade_force
        self.faction = faction
        self.supply_limit = supply_limit
        self.supply_used = supply_used

    def __str__(self):
        return f"Crusade(crusade_force={self.crusade_force}, faction={self.faction}, supply_limit={self.supply_limit}, supply_used={self.supply_used})"

    def obj2dict(self):
        return {
            'crusade_force': self.crusade_force,
            'faction': self.faction,
            'supply_limit': self.supply_limit,
            'supply_used': self.supply_used
        }

    @staticmethod
    def dict2obj(dict):
        crusade_force = dict['crusade_force']
        faction = dict['faction']
        supply_limit = dict['supply_limit']
        supply_used = dict['supply_used']

        crusade = Crusade(crusade_force, faction, supply_limit)
        crusade.supply_used = supply_used

        return crusade

class CrusadeService:

    def __init__(self):
        self.storage = Storage()

    def save(self, crusade: Crusade) -> Crusade:
        FileHandler.save_to_file(crusade.obj2dict(), crusade.crusade_force)
        self.storage.save_crusade(crusade)
        logging.info(f'Saved {crusade.crusade_force}')
        return crusade

    def get_all(self):
        logging.info('Get all Crusades...')
        crusades = self.storage.get_crusades()
        return crusades
