# __init__.py
import json
import logging
from flask import Flask

from app.core.file_handler import FileHandler
from app.core.in_memory_storage import Storage
from app.crusade_force.crusade import Crusade

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


def create_app(app_config=None):
    app.config.from_object(app_config)

    load_crusades_to_storage()
    from app.core import bp as core_bp
    from app.dice_rolls import bp as dice_rolls_bp
    from app.crusade_force import bp as crusade_bp

    app.register_blueprint(core_bp)
    app.register_blueprint(dice_rolls_bp)
    app.register_blueprint(crusade_bp)

    return app


def load_crusades_to_storage():
    app.logger.info("Loading crusades to storage...")
    storage = Storage()
    crusades_from_file = []
    for file_path in FileHandler.get_files_in_directory():
        crusades_from_file.append(__get_crusade_from_file(file_path))
    storage.load_crusades(crusades_from_file)


def __get_crusade_from_file(file_path):
    with open(file_path, 'r') as file:
        return Crusade.dict2obj(json.load(file))


