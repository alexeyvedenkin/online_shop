from typing import Any

from src.exceptions import NonPositiveProductQuantity
from src.product import Product
from src.trading import Trading


class Order(Trading):

    id_num = 1

    def __init__(self) -> None:
        self.product = None
        self.quantity = 0
        self.id_num = Order.id_num
        Order.id_num += 1

    def __str__(self) -> str:
        if self.product is None:
            return f"Заказ №{self.id_num}: Продукт не добавлен."
        return (f"Заказ №{self.id_num}: {self.product.name}, Количество: {self.quantity}, "
                f"Общая стоимость: {self.calculate_total_cost()} руб.\n")

    def add_product(self, product: Product, quantity: int) -> None:
        try:
            if not isinstance(product, Product):
                raise TypeError("Товар должен соответствовать классу Product")
            if quantity <= 0:
                raise NonPositiveProductQuantity("Нельзя добавить товар с нулевым или отрицательным количеством")
            self.product = product
            self.quantity = quantity
            print("Товар добавлен успешно")
        except NonPositiveProductQuantity as e:
            print(str(e))
        except TypeError as te:
            print(str(te))
        finally:
            print("Обработка добавления товара завершена")

    def calculate_total_cost(self) -> float:
        return self.product.price * self.quantity


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    order = Order()  # Create an order instance
    order.add_product(product1, 2)  # Add product correctly
    print(order)
    order = Order()  # Create an order instance
    order.add_product(product1, 0)
    print(order)