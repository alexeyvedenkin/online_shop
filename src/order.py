from src.exceptions import NonPositiveProductQuantity
from src.product import Product
from src.trading import Trading


class Order(Trading):
    """Определяет товары (работы, услуги), предназначенные
    к оплате покупателем, формирует стоимость к оплате
    """
    id_num = 1

    def __init__(self) -> None:
        """Определяет структуру экземпляра класса Order
        """
        self.product = None
        self.quantity = 0
        self.id_num = Order.id_num
        Order.id_num += 1

    def __str__(self) -> str:
        """Определяет формат вывода в консоль экземпляра класса Order
        """
        if self.product is None:
            return f"Заказ №{self.id_num}: Продукт не добавлен.\n"
        return (f"Заказ №{self.id_num}: {self.product.name}, Количество: {self.quantity}, "
                f"Общая стоимость: {self.calculate_total_cost()} руб.\n")

    def add_product(self, product: Product, quantity: int) -> None:
        """Выполняет добавление товара в экземпляр класса Order
        """
        try:
            if not isinstance(product, Product):
                raise TypeError("Товар должен соответствовать классу Product")
            if quantity <= 0:
                raise NonPositiveProductQuantity("Нельзя добавить товар с нулевым или отрицательным количеством")
            self.product = product
            self.quantity = quantity
            print("Товар добавлен успешно")
        finally:
            print("Обработка добавления товара завершена")

    def calculate_total_cost(self) -> float:
        """Определяет общую стоимость в экземпляре класса Order
        """
        if self.product:  # Проверка, установлен ли продукт
            return self.product.price * self.quantity
        return 0.0
