from Lab_4.Product import Product


class Phone(Product):
    def __init__(self, name: str, price: float, brand: str, model: str, screen_size: float) -> None:
        super().__init__(name, price)
        self._brand = brand
        self._model = model
        self._screen_size = screen_size

    def __str__(self) -> str:
        """Возвращает строку с описанием телефона, содержащей название бренда, модель, размер экрана, цену и описание
        если имеется.

        Returns:
            str: Описание телефона.
        """
        r = f"{self._brand} {self._model}, Screen Size: {self._screen_size}, Price: ${self._price}"
        if super().description is not None:
            r += f"\n{super().description}"
        return r

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def screen_size(self) -> float:
        return self._screen_size

    @screen_size.setter
    def screen_size(self, new_size: float) -> None:
        if new_size <= 0:
            raise ValueError("Screen size must be positive")
        self._screen_size = new_size
