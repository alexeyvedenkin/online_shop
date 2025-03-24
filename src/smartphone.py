from typing import Any

from src.product import Product


class Smartphone(Product):
    """Определяет класс товаров, соответствующих смартфонам
    """
    def __init__(self, name: str, description: str,
                 price: float, quantity: int, efficiency: float, model: str, memory: int, color: str) -> None:
        """Определяет параметры экземпляра класса Smartphone
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self: Any, other: Any) -> Any:
        """Выполняет суммирование количества двух экземпляров
        класса Smartphone
        """
        if isinstance(other, Smartphone):
            return self.quantity + other.quantity
        else:
            raise TypeError
