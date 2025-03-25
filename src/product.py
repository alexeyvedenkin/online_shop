import logging
import os
from typing import Any

from config import LOGS_DIR
from src.base_product import BaseProduct
from src.exceptions import NonPositiveProductQuantity
# from src.category import Category
from src.print_mixin import PrintMixin

logger = logging.getLogger("product")
logger.setLevel(logging.DEBUG)
log_file_path = os.path.join(LOGS_DIR, 'product.log')
file_handler = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


class Product(BaseProduct, PrintMixin):
    """Определяет перечень товаров, предназначенных к продаже
    """
    all_products: list = []  # Список продуктов

    def __init__(self: Any, name: str, description: str, price: float, quantity: int = 1) -> None:
        """Определяет параметры для экземпляра класса Product
        """
        self.name = name
        self.description = description
        self.__price = price
        logger.debug('Начало определения количества в экземпляре класса Product')
        if quantity > 0:
            self.quantity = quantity
            logger.debug('Положительное количество в экземпляре класса Product')
        else:
            logger.debug('Не положительное количество в экземпляре класса Product')
            raise NonPositiveProductQuantity('«Товар с нулевым или отрицательным количеством не может быть добавлен»')
        # Добавление продукта в список all_products
        Product.all_products.append(self)
        logger.debug('Товар добавлен в общий список класса Product')
        super().__init__()

    def __str__(self) -> str:
        """Определяет формат вывода информации о товарах в консоль
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self: Any, other: Any) -> int:
        """Выполняет суммирование количества двух экземпляров
        класса Product
        """
        if isinstance(other, Product):
            logger.debug('Добавляемый объект принадлежит классу Product')
            return self.quantity + other.quantity
        else:
            logger.debug('Добавляемый объект не принадлежит классу Product')
            raise TypeError

    @property
    def price(self) -> Any:
        """Фиксирует параметр price экземпляра класса Product, как приватный
        """
        logger.debug('Определен параметр price в экземпляре класса Product')
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Выполняет проверку на соответствие типа
        и устанавливает новое значение для свойства price
        """
        logger.debug('Установлен флаг проверки подтверждения уменьшения цены в экземпляре класса Product')
        price_reducing_confirmation = True
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            logger.error('Введена не положительная цена в экземпляре класса Product')
            return self.price
        elif new_price < self.__price:
            logger.debug('Получена цена меньше имеющейся в экземпляре класса Product')
            if input(f'Старая цена: {self.__price}руб., новая цена: {new_price}руб. \n'
                     f'Подтверждаете уменьшение цены? y/n : ') not in ['Y', 'y']:
                logger.info('Отказано в уменьшении цены')
                price_reducing_confirmation = False
        if price_reducing_confirmation:
            logger.info('Подтверждено уменьшение цены')
            self.__price = new_price
            logger.debug('Установлена новая цена в экземпляре класса Product')

    @classmethod
    def new_product(cls, data: dict[Any, Any]) -> 'Product':  # Проверка наименований
        """Выполняет добавление нового экземпляра класса Product
        """
        logger.debug('Обращение к класс-методу new_product в классе Product')
        existing_product = next((p for p in cls.all_products if p.name == data["name"]), None)
        if existing_product:
            logger.debug('Обнаружено совпадение с имеющимся товаром в классе Product')
            print(f"Продукт с именем {data['name']} уже существует.")
            # Увеличение количества
            if data["quantity"] > 0:
                existing_product.quantity += data["quantity"]
                logger.info('Увеличено количество совпадающего товара')
                print(f"Количество продукта {data['name']} увеличено до {existing_product.quantity}.")
                return existing_product
            else:
                logger.info('Отказано в уменьшении количества совпадающего товара')
                print("Нельзя добавить нулевое или отрицательное количество продукта.")
                return None
        else:
            logger.info('Нет совпадений с имеющимися товарами')
        # Проверка количества
            if data["quantity"] > 0:
                logger.debug('Проверено количество добавляемого товара')
                # Создание нового продукта
                new_product = cls(
                    data["name"],  # Название
                    data["description"],  # Описание
                    data["price"],  # Цена
                    data["quantity"]  # Количество
                )
                logger.info('Создан новый экземпляр класса Product')
                return new_product
            else:
                logger.debug('Отказано в уменьшении количества совпадающего товара')
                raise NonPositiveProductQuantity(
                    '«Товар с нулевым или отрицательным количеством не может быть добавлен»')

    @classmethod
    def get_total_cost(cls) -> Any:
        """Подсчитывает общую стоимость товаров на складе
        """
        total_cost = sum(product.price * product.quantity for product in cls.all_products)
        if total_cost == 0 and not cls.all_products:
            return "Нет продуктов"
        return total_cost
