import json
import os

from src.category import Category
from src.product import Product
from typing import Any

def read_json(path: str) -> dict:
    """Считывает данные из файла JSON и возвращает словарь
    """
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def create_object_from_json(data: Any) -> list:
    """Получает данные из словаря, преобразовывает их в класс Category
    и возвращает список данных
    """
    categories = []
    for category in data:
        goods = []
        for good in category['products']:
            goods.append(Product(**good))
        category['products'] = goods
        categories.append(Category(**category))

    return categories
