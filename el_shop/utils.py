class Item():
    pay_rate = 1
    items = []


    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        Item.items.append(self)


    def calculate_total_price(self):
        return self.price * self.count


    def apply_discount(self):
        self.price = self.price * self.pay_rate


    def __repr__(self):
        return f'(Название товара: {self.name}, Цена за штуку: {self.price}, Количество: {self.count})'

