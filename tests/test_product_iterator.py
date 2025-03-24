from src.category import Category
from src.product_iterator import ProductIterator


def test_product_iterator_iter(first_category: Category) -> None:
    iterator = ProductIterator(first_category)

    iterator.__iter__()
    assert iterator.index == 0
