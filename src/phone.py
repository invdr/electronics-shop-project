from src.item import Item


class Phone(Item):
    """Класс-наследник от класса Item"""
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Инициализация экземпляра класса с атрибутами класса-родителя и новым атрибутом
        "number_of_sim" для кол-ва сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Геттер для кол-ва сим-карт."""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        """Сеттер для кол-ва сим-карт с проверкой на целое число и большее нуля"""
        if not isinstance(number, int) or number <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = number

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', {self.price}"
                f", {self.quantity}, {self.number_of_sim})")
