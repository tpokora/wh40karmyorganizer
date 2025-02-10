import logging

from flask import render_template
from flask.views import MethodView

from app.crusade_force import bp
from app.crusade_force.crusade import CrusadeService

CRUSADES_HTML_TEMPLATE = 'crusade_force/crusade_force.html'

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


class CrusadeForcesView(MethodView):
    def __init__(self):
        self.crusade_service = CrusadeService()

    def get(self) -> str:
        logging.info("Displaying all crusade forces...")
        return render_template(CRUSADES_HTML_TEMPLATE, crusade_forces=self.crusade_service.get_all())


bp.add_url_rule('/crusades', view_func=CrusadeForcesView.as_view('crusade_forces_home'))
