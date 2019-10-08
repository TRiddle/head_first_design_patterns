from abc import ABCMeta, abstractmethod

class Beverage(metaclass=ABCMeta):

    def __init__(self):
        self.description = 'Unknown Beverage'

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage):

    @abstractmethod
    def cost(self):
        pass


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return '{}, Mocha'.format(self.beverage.get_description())

    def cost(self):
        return 0.2 + beverage.cost()


class Espresso(Beverage):

    def __init__(self):
        super(Espresso, self).__init__()
        self.description = 'Espresso'

    def cost(self):
        return 1.99


class HouseBlend(Beverage):

    def __init__(self):
        super(HouseBlend, self).__init__()
        self.description = 'House Blend Coffee'

    def cost(self):
        return 0.89


if __name__ == '__main__':
    beverage = Espresso()
    print('{} ${}'.format(beverage.get_description(), beverage.cost()))

    beverage2 = HouseBlend()
    beverage2 = Mocha(beverage2)
    print('{} ${}'.format(beverage2.get_description(), beverage2.cost()))
