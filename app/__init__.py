# __init__.py
from flask import Flask, request, jsonify

from app.adapter.file_handler import FileHandler
from app.domain.army import Army


def create_app(app_config=None):
    app = Flask(__name__)
    app.config.from_object(app_config)

    #create_armies_list()

    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'

    @app.route('/army', methods=["POST"])
    def create_army():
        name = request.json['name']
        faction = request.json['faction']

        army = Army(name, faction)

        FileHandler.save_to_file(army, army.name)

        return jsonify(army.__dict__)

    return app

#def create_armies_list():
#    pass

