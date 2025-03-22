from abc import ABC, abstractmethod


class Trading(ABC):
    """Абстрактный класс для задания параметров классам,
    связанным с торговлей
    """

    @classmethod
    @abstractmethod
    def add_product(cls, *args, **kwargs):
        pass
