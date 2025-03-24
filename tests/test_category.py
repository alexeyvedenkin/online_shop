from typing import Any

import pytest

from src.category import Category
from src.exceptions import NonPositiveProductQuantity
from src.product import Product


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Smart"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2


# def test_category_products_property(first_category: Category) -> None:
#     assert first_category.products_in_list == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 2 шт.\n"
#                                        "Samsung Galaxy S24 Ultra, 185000.0 руб. Остаток: 5 шт.")


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


def test_avg_price_with_no_products(category_without_product) -> None:
    category = category_without_product
    assert category.avg_price_in_category() == 0.0  # Testing for no products


def test_avg_price_with_products(product, test_product4) -> None:
    products = [product, test_product4]
    category = Category('Smart', 'Smartphone', products)
    assert category.avg_price_in_category() == 151500.0


def test_avg_price_with_one_product(product) -> None:
    products = [product]
    category = Category('Smart', 'Smartphone', products)
    assert category.avg_price_in_category() == 180000.0  # Only one product


def test_add_product_success(first_category: Category, product) -> None:
    category = first_category
    category.add_product(product)  # This should succeed
    assert len(category._Category__products) == 3  # Check if product was added


def test_add_product_non_positive_quantity(first_category: Category, test_product_zero_quantity) -> None:
    with pytest.raises(TypeError):
        first_category.add_product(test_product_zero_quantity)  # Should raise an error


# def test_setter_with_valid_list(first_category: Category, product) -> None:
#     new_products = [product]
#     first_category.products = new_products
#     expected_string = ''.join(str(prod) for prod in new_products)  # String from products
#     assert str(first_category).strip() == f"{first_category.name}, количество продуктов: {len(first_category.products)} шт.".strip()
#
#
# def test_setter_with_single_product(first_category: Category, product: Product) -> None:
#     new_products = [product]  # Define new_products with the product fixture
#     first_category.products = product  # Set a single product to first_category
#
#     # Test if products can be set with a single product
#     expected_string = ''.join(str(prod) for prod in new_products).strip()  # Combine string representations
#     assert str(first_category.products).strip() == expected_string.strip()


def test_setter_with_invalid_type(first_category: Category) -> None:
    # Test if a TypeError is raised for invalid input
    with pytest.raises(TypeError):
        first_category.products = "Invalid product"


def test_product_name_count(first_category):
    # Assert that the initial product count is correct
    assert first_category.product_name_count == 2  # There are two products in first_category

    # Add another product to the category
    new_product = Product("Apple iPhone 14", "128GB, Черный цвет", 100000.0, 3)
    first_category.add_product(new_product)

    # Assert that the product count has increased
    assert first_category.product_name_count == 3


def test_category_products(category_without_product, product, test_product4):
    # Create a category
    category = category_without_product

    # # Create Product instances
    # product1 = Product("iPhone 14", "Latest Apple iPhone", 999.99, 10)
    # product2 = Product("Samsung Galaxy S23", "Premium Samsung smartphone", 899.99, 5)

    # Add products to the category
    category.add_product(product)
    category.add_product(test_product4)

    # Fetch the products from the category
    products_in_category = category.products

    # Check that the products match what we added
    assert products_in_category == [product, test_product4], "Products in category do not match expected"

    # Check the count of products
    assert category.product_name_count == 2, "Product count in category should be 2"


def test_print_list(first_category, capfd):
    # Call the print_list method
    first_category.print_list()

    # Capture the print output
    captured = capfd.readouterr()

    # Prepare the expected output string
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 2 шт.\n"
        "Samsung Galaxy S24 Ultra, 185000.0 руб. Остаток: 5 шт."
    )

    # Assert if the captured output matches the expected output
    assert captured.out.strip() == expected_output.strip()


def test_product_list(first_category):
    # Expected output
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 2 шт.\n"
        "Samsung Galaxy S24 Ultra, 185000.0 руб. Остаток: 5 шт."
    )

    # Call the product_list method
    actual_output = first_category.product_list

    # Assert the output is as expected
    assert actual_output == expected_output


def test_set_products_with_product():
    category = Category("Smartphones", "Latest smartphone models")
    product = Product("iPhone 14", "128GB, Black", 999.99, 1)

    category.products = product  # Set a single product
    assert len(category._Category__products) == 1  # Check if the products list contains 1 product
    assert category._Category__products[0] == product  # Check if it's the correct product


def test_set_products_with_list():
    category = Category("Smartphones", "Latest smartphone models")
    product1 = Product("Pixel 7", "128GB, White", 599.99, 2)
    product2 = Product("Samsung Galaxy S22", "256GB, Black", 799.99, 3)

    category.products = [product1, product2]  # Set multiple products
    assert len(category._Category__products) == 2  # Check if the products list contains 2 products
    assert category._Category__products == [product1, product2]  # Check if the correct products are set


def test_set_invalid_products():
    category = Category("Smartphones", "Latest smartphone models")

    with pytest.raises(TypeError):  # Expect error for invalid type
        category.products = "Not a product"  # Set an invalid type
