import pytest

from typing import Any

from src.exceptions import NonPositiveProductQuantity
from src.order import Order
from src.product import Product


def test_order_init() -> None:
    order = Order()
    assert order.product is None
    assert order.quantity == 0


def test_add_product_success(product: Product) -> None:
    order = Order()
    order.add_product(product, 2)
    assert order.product == product
    assert order.quantity == 2
    assert order.calculate_total_cost() == 360000.0


def test_add_invalid_product(test_product_without_quantity: Any) -> None:
    order = Order()

    try:
        order.add_product(test_product_without_quantity, None)
    except TypeError:
        pass

    with pytest.raises(NonPositiveProductQuantity):
        order.add_product(test_product_without_quantity, -1)

    with pytest.raises(NonPositiveProductQuantity):
        order.add_product(test_product_without_quantity, 0)


def test_order_str(test_product6: Product) -> None:
    order = Order()
    order.add_product(test_product6, 1)
    order_str = str(order)
    assert order_str.startswith("Заказ №")
    assert test_product6.name in order_str
    assert str(test_product6.price * 1) in order_str


def test_order_str_with_product(product: Product) -> None:
    order = Order()
    order.add_product(product, 2)
    expected_id_num = order.id_num
    expected_str = f"Заказ №{expected_id_num}: {product.name}, Количество: 2, Общая стоимость: 360000 руб.\n"
    assert str(order) == expected_str


def test_add_valid_product(test_product_without_quantity: Any) -> None:
    order = Order()

    try:
        order.add_product(test_product_without_quantity, 1)
        assert order.product == test_product_without_quantity
        assert order.quantity == 1
    except Exception:
        pytest.fail("Adding valid product raised an exception.")


def test_add_invalid_product_type() -> None:
    order = Order()
    invalid_product = ''

    with pytest.raises(TypeError):
        order.add_product(invalid_product, 1)


def test_order_str_without_product() -> None:
    order = Order()
    expected_str = f"Заказ №{order.id_num}: Продукт не добавлен.\n"
    assert str(order) == expected_str
