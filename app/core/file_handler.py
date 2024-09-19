import glob
import json
import logging
import os

STORAGE="storage"

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


class FileHandler:

    def save_to_file(self, data: any, file_path: str):
        file_path = f"{STORAGE}/{file_path}.json".replace(" ", "_")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data.__dict__))

    def get_files_in_directory(self):
        armies = glob.glob(f"{STORAGE}/*.json")
        logging.info(armies)
        return armies
