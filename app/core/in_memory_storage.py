from app.core.file_handler import FileHandler

class Storage:
    def __init__(self):
        self.crusades = []

    def load_crusades(self):
        self.crusades = FileHandler.get_files_in_directory()

    def get_crusades(self):
        return self.crusades


STORAGE = Storage()