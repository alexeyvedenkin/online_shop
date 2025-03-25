from typing import Any

from src.product import Product


class LawnGrass(Product):
    """Определяет класс товаров, соответствующих газонной траве
    """
    def __init__(self, name: str, description: str,
                 price: float, quantity: int, country: str, germination_period: str, color: str) -> None:
        """Определяет параметры экземпляра класса LawnGrass
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> Any:
        """Выполняет суммирование количества двух экземпляров
        класса LawnGrass
        """
        if isinstance(other, LawnGrass):
            return self.quantity + other.quantity
        else:
            raise TypeError
