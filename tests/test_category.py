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


def test_add_product_success(first_category, product):
    category = first_category
    category.add_product(product)  # This should succeed
    assert len(category._Category__products) == 3  # Check if product was added


def test_add_product_non_positive_quantity(first_category, test_product_zero_quantity):
    with pytest.raises(TypeError):
        first_category.add_product(test_product_zero_quantity)  # Should raise an error


def test_setter_with_valid_list(first_category, product):
    new_products = [product]
    first_category.products = new_products

    # Сравните список продуктов с ожидаемым списком новых продуктов
    expected_string = ''.join(str(prod) for prod in new_products)  # Combine string representations
    assert str(first_category.products).strip() == expected_string.strip()


def test_setter_with_single_product(first_category, product):
    new_products = [product]  # Define new_products with the product fixture
    first_category.products = product  # Set a single product to first_category

    # Test if products can be set with a single product
    expected_string = ''.join(str(prod) for prod in new_products)  # Combine string representations
    assert str(first_category.products).strip() == expected_string.strip()


def test_setter_with_invalid_type(first_category):
    # Test if a TypeError is raised for invalid input
    with pytest.raises(TypeError):
        first_category.products = "Invalid product"
