from src.category import Category


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Smart"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(first_category.product_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3


def test_category_products_property(first_category):
    assert first_category.products == ("Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 2\n"
                                       "Samsung Galaxy S24 Ultra, 256GB, Серый цвет, 200MP камера, 185000.0, 5\n")


def test_category_products_setter(first_category, product):
    assert len(first_category.product_in_list) == 2
    first_category.products = product
    assert len(first_category.product_in_list) == 3

