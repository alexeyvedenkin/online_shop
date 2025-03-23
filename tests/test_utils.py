import json

from src.utils import create_object_from_json, read_json


def test_read_json(test_data) -> None:

    # Создаем тестовый JSON-файл
    file_path = 'test.json'
    # test_data = {
    #     "name": "Смартфоны",
    #     "description": "Смартфоны, как средство не только коммуникации",
    #     "products": [
    #         {
    #             "name": "Samsung Galaxy C23 Ultra",
    #             "description": "256GB, Серый цвет, 200MP камера",
    #             "price": 180000.0,
    #             "quantity": 5
    #         }
    #     ]
    # }
    with open(file_path, 'w') as file:
        json.dump(test_data, file)

    # Тестируем функцию
    data = read_json(file_path)
    assert data == test_data


def test_create_object_from_json_empty_products():
    data = {
        'name': 'Electronics',
        'description': 'Devices and gadgets',
        'products': None
    }
    result = create_object_from_json(data)
    assert len(result) == 1                # Expect one category
    assert result[0].name == 'Electronics'  # Check category name
    assert result[0].description == 'Devices and gadgets'  # Check description


def test_create_object_from_json_with_products(test_data):
    result = create_object_from_json(test_data)
    assert len(result) == 1
    assert len(result[0].products_in_list) == 1
    assert result[0].products_in_list[0].name == 'Samsung Galaxy C23 Ultra'
