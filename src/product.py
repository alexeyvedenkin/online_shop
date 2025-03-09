from typing import Any


class Product:
    all_products: list = []  # Список продуктов
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Определены параметры класса Product
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        # Добавление продукта в список all_products
        Product.all_products.append(self)

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

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
    def get_total_cost(cls):
        """Подсчитывает общую стоимость товаров на складе"""
        return sum(product.price * product.quantity for product in cls.all_products)

# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(product1)
#     print(product2)
#     print(product3)
#
#     print(f"Общая стоимость товаров на складе: {float(Product.get_total_cost())} руб.\n")
#
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#
#     print(f"Общая стоимость товаров на складе: {float(Product.get_total_cost())} руб.\n")
#
#     new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
#
#     print(f"Общая стоимость товаров на складе: {float(Product.get_total_cost())} руб.\n")
#
#     for product in Product.all_products:
#         print(product)
