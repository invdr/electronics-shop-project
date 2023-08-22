import pytest

from src.keyboard import *

@pytest.fixture
def keyboard_item():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_keyboard(keyboard_item):
    assert keyboard_item.name == 'Dark Project KD87A'
    assert keyboard_item.price == 9600
    assert keyboard_item.quantity == 5
    keyboard_item.change_lang()
    assert keyboard_item.language == 'RU'
    keyboard_item.change_lang()
    assert keyboard_item.language == 'EN'


