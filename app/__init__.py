# __init__.py
import json
import logging
import os
from dotenv import load_dotenv
from flask import Flask
from .database import db
from app.crusade_force import models

from app.core.file_handler import FileHandler
from app.core.in_memory_storage import Storage
from app.crusade_force.crusade import Crusade

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

load_dotenv()


def create_app(app_config=None):
    wh40k_app = Flask(__name__)
    __configure(wh40k_app, app_config)
    __configure_database_connection(wh40k_app)

    load_crusades_to_storage(wh40k_app)

    from app.core import bp as core_bp
    from app.dice_rolls import bp as dice_rolls_bp
    from app.crusade_force import bp as crusade_bp

    wh40k_app.register_blueprint(core_bp)
    wh40k_app.register_blueprint(dice_rolls_bp)
    wh40k_app.register_blueprint(crusade_bp)

    return wh40k_app


def __configure(app: Flask, app_config):
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(app_config)


def __configure_database_connection(app:Flask) -> None:
    db.init_app(app)
    __test_db_connection(app)


def __test_db_connection(app: Flask) -> None:
    with app.app_context():
        try:
            db.engine.connect()
            logging.info("Successfully connected to the database.")
        except Exception as e:
            logging.error(f"Failed to connect to the database. Error: {e}")


def load_crusades_to_storage(app: Flask) -> None:
    app.logger.info("Loading crusades to storage...")
    storage = Storage()
    crusades_from_file = []
    for file_path in FileHandler.get_files_in_directory():
        crusades_from_file.append(__get_crusade_from_file(file_path))
    storage.load_crusades(crusades_from_file)


def __get_crusade_from_file(file_path):
    with open(file_path, 'r') as file:
        return Crusade.dict2obj(json.load(file))


app = create_app()


@app.cli.command("init-db")
def init_db():
    with app.app_context():
        try:
            db.create_all()
            logging.info("Database tables created successfully.")
            logging.info("Created tables:")
            for table in db.metadata.tables:
                logging.info(f"- {table}")
        except Exception as e:
            logging.error(f"An error occurred while creating tables: {e}")
