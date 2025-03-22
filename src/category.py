import logging
import os

from config import LOGS_DIR
from typing import Any, Optional

from src.exceptions import NonPositiveProductQuantity
from src.product import Product
from src.trading import Trading


logger = logging.getLogger("category")
logger.setLevel(logging.DEBUG)
log_file_path = os.path.join(LOGS_DIR, 'category.log')
file_handler = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


class Category(Trading):
    name: str
    description: str
    __products: list
    category_count = 0

    def __init__(self, name: str, description: str, products: Optional[Any] = None) -> None:
        """Определены параметры класса Category
        """
        self.name = name
        logger.debug('Определен атрибут name для экземпляра класса Category')
        self.description = description
        logger.debug('Определен атрибут description для экземпляра класса Category')
        if isinstance(products, list):
            self.__products = products if products else []
            logger.debug('Добавлен список products в экземпляр класса Category')
        else:
            self.__products = [products] if products else []
            logger.debug('Добавлен пустой список для атрибута products в экземпляр класса Category')

        Category.category_count += 1

    def __str__(self) -> Any:
        logger.debug('Применен метод __str__ для экземпляра класса Category')
        return f"{self.name}, количество продуктов: {self.total_product_count} шт."

    @property
    def products_in_list(self) -> Any:
        return self.__products

    @property
    def product_name_count(self) -> int:
        return len(self.__products)

    @property
    def total_product_count(self) -> float:
        return sum(product.quantity for product in self.__products) if self.__products else 0

    def add_product(self, product: Product) -> Any:
        if not isinstance(product, Product):
            logger.debug('Не выполнено соответствие товара классу Product')
            raise TypeError("Товар должен соответствовать классу Product")
        else:
            try:
                if product.quantity <= 0:
                    raise NonPositiveProductQuantity("Нельзя добавить товар с нулевым или отрицательным количеством")
            except NonPositiveProductQuantity as e:
                print(str(e))
            else:
                self.__products.append(product)
                print()
                print("Товар добавлен успешно")
            finally:
                print()
                print("Обработка добавления товара завершена")
                print()

            logger.info('Товар, соответствующий классу Product, добавлен в экземпляр класса Category')

    @property
    def get_total_product_count(self) -> Any:
        # Подсчет общего количества товаров в категории
        self.total_product_count = sum(product.quantity for product in self.__products) if self.__products else 0
        return self.total_product_count

    def print_list(self) -> Any:
        logger.debug('Применен метод print_list для экземпляра класса Category')
        print(self.products)

    @property
    def products(self) -> Any:
        logger.debug('Начало определения списка товаров в экземпляре класса Category')
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        logger.info('Список товаров в экземпляре класса Category сформирован')
        return product_str

    @products.setter
    def products(self, value: Any):
        logger.debug('Установка нового значения для свойства products в экземпляре класса Category')
        if isinstance(value, list):
            self.__products = value
        elif isinstance(value, Product):
            self.__products = [value]
        else:
            raise TypeError("Недопустимый тип")
        logger.info('Свойство products в экземпляре класса Category установлено')

    def avg_price_in_category(self):
        if not self.__products:
            print("Товары в категории закончились")
            return 0.0
        logger.debug('Начало применения метода avg_price_in_category в экземпляре класса Category')
        result = (sum(product.price for product in self.products_in_list) /
                len(self.products_in_list))
        return round(result, 2)
