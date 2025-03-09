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

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    @property
    def products_in_list(self) -> Any:
        return self.__products

    def add_product(self, product: Product) -> Any:
        # Check if product is an instance of Product
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product")
        self.__products.append(product)
        Category.product_count += 1

    def print_list(self) -> Any:
        print(self.__products)

    @property
    def products(self) -> Any:
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
    print(category1.products)

    print(category1)