import logging
import os

from config import LOGS_DIR
from typing import Any

from src.base_product import BaseProduct
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
    all_products: list = []  # Список продуктов

    def __init__(self, name: str, description: str, price: float, quantity=1) -> None:
        """Определены параметры класса Product
        """
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('«Товар с нулевым или отрицательным количеством не может быть добавлен»')
        # Добавление продукта в список all_products
        Product.all_products.append(self)
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.quantity + other.quantity
        else:
            raise TypeError

    @property
    def price(self) -> Any:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> Any:
        price_reducing_confirmation = True
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        elif new_price < self.__price:
            if input(f'Старая цена: {self.__price}руб., новая цена: {new_price}руб. \n'
                     f'Подтверждаете уменьшение цены? y/n : ') not in ['Y', 'y']:
                price_reducing_confirmation = False
        if price_reducing_confirmation:
            self.__price = new_price
        return self.__price

    @classmethod
    def new_product(cls, data: dict) -> Any:  # Проверка наименований
        existing_product = next((p for p in cls.all_products if p.name == data["name"]), None)
        if existing_product:
            print(f"Продукт с именем {data['name']} уже существует.")
            # Увеличение количества
            if data["quantity"] > 0:
                existing_product.quantity += data["quantity"]
                print(f"Количество продукта {data['name']} увеличено до {existing_product.quantity}.")
            else:
                print("Нельзя добавить нулевое или отрицательное количество продукта.")
            return existing_product
        else:
            # Проверка количества
            if data["quantity"] > 0:
                # Создание нового продукта
                new_product = cls(
                    data["name"],  # Название
                    data["description"],  # Описание
                    data["price"],  # Цена
                    data["quantity"]  # Количество
                )
                return new_product
            else:
                raise ValueError('«Товар с нулевым или отрицательным количеством не может быть добавлен»')

    @classmethod
    def get_total_cost(cls) -> Any:
        """Подсчитывает общую стоимость товаров на складе"""
        return sum(product.price * product.quantity for product in cls.all_products)


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(f"Общая стоимость товаров на складе: {float(Product.get_total_cost())} руб.\n")

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 1)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": -5})
