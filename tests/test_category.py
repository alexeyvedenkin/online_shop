from typing import Any

import pytest

from src.category import Category
from src.product import Product


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Smart"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2


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


def test_avg_price_with_no_products(category_without_product: Category) -> None:
    category = category_without_product
    assert category.avg_price_in_category() == 0.0  # Testing for no products


def test_avg_price_with_products(product: Product, test_product4: Product) -> None:
    products = [product, test_product4]
    category = Category('Smart', 'Smartphone', products)
    assert category.avg_price_in_category() == 151500.0


def test_avg_price_with_one_product(product: Product) -> None:
    products = [product]
    category = Category('Smart', 'Smartphone', products)
    assert category.avg_price_in_category() == 180000.0  # Only one product


def test_add_product_success(first_category: Category, product: Product) -> None:
    category = first_category
    category.add_product(product)
    assert len(category._Category__products) == 3


def test_add_product_non_positive_quantity(first_category: Category, test_product_zero_quantity: Any) -> None:
    with pytest.raises(TypeError):
        first_category.add_product(test_product_zero_quantity)  # Should raise an error


def test_setter_with_invalid_type(first_category: Category) -> None:
    # Test if a TypeError is raised for invalid input
    with pytest.raises(TypeError):
        first_category.products = "Invalid product"


def test_product_name_count(first_category: Category) -> None:
    assert first_category.product_name_count == 2
    new_product = Product("Apple iPhone 14", "128GB, Черный цвет", 100000.0, 3)
    first_category.add_product(new_product)
    assert first_category.product_name_count == 3


def test_category_products(category_without_product: Category, product: Product, test_product4: Product) -> None:
    category = category_without_product
    category.add_product(product)
    category.add_product(test_product4)
    products_in_category = category.products
    assert products_in_category == [product, test_product4], "Products in category do not match expected"
    assert category.product_name_count == 2, "Product count in category should be 2"


def test_print_list(first_category: Category, capfd: pytest.CaptureFixture[str]) -> None:
    first_category.print_list()
    captured = capfd.readouterr()
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 2 шт.\n"
        "Samsung Galaxy S24 Ultra, 185000.0 руб. Остаток: 5 шт."
    )
    assert captured.out.strip() == expected_output.strip()


def test_product_list(first_category: Category) -> None:
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 2 шт.\n"
        "Samsung Galaxy S24 Ultra, 185000.0 руб. Остаток: 5 шт."
    )
    actual_output = first_category.product_list
    assert actual_output == expected_output


def test_set_products_with_product() -> None:
    category = Category("Smartphones", "Latest smartphone models")
    product = Product("iPhone 14", "128GB, Black", 999.99, 1)

    category.products = product  # Set a single product
    assert len(category._Category__products) == 1
    assert category._Category__products[0] == product


def test_set_products_with_list() -> None:
    category = Category("Smartphones", "Latest smartphone models")
    product1 = Product("Pixel 7", "128GB, White", 599.99, 2)
    product2 = Product("Samsung Galaxy S22", "256GB, Black", 799.99, 3)

    category.products = [product1, product2]
    assert len(category._Category__products) == 2
    assert category._Category__products == [product1, product2]


def test_set_invalid_products() -> None:
    category = Category("Smartphones", "Latest smartphone models")

    with pytest.raises(TypeError):
        category.products = "Недопустимый тип"
