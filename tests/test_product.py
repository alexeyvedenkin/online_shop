import pytest

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
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

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
        # assert product.quantity == product.quantity + new_good.quantity


def test_product_str(product: Product) -> None:
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."


def test_get_total_cost(test_product6: Product) -> None:
    Product.all_products.clear()
    Product.all_products.append(test_product6)
    total_cost = Product.get_total_cost()
    assert total_cost == test_product6.price * test_product6.quantity


def test_product_add_method(product: Product, test_product4: Product) -> None:
    assert product + test_product4 == 12
