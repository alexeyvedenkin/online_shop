from typing import Any, Optional

from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    # product_name_count = 0
    # total_product_count = 0

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
        # self.product_name_count = len(self.__products)
        # self.total_product_count = sum(product.quantity for product in self.__products) if self.__products else 0

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
        # Check if product is an instance of Product
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
        self.__products.append(product)
