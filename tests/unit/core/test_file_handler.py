import json
import os

from app.core.file_handler import FileHandler

def test_create_new_file():
    # given
    data = {'data': 'test_data'}
    file_name = 'test_file'

    # when
    FileHandler.save_to_file(data, file_name)

    # then
    __assert_file(data, file_name)

def test_get_files_in_directory():
    # given
    data = {'data': 'test_data'}
    file_name = 'test_file'
    FileHandler.save_to_file(data, file_name)

    # when
    files_in_directory = FileHandler.get_files_in_directory()

    # then
    assert 1 == len(files_in_directory)
    expected_file_name = f"{file_name}.json"
    assert any(expected_file_name in file for file in files_in_directory)
    __remove_file(file_name)


def __assert_file(data: dict, file_name: str):
    try:
        with open(f'storage/{file_name}.json', 'r') as file:
            read_data = json.load(file)
            assert read_data == data
    except FileNotFoundError:
        assert False
    finally:
        __remove_file(file_name)


def __remove_file(file_name: str):
    os.remove(f'storage/{file_name}.json')
