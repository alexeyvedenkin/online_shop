from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin



class Product(BaseProduct, PrintMixin):
    all_products: list = []  # Список продуктов

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Определены параметры класса Product
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
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
            existing_product.quantity += data["quantity"]
            print(f"Количество продукта {data['name']} увеличено до {existing_product.quantity}.")
            return existing_product
        else:
            # Создание нового продукта
            new_product = cls(
                data["name"],  # Название
                data["description"],  # Описание
                data["price"],  # Цена
                data["quantity"]  # Количество
            )
            cls.all_products.append(new_product)  # Добавление в список
        return new_product

    @classmethod
    def get_total_cost(cls) -> Any:
        """Подсчитывает общую стоимость товаров на складе"""
        return sum(product.price * product.quantity for product in cls.all_products)
