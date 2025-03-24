from typing import Any

from src.category import Category


class ProductIterator:
    """Выполняет подсчет количества товаров в категории
    """
    def __init__(self, category_obj: Category) -> None:
        """Определяет параметры экземпляра класса ProductIterator
        """
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> Any:
        """Обнуляет счетчик товаров при повторном применении
        """
        self.index = 0
        return self

    def __next__(self) -> Any:
        """Определяет результат подсчета количества товаров в категории
        """
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
