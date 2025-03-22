import pytest

from src.order import Order


def test_order_init() -> None:
    order = Order()
    assert order.product is None
    assert order.quantity == 0


def test_add_product_success(product):
    order = Order()
    order.add_product(product, 2)
    assert order.product == product
    assert order.quantity == 2
    assert order.calculate_total_cost() == 360000.0


def test_order_str(test_product6):
    order = Order()
    order.add_product(test_product6, 1)
    order_str = str(order)
    assert order_str.startswith("Заказ №")
    assert test_product6.name in order_str
    assert str(test_product6.price * 1) in order_str
