from abc import ABCMeta, abstractmethod


class Duck(metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):

    def quack(self):
        print('Quack.')

    def fly(self):
        print('I am flying.')


class Turkey(metaclass=ABCMeta):

    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class WildTurkey(Turkey):

    def gobble(self):
        print('Gobble gobble.')

    def fly(self):
        print('I am flying a short distance')


class TurkeyAdapter(Duck):

    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        turkey.gobble()

    def fly(self):
        for i in range(5):
            turkey.fly()


def test_duck(duck):
    duck.quack()
    duck.fly()


if __name__ == '__main__':
    duck = MallardDuck()

    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)

    print('The Turkey says...')
    turkey.gobble()
    turkey.fly()

    print('\nThe Duck says...')
    test_duck(duck)

    print('\nThe TurkeyAdapter says...')
    test_duck(turkey_adapter)
