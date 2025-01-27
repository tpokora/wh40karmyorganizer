import logging
from flask import Blueprint

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

bp = Blueprint('core', __name__)

from app.core import home_routes
