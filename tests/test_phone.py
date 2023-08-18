from tests.test_item import item_1, phone_1


# TestCases for homework-4
def test_phone_init(phone_1):
    assert phone_1.name == 'iPhone 14'
    assert phone_1.number_of_sim == 2


def test___add__(item_1, phone_1):
    assert item_1 + phone_1 == 25
    assert item_1 + 10000 == "Нельзя складывать классы Phone или Item с экземплярами не Phone или Item"


def test___repr__(phone_1):
    assert repr(phone_1) == "Phone('iPhone 14', 120000, 5, 2)"
