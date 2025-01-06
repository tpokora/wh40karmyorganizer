import logging

from app.core.file_handler import FileHandler
from app.core.in_memory_storage import Storage
from app.crusade.model import Crusade


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
