class Person:

    def __init__(self, networth, cars, partner):
        self.__netWorth = networth
        self.__cars = cars
        self.__partner = partner

    @property
    def networth(self):
        return self.__netWorth

    @networth.setter
    def networth(self, value):
        self.__netWorth = value

