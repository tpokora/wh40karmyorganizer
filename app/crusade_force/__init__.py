from flask import Blueprint

bp = Blueprint('crusade', __name__)

from app.crusade_force import crusade_rest_routes
