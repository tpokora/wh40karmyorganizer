import json
import os


class FileHandler:

    @staticmethod
    def save_to_file(data: any, file_path: str):
        file_path = f"storage/{file_path}.json".replace(" ", "_")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data.__dict__))
