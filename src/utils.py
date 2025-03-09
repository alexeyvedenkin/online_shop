import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """Считывает данные из файла JSON и возвращает словарь
    """
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def create_object_from_json(data: dict) -> list:
    """Получает данные из словаря, преобразовывает их в класс Category
    и возвращает список данных
    """
    if 'products' not in data or data['products'] is None:
        return [Category(data['name'], data['description'])]
    goods = []
    for good in data['products']:
        goods.append(Product(**good))
    category = Category(data['name'], data['description'], goods)
    return [category]
