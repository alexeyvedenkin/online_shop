from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Определяет необходимость создания
    нового продукта в дочернем классе
    """
    @classmethod
    @abstractmethod
    def new_product(cls: Any, *args: Any, **kwargs: Any) -> None:
        pass
