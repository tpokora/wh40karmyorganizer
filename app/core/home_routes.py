import logging

from flask import render_template

from app.core import bp

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


@bp.route('/', methods=['GET'])
def home() -> str:
    header = "Welcome to Warhammer 40K Army Organizer!"
    return render_template('core/home.html', header=header)