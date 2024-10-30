import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


class Storage:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Storage, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Check if the instance is already initialized
            self.crusades = []
            self.initialized = True  # Mark as initialized

    def load_crusades(self, crusades_dict):
        self.crusades = crusades_dict

    def get_crusades(self):
        return self.crusades

    def save_crusade(self, crusade):
        self.crusades.append(crusade)
