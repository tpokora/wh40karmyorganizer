from flask import Blueprint

bp = Blueprint('crusade', __name__)

from app.crusade import crusade_routes
