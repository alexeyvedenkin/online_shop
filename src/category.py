from typing import Any, Optional

from src.exceptions import NonPositiveProductQuantity
from src.product import Product
from src.trading import Trading


class Category(Trading):
    name: str
    description: str
    __products: list
    category_count = 0

    def __init__(self, name: str, description: str, products: Optional[Any] = None) -> None:
        """Определены параметры класса Category
        """
        self.name = name
        self.description = description
        if isinstance(products, list):
            self.__products = products if products else []
        else:
            self.__products = [products] if products else []
        Category.category_count += 1

    def __str__(self) -> Any:
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
            raise TypeError("Product must be an instance of Product")
        self.__products.append(product)

    @property
    def get_total_product_count(self) -> Any:
        # Подсчет общего количества товаров в категории
        self.total_product_count = sum(product.quantity for product in self.__products) if self.__products else 0
        return self.total_product_count

    def print_list(self) -> Any:
        print(self.products)

    @property
    def products(self) -> Any:
        product_str = ""
        for product in self.__products:
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
                self.__products.append(product)
                print("Товар добавлен успешно")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    def avg_price_in_category(self):
        try:
            return (sum(product.price for product in self.products_in_list) /
                    sum(product.quantity for product in self.products_in_list))
        except ZeroDivisionError:
            print("Товары в категории закончились")
            return 0.0


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(f"Общая стоимость товаров на складе: {float(Product.get_total_cost())} руб.\n")

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
    print(category1)
    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1)
    print(category1.products)

    print(category1.avg_price_in_category())

    # product5 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 0)
    category2 = Category("Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        )
    print(category2.avg_price_in_category())
