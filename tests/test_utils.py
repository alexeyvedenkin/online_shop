def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"


def test_category_init(first_category, second_category):
    assert first_category.name == "Smart"
    assert first_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3

