# __init__.py
import logging
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


def create_app(app_config=None):
    app.config.from_object(app_config)

    create_armies_list()
    from app.army import bp as army_bp
    from app.core import bp as core_bp

    app.register_blueprint(army_bp)
    app.register_blueprint(core_bp)

    return app


def create_armies_list():
    app.logger.info("Creating armies list...")
