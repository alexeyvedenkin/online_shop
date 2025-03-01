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


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    # print(product1.name)
    # print(product1.description)
    # print(product1.price)
    # print(product1.quantity)
    product2 = Product("Samsung Galaxy S24 Ultra", "256GB, Серый цвет, 200MP камера", 185000.0, 5)
    product3 = Product("Samsung Galaxy S25 Ultra", "256GB, Серый цвет, 200MP камера", 190000.0, 5)
    product4 = Product("Samsung Galaxy S26 Ultra", "256GB, Серый цвет, 200MP камера", 195000.0, 5)

    category = Category('Smart', "Смартфоны, как средство не только коммуникации",
              [product1, product2, product3, product4])
    category1 = [product1, product2, product3, product4]
    category2 = [product1]
    print(Category.category_count)
    print(Category.product_count)
    print(category.products)
    # goods_raw = read_json('../data/products.json')
    # print(list(goods_raw))
    # categories_data = create_object_from_json(goods_raw)
    # print(categories_data[0])
    print(category.name)
    print(category.description)
    # print(category.products)
    # print(category1)
    # print(category2)
    product5 = Product("Apple S26 Ultra", "256GB, Серый цвет, 200MP камера", 200000.0, 5)
    category.products = product5
    print(category.products)
    print(Category.product_count)

