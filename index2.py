class Computer():
    def __init__(self):
        self.__maxprice__ = 900
    def sell(self):
        print(f"Selling price: {self.__maxprice__}")
    def setMaxPrice(self, price):
        self.__maxprice__ = price

c = Computer()
c.sell()
c.__maxprice__ = 1000
c.sell()
c.setMaxPrice(1000)
c.sell()