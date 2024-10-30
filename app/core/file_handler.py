import glob
import json
import logging
import os

STORAGE_DIR= "storage"

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


class FileHandler:

    @staticmethod
    def save_to_file(data: any, file_name: str):
        file_path = f"{STORAGE_DIR}/{file_name}.json".replace(" ", "_")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data.__dict__))

    @staticmethod
    def get_files_in_directory():
        crusade_forces_files = glob.glob(f"{STORAGE_DIR}/*.json")
        logging.info(crusade_forces_files)
        return crusade_forces_files
