from src.product import Product
from typing import Any, Optional


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[Any]=None) -> None:
        """Определены параметры класса Category
        """
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products_in_list(self) -> Any:
        return self.__products

    def add_product(self, product: Product) -> Any:
        # Check if product is an instance of Product
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product")
        self.__products.append(product)
        Category.product_count += 1

    # def get_products(self):
    #     return self.__products

    def print_list(self) -> Any:
        print(self.__products)

    @property
    def products(self) -> Any:
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    # @products.setter
    # def products(self, product: Product) -> Any:
    #     self.__products.append(product)
    #     Category.product_count += 1
