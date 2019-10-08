from abc import ABCMeta, abstractmethod


class PizzaIngredientFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return 'Thin Crust Dough'

    def create_sauce(self):
        return 'Marinara Sauce'

    def create_cheese(self):
        return 'Reggiano Cheese'

    def create_veggies(self):
        veggies = ['Garlic', 'Onion', 'Mushroom', 'RedPepper']
        return veggies

    def create_pepperoni(self):
        return 'Sliced Pepperoni'

    def create_clam(self):
        return 'Fresh Clams'


class Pizza(object):

    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('Bake for 25 minutes at 350.')

    def cut(self):
        print('Cutting the pizza into diagonal slices.')

    def box(self):
        print('Place pizza in official PizzaStore box.')

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class CheesePizza(Pizza):

    def __init__(self, ingredient_factory):
        super(CheesePizza, self).__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print('Preparing {}'.format(self.name))
        self.dough = self.ingredient_factory.create_dough()
        print('\tTossing {}...'.format(self.dough))
        self.sauce = self.ingredient_factory.create_sauce()
        print('\tAdding {}...'.format(self.sauce))
        self.cheese = self.ingredient_factory.create_cheese()
        print('\tAdding {}...'.format(self.cheese))


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
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if item == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('New York Style Cheese Pizza')

        return pizza


if __name__ == '__main__':
    nystore = NYPizzaStore()
    pizza = nystore.order_pizza('cheese')
    print('Ethan ordered a {}.'.format(pizza.get_name()))
