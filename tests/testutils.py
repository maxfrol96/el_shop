import unittest
from el_shop.utils import Item

class Testutils(unittest.TestCase):
    def setUp(self):
        self.item = Item("Ноутбук", 20000, 5)
    def test_calculate_total_price(self):
        self.assertEqual(self.item.calculate_total_price(), 100000)

    def test_apply_discount(self):
        self.assertEqual(self.item.apply_discount(), None)

