import json

from src.utils import create_object_from_json, read_json


def test_read_json(test_data: dict) -> None:

    file_path = 'test.json'

    with open(file_path, 'w') as file:
        json.dump(test_data, file)

    data = read_json(file_path)
    assert data == test_data


def test_create_object_from_json_empty_products() -> None:
    data = {
        'name': 'Electronics',
        'description': 'Devices and gadgets',
        'products': None
    }
    result = create_object_from_json(data)
    assert len(result) == 1
    assert result[0].name == 'Electronics'
    assert result[0].description == 'Devices and gadgets'


def test_create_object_from_json_with_products(test_data: dict) -> None:
    result = create_object_from_json(test_data)
    assert len(result) == 1
    assert len(result[0].products_in_list) == 1
    assert result[0].products_in_list[0].name == 'Samsung Galaxy C23 Ultra'
