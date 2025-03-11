import json

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
