from src.product import Product

class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    # def __init__(self, name, description, __products: list = None):
    #     """Определены параметры класса Category
    #     """
    #     self.name = name
    #     self.description = description
    #     # Check if products is a list
    #     if __products is None:
    #         self.__products = []
    #     # elif not isinstance(__products, list):
    #     #     raise TypeError("Products must be a list")
    #     else:
    #         self.__products = __products
    #     Category.category_count += 1
    #     Category.product_count += len(__products) if __products else 0

    def __init__(self, name, description, __products=None):
        """Определены параметры класса Category
        """
        self.name = name
        self.description = description
        self.__products = __products if __products else []
        Category.category_count += 1
        Category.product_count += len(__products) if __products else 0

    def add_product(self, product: Product):
        # Check if product is an instance of Product
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product")
        self.__products.append(product)
        Category.product_count += 1

    def get_products(self):
        return self.__products


    # def add_product(self, product: Product):
    #     self.__products.append(product)

    # Метод для вывода приватного атрибута
    def print_list(self):
        print(self.__products)

    #
    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
    #
    #
    @products.setter
    def products(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    #
    # @property
    # def product_in_list(self):
    #     return self.__products


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
    print(category1.product_count)
    print(category1.products)
    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(555)
    print(category1.products)
    print(666)
    print(category1.product_count)