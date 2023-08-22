from src.item import Item


class MixinLayout:
    __LANG = 'EN'

    def __init__(self):
        self.__language = self.__LANG

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == self.__LANG:
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLayout):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__language = 'EN'
