class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Определены параметры класса Product
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, data):
        # Метод создания нового продукта из словаря
        return cls(
            data["name"],  # Название продукта
            data["description"],  # Описание продукта
            data["price"],  # Цена продукта
            data["quantity"]  # Количество продукта
        )

    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        self.__price = new_price


#
if __name__ == '__main__':
    product2 = Product("Honor 70S+ pro", "512GB, Черный цвет, 400MP камера", 180000.0, 5)
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    product2.price = -10000.0
    print(product2.price)
    product2.price = 210000.0
    print(product2.price)