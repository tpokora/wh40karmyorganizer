import logging

from app.core.file_handler import FileHandler

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


class Army:
    def __init__(self, name, faction):
        self.name = name
        self.faction = faction


class ArmyService:

    def __init__(self):
        self.__file_handler = FileHandler()

    def save(self, army: Army) -> Army:
        self.__file_handler.save_to_file(army, army.name)
        logging.info(f"Army created: {army.name}")
        return army

    def get_all(self):
        logging.info("Return all armies")
        return self.__file_handler.get_files_in_directory()
