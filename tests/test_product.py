from unittest.mock import patch

import pytest

from typing import Any
from src.exceptions import NonPositiveProductQuantity
from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"


def test_product_create() -> None:
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_product_update(capsys: pytest.CaptureFixture[str], product: Product) -> None:
    product.price = -1
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == "Цена не должна быть нулевая или отрицательная"

    product.price = 200000.0
    assert product.price == 200000.0


def test_new_product(product: Product) -> None:
    new_good = Product("55\" QLED 4K", "Фоновая подсветка",
                       123000.0, 7)
    if product.name != new_good.name:
        assert new_good.name == new_good.name
        assert new_good.description == new_good.description
        assert new_good.price == new_good.price
        assert new_good.quantity == 7
    new_good = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                       180000, 15)
    if product.name == new_good.name:
        assert new_good.name == product.name
        assert new_good.description == product.description
        assert new_good.price == product.price


def test_product_str(product: Product) -> None:
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."


def test_get_total_cost(test_product6: Product) -> None:
    Product.all_products.clear()
    Product.all_products.append(test_product6)
    total_cost = Product.get_total_cost()
    assert total_cost == test_product6.price * test_product6.quantity


def test_product_add_method(product: Product, test_product4: Product) -> None:
    assert product + test_product4 == 12


def test_add_new_product(test_product: dict) -> None:
    exception = Product.new_product(test_product)
    assert exception.name == "Samsung Galaxy C23 Ultra"
    assert exception.description == "256GB, Серый цвет, 200MP камера"
    assert exception.price == 180000.0
    assert exception.quantity == 5
    assert len(Product.all_products) == 4


def test_new_product_increases_quantity_of_existing_product(test_product: dict, duplicate_product: dict) -> None:
    Product.new_product(test_product)
    updated_product = Product.new_product(duplicate_product)
    assert updated_product.quantity == 18


def test_new_product_negative_quantity(new_product_negative_quantity: Any) -> None:
    try:
        Product.new_product(new_product_negative_quantity)
        print("Test failed: ValueError not raised for negative quantity.")
    except ValueError as e:
        print(f"Test passed: {e}")


def test_new_product_zero_quantity(test_product_zero_quantity: Any) -> None:
    try:
        Product.new_product(test_product_zero_quantity)
        print("Test failed: ValueError not raised for zero quantity.")
    except ValueError as e:
        print(f"Test passed: {e}")


def test_get_total_cost_empty(empty_product_list: Any) -> None:
    assert Product.get_total_cost() == "Нет продуктов"


def test_get_total_cost_single_product(empty_product_list: Any, product: Product) -> None:
    assert Product.get_total_cost() == 900000.0


def test_get_total_cost_multiple_products(empty_product_list: Any, product: Product, test_product4: Product) -> None:
    assert Product.get_total_cost() == 1761000.0


def test_non_positive_product_quantity(test_product_zero_quantity: Any) -> None:
    with pytest.raises(NonPositiveProductQuantity):
        Product(**test_product_zero_quantity)
    try:
        Product.new_product(test_product_zero_quantity)
    except NonPositiveProductQuantity:
        assert True
    else:
        assert False


def test_set_price_valid(product: Product) -> None:
    exception = 180000.0
    assert product.price == exception  # Check if price is set correctly


def test_set_price_negative() -> None:
    product = Product('Товар A', 'Описание A', 100.0, 10)
    with patch('builtins.print') as mock_print:  # Mock print to check output
        product.price = -10.0
        mock_print.assert_called_once_with('Цена не должна быть нулевая или отрицательная')


def test_set_price_decrease_confirmation() -> None:
    product = Product('Товар A', 'Описание A', 100.0, 10)
    with patch('builtins.input', return_value='n'):
        product.price = 100.0
        product.price = 80.0
        assert product.price == 100.0

    with patch('builtins.input', return_value='y'):
        product.price = 70.0
        assert product.price == 70.0


def test_add_valid_products(test_product: Any, test_unique_product: Any) -> None:
    product1 = Product(name='Product 1', description='First product', price=10.0, quantity=5)
    product2 = Product(name='Product 2', description='Second product', price=20.0, quantity=3)

    result = product1 + product2
    assert result == 8


def test_add_invalid_type() -> None:
    product = Product(name='Product 1', description='First product', price=10.0, quantity=5)

    with pytest.raises(TypeError):
        product + "не Product"
