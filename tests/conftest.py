from typing import Any

import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


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
def category_without_product() -> Any:
    category = Category(
        name="Smart",
        description="Смартфоны, как средство не только коммуникации",
    )
    return category


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


@pytest.fixture
def smartphone1() -> Smartphone:
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                      180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone2() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space",
                      210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass1() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона",
                     500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2() -> LawnGrass:
    return LawnGrass("Газонная трава 2", "Выносливая трава",
                     450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def test_product_without_quantity() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000)


@pytest.fixture
def test_data() -> Any:
    return {
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


@pytest.fixture
def test_product() -> Any:
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }


@pytest.fixture
def test_unique_product() -> Any:
    """Тестовый продукт, не определенный ранее
        """
    return {
        "name": "Газонная трава 2",
        "description": "Выносливая трава",
        "price": 450.0,
        "quantity": 15
    }


@pytest.fixture
def duplicate_product() -> Any:
    """Тестовый продукт, дублирующий наименование
        """
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 8
    }


@pytest.fixture
def new_product_negative_quantity() -> Any:
    """Тестовый продукт с отрицательным количеством
        """
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": -1
    }


@pytest.fixture
def test_product_zero_quantity() -> Any:
    """Тестовый продукт с нулевым количеством
    """
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 0
    }


# @pytest.fixture
# def empty_category() -> Category:
#     """A test fixture that creates a Category with no products."""
#     return Category(name="Empty", description="Category with no products")
