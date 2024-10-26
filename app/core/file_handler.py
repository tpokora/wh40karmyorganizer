import glob
import json
import logging
import os

STORAGE="storage"

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


class FileHandler:

    @staticmethod
    def save_to_file(data: any, file_name: str):
        file_path = f"{STORAGE}/{file_name}.json".replace(" ", "_")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data.__dict__))

    @staticmethod
    def get_files_in_directory():
        armies = glob.glob(f"{STORAGE}/*.json")
        logging.info(armies)
        return armies
