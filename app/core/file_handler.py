import glob
import json
import logging
import os

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


class FileHandler:

    STORAGE_DIR = "storage"

    @staticmethod
    def save_to_file(data: dict, file_name: str) -> None:
        file_path = os.path.join(FileHandler.STORAGE_DIR, FileHandler.__get_json_file_name(file_name))
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data))

    @staticmethod
    def get_files_in_directory() -> list[str]:
        crusade_forces_files = glob.glob(os.path.join(FileHandler.STORAGE_DIR, "*.json"))
        logging.info(crusade_forces_files)
        return crusade_forces_files

    @staticmethod
    def __get_json_file_name(file_name: str) -> str:
        file_name = file_name + ".json"
        return file_name.replace(" ", "_")
