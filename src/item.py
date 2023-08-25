import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    csv_file_path = '../src/items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # добавление инициализатора для класса MixinLayout
        super().__init__()

        Item.all.append(self)

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return f"Нельзя складывать классы Phone или Item с экземплярами не Phone или Item"

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.__name}', {self.price}"
                f", {self.quantity})")

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name=csv_file_path):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла
        по пути csv_file_path."""
        cls.all.clear()

        try:
            with open(file_name, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                file_header = reader.fieldnames
                if len(file_header) < 3:
                    raise InstantiateCSVError('Файл содержит меньше 3 столбцов')
                for row in reader:
                    name = row["name"]
                    price = row["price"]
                    quantity = row["quantity"]
                    cls(name, float(price), int(quantity))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(number):
        """Статический метод, возвращающий число из числа-строки."""
        return int(float(number))


class InstantiateCSVError(Exception):
    """Класс для выбрасывания пользовательского исключения по кол-ву столбцов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл поврежден.'

    def __str__(self):
        return f"Ошибка: {self.message}"
