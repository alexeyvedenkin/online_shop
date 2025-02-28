import json

from src.utils import read_json

from src.category import Category
from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Smart"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3


def test_read_json() -> None:

    # Создаем тестовый JSON-файл
    file_path = 'test.json'
    test_data = {'key': 'value'}
    with open(file_path, 'w') as file:
        json.dump(test_data, file)

    # Тестируем функцию
    data = read_json(file_path)
    assert data == test_data
