from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls):
        pass
