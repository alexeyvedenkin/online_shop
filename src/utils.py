import json
import os


def read_json(path: str) -> dict:
    """Считывает данные из файла JSON и возвращает словарь
    """
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data






