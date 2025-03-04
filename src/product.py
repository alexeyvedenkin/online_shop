class Product:
    all_products = []  # Список продуктов
    name: str
    description: str
    price: float
    quantity: int

    @classmethod
    def new_product(cls, data):  # Проверка наименований
        existing_product = next((p for p in cls.all_products if p.name == data["name"]), None)
        if existing_product:
            print(f"Продукт с именем {data['name']} уже существует.")
            # Увеличение количества
            existing_product.quantity += data["quantity"]
            print(f"Количество продукта {data['name']} увеличено до {existing_product.quantity}.")
        # # Запрос на изменение цены
        # if existing_product.price != data["price"]:
        #     response = input(
        #     f"Цена {data['name']} отличается. Текущая цена: {existing_product.price}, новая: {data['price']}. Изменить? (да/нет): ")
        #     if response.lower() == "да":
        #         existing_product.price = data["price"]
        #         print(f"Цена продукта {data['name']} изменена на {existing_product.price}.")
        #     else:
        #         print("Изменение отменено.")
        #         return existing_product
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

    def __init__(self, name, description, price, quantity):
        """Определены параметры класса Product
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    # # @classmethod
    # def new_product(cls, data):
    #     # Метод создания нового продукта из словаря
    #     return cls(
    #         data["name"],  # Название продукта
    #         data["description"],  # Описание продукта
    #         data["price"],  # Цена продукта
    #         data["quantity"]  # Количество продукта
    #     )
    #
    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price: float):
        price_reducing_confirmation = True
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        elif new_price < self.__price:
            if input(f'Старая цена: {self.__price}руб., новая цена: {new_price}руб. Подтверждаете уменьшение цены? y/n : ') not in ['Y', 'y']:
                price_reducing_confirmation = False
        if price_reducing_confirmation:
            self.__price = new_price
        return self.__price

#
if __name__ == '__main__':
    product2 = Product("Honor 70 Pro+", "512GB, Черный цвет, 400MP камера", 180000.0, 5)
    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(Product.all_products)
    print(1000)
    product2.price = -10000.0
    print(product2.price)
    product2.price = 110000.0
    print(product2.price)
    product2.price = 120000.0
    print(product2.price)
    print(2000)
    print(Product.all_products)
    print(3000)
    product3 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)
    print(4000)
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)
    print(5000)
    new_product.price = 800
    print(new_product.price)