from Lab_4.Product import Product


class Set(Product):

    def __init__(self, item1: Product, item2: Product):
        super().__init__(item1.name + ", " + item2.name, item1.price + item2.price)
        self.item1 = item1
        self.item2 = item2
        self._volume = item1.volume + item2.volume

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        raise AttributeError("Cannot set price for a set of products")

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, value: float):
        raise AttributeError("Cannot set volume for a set of products")

    def __str__(self) -> str:
        return f"Набор: {self.item1.name}, {self.item2.name}. Total price: {self.price:.2f}, Total volume: {self.volume:.2f}"
