from src.product import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) == Smartphone:
            return self.quantity + other.quantity
        else:
            raise TypeError


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                       180000.0, 5)
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                        180000.0, 5, 95.5, "S23 Ultra", 256, "Серый цвет" )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space",
                             210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий",
                             31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1 + smartphone2)
