class Product:
    def __init__(self, name: str, price: float, description: str = None, volume: float = 0):
        """
        Конструктор класса Product.

        :param name: Название товара.
        :param price: Цена товара.
        :param description: Описание товара.
        :param volume: Объем товара в кубических сантиметрах.
        """
        self._name = name
        self._price = price
        self._description = description
        self._volume = volume

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта класса.

        :return: Строковое представление объекта класса.
        """
        return f"{self._name} - ${self._price}\n{self._description}"

    def apply_discount(self, discount: float) -> float:
        """
        Вычисляет стоимость товара с учетом скидки.

        :param discount: Размер скидки в процентах.
        :return: Цена товара со скидкой.
        """
        discounted_price = self._price * (100 - discount) / 100
        return max(0.01, round(discounted_price, 2))

    def get_quantity_in_box(self, width: float, height: float, depth: float) -> int:
        """
        Вычисляет количество товара, помещающегося в коробку заданных размеров.

        :param width: Ширина коробки, см.
        :param height: Высота коробки, см.
        :param depth: Глубина коробки, см.
        :return: Количество товара, помещающегося в коробку.
        """
        box_volume = width * height * depth
        return int(box_volume // self._volume)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def discount(self) -> float:
        return self._discount

    @discount.setter
    def discount(self, value: float):
        self._discount = value

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    # Сеттер для поля _volume, принимающий длину, ширину и высоту товара
    def set_volume(self, length: float, width: float, height: float):
        self._volume = length * width * height

    def __add__(self, other):
        """
        Переопределяет действие символа "+"
        Создаёт набор из 2 элементов

        :param Товар
        :return: Набор из 2 товаров
        """
        from Lab_4.Set import Set
        return Set(self, other)