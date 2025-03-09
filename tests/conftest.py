from typing import Any

import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def empty_product_list() -> None:
    """Очищает список продуктов перед каждым тестом"""
    Product.all_products.clear()


@pytest.fixture
def first_category() -> Category:
    category = Category(
        name="Smart",
        description="Смартфоны, как средство не только коммуникации",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 2),
            Product("Samsung Galaxy S24 Ultra", "256GB, Серый цвет, 200MP камера", 185000.0, 5)
        ]
    )
    return category


@pytest.fixture
def second_category() -> Category:
    return Category(
        name="TV",
        description="Телевизоры",
        products=[
            Product("Samsung Galaxy S25 Ultra", "256GB, Серый цвет, 200MP камера", 190000.0, 5)
        ]
    )


@pytest.fixture
def product() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000, 5)


@pytest.fixture
def test_product4() -> Product:
    return Product("55\" QLED 4K", "Фоновая подсветка",
                   123000.0, 7)


@pytest.fixture
def test_product6() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 15)


@pytest.fixture()
def product_iterator(first_category: Category) -> Any:
    return ProductIterator(first_category)
