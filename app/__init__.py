# __init__.py
import logging
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


def create_app(app_config=None):
    app.config.from_object(app_config)

    create_crusade_list()
    from app.core import bp as core_bp
    from app.crusade import bp as crusade_bp

    app.register_blueprint(core_bp)
    app.register_blueprint(crusade_bp)

    return app


def create_crusade_list():
    app.logger.info("Loading crusades...")
