from src.category import Category
from src.product import Product


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Smart"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    # assert first_category.product_name_count == 3
    # assert second_category.product_name_count == 3


def test_category_products_property(first_category: Category) -> None:
    assert first_category.products == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 2 шт.\n"
                                       "Samsung Galaxy S24 Ultra, 185000.0 руб. Остаток: 5 шт.\n")


def test_category_products_setter(first_category: Category, product: Product) -> None:
    assert len(first_category.products_in_list) == 2
    first_category.products = product
    assert len(first_category.products_in_list) == 3
