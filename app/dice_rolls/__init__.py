from flask import Blueprint

bp = Blueprint('dice_rolls', __name__)

from app.dice_rolls import dice_roll_routes
