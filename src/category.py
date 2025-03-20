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
                print("Товар добавлен успешно")
            finally:
                print("Обработка добавления товара завершена")
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

    def avg_price_in_category(self):
        if not self.__products:
            print("Товары в категории закончились")
            return 0.0
        logger.debug('Начало применения метода avg_price_in_category в экземпляре класса Category')
        result = (sum(product.price for product in self.products_in_list) /
                len(self.products_in_list))
        return round(result, 2)


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    print(11)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    print(12)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    print(13)
    logger.info('Добавлены новые экземпляры класса Product')
    print(f"Общая стоимость товаров на складе: {float(Product.get_total_cost())} руб.\n")
    logger.info('Успешно применен метод avg_price_in_category')
    print(14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
    print(15)
    logger.info('Сформирован новый экземпляр класса Category')
    print(category1)
    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    print(101)
    category1.add_product(product4)
    print(category1.products)
    # print(len(category1))
    print(100)
    print(category1)
    print(200)
    print(category1.products)
    print(300)

    print(f'Средняя цена товаров в категории:{category1.avg_price_in_category()}')
    print(400)
    product5 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 3)
    print(500)
    category2 = Category("Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
                         [product5])
    print(f'Категория: {category2.name}, {category2}')
    print(f'Средняя цена товаров в категории:{category2.avg_price_in_category()}')
    print(600)

    print(category2.avg_price_in_category())
