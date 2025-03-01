import pytest

from src.utils import Category, Product


@pytest.fixture
def first_category():
    return Category(
        name="Smart",
        description="Смартфоны, как средство не только коммуникации",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 2),
            Product("Samsung Galaxy S24 Ultra", "256GB, Серый цвет, 200MP камера", 185000.0, 5)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name="TV",
        description="Телевизоры",
        products=[
            Product("Samsung Galaxy S25 Ultra", "256GB, Серый цвет, 200MP камера", 190000.0, 5)
        ]
    )


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5
                   )
