import pytest

from src.category import Category
from src.product_iterator import ProductIterator


# Test the ProductIterator
def test_product_iterator_iter(first_category):
    iterator = ProductIterator(first_category)

    # Call __iter__ and ensure index is reset to 0
    iterator.__iter__()
    assert iterator.index == 0  # Index should be reset to 0
