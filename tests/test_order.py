from src.order import Order


def test_order_init(product, quantity=2) -> None:
    order = Order(product, 2)
    assert order.id_num == 1
    assert order.product == product
    assert order.quantity == 2


def test_order_add_product(test_product4, quantity=2) -> None:
    order = Order(test_product4, 2)
    product2 = test_product4
    new_order = order.add_product(product2, 3)
    assert new_order.product == test_product4
    assert new_order.quantity == 3


def test_order_str(test_product6):
    order = Order(test_product6, 1)
    order_str = str(order)
    assert order_str.startswith("Заказ №")
    assert test_product6.name in order_str
    assert str(test_product6.price * 1) in order_str
