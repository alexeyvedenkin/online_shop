from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"


def test_product_create():
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product.name = "Xiaomi Redmi Note 11"
    product.description = "1024GB, Синий"
    product.price = 31000.0
    product.quantity = 14


def test_product_update(capsys, product):
    product.price = -1
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product.price = 200000.0
    assert product.price == 200000.0
