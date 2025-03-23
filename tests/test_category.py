from typing import Any

import pytest

from src.category import Category
from src.product import Product
from tests.conftest import category_without_product


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Smart"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_category_products_property(first_category: Category) -> None:
    assert first_category.products == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 2 шт.\n"
                                       "Samsung Galaxy S24 Ultra, 185000.0 руб. Остаток: 5 шт.\n")


def test_category_products_setter(first_category: Category, product: Product) -> None:
    assert len(first_category.products_in_list) == 2
    first_category.products_in_list.append(product)
    assert len(first_category.products_in_list) == 3


def test_category_str(first_category: Category) -> None:
    assert str(first_category) == "Smart, количество продуктов: 7 шт."


def test_product_iterator(product_iterator: Any) -> None:
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Samsung Galaxy S24 Ultra"
    with pytest.raises(StopIteration):
        next(product_iterator)


def test_avg_price_with_no_products(category_without_product):
    category = category_without_product
    assert category.avg_price_in_category() == 0.0  # Testing for no products

def test_avg_price_with_products(product, test_product4):
    products = [product, test_product4]
    category = Category('Smart', 'Smartphone', products)
    assert category.avg_price_in_category() == 151500.0

def test_avg_price_with_one_product(product):
    products = [product]
    category = Category('Smart', 'Smartphone',products)
    assert category.avg_price_in_category() == 180000.0  # Only one product