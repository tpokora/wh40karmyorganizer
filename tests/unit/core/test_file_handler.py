import json

from app.army.army import Army
from app.core.file_handler import FileHandler

file_handler = FileHandler()


def test_file_handler():
    # given
    test_army = Army("test_name", "test_faction")
    test_file_name = "test_file"

    # when
    file_handler.save_to_file(test_army, test_file_name)

    # then
    with open(f"storage/{test_file_name}.json", 'r', encoding='utf-8') as file:
        army = json.load(file)
        assert army['name'] == test_army.name
        assert army['faction'] == test_army.faction

