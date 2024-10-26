import logging

from app.core.file_handler import FileHandler

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

class Crusade:
    def __init__(self, name, faction):
        self.name = name
        self.faction = faction


class CrusadeService:

    def save(self, crusade: Crusade) -> Crusade:
        FileHandler.save_to_file(crusade, crusade.name)
        logging.info(f'Saved {crusade.name}')
        return crusade

    def load_all(self):
        logging.info('Loading all Crusades...')
        return FileHandler.get_files_in_directory()
