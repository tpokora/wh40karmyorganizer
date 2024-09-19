from flask import Blueprint

bp = Blueprint('army', __name__)

from app.army import routes
