from el_shop.utils import Item, sum

def test_calculate_total_price():
    item = Item("Ноутбук", 20000, 5)
    assert item.calculate_total_price() == 100000

