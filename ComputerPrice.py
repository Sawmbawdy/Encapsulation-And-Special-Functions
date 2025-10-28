class Computer:
    __max = 900
    def sell(self):
        print("Selling Price:",self.__max)
    def SetMaxPrice(self,price):
        self.__max = price

c = Computer()
c.sell()

c.__max = 1000
c.sell()

c.SetMaxPrice(10000)
c.sell()