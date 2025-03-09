from typing import Any, Optional

from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_name_count = 0
    total_product_count = 0

    def __init__(self, name: str, description: str, products: Optional[Any] = None) -> None:
        """Определены параметры класса Category
        """
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        self.product_name_count = len(self.__products)
        self.total_product_count = sum(product.quantity for product in self.__products) if self.__products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.total_product_count} шт."

    @property
    def products_in_list(self) -> Any:
        return self.__products

    @property
    def get_total_product_count(self):
        # Подсчет общего количества товаров в категории
        self.total_product_count = sum(product.quantity for product in self.__products) if self.__products else 0
        return self.total_product_count

    def add_product(self, product: Product) -> Any:
        # Check if product is an instance of Product
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product")
        self.__products.append(product)
        self.product_name_count += 1
        # self.total_product_count += product.quantity

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


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#     print(category1)
#     print(category1.products)
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
#
#     print(category1)
