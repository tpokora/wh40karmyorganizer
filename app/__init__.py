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
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['WTF_CSRF_ENABLED'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(app_config)

    db.init_app(app)

    # Test database connection
    with app.app_context():
        try:
            db.engine.connect()
            print("Successfully connected to the database.")
        except Exception as e:
            print(f"Failed to connect to the database. Error: {e}")

    load_crusades_to_storage(app)
    from app.core import bp as core_bp
    from app.dice_rolls import bp as dice_rolls_bp
    from app.crusade_force import bp as crusade_bp

    app.register_blueprint(core_bp)
    app.register_blueprint(dice_rolls_bp)
    app.register_blueprint(crusade_bp)

    return app


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
            print("Database tables created successfully.")
            # Print the list of created tables
            print("Created tables:")
            for table in db.metadata.tables:
                print(f"- {table}")
        except Exception as e:
            print(f"An error occurred while creating tables: {e}")
