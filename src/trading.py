from abc import ABC, abstractmethod
from typing import Any


class Trading(ABC):
    """Абстрактный класс для задания параметров классам,
    связанным с торговлей
    """

    @classmethod
    @abstractmethod
    def add_product(cls: Any, *args: Any, **kwargs: Any) -> Any:
        """Устанавливает необходимость добавления продукта
        в экземпляре дочернего класса
        """
        pass
