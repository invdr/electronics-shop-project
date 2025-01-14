import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture
def item_1():
    """Добавляем fixture для инициализации экземпляра класса для теста"""
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone_1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_item_init(item_1):
    """Когда создаем экземпляр класса item_1 с Х атрибутами, то возвращается Х
    атрибут"""
    assert item_1.name == 'Смартфон'
    assert item_1.price == 10000
    assert item_1.quantity == 20


def test_calculate_total_price(item_1):
    """После создания экземпляра класса item_1 и вызова метода
    calculate_total_price(), возвращается price * quantity"""
    assert item_1.calculate_total_price() == 200_000  # 10_000 * 20


def test_apply_discount(item_1):
    """После создания экземпляра класса item_1 и вызова метода
    apply_discount(), item_1.price становится равным price * pay_rate"""
    # устанавливаем новый коэффициент
    item_1.pay_rate = 0.8
    # вызываем функцию для установления скидки иcходя из pay_rate
    item_1.apply_discount()
    assert item_1.price == 8000.0


# TestCase for homework-2
def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СмартфонПервыйДесяток'
    assert item.name == 'СмартфонПе'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1

    with pytest.raises(FileNotFoundError):
        not_file = '../src/items_err.csv'
        Item.instantiate_from_csv(not_file)

    error_file = '../src/items_error.csv'

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(error_file)


def test_string_number():
    assert Item.string_to_number('123') == 123
    assert Item.string_to_number(123.0) == 123
    assert Item.string_to_number(123) == 123


# TestCases for homework-3
def test___repr___(item_1):
    assert repr(item_1) == "Item('Смартфон', 10000, 20)"
    assert str(item_1) == "Смартфон"


# TestCases for homework-4
def test___add__(item_1, phone_1):
    assert item_1 + phone_1 == 25
    assert item_1 + 10000 == "Нельзя складывать классы Phone или Item с экземплярами не Phone или Item"
