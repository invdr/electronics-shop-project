import pytest

from src.item import Item


@pytest.fixture
def item_1():
    """Добавляем fixture для инициализации экземпляра класса для теста"""
    return Item("Item", 10000, 20)


def test_item_init(item_1):
    """Когда создаем экземпляр класса item_1 с Х атрибутами, то возвращается Х
    атрибут"""
    assert item_1.name == 'Item'
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
    # вызываем функцию для установления скидки изходя из pay_rate
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


def test_string_number():
    assert Item.string_to_number('123') == 123
    assert Item.string_to_number(123.0) == 123
    assert Item.string_to_number(123) == 123
