class PrintMixin:
    """Определяет дополнительное форматирование
    для вывода результатов в консоль
    """

    def __init__(self) -> None:
        """Определяет параметры класса PrintMixin
        """
        print(repr(self))

    def __repr__(self) -> str:
        """Определяет параметры,
        необходимые к применению в дочерних классах
        """
        return f"{self.__class__.__name__}({getattr(self, 'name', 'N/A')}, " \
               f"{getattr(self, 'description', 'N/A')}, " \
               f"{getattr(self, 'price', 'N/A')}, " \
               f"{getattr(self, 'quantity', 'N/A')})"
