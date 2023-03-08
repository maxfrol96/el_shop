from el_shop.utils import Item, Phone, KeyBoard


def test_calculate_total_price():
    item = Item("Ноутбук", 20000, 5)
    assert item.calculate_total_price() == 100000


def test_is_integer():
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item = Item("iPhone 14", 120_000, 5)
    assert phone1 + item == 10

def test_KeyBoard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert kb.language == 'EN'
    assert kb.change_lang() == 'RU'