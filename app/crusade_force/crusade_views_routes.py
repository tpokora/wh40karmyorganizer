import logging

from flask import render_template, abort
from flask.views import MethodView

from app.crusade_force import bp
from app.crusade_force.crusade import CrusadeService

CRUSADES_HTML_TEMPLATE = 'crusade_force/crusade_force.html'
CRUSADE_DETAIL_HTML_TEMPLATE = 'crusade_force/crusade_detail.html'

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


class CrusadeForcesView(MethodView):
    def __init__(self):
        self.crusade_service = CrusadeService()

    def get(self) -> str:
        logging.info("Displaying all crusade forces...")
        return render_template(CRUSADES_HTML_TEMPLATE, crusade_forces=self.crusade_service.get_all())


class CrusadeForceView(MethodView):
    def __init__(self):
        self.crusade_service = CrusadeService()

    def get(self, crusade_id: str) -> str:
        logging.info(f"Displaying crusade force with id: {crusade_id}")
        try:
            crusade = self.crusade_service.get_by_id(crusade_id)
            return render_template(CRUSADE_DETAIL_HTML_TEMPLATE, crusade=crusade)
        except ValueError as e:
            logging.error(f"Crusade force not found: {str(e)}")
            abort(404)


bp.add_url_rule('/crusades', view_func=CrusadeForcesView.as_view('crusade_forces_home'))
bp.add_url_rule('/crusades/<string:crusade_id>', view_func=CrusadeForceView.as_view('crusade_force_detail'))
