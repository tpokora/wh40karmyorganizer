import json

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


class Army:
    def __init__(self, name, faction):
        self.name = name
        self.faction = faction


def save_to_file(army: Army):
    file_name = f"{army.name}.json".replace(" ", "_")
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(json.dumps(army.__dict__))


@app.route('/army', methods=["POST"])
def create_army():
    name = request.json['name']
    faction = request.json['faction']

    army = Army(name, faction)

    save_to_file(army)

    return jsonify(army.__dict__)


if __name__ == '__main__':
    app.run()
