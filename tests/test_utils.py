import json

from src.utils import read_json


def test_read_json() -> None:

    # Создаем тестовый JSON-файл
    file_path = 'test.json'
    test_data = {'key': 'value'}
    with open(file_path, 'w') as file:
        json.dump(test_data, file)

    # Тестируем функцию
    data = read_json(file_path)
    assert data == test_data
