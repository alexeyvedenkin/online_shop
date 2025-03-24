class PrintMixin:

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({getattr(self, 'name', 'N/A')}, " \
               f"{getattr(self, 'description', 'N/A')}, " \
               f"{getattr(self, 'price', 'N/A')}, " \
               f"{getattr(self, 'quantity', 'N/A')})"
