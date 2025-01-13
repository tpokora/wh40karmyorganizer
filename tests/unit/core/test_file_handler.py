import json
import os
import unittest
from unittest.mock import patch

from app.core.file_handler import FileHandler


class FileStorageTest(unittest.TestCase):
    def setUp(self):
        self.storage_path = self.__get_storage_path()

    def remove_file(self, file_name: str) -> None:
        os.path.join(self.storage_path, file_name.join(".json"))

    @staticmethod
    def __get_storage_path() -> str:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        index = script_dir.find('tests')
        if index == -1:
            return script_dir
        index += 5
        return script_dir[:index]


class FileHandlerTest(FileStorageTest):

    def setUp(self):
        super().setUp()

    def test_create_new_file(self):
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
            # given
            data = {'data': 'test_data'}
            file_name = 'test_file'

            # when
            FileHandler.save_to_file(data, file_name)

            # then
            self.__assert_file(data, file_name)
            self.remove_file(file_name)

    def test_get_files_in_directory(self):
        with patch.object(FileHandler, 'STORAGE_DIR', self.storage_path):
            assert FileHandler.STORAGE_DIR == self.storage_path
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
            self.remove_file(file_name)

    def __assert_file(self, data: dict, file_name: str):
        file_path = os.path.join(self.storage_path, file_name + ".json")
        try:
            with open(file_path, 'r') as file:
                read_data = json.load(file)
                assert read_data == data
        except FileNotFoundError:
            assert False
        finally:
            self.remove_file(file_name)
