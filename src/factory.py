from abc import ABCMeta, abstractmethod


class Pizza(object):

    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print('Preparing {}'.format(self.name))
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings...')
        for topping in self.toppings:
            print("\t{}".format(topping))

    def bake(self):
        print('Bake for 25 minutes at 350.')

    def cut(self):
        print('Cutting the pizza into diagonal slices.')

    def box(self):
        print('Place pizza in official PizzaStore box.')

    def get_name(self):
        return self.name


class NYStyleCheesePizza(Pizza):

    def __init__(self):
        super(NYStyleCheesePizza, self).__init__()
        self.name = 'NY Style Sauce and Cheese Pizza'
        self.sauce = 'Marinara Sauce'
        self.toppings.append('Grated Reggiano cheese')


class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        super(ChicagoStyleCheesePizza, self).__init__()
        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')

    def cut(self):
        print('Cutting the pizza into square slices.')


class PizzaStore(metaclass=ABCMeta):

    def order_pizza(self, type):
        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self):
        pass


class NYPizzaStore(PizzaStore):

    def create_pizza(self, item):
        if item == 'cheese':
            return NYStyleCheesePizza()
        else:
            return None


if __name__ == '__main__':
    nystore = NYPizzaStore()
    pizza = nystore.order_pizza('cheese')
    print('Ethan ordered a {}.'.format(pizza.get_name()))
