from abc import ABCMeta, abstractmethod


class FlyBehavior(metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):

    def fly(self):
        print('I am flying!')


class FlyNoWay(FlyBehavior):

    def fly(self):
        print('I can not fly.')


class FlyRocketPowered(FlyBehavior):

    def fly(self):
        print('I am flying with a rocket!')


class QuackBehavior(metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):

    def quack(self):
        print('Quack.')


class MuteQuack(QuackBehavior):

    def quack(self):
        print('Silence...')


class Squack(QuackBehavior):

    def quack(self):
        print('Squack.')


class Duck(metaclass=ABCMeta):

    def __init__(self):
        fly_behavior = None
        quack_behavior = None

    @abstractmethod
    def display(self):
        pass

    def set_fly_behavior(self, fb):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb):
        self.quack_behavior = qb

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print('All ducks float, even decoys!')


class MallardDuck(Duck):

    def __init__(self):
        super(MallardDuck, self).__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self):
        print('I am a real Mallard duck.')


class ModelDuck(Duck):

    def __init__(self):
        super(ModelDuck, self).__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyNoWay()

    def display(self):
        print('I am a model duck.')


if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()
