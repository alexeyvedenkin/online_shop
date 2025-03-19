from typing import Any

from src.exceptions import NonPositiveProductQuantity
from src.product import Product
from src.trading import Trading


class Order(Trading):

    id_num = 1

    def __init__(self, product: Product, quantity: int) -> None:
        self.id_num = Order.id_num
        self.product = product
        self.quantity = quantity
        Order.id_num += 1

    def __str__(self) -> str:
        # Return a string representation of the order
        return (f"Заказ №{self.id_num}: {self.product.name}, Количество: {self.quantity},"
                f" Общая стоимость: {self.calculate_total_cost()} руб.")

    def add_product(self, product: Product, quantity: int) -> Any:
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product")
        try:
            if product.quantity <= 0:
                raise NonPositiveProductQuantity("Нельзя добавить товар с нулевым или отрицательным количеством")
        except NonPositiveProductQuantity as e:
            print(str(e))
        else:
            self.products.append(product)
            print("Товар добавлен успешно")
        finally:
            print("Обработка добавления товара завершена")
        return Order(product, quantity)

    def calculate_total_cost(self) -> float:
        # Calculate the total cost of the order
        return self.product.price * self.quantity

    @property
    def products(self) -> Any:
        product_str = ""
        for product in self.products:
            product_str += f"{str(product)}\n"
        return product_str

    @products.setter
    def products(self, product: Product) -> Any:
        if isinstance(product, Product):
            try:
                if product.quantity <= 0:
                    raise NonPositiveProductQuantity("Нельзя добавить товар с нулевым или отрицательным количеством")
            except NonPositiveProductQuantity as e:
                print(str(e))
            else:
                self.products.append(product)
                print("Товар добавлен успешно")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                       180000.0, 5)
    order = Order(product1, 2)
    print(order)
    order = Order(product1, 0)
    print(order)
