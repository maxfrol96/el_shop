import csv


class Item:
    pay_rate = 1
    all = []

    def __init__(self, name, price, count):
        self.__name = name
        self.price = price
        self.count = count
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        self.__name = name

    def calculate_total_price(self):
        return self.price * self.count

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r', encoding='windows-1251') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
            for a in rows[1:len(rows)]:
                if Item.is_integer(float(a[1])):
                    a[1] = int(a[1])
                if Item.is_integer(float(a[2])):
                    a[2] = int(a[2])
                cls(a[0], a[1], a[2])

    @staticmethod
    def is_integer(num):
        if num - int(num) == 0:
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Item):
            return self.count + other.count

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__name}, {self.price}, {self.count})'

    def __str__(self):
        return f'{self.__name}'


class Phone(Item):

    def __init__(self, name, price, count, sims):
        super().__init__(name, price, count)
        self.sims = sims
        # if number_of_sim == 0:
        #     raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @property
    def number_of_sim(self):
        return self.sims

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim == 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.sims = number_of_sim

    def __add__(self, other):
        if isinstance(other, Item):
            return self.count + other.count





