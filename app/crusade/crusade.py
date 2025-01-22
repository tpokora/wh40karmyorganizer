import logging

from app.core.file_handler import FileHandler
from app.core.in_memory_storage import Storage
from app.crusade.model import Crusade, CrusadeFieldValidationException


class CrusadeExistException(CrusadeFieldValidationException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class CrusadeService:

    def __init__(self):
        self.storage = Storage()

    def save(self, crusade: Crusade) -> Crusade:
        self.__crusade_exists(crusade)
        self.__save_to_file(crusade)
        logging.info(f'Saved {crusade.crusade_force}')
        return crusade

    def get_all(self):
        logging.info('Get all Crusades...')
        crusades = self.storage.get_crusades()
        return crusades

    def __save_to_file(self, crusade: Crusade) -> Crusade:
        FileHandler.save_to_file(crusade.obj2dict(), crusade.crusade_id)
        self.storage.save_crusade(crusade)
        return crusade

    def __crusade_exists(self, crusade: Crusade):
        if any(crusade_from_storage.crusade_force == crusade.crusade_force
               for crusade_from_storage in self.storage.get_crusades()):
            raise CrusadeExistException(f"Crusade force '{crusade.crusade_force}' exists")
