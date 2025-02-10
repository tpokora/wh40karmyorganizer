# __init__.py
import logging
import os

from dotenv import load_dotenv
from flask import Flask

from app.crusade_force import models
from app.crusade_force.crusade import Crusade
from app.database import db

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

load_dotenv()


def create_app(app_config=None):
    wh40k_app = Flask(__name__)
    __configure(wh40k_app, app_config)
    __configure_database_connection(wh40k_app)

    from app.core import bp as core_bp
    from app.dice_rolls import bp as dice_rolls_bp
    from app.crusade_force import bp as crusade_bp

    wh40k_app.register_blueprint(core_bp)
    wh40k_app.register_blueprint(dice_rolls_bp)
    wh40k_app.register_blueprint(crusade_bp)

    return wh40k_app


def __configure(app: Flask, app_config: str) -> None:
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['WTF_CSRF_ENABLED'] = True
    if app_config:
        app.config.from_object(app_config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config.from_object(app_config)


def __configure_database_connection(app: Flask) -> None:
    db.init_app(app)
    __test_db_connection(app)


def __test_db_connection(app: Flask) -> None:
    with app.app_context():
        try:
            db.engine.connect()
            if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
                logging.info("Successfully connected to SQLite database.")
            else:
                logging.info("Successfully connected to PostgreSQL database.")
        except Exception as e:
            logging.error(f"Failed to connect to the database. Error: {e}")


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
