import json

# from src.category import Category
# from src.product import Product
from src.utils import read_json


def test_read_json() -> None:

    # Создаем тестовый JSON-файл
    file_path = 'test.json'
    test_data = {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            }
        ]
    }
    with open(file_path, 'w') as file:
        json.dump(test_data, file)

    # Тестируем функцию
    data = read_json(file_path)
    assert data == test_data


# def test_create_object_from_json() -> None:
#     file_path = 'test.json'
#     with open(file_path, 'r', encoding='utf-8') as file:
#         result = json.load(file)
#     product = Product(
#         result['products'][0]['name'],
#         result['products'][0]['description'],
#         result['products'][0]['price'],
#         result['products'][0]['quantity']
#     )
#     category = Category(result['name'], result['description'], [str(product)])
#     assert category.name == "Смартфоны"
#     assert category.description == "Смартфоны, как средство не только коммуникации"
#     assert category.products == str(product) + "\n"
#     assert len(create_object_from_json(result)) == 1
