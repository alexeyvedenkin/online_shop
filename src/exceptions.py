from typing import Optional


class NonPositiveProductQuantity(Exception):
    """Определяет самостоятельные виды исключений для проекта
    """

    def __init__(self, message: Optional[str]) -> None:
        super().__init__(message)
